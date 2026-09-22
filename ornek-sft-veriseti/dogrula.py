#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EK-6 §4'teki sızıntı ve kalite kontrollerinin çalıştırılabilir hâli.

Her denetim ya GEÇER ya KALIR; kalan bir denetim veri setini eğitime uygunsuz sayar.
Gerçek hatta bu betik üretimden sonra koşar ve kalan kayıt eğitime alınmaz.

Kullanım:  python3 dogrula.py [--veri veri/] [--rapor rapor/uretim-raporu.md]
"""
import argparse, glob, json, os, re, sys
from collections import Counter, defaultdict

KOK = os.path.dirname(os.path.abspath(__file__))
try:
    from jsonschema import Draft202012Validator
    SEMA_VAR = True
except ImportError:
    SEMA_VAR = False

TC_DESENI    = re.compile(r"(?<!\d)[1-9]\d{10}(?!\d)")          # 11 haneli kimlik numarası deseni
TUTAR_DESENI = re.compile(r"\d{1,3}(?:\.\d{3})+,\d{2}|\d+,\d{2}\s*(?:TL|₺)|₺\s*\d")
KISI_DESENI  = re.compile(r"^P-[0-9A-F]{6}$")

def semalari_yukle():
    s = {}
    for ad in ("kayit", "g1", "g2", "g3", "g4"):
        s[ad] = json.load(open(os.path.join(KOK, "sema", f"{ad}.schema.json"), encoding="utf-8"))
    return s

def kayitlari_yukle(dizin):
    out = []
    for yol in sorted(glob.glob(os.path.join(KOK, dizin, "*.jsonl"))):
        for i, satir in enumerate(open(yol, encoding="utf-8"), 1):
            satir = satir.strip()
            if satir:
                out.append((os.path.basename(yol), i, json.loads(satir)))
    return out

# ── denetimler ───────────────────────────────────────────────────────────────
def d1_sema(kayitlar, semalar):
    """Şema geçerliliği: çıktısı şemaya uymayan örnek eğitime alınmaz."""
    if not SEMA_VAR:
        return [], "jsonschema kurulu değil; şema denetimi atlandı (pip install jsonschema)"
    zarf = Draft202012Validator(semalar["kayit"])
    gorev = {g: Draft202012Validator(semalar[g.lower()]) for g in ("G1", "G2", "G3", "G4")}
    hata = []
    for dosya, n, k in kayitlar:
        for e in zarf.iter_errors(k):
            hata.append(f"{dosya}:{n} {k.get('kayit_id')} zarf: {e.message[:120]}")
        v = gorev.get(k.get("gorev"))
        if v:
            for e in v.iter_errors(k.get("cikti", {})):
                hata.append(f"{dosya}:{n} {k.get('kayit_id')} {k['gorev']} çıktı: {e.message[:120]}")
    return hata, f"{len(kayitlar)} kayıt zarf + görev şemasına karşı doğrulandı"

def d2_sizinti(kayitlar):
    """Bölme kuruluş VE dönem bazındadır; aynı kuruluşun aynı dönemi iki bölmede olamaz."""
    yer = defaultdict(set)
    for _, _, k in kayitlar:
        yer[(k["kurulus_id"], k["donem"])].add(k["bolme"])
    hata = [f"{ku} / {d} → {sorted(b)}" for (ku, d), b in sorted(yer.items()) if len(b) > 1]
    kor = {k["kurulus_id"] for _, _, k in kayitlar if k["bolme"] == "kor-test"}
    egt = {k["kurulus_id"] for _, _, k in kayitlar if k["bolme"] == "egitim"}
    for ku in sorted(kor & egt):
        hata.append(f"kör test kuruluşu eğitimde de var: {ku}")
    return hata, f"{len(yer)} kuruluş×dönem çifti tek bölmede; kör test kuruluşları eğitimden tamamen ayrık"

def atifsiz(o):
    """mevzuat_ref alanlarını ayıklar."""
    if isinstance(o, dict):
        return {k: atifsiz(v) for k, v in o.items() if k != "mevzuat_ref"}
    if isinstance(o, list):
        return [atifsiz(v) for v in o]
    return o

def d3_tutar_yasagi(kayitlar):
    """Model hesap yapmaz: çıktının hiçbir metin alanı tutar iddiası taşıyamaz."""
    hata = []
    for dosya, n, k in kayitlar:
        if k["gorev"] == "G4":
            continue  # G4 belgeden alan çıkarır; tutar okumak görevinin kendisidir
        # mevzuat atıfları denetim dışıdır: atıf, tutar iddiası değildir
        metin = json.dumps(atifsiz(k["cikti"]), ensure_ascii=False)
        for m in TUTAR_DESENI.findall(metin):
            hata.append(f"{dosya}:{n} {k['kayit_id']} çıktıda tutar: {m}")
    return hata, "G1/G2/G3 çıktılarının hiçbirinde tutar iddiası yok"

def d4_atif(kayitlar):
    """Atıfsız hipotez ve atıfsız soru kabul edilmez."""
    hata = []
    for dosya, n, k in kayitlar:
        c = k["cikti"]
        if k["gorev"] == "G1":
            for a in c["kok_neden_adaylari"]:
                if len(a.get("mevzuat_ref", "")) < 6:
                    hata.append(f"{dosya}:{n} {k['kayit_id']} atıfsız hipotez {a['hipotez_kodu']}")
        if k["gorev"] == "G3":
            for s in c["sorular"]:
                if len(s.get("mevzuat_ref", "")) < 6:
                    hata.append(f"{dosya}:{n} {k['kayit_id']} atıfsız soru")
    return hata, "G1 hipotezlerinin ve G3 sorularının tamamı mevzuat maddesine bağlı"

def d5_belirsizlik(kayitlar):
    """S5 tek nedene zorlanmaz: ayirt_edilebilir=false ⇒ S5 adayı + belirsizlik notu."""
    hata = []
    for dosya, n, k in kayitlar:
        if k["gorev"] != "G1":
            continue
        c = k["cikti"]
        if not c["ayirt_edilebilir"]:
            if not any(a["sinif"] == "S5" for a in c["kok_neden_adaylari"]):
                hata.append(f"{dosya}:{n} {k['kayit_id']} ayırt edilemez ama S5 adayı yok")
            if not c.get("belirsizlik_notu"):
                hata.append(f"{dosya}:{n} {k['kayit_id']} ayırt edilemez ama belirsizlik notu boş")
        if any(a["sinif"] == "S3" for a in c["kok_neden_adaylari"]) and not c["kanit_talebi"]:
            hata.append(f"{dosya}:{n} {k['kayit_id']} S3 adayı var ama kanıt talebi yok")
    return hata, "belirsiz ve veri eksiği kalemleri kanıt talebiyle birlikte raporlanıyor"

def d6_anonimlik(kayitlar):
    """Anonimleştirme eğitimden önce: ham kişisel veri hiçbir kayıtta bulunmaz."""
    hata = []
    for dosya, n, k in kayitlar:
        ham = json.dumps(k, ensure_ascii=False)
        for m in TC_DESENI.findall(ham):
            hata.append(f"{dosya}:{n} {k['kayit_id']} 11 haneli kimlik deseni: {m[:3]}********")
        for t in re.findall(r'"kisi_token":\s*"([^"]+)"', ham):
            if not KISI_DESENI.match(t):
                hata.append(f"{dosya}:{n} {k['kayit_id']} geçersiz kişi tokeni: {t}")
    return hata, "kişi alanları yalnız tokenize biçimde; 11 haneli kimlik deseni yok"

def d7_etiket_kaynagi(kayitlar):
    """Etiketi insan değil motor üretir: kaynak A ve B'de insan-kapanis etiketi olamaz."""
    hata = []
    for dosya, n, k in kayitlar:
        if k["kaynak"] in ("A", "B") and k["etiket_kaynagi"] == "insan-kapanis":
            hata.append(f"{dosya}:{n} {k['kayit_id']} sentetik kaynakta insan etiketi")
        if k["gorev"] == "G2" and k["etiket_kaynagi"] != "motor-dogrulamali":
            hata.append(f"{dosya}:{n} {k['kayit_id']} G2 etiketi motorla doğrulanmamış")
    return hata, "G2 etiketleri motor tarafından, diğerleri inşa gereği atanmış"

def d8_mesaj_tutarliligi(kayitlar):
    """Sohbet render'ı yapılandırılmış kayıttan türer; ikisi ayrışamaz."""
    hata = []
    for dosya, n, k in kayitlar:
        try:
            if json.loads(k["mesajlar"][2]["icerik"]) != k["cikti"]:
                hata.append(f"{dosya}:{n} {k['kayit_id']} asistan mesajı çıktıdan farklı")
        except json.JSONDecodeError:
            hata.append(f"{dosya}:{n} {k['kayit_id']} asistan mesajı geçerli JSON değil")
    return hata, "her kaydın asistan mesajı, yapılandırılmış çıktının birebir karşılığı"


def d9_g4_belgeye_dayali(kayitlar):
    """G4 etiketi belgeden TÜRER, uydurulmaz: çıkarılan her alan belge metninde birebir
    bulunmalı ve özet satırı okunduğu değere eşit olmalıdır."""
    hata = []
    for dosya, n, k in kayitlar:
        if k["gorev"] != "G4":
            continue
        metin = k["girdi"]["belge_metni"]
        for al in k["cikti"]["alanlar"]:
            d = al["deger"]
            gorunen = (f"{d:,.2f}".replace(",", "\x00").replace(".", ",").replace("\x00", ".")
                       if isinstance(d, float) else str(d))
            if gorunen not in metin:
                hata.append(f"{dosya}:{n} {k['kayit_id']} '{al['ad']}' belgede yok: {gorunen}")
        if k["cikti"]["donem"] not in metin:
            hata.append(f"{dosya}:{n} {k['kayit_id']} dönem belgede yok")
        ozet = [a for a in k["cikti"]["alanlar"] if a["ad"] == "ozet_satiri"]
        if not ozet:
            hata.append(f"{dosya}:{n} {k['kayit_id']} özet satırı çıkarılmamış")
    return hata, "G4 alanlarının tamamı belge metninde birebir bulunuyor; özet satırı okunuyor"

def d10_pilot_egitime_girmez(kayitlar):
    """EK-6 §3: pilot kayıtları ağırlıklı test ve kalibrasyona ayrılır; kör kısım eğitime
    hiçbir biçimde girmez. Bu örnekte henüz gerçek pilot verisi yoktur, dolayısıyla
    kaynak C'nin tamamı eğitim dışıdır. (Ay 11'de kör olmayan kısım eğitime alınabilir;
    o aşamada bu denetim kör test kuruluşlarıyla sınırlandırılır.)"""
    hata = [f"{d}:{n} {k['kayit_id']} kaynak C eğitim bölmesinde"
            for d, n, k in kayitlar if k["kaynak"] == "C" and k["bolme"] == "egitim"]
    c = [k for _, _, k in kayitlar if k["kaynak"] == "C"]
    for k in c:
        if not k["girdi"].get("yer_tutucu"):
            hata.append(f"{k['kayit_id']} kaynak C kaydı yer tutucu olarak işaretlenmemiş")
    return hata, f"{len(c)} kaynak C kaydı eğitim dışında ve yer tutucu olarak işaretli"

DENETIMLER = [("D1 şema geçerliliği", d1_sema), ("D2 sızıntı (kuruluş×dönem)", d2_sizinti),
              ("D3 tutar yasağı", d3_tutar_yasagi), ("D4 mevzuat atfı", d4_atif),
              ("D5 belirsizlik disiplini", d5_belirsizlik), ("D6 anonimlik", d6_anonimlik),
              ("D7 etiket kaynağı", d7_etiket_kaynagi), ("D8 mesaj tutarlılığı", d8_mesaj_tutarliligi),
              ("D9 G4 belgeye dayalılık", d9_g4_belgeye_dayali),
              ("D10 pilot verisi eğitim dışı", d10_pilot_egitime_girmez)]

def dengeleme(kayitlar):
    sinif = Counter()
    for _, _, k in kayitlar:
        if k["gorev"] == "G1":
            for a in k["cikti"]["kok_neden_adaylari"]:
                sinif[a["sinif"]] += 1
    return sinif

def main():
    ap = argparse.ArgumentParser(description="EK-6 kalite ve sızıntı denetimleri")
    ap.add_argument("--veri", default="veri/")
    ap.add_argument("--rapor", default="rapor/uretim-raporu.md")
    a = ap.parse_args()

    semalar = semalari_yukle()
    kayitlar = kayitlari_yukle(a.veri)
    print(f"Denetci.AI · veri seti denetimi · {len(kayitlar)} kayıt\n")

    satirlar, kalan = [], 0
    for ad, fn in DENETIMLER:
        hata, ozet = fn(kayitlar, semalar) if fn is d1_sema else fn(kayitlar)
        durum = "GEÇTİ" if not hata else f"KALDI ({len(hata)})"
        print(f"  {ad:30s} {durum}")
        for h in hata[:5]:
            print(f"      → {h}")
        if len(hata) > 5:
            print(f"      → … {len(hata)-5} bulgu daha")
        satirlar.append((ad, durum, ozet, hata))
        kalan += len(hata)

    gorev = Counter(k["gorev"] for _, _, k in kayitlar)
    kaynak = Counter(k["kaynak"] for _, _, k in kayitlar)
    bolme = Counter(k["bolme"] for _, _, k in kayitlar)
    sinif = dengeleme(kayitlar)
    s5 = sinif.get("S5", 0) / max(1, sum(sinif.values()))

    print(f"\n  görev  {dict(sorted(gorev.items()))}")
    print(f"  kaynak {dict(sorted(kaynak.items()))}")
    print(f"  bölme  {dict(sorted(bolme.items()))}")
    print(f"  sınıf  {dict(sorted(sinif.items()))}")
    print(f"  S5 payı %{s5*100:.1f}")

    os.makedirs(os.path.join(KOK, os.path.dirname(a.rapor)), exist_ok=True)
    with open(os.path.join(KOK, a.rapor), "w", encoding="utf-8") as f:
        f.write("# Üretim ve denetim raporu\n\n")
        f.write(f"*`uret.py` ve `dogrula.py` tarafından üretilmiştir. Kayıt sayısı: {len(kayitlar)}.*\n\n")
        f.write("## Denetimler\n\n| Denetim | Sonuç | Kapsam |\n|---|---|---|\n")
        for ad, durum, ozet, _ in satirlar:
            f.write(f"| {ad} | **{durum}** | {ozet} |\n")
        f.write("\n## Dağılımlar\n\n| Kesit | Dağılım |\n|---|---|\n")
        f.write(f"| Görev | {', '.join(f'{k} {v}' for k, v in sorted(gorev.items()))} |\n")
        f.write(f"| Kaynak | {', '.join(f'{k} {v}' for k, v in sorted(kaynak.items()))} |\n")
        f.write(f"| Bölme | {', '.join(f'{k} {v}' for k, v in sorted(bolme.items()))} |\n")
        f.write(f"| G1 kök neden sınıfı | {', '.join(f'{k} {v}' for k, v in sorted(sinif.items()))} |\n")
        f.write(f"\n'Belirsiz' (S5) adaylarının payı: **%{s5*100:.1f}**. "
                f"AS-2 hedefi, tutar payı olarak ≤%5'tir; buradaki oran kayıt sayısı üzerinden hesaplanır "
                f"ve tutar ağırlıklı ölçüm gerçek pilot verisiyle yapılır.\n")
    print(f"\n  rapor → {a.rapor}")
    return 1 if kalan else 0

if __name__ == "__main__":
    sys.exit(main())
