#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EK-6 üretim hattının çalışan örneği.

    senaryo/enjeksiyon verisi → motor koşumu → fark imzası + kural sürümü + tutarlılık ihlalleri
        → görev başına girdi-çıktı çifti → şema doğrulaması → eğitim/test bölmesi

Buradaki MOTOR, doğrulanmış deterministik hesap çekirdeğinin yerine duran küçük bir
taklittir (stub): aynı arayüzü verir, aynı fark imzasını üretir, ama yalnızca bu
senaryoların aritmetiğini bilir. Gerçek hatta yerine çekirdek konur; kayıtların biçimi
ve etiket kaynağı değişmez.

Kullanım:  python3 uret.py [--tohum 20260922] [--cikti veri/]
"""
import argparse, hashlib, json, os, random, unicodedata
from collections import Counter, defaultdict

KOK = os.path.dirname(os.path.abspath(__file__))
SURUM = "1.0"

# ── kimlik üretimi (tokenize; ham kişisel veri hiçbir aşamada yoktur) ─────────
def kisi_token(rnd):
    return "P-" + "".join(rnd.choice("0123456789ABCDEF") for _ in range(6))

def ay_ekle(donem, n):
    """'2024-11' + 2 ay → '2025-01'. Yıl sınırını doğru geçer."""
    y, a = map(int, donem.split("-"))
    t = (y * 12 + (a - 1)) + n
    return f"{t // 12:04d}-{t % 12 + 1:02d}"

def tl(x):
    """Türkçe para biçimi: 1.234.567,89"""
    return f"{x:,.2f}".replace(",", "\x00").replace(".", ",").replace("\x00", ".")

# ── MOTOR taklidi: senaryo + parametre → fark imzası ─────────────────────────
def motor(sen, p, rnd):
    """Deterministik hesap çekirdeğinin yerine duran taklit.
    Döndürdüğü fark imzası, gerçek çekirdeğin ürettiğiyle aynı alanları taşır."""
    sid, ay = sen["id"], p["ay_sayisi"]
    kalemler, ihlal = [], list(sen["ihlal_edilen_kural"])

    if sid in ("S01", "S10"):
        a_b, a_d, m = p["alfa_beyan"], p.get("alfa_dogru", 1.00), p["matrah"]
        if sid == "S10":
            a_d = 1.00  # 4691'de oran derece bağlı değildir
        beyan, dogru = m * a_b, m * a_d
        kalemler = [("gv_terkin", beyan * ay, dogru * ay)]
    elif sid == "S02":
        tavan, m = p["tavan"], p["matrah"]
        k = p["kisi_sayisi"]
        kalemler = [("sgk_5746_matrah", m * k * ay, tavan * k * ay)]
    elif sid == "S03":
        m = p["matrah"]
        kalemler = [("bes_puan_indirimi", m * 0.05 * ay, None)]  # doğru değer bilinemez
    elif sid == "S04":
        m = p["matrah"]
        kalemler = [("gv_terkin", m * 0.90 * ay, m * 0.80 * ay)]
    elif sid == "S05":
        t1, sap = p["tablo1"], p["ek_bildirim_sapma"]
        kalemler = [("gv_terkin", t1, t1 + sap)]
    elif sid == "S06":
        kalemler = [("gv_terkin", p["artik"], 0.0)]
    elif sid == "S07":
        m = p["matrah"]
        kalemler = [("gv_terkin", m * 0.80 * ay, m * 0.80 * ay + m * 0.80)]  # bir ay kayma
    elif sid == "S08":
        m, k = p["matrah"], p["kisi_sayisi"]
        kalemler = [("gv_terkin", m * 0.80 * k * ay * 2, m * 0.80 * k * ay)]  # çifte istisna
    elif sid == "S09":
        tze, d = p["arge_tze"], p["destek_kisi"]
        azami = -(-int(tze) // 10)  # ceil(TZE/10)
        kalemler = [("destek_personeli_sayisi", float(d * ay), float(min(d, azami) * ay))]
        p["_azami"] = azami
    elif sid == "S11":
        y, a = p["yillik_toplam"], p["artik"]
        kalemler = [("kvk_toplam", y, y - a)]
    elif sid == "S12":
        m, k = p["matrah"], p["kisi_sayisi"]
        kalemler = [("sgk_isveren_destegi", m * 0.05 * k * ay, 0.0)]
    elif sid == "S13":
        m, k = p["matrah"], p["kisi_sayisi"]
        kalemler = [("sgk_isveren_destegi", 0.0, m * 0.05 * k * ay)]
    elif sid == "S14":
        m, k = p["matrah"], p["kisi_sayisi"]
        kalemler = [("gv_terkin", 0.0, m * 0.80 * k * ay)]

    imza = []
    for ad, beyan, dogru in kalemler:
        if dogru is None:
            imza.append({"kalem": ad, "beyan": round(beyan, 2), "yeniden_hesap": None,
                         "fark": None, "yon": "hesaplanamadi",
                         "not": "Girdi eksik olduğu için karşı-olgusal hesap koşulmamıştır."})
        else:
            fark = round(beyan - dogru, 2)
            imza.append({"kalem": ad, "beyan": round(beyan, 2), "yeniden_hesap": round(dogru, 2),
                         "fark": fark,
                         "yon": "aleyhte" if fark > 0 else ("lehte" if fark < 0 else "yok")})
    return {"fark_imzasi": imza, "ihlal_edilen_kurallar": ihlal}

# ── görev girdileri ve çıktıları ─────────────────────────────────────────────
SISTEM = (
 "Sen 5746 ve 4691 teşvik mevzuatı üzerinde çalışan bir denetim asistanısın. "
 "Deterministik hesap motorunun ürettiği fark imzasını incelersin.\n"
 "Kesin sınırların: tutar HESAPLAMAZSIN, yeni rakam ÜRETMEZSİN, kapanış kararı VERMEZSİN. "
 "Ürettiğin her şey bir bulgu yorumu, bir belge talebi veya bir sorudur.\n"
 "Her hipotez bir mevzuat maddesine atıf taşır. Birden çok hipotez aynı fark imzasını "
 "açıklıyorsa tek nedene zorlamaz, S5 (ayırt edilemez) dersin. Gerekli girdi yoksa S3 "
 "(veri eksiği) dersin ve bunu asla gerçek hata sınıfına veya tutar iddiasına çevirmezsin.\n"
 "Çıktını yalnızca istenen JSON şemasında verirsin."
)

def g1_cikti(sen, ctx, pi=1):
    """Kök neden adayları. Rakip hipotez KENDİ sınıfıyla gelir; ayırt edilemeyen
    vakada her zaman, ayırt edilebilen vakada örneklerin bir kısmında listelenir —
    net bir bulgunun tek adayı olması da gerçekçidir."""
    ana = {"sira": 1, "sinif": sen["beklenen_sinif"], "hipotez_kodu": sen["hipotez_kodu"],
           "aciklama": ctx["aciklama"], "mevzuat_ref": sen["mevzuat_ref"]}
    adaylar = [ana]
    if sen.get("rakip_hipotez") and (not sen["ayirt_edilebilir"] or pi % 2 == 0):
        adaylar.append({"sira": 2,
                        "sinif": sen["rakip_sinif"],
                        "hipotez_kodu": sen["rakip_hipotez"],
                        "aciklama": ctx["rakip_aciklama"],
                        "mevzuat_ref": sen["rakip_mevzuat_ref"]})
    if not sen["ayirt_edilebilir"] and not any(a["sinif"] == "S5" for a in adaylar):
        adaylar.append({"sira": len(adaylar) + 1, "sinif": "S5", "hipotez_kodu": "H-AYIRT-EDILEMEZ",
                        "aciklama": ctx["rakip_aciklama"], "mevzuat_ref": sen["mevzuat_ref"]})
    return {"kok_neden_adaylari": adaylar,
            "ayirt_edilebilir": sen["ayirt_edilebilir"],
            "belirsizlik_notu": None if sen["ayirt_edilebilir"] else ctx["belirsizlik"],
            "kanit_talebi": [sen["cozen_belge"]]}

def g2_cikti(sen, ctx):
    etki = ("hipotezler ayrışır" if not sen["ayirt_edilebilir"] else
            "sınıf S3'ten çıkar" if sen["beklenen_sinif"] == "S3" else
            "fark tolerans bandına iner")
    return {"belge": sen["cozen_belge"], "alan": sen["cozen_alan"],
            "kapsam": {"donem_araligi": ctx["donem_araligi"], "kisi_token": ctx["kisi"]},
            "gerekce": ctx["g2_gerekce"], "beklenen_etki": etki}

def g3_cikti(sen, ctx):
    out = []
    for i, s in enumerate(sen["beklenen_sorular"][:3], 1):
        out.append({"soru": s["soru"].replace("{kisi}", ctx["kisi"] or "ilgili personel"),
                    "mevzuat_ref": sen["mevzuat_ref"], "amac": s["amac"]})
    return {"sorular": out}

BELGE_TURLERI = ["MUHSGK Tablo-1", "SGK onaylı hizmet listesi", "Ar-Ge personel ek bildirim XML",
                 "SGK tahakkuk fişi", "MUHSGK damga vergisi tablosu"]

def belge_uret(belge, donem, tutarli, rnd):
    """Önce belge YAPISI kurulur, metin ondan render edilir, etiket de ondan türer.
    Böylece G4 etiketi belgenin kendisiyle kuruşu kuruşuna tutar: 'doğru cevap'
    belgenin iç toplam kontrolünden gelir, uydurulmaz (EK-6 §2, G4 satırı)."""
    a = lambda ad, deger, birim: {"ad": ad, "deger": deger, "birim": birim}

    if belge == "MUHSGK Tablo-1":
        matrah = round(rnd.uniform(380000, 640000), 2)
        oran   = rnd.choice([0.80, 0.90, 0.95])
        terkin = round(matrah * oran, 2)
        kisi   = rnd.randint(14, 38)
        ozet   = terkin if tutarli else round(terkin + rnd.uniform(900, 2600), 2)
        metin = (f"MUHTASAR VE PRİM HİZMET BEYANNAMESİ · TABLO-1 · DÖNEM {donem}\n"
                 f"  Terkine konu matrah .......... {tl(matrah)}\n"
                 f"  Terkin edilen tutar .......... {tl(terkin)}\n"
                 f"  Çalışan sayısı ............... {kisi}\n"
                 f"  Dönem kodu ................... {donem.replace('-', '')}\n"
                 f"  ÖZET SATIRI (terkin) ......... {tl(ozet)}")
        alanlar = [a("terkine_konu_matrah", matrah, "TL"), a("terkin_tutari", terkin, "TL"),
                   a("calisan_sayisi", kisi, "kişi"), a("donem_kodu", donem.replace("-", ""), "kod"),
                   a("ozet_satiri", ozet, "TL")]
        hesap, karsilastirilan = terkin, "terkin edilen tutar"

    elif belge == "SGK onaylı hizmet listesi":
        m1 = round(rnd.uniform(120000, 220000), 2)
        m2 = round(rnd.uniform(28000, 64000), 2)
        gun = rnd.choice([30, 28, 26])
        top = round(m1 + m2, 2)
        ozet = top if tutarli else m1
        metin = (f"SGK ONAYLI HİZMET LİSTESİ · DÖNEM {donem}\n"
                 f"  Kanun türü 05746 · prim gün {gun} · PEK matrah {tl(m1)}\n"
                 f"  Kanun türü 5510  · prim gün {gun} · PEK matrah {tl(m2)}\n"
                 f"  ÖZET SATIRI (matrah toplamı) . {tl(ozet)}")
        alanlar = [a("prim_gun_sayisi", gun, "gün"), a("pek_matrah_05746", m1, "TL"),
                   a("pek_matrah_5510", m2, "TL"), a("kanun_turu_1", "05746", "kod"),
                   a("kanun_turu_2", "5510", "kod"), a("ozet_satiri", ozet, "TL")]
        hesap, karsilastirilan = top, "iki satırın matrah toplamı"

    elif belge == "Ar-Ge personel ek bildirim XML":
        kisiler = [(kisi_token(rnd), round(rnd.uniform(60000, 190000), 2)) for _ in range(rnd.randint(2, 3))]
        top = round(sum(t for _, t in kisiler), 2)
        ozet = top if tutarli else round(top - rnd.uniform(4000, 13000), 2)
        satir = "\n".join(f'  <kisi token="{k}" terkin="{tl(t)}"/>' for k, t in kisiler)
        metin = f'<ekBildirim donem="{donem}">\n{satir}\n  <toplam>{tl(ozet)}</toplam>\n</ekBildirim>'
        alanlar = [a("bildirilen_kisi", len(kisiler), "kişi")]
        for k, t in kisiler:
            alanlar.append({"ad": "kisi_terkin", "deger": t, "birim": "TL", "kisi_token": k})
        alanlar.append(a("ozet_satiri", ozet, "TL"))
        hesap, karsilastirilan = top, "kişi bazlı terkin toplamı"

    elif belge == "SGK tahakkuk fişi":
        tut = round(rnd.uniform(64000, 148000), 2)
        kod = rnd.choice(["05746", "15746"])
        ozet = tut if tutarli else round(tut + rnd.uniform(300, 900), 2)
        metin = (f"SGK TAHAKKUK FİŞİ · DÖNEM {donem}\n"
                 f"  Tahakkuk tutarı .............. {tl(tut)}\n"
                 f"  Belge türü ................... {kod}\n"
                 f"  ÖZET SATIRI .................. {tl(ozet)}")
        alanlar = [a("tahakkuk_tutari", tut, "TL"), a("belge_turu", kod, "kod"), a("ozet_satiri", ozet, "TL")]
        hesap, karsilastirilan = tut, "tahakkuk tutarı"

    else:  # MUHSGK damga vergisi tablosu
        tut = round(rnd.uniform(2800, 7400), 2)
        ozet = tut if tutarli else round(tut + rnd.uniform(60, 190), 2)
        metin = (f"MUHSGK DAMGA VERGİSİ İSTİSNA TABLOSU · DÖNEM {donem}\n"
                 f"  İstisna tutarı ............... {tl(tut)}\n"
                 f"  ÖZET SATIRI .................. {tl(ozet)}")
        alanlar = [a("dv_muafiyet_tutari", tut, "TL"), a("ozet_satiri", ozet, "TL")]
        hesap, karsilastirilan = tut, "istisna tutarı"

    gecti = abs(round(hesap - ozet, 2)) <= 0.01      # tolerans bandı: kişi-kalem ±0,01 TL
    cikti = {"belge_turu": belge, "donem": donem, "alanlar": alanlar,
             "ic_toplam_kontrolu": {"gecti": gecti,
                "aciklama": (f"Belgeden okunan {karsilastirilan}, özet satırıyla tolerans bandı içinde uyuşmaktadır."
                             if gecti else
                             f"Belgeden okunan {karsilastirilan} ile özet satırı uyuşmamaktadır; "
                             f"belge içi tutarsızlık başlı başına bulgudur ve dönemin nüsha zinciri kontrolünü tetikler.")}}
    return metin, cikti

# ── anlatı yardımcıları ──────────────────────────────────────────────────────
def aciklamalar(sen, imza, p, ctx):
    k = imza[0]
    yon = k["yon"]
    if sen["beklenen_sinif"] == "S3":
        a = ("Karşı-olgusal hesap koşulamamıştır: kanun türü seçimini belirleyen muaccel borç durumu "
             "dosyada yoktur. Bu kalem veri eksiği sınıfındadır; eksik bir tutar iddiası üretilemez, "
             "ikinci tur veri talebine ve dönem güven skoruna işlenir.")
    elif sen["beklenen_sinif"] == "S1":
        a = ("Fark, kişi-kalem ve dönem toplamı tolerans bandının içindedir ve kalem düzeyindeki kuruş "
             "yuvarlamasıyla açıklanmaktadır. Bulgu değildir; yalnız adet ve tutar özetinde raporlanır.")
    elif sen["beklenen_sinif"] == "S2":
        a = ("Fark tüm dönemlerde aynı yönde ve aynı desendedir; ücretin ödendiği ay ile çalışma ayının "
             "ayrışmasıyla açıklanmaktadır. Bu bir hata değil, firmanın tutarlı uyguladığı bir yöntem "
             "farkıdır; muhasebe politikası profiline yazılıp tüm dönemlere aynı biçimde uygulanmalıdır.")
    elif sen["beklenen_sinif"] == "S4b":
        a = ("Kapsamdaki personel için destek bazı aylarda hiç bildirilmemiştir; fark lehtedir. Eksik aylar "
             "geriye yönelik yararlanma penceresinin dışında kaldığından tutar geri alınamaz; bulgu, süreç "
             "düzeltildiğinde tekrar etmeyecek yıllık kayıp olarak raporlanır.")
    elif sen["beklenen_sinif"] == "S4a":
        a = ("Fark lehtedir ve dönem düzeltme zamanaşımı içindedir; düzeltme yoluyla talep edilebilir. "
             "Bulgunun dayanağı, yeniden hesabın beyan edilen tutardan yukarı yönde ayrışmasıdır.")
    elif sen["beklenen_sinif"] == "S5":
        a = ("Fark imzası birden fazla hipotezle aynı ölçüde açıklanabilmektedir; eldeki belgeler hipotezleri "
             "ayırmaya yetmemektedir. Kalem tek nedene zorlanmaz, belirsiz olarak raporlanır ve ayırt edici "
             "belge istenir.")
    else:  # S4c
        a = (f"Yeniden hesap, beyan edilen tutardan {yon} yönde ayrışmaktadır ve ayrışma "
             f"{sen['ad'].lower()} ile açıklanmaktadır. Fazla yararlanma sınıfındadır; geri isteme ve "
             f"gecikme zammı riski taşır, kapanış kararı yeminli mali müşavir oturumuna aittir.")
    if not sen.get("rakip_hipotez"):
        r = ""
    elif not sen["ayirt_edilebilir"]:
        r = ("Aynı fark imzası bu hipotezle de aynı ölçüde açıklanabilmektedir; iki hipotezi ayıracak "
             "belge eldeki envanterde yoktur. Bu nedenle kalem tek nedene bağlanmaz.")
    else:
        r = (f"Bu hipotez de aynı yönde fark üretebildiği için ikinci sırada değerlendirilmiştir; ancak onu "
             f"doğrulayacak {sen['rakip_kural']} tutarlılık kuralı bu dönemde ihlal sinyali vermemiştir. "
             f"{sen['cozen_belge']} geldiğinde hipotez ya elenir ya doğrulanır.")
    b = ("İki hipotez aynı fark imzasını üretmektedir. En küçük artığı veren hipoteze zorlamak, yanlış "
         "kök neden atfı riski doğurur; ayırt edici belge gelene kadar kalem belirsizdir.")
    g2 = (f"{sen['cozen_belge']} belgesindeki {sen['cozen_alan']} alanı, hipotezi kanıta bağlayan tek "
          f"alandır; belge getirilip motor yeniden koşulduğunda farkın çözülüp çözülmediği otomatik "
          f"olarak görülür.")
    return {"aciklama": a, "rakip_aciklama": r or a, "belirsizlik": b, "g2_gerekce": g2, **ctx}

# ── kuruluş/dönem havuzu ve bölme ────────────────────────────────────────────
KURULUSLAR = {
    "A": ["KUR-SENT-01", "KUR-SENT-02", "KUR-SENT-03", "KUR-SENT-04", "KUR-SENT-05", "KUR-SENT-06"],
    "B": ["KUR-ENJ-01", "KUR-ENJ-02", "KUR-ENJ-03", "KUR-ENJ-04"],
}
# EK-6 §4: bölme kuruluş VE dönem bazındadır; kör test kuruluşu eğitime hiç girmez
KOR_TEST_KURULUS = {"KUR-SENT-06", "KUR-ENJ-04"}
KALIBRASYON_KURULUS = {"KUR-SENT-05", "KUR-ENJ-03"}

def bolme_sec(kurulus):
    if kurulus in KOR_TEST_KURULUS:   return "kor-test"
    if kurulus in KALIBRASYON_KURULUS: return "kalibrasyon"
    return "egitim"

DONEMLER = ["2024-11", "2025-01", "2025-03", "2025-06", "2025-08", "2025-10", "2026-02"]

def parametre_kombinasyonlari(uzay, n, rnd):
    out = []
    for _ in range(n):
        out.append({k: rnd.choice(v) for k, v in uzay.items()})
    # tekrarları ele
    esiz, gorulen = [], set()
    for p in out:
        a = json.dumps(p, sort_keys=True)
        if a not in gorulen:
            gorulen.add(a); esiz.append(p)
    return esiz

# ── ana üretim ───────────────────────────────────────────────────────────────
def uret(tohum, cikti_dizin):
    rnd = random.Random(tohum)
    lib = json.load(open(os.path.join(KOK, "senaryolar", "senaryo-kutuphanesi.json"), encoding="utf-8"))
    kayitlar, sayac = [], Counter()

    def yeni_id(kaynak, sid, pi, gorev):
        sayac[gorev] += 1
        return f"{kaynak}-{sid}-p{pi:02d}-{gorev}-{sayac[gorev]:04d}"

    for sen in lib["senaryolar"]:
        params = parametre_kombinasyonlari(sen["parametre_uzayi"], 4, rnd)
        for pi, p in enumerate(params, 1):
            kurulus = rnd.choice(KURULUSLAR["A"])
            donem = rnd.choice(DONEMLER)
            rejim = "4691" if sen["id"] == "S10" else ("5746+4691" if sen["id"] == "S08" else "5746")
            bolme = bolme_sec(kurulus)
            kisi = kisi_token(rnd)
            snapshot = f"{donem} @ bilgi:2026-06-30"
            kosum = motor(sen, p, rnd)
            aralik = f"{donem}..{ay_ekle(donem, p['ay_sayisi'] - 1)}" if p["ay_sayisi"] > 1 else donem
            ctx = aciklamalar(sen, kosum["fark_imzasi"], p, {"kisi": kisi, "donem_araligi": aralik})

            ortak = dict(kaynak="A", senaryo_id=sen["id"], kurulus_id=kurulus, donem=donem,
                         rejim=rejim, mevzuat_snapshot=snapshot, bolme=bolme,
                         ihlal_edilen_kural=kosum["ihlal_edilen_kurallar"],
                         uretim={"uretici": "uret.py", "surum": SURUM, "tohum": tohum,
                                 "motor_kosum": hashlib.sha256(
                                     json.dumps([sen["id"], p], sort_keys=True).encode()).hexdigest()[:12]})

            girdi_g1 = {"fark_imzasi": kosum["fark_imzasi"],
                        "uygulanan_kural_surumu": snapshot,
                        "ihlal_edilen_tutarlilik_kurallari": kosum["ihlal_edilen_kurallar"],
                        "rejim": rejim, "kisi_token": kisi, "donem_araligi": aralik,
                        "belge_envanteri": belge_envanteri(sen, rnd)}

            # G1
            kayitlar.append(kayit(yeni_id("A", sen["id"], pi, "G1"), "G1", ortak,
                                  girdi_g1, g1_cikti(sen, ctx, pi), "insa-geregi"))
            # G2
            g2_girdi = dict(girdi_g1, onceki_yorum={"hipotez_kodu": sen["hipotez_kodu"],
                                                    "sinif": sen["beklenen_sinif"]})
            k2 = kayit(yeni_id("A", sen["id"], pi, "G2"), "G2", ortak, g2_girdi,
                       g2_cikti(sen, ctx), "motor-dogrulamali")
            k2["girdi"]["motor_geri_bildirimi"] = {"cozdu": True,
                "not": "Önerilen belge getirilip motor yeniden koşulduğunda fark çözülmüştür; etiket otomatik atanmıştır."}
            kayitlar.append(k2)
            # G3
            kayitlar.append(kayit(yeni_id("A", sen["id"], pi, "G3"), "G3", ortak,
                                  dict(girdi_g1, baglam={"sinif": sen["beklenen_sinif"],
                                                         "hipotez_kodu": sen["hipotez_kodu"]}),
                                  g3_cikti(sen, ctx), "insa-geregi"))
            # G4 — senaryonun çözen belgesi bir beyan belgesiyse alan çıkarımı örneği
            if sen["cozen_belge"] in BELGE_TURLERI and pi <= 2:
                metin, g4 = belge_uret(sen["cozen_belge"], donem, tutarli=(pi == 1), rnd=rnd)
                kayitlar.append(kayit(yeni_id("A", sen["id"], pi, "G4"), "G4", ortak,
                                      {"belge_turu": sen["cozen_belge"], "donem": donem,
                                       "belge_metni": metin},
                                      g4, "belge-ic-toplam"))

    # ── Kaynak B: hata enjeksiyonlu kalibrasyon seti (çoklu neden ağırlıklı) ──
    for i in range(1, 13):
        sen_a, sen_b = rnd.sample([s for s in lib["senaryolar"] if s["beklenen_sinif"].startswith("S4")], 2)
        kurulus = rnd.choice(KURULUSLAR["B"]); donem = rnd.choice(DONEMLER)
        bolme = bolme_sec(kurulus); kisi = kisi_token(rnd)
        snapshot = f"{donem} @ bilgi:2026-06-30"
        p_a = {k: v[0] for k, v in sen_a["parametre_uzayi"].items()}
        p_b = {k: v[0] for k, v in sen_b["parametre_uzayi"].items()}
        imza = motor(sen_a, p_a, rnd)["fark_imzasi"] + motor(sen_b, p_b, rnd)["fark_imzasi"]
        kurallar = sorted(set(sen_a["ihlal_edilen_kural"] + sen_b["ihlal_edilen_kural"]),
                          key=lambda k: int(k[1:]))
        coklu = {"kok_neden_adaylari": [
                    {"sira": 1, "sinif": sen_a["beklenen_sinif"], "hipotez_kodu": sen_a["hipotez_kodu"],
                     "aciklama": ("Fark imzası iki ayrı kalemde birbirinden bağımsız iki bozulma taşımaktadır; "
                                  "birinci bozulma bu hipotezle açıklanmaktadır."),
                     "mevzuat_ref": sen_a["mevzuat_ref"]},
                    {"sira": 2, "sinif": sen_b["beklenen_sinif"], "hipotez_kodu": sen_b["hipotez_kodu"],
                     "aciklama": ("İkinci kalemdeki bozulma birinciyle aynı kök nedene indirgenemez; ayrı bir "
                                  "hipotez olarak raporlanır ve ayrı kanıt ister."),
                     "mevzuat_ref": sen_b["mevzuat_ref"]}],
                 "ayirt_edilebilir": True, "belirsizlik_notu": None,
                 "kanit_talebi": sorted({sen_a["cozen_belge"], sen_b["cozen_belge"]})}
        ortak = dict(kaynak="B", senaryo_id=sen_a["id"], kurulus_id=kurulus, donem=donem,
                     rejim="5746", mevzuat_snapshot=snapshot, bolme=bolme, ihlal_edilen_kural=kurallar,
                     uretim={"uretici": "uret.py", "surum": SURUM, "tohum": tohum,
                             "motor_kosum": hashlib.sha256(f"B{i}{sen_a['id']}{sen_b['id']}".encode()).hexdigest()[:12]})
        girdi = {"fark_imzasi": imza, "uygulanan_kural_surumu": snapshot,
                 "ihlal_edilen_tutarlilik_kurallari": kurallar, "rejim": "5746",
                 "kisi_token": kisi, "donem_araligi": donem,
                 "belge_envanteri": belge_envanteri(sen_a, rnd),
                 "enjeksiyon_notu": "Doğrulanmış gerçek dönem verisi anonimleştirilmiş, üzerine iki bilinen bozulma enjekte edilmiştir."}
        kayitlar.append(kayit(yeni_id("B", sen_a["id"], i, "G1"), "G1", ortak, girdi, coklu, "insa-geregi"))
        ctx = aciklamalar(sen_a, imza, p_a, {"kisi": kisi, "donem_araligi": donem})
        kayitlar.append(kayit(yeni_id("B", sen_a["id"], i, "G2"), "G2", ortak,
                              dict(girdi, onceki_yorum={"hipotez_kodu": sen_a["hipotez_kodu"],
                                                        "sinif": sen_a["beklenen_sinif"]}),
                              g2_cikti(sen_a, ctx), "motor-dogrulamali"))

    # ── yaz ──────────────────────────────────────────────────────────────────
    os.makedirs(os.path.join(KOK, cikti_dizin), exist_ok=True)
    gruplar = defaultdict(list)
    for k in kayitlar:
        gruplar[k["bolme"]].append(k)
    for bolme, ks in gruplar.items():
        yol = os.path.join(KOK, cikti_dizin, f"{bolme}.jsonl")
        with open(yol, "w", encoding="utf-8") as f:
            for k in ks:
                f.write(json.dumps(k, ensure_ascii=False) + "\n")
        print(f"  {bolme:12s} {len(ks):4d} kayıt → {cikti_dizin}{bolme}.jsonl")
    return kayitlar


# ── Kaynak C: pilot mutabakat kayıtları (YER TUTUCU) ─────────────────────────
C_UYARI = ("YER TUTUCU. Gerçek pilot kaydı DEĞİLDİR; pilot verisi ay 10–12'de, gizlilik sözleşmesi ve "
           "anonimleştirme sonrası oluşacaktır (EK-6 §3 Kaynak C). Bu satırlar yalnızca kaynak C'nin "
           "kayıt biçimini ve 'insan kapanış kararı' etiketinin nereye yazıldığını gösterir. Eğitime girmez.")

def kaynak_c_yer_tutucu(tohum, cikti_dizin):
    rnd = random.Random(tohum + 1)
    lib = json.load(open(os.path.join(KOK, "senaryolar", "senaryo-kutuphanesi.json"), encoding="utf-8"))
    kayitlar = []
    for i, (sid, kurulus, bolme) in enumerate(
            [("S01", "KUR-PILOT-01", "kor-test"), ("S05", "KUR-PILOT-01", "kor-test"),
             ("S07", "KUR-PILOT-02", "kalibrasyon")], 1):
        sen = next(x for x in lib["senaryolar"] if x["id"] == sid)
        p = {k: v[0] for k, v in sen["parametre_uzayi"].items()}
        donem = rnd.choice(DONEMLER); kisi = kisi_token(rnd)
        snapshot = f"{donem} @ bilgi:2026-06-30"
        kosum = motor(sen, p, rnd)
        aralik = f"{donem}..{ay_ekle(donem, p['ay_sayisi'] - 1)}" if p["ay_sayisi"] > 1 else donem
        ctx = aciklamalar(sen, kosum["fark_imzasi"], p, {"kisi": kisi, "donem_araligi": aralik})
        ortak = dict(kaynak="C", senaryo_id=sid, kurulus_id=kurulus, donem=donem, rejim="5746",
                     mevzuat_snapshot=snapshot, bolme=bolme,
                     ihlal_edilen_kural=kosum["ihlal_edilen_kurallar"],
                     uretim={"uretici": "uret.py", "surum": SURUM, "tohum": tohum})
        girdi = {"fark_imzasi": kosum["fark_imzasi"], "uygulanan_kural_surumu": snapshot,
                 "ihlal_edilen_tutarlilik_kurallari": kosum["ihlal_edilen_kurallar"],
                 "rejim": "5746", "kisi_token": kisi, "donem_araligi": aralik,
                 "belge_envanteri": belge_envanteri(sen, rnd),
                 "yer_tutucu": True, "uyari": C_UYARI,
                 "kapanis_karari": {"karar_veren": "YMM (anonim)", "oturum": f"mutabakat-oturumu-{i}",
                                    "karsi_gorus": None,
                                    "not": "Gerçek hatta bu alan oturumda yazılır; etiketin kaynağı budur."}}
        kayitlar.append(kayit(f"C-{sid}-p{i:02d}-G1-{9000+i:04d}", "G1", ortak, girdi,
                              g1_cikti(sen, ctx, pi=1), "insan-kapanis"))
    yol = os.path.join(KOK, cikti_dizin, "kaynak-c-yer-tutucu.jsonl")
    with open(yol, "w", encoding="utf-8") as f:
        for k in kayitlar:
            f.write(json.dumps(k, ensure_ascii=False) + "\n")
    print(f"  {'kaynak-C':12s} {len(kayitlar):4d} kayıt → {cikti_dizin}kaynak-c-yer-tutucu.jsonl  (YER TUTUCU)")
    return kayitlar

def belge_envanteri(sen, rnd):
    tum = ["SGK onaylı hizmet listesi", "MUHSGK Tablo-1", "bordro dökümü", "SGK tahakkuk fişi"]
    env = list(tum)
    if sen["beklenen_sinif"] != "S3" and sen["cozen_belge"] not in env and rnd.random() < 0.5:
        pass  # çözen belge bilerek dışarıda bırakılır: G2'nin işi onu istemektir
    return {"mevcut": env, "eksik": [sen["cozen_belge"]] if sen["cozen_belge"] not in env else []}

def belge_metni(belge, donem, tutarli):
    satirlar = {
      "MUHSGK Tablo-1": f"MUHTASAR VE PRİM HİZMET BEYANNAMESİ · TABLO-1 · DÖNEM {donem}\n"
                        f"  Terkine konu matrah .......... 512.480,00\n"
                        f"  Terkin edilen tutar .......... 409.984,00\n"
                        f"  Çalışan sayısı ............... 27\n"
                        f"  ÖZET SATIRI .................. {'409.984,00' if tutarli else '412.100,00'}",
      "SGK onaylı hizmet listesi": f"SGK ONAYLI HİZMET LİSTESİ · DÖNEM {donem}\n"
                        f"  Kanun türü 05746 · prim gün 30 · PEK matrah 188.400,00\n"
                        f"  Kanun türü 5510  · prim gün 30 · PEK matrah  44.200,00\n"
                        f"  ÖZET SATIRI .................. {'232.600,00' if tutarli else '188.400,00'}",
      "Ar-Ge personel ek bildirim XML": f"<ekBildirim donem=\"{donem}\">\n"
                        f"  <kisi token=\"P-3C91A0\" terkin=\"148.200,00\"/>\n"
                        f"  <kisi token=\"P-B47E22\" terkin=\"261.784,00\"/>\n"
                        f"  <toplam>{'409.984,00' if tutarli else '396.500,00'}</toplam>\n</ekBildirim>",
      "SGK tahakkuk fişi": f"SGK TAHAKKUK FİŞİ · DÖNEM {donem}\n  Tahakkuk tutarı 96.412,55 · Belge türü 05746\n"
                        f"  ÖZET SATIRI .................. {'96.412,55' if tutarli else '97.000,00'}",
      "MUHSGK damga vergisi tablosu": f"MUHSGK DAMGA VERGİSİ İSTİSNA TABLOSU · DÖNEM {donem}\n"
                        f"  İstisna tutarı 4.318,20\n  ÖZET SATIRI .................. {'4.318,20' if tutarli else '4.402,00'}",
    }
    return satirlar[belge]

GOREV_TALIMAT = {
 "G1": "Aşağıdaki fark imzasını incele. Kök neden adaylarını olasılık sırasına göre ver, her birini bir mevzuat maddesine bağla.",
 "G2": "Bu bulgu için tek bir somut sonraki adım söyle: hangi belgeye bakılacak, o belgede hangi alan kontrol edilecek.",
 "G3": "Bu bulgu karşısında bir denetçinin soracağı en çok üç soruyu üret. Her soru bir mevzuat maddesine atıf taşısın.",
 "G4": "Aşağıdaki belge metninden yapılandırılmış alanları çıkar ve belgenin kendi özet satırıyla iç toplam kontrolünü yap.",
}

def kayit(kid, gorev, ortak, girdi, cikti, etiket_kaynagi):
    k = {"kayit_id": kid, "gorev": gorev, **ortak, "etiket_kaynagi": etiket_kaynagi,
         "girdi": girdi, "cikti": cikti}
    k["mesajlar"] = [
        {"rol": "sistem", "icerik": SISTEM},
        {"rol": "kullanici", "icerik": GOREV_TALIMAT[gorev] + "\n\n" +
                                      json.dumps(girdi, ensure_ascii=False, indent=2)},
        {"rol": "asistan", "icerik": json.dumps(cikti, ensure_ascii=False, indent=2)},
    ]
    # zarf şemasındaki alan sırası: uretim en sonda
    uretim = k.pop("uretim")
    k["uretim"] = uretim
    return k

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="EK-6 örnek SFT veri seti üreticisi")
    ap.add_argument("--tohum", type=int, default=20260922)
    ap.add_argument("--cikti", default="veri/")
    a = ap.parse_args()
    print(f"Denetci.AI · örnek SFT veri seti · tohum {a.tohum}")
    ks = uret(a.tohum, a.cikti)
    ks += kaynak_c_yer_tutucu(a.tohum, a.cikti)
    print(f"  {'TOPLAM':12s} {len(ks):4d} kayıt")
