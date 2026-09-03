# Oy Verilen Proje (ARGUS) × Mevcut Trendler — Yeniden Değerlendirme

*İki saha sinyali almış ARGUS'un (5746 uyum/hesap platformu), v3 trend araştırmasının dört merceğinden yeniden değerlendirilmesi ve KarbonKanıt ile ilişkisinin netleştirilmesi.*

---

> **⚠️ DÜZELTME (Eylül 2026, doğrulama sonrası):** Bu dokümandaki CBAM/SKDM önerisi iki olgu hatası içeriyordu ve **geçersizdir**: (1) CBAM Tüzüğü (AB) 2023/956 Ek-I listesi çimento, elektrik, gübre, demir-çelik, alüminyum ve hidrojeni kapsar — **seramik kapsamda değildir**, dolayısıyla önerilen Kale/seramik pilotu bu mevzuat için geçersizdi; (2) beyan yükümlüsü AB'deki yetkili bildirimcidir (ithalatçı), Türk üretici değildir — üretici yalnızca alıcısına veri sağlar, ki bu daha zayıf ve türev bir ticari ihtiyaçtır. CBAM ayağı bu nedenle Denetci projesinden **tamamen çıkarılmıştır**; platform tezi 4691 kardeş kural setiyle sınanmaktadır. Güncel ve geçerli kapsam için `denetci-proje-bilgi-formu.md` esas alınmalıdır.



## 1. ARGUS'u v3'ün Dört Merceğinden Geçirince

### Mercek 1 — Trend zamanlaması: 4/5 (mimari rüzgâr güçlü, büyüme yönü yerel)

v3 araştırmasının en çarpıcı bulgusu ARGUS'un aleyhine değil **lehine**: Gartner 2026'nın üç trendi (alan-özgü küçük modeller/DSLM, geopatriation, digital provenance) + KVKK'nın Kasım 2025 Üretken YZ Rehberi (bulut LLM'e prompt = yurt dışına aktarım) + IDC'nin "%70 kompozit YZ'ye geçecek" öngörüsü, ARGUS'un mimari felsefesini (deterministik çekirdek + dar-görevli yerel LLM + kapalı devre CPU masaüstü + hash zincirli değişmez baz) **analist konsensüsüyle ana akım** ilan ediyor. ARGUS trende geç kalmış bir proje değil; trendin önünde tasarlanmış bir proje.

Eksi yönü: ARGUS'un talep tetiği bir büyüme trendi değil, **sabit bir yerel mevzuat**. 5746 teşvikleri 31.12.2028'e kadar uzatılmış durumda — bu hem güvence (2028'e kadar pazar garantili) hem **gölge: sunset/yeniden yapılanma riski**. CBAM'in takvimi ise ters yönde çalışıyor (2026 ücretli dönem → 2028'de ~180 ürüne genişleme).

### Mercek 2 — Pazar: 3/5 (doğrulanmış ama tavanlı)

ARGUS pazarı Türkiye-sınırlı (1.363 Ar-Ge + 342 Tasarım Merkezi; gerçekçi set 400-600), rakipli (ArgeMemory, Ar-GeNet) ve 2028 sonrası belirsiz. KarbonKanıt pazarı bugün yüzlerce AB ihracatçısı + 2028 genişlemesiyle katlanan taban + boş yerli segment. Pazar merceğinde KarbonKanıt açık ara üstün — v3 sıralamasının nedeni bu.

### Mercek 3 — Argelog uyumu + hızlı gelir: 5/5 (kimse ARGUS'u geçemiyor)

Burada tablo tersine dönüyor ve v3'te yeterince vurgulanmayan kritik nokta şu: **ARGUS'un elinde KarbonKanıt'ın sahip olmadığı üç şey var:**
1. **İki gerçek saha oyu** (Kale + ikinci firma) — KarbonKanıt'ın 19/20'si analiz masası puanıdır, henüz tek müşteri "evet"i yoktur. Saha oyu > masa puanı.
2. **Bugün çalışan, Bakanlık-doğrulamalı motor** — CBAM kural seti ise sıfırdan yazılacak (motor mimarisi taşınır ama emisyon faktörleri, AB metodolojisi, doğrulayıcı gereksinimleri ayrı alan bilgisi ister).
3. **Hazır hizmet-önce gelir hattı** — tarama/pilot paketleri tanımlı, ilk fatura haftalar mesafesinde.

### Mercek 4 — Şüpheci: 3/5 (bilinen, yönetilebilir ama gerçek riskler)

ARGUS'un riskleri belgeli: YMM/SMMM alanına yakınlık ve veri kilidi, "kendi hatanı satın alma" direnci, yerli rakiplerin "yeterince iyi" görülmesi, 2028 sunset gölgesi. KarbonKanıt'ın riskleri farklı: AB takvim esnemesi, AB kökenli yazılım/danışmanlık rekabeti ve **doğrulanmamış talep**.

**Yeniden değerlendirme skoru: ARGUS ~15/20** — v3 listesine konsa 2.-3. sıraya oturur; KarbonKanıt'ın (19/20) arkasında ama farkın tamamı pazar tavanından geliyor, uygulanabilirlik ve gelir yakınlığında ARGUS önde.

## 2. Kritik İçgörü: Bu Bir İkilem Değil

ARGUS ve KarbonKanıt **aynı kasın iki uygulaması**: "tarihli bir mevzuatı, Bakanlık/denetçi karşısında savunulabilir deterministik hesap motoruna + kapalı devre dar-LLM veri katmanına çevirmek." Teknopark formundaki Ar-Ge soruları zaten mevzuat-bağımsız yazılmış durumda:

| Ar-Ge sorusu | 5746'da (ARGUS) | CBAM'de (KarbonKanıt) |
|---|---|---|
| AS-1 bitemporal mevzuat versiyonlama | Teşvik oranları, 7555 tavanı | Emisyon faktörleri, AB uygulama tüzükleri, kapsam genişlemeleri |
| AS-2 kök-neden fark teşhisi | Beyan vs yeniden hesap | Beyan edilen vs hesaplanan gömülü emisyon |
| AS-3 güven-yayılımlı kısmi baz | Bordro/beyan eksikleri | Ölçüm vs varsayılan değer hiyerarşisi (CBAM'in tam kendisi) |
| AS-4 küçük-örneklem anomali | Dönem serisi | Üretim dönemi emisyon serisi |
| AS-5 CPU damıtılmış dar LLM | Bordro/belge yapılandırma | Enerji faturası/proses kaydı yapılandırma |

İkinci mevzuat rejimi eklemek Ar-Ge iddialarını sulandırmaz; tam tersine **"çok-rejimli genelleme"** boyutu ekleyerek güçlendirir (hakem karşısında "tek mevzuata özel araç" itirazını da kapatır).

## 3. Önerilen Yol: Çift Regülasyonlu Tek Platform (Seçenek A)

- **Teknopark başvurusu tek projede birleşir:** "Kapalı devre, deterministik **çok-mevzuatlı uyum ve hesap platformu**" — doğrulanmış ilk uygulama 5746 (ARGUS, iki saha oyu + çalışan motor + hızlı gelir), ikinci kural seti ve büyüme motoru CBAM (KarbonKanıt). Mevcut formun %80'i (mimari ilkeler, AS-1..AS-5, BAZ Hattı, CPU/masaüstü, bütçe iskeleti) aynen kalır; kapsam bölümüne CBAM kural seti iş paketi eklenir.
- **Gelir zamanlaması kendiliğinden örtüşüyor:** 2026-27 nakit ARGUS hizmet hattından (oy verilmiş, hazır); 2027-28 büyüme CBAM'den (takvim zorunlu); 2028'de 5746 sunset riski gerçekleşse bile aynı motor CBAM genişlemesiyle büyüyor — **tek platform, iki mevzuatla riskten korunmuş.**
- **Kale çift pilot sahası:** 5746 uyum pilotu (mevcut plan) + seramikte ürün-bazlı gömülü emisyon doğrulaması (U1-R/enerji verisiyle) — tek müşteri ilişkisinden iki hipotezin kanıtı.
- **Doğrulama asimetrisi hemen kapatılmalı:** KarbonKanıt'a saha oyu kazandırmadan büyük yatırım yapılmaz. Zaten planlanan keşif görüşmelerine (Kale + ikinci firma + 2-3 AB ihracatçısı) tek soru bloku eklenir: *"CBAM beyanlarınızı bugün kim, neyle yapıyor; 2028 genişlemesi için planınız ne; denetlenebilir yerli bir motora ne ödersiniz?"* — maliyeti sıfır, iki hipotez aynı görüşmede test edilir.

### Reddedilen alternatifler
- **B) İki ayrı proje:** 10 kişilik ekip iki amiral taşıyamaz (v3'ün kendi tespiti); ortak çekirdek iki kez inşa edilir.
- **C) KarbonKanıt'a tam pivot:** İki gerçek saha oyunu ve haftalar mesafesindeki geliri, henüz tek müşteri konuşulmamış bir fikir için terk etmek olur — masa puanı saha oyunun yerine geçmez.

## 4. Sonraki Somut Adımlar

1. Keşif görüşmesi soru setine CBAM bloku ekle (Kale + ikinci firma + 2-3 ihracatçı) — **saha oyu testi**.
2. Teknopark formunu "çok-mevzuatlı platform" çerçevesine revize et: özet/vizyon + CBAM iş paketi (+2-3 adam-ay bandında, bütçe etkisiyle) — ARGUS omurgası korunarak.
3. TÜBİTAK 1711 penceresi (18 Eylül) ayrı koşuda: SeramLM/DöngüLab/ReçeteİKİZ hattı hibe programı olarak (v3 önerisi geçerli).
4. CBAM alan bilgisi ortağı belirle (karbon/sürdürülebilirlik danışmanı — YMM'nin bu alandaki muadili; kural setinin "madde madde teyit" deseni buraya da uygulanır).

---

*İlgili: `arge-proje-fikirleri-v3-trend.md` (trend araştırması ve 10 fikir), `argus-teknopark-basvuru-formu.md` (korunacak omurga), `arge-proje-fikirleri.md` (ARGUS'un saha sinyalleri ve market-fit analizi).*
