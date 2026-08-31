# Proje Fikirleri v2 — Sıfırdan Yeniden Değerlendirme

*İlk 10 fikir ve ARGUS yönü "tam uygun olmadı" geri bildirimi üzerine, oturum boyunca netleşen gerçek kısıtlar filtre alınarak yapılan yeniden değerlendirme ve yeni amiral proje önerisi.*

---

## 1. Önce Dürüst Teşhis: İlk 10 Fikir Neden Tam Oturmadı

1. **Hepsi yönetim/uyum katmanıydı, teknik Ar-Ge'nin kendisi değildi.** TEYDEB, TRL, portföy riski, RegTech... alıcısı dar bir yönetici kesiti; "herkesin ihtiyacı" değil. Oysa oturumda kalbin nerede attığı belliydi: **Kale'nin reçete + kalite + laboratuvar verisi, U1-R döngüsü** — yani deneyin, formülün, üretim sonucunun dünyası. 10 fikrin hiçbiri orada değildi.
2. **RegTech (ARGUS) YMM/danışman alanına fazla yakın.** 3568 sınırları, SMMM veri kilidi, "kendi hatanı satın alma" direnci — hepsi analizlerde tespit edildi; her biri yönetilebilir ama toplamı sürtünmeli bir satış demek.
3. **Kapalı devre + CPU + kişisel bilgisayar + kolay kullanım kısıtları sonradan geldi** ve eski listenin yarısını (tech scouting, açık inovasyon ağı, foresight) yapısal olarak eledi.
4. **"Hızlı para + herkesin ihtiyacı" çifti hiçbirinde tam yoktu:** ya mevzuat kancası vardı ama niş (ARGUS), ya geniş ama uzak (platform fikirleri).

**Geçerliliğini koruyanlar:** pazar verileri (1.363 Ar-Ge + 342 tasarım merkezi + 11.000+ teknopark firması), hesap çekirdeği varlığı, BAZ Hattı'nın "retrospektif içeri alma → doğrulama → hafızaya dönüştürme" deseni ve ARGELOG.AI vizyonu. Bunlar atılmıyor; yeniden konumlanıyor.

## 2. Yeni Filtre — Oturumdan Damıtılan 7 Kriter

Bir fikir ancak şunların tamamına uyuyorsa aday:

| # | Kriter |
|---|---|
| K1 | Kapalı devre, **CPU-yalnız, sıradan kişisel bilgisayarda** çalışan masaüstü ürün |
| K2 | **Kolay kullanım:** kurulumdan ilk değere ≤1 saat, BT projesi değil |
| K3 | **Herkesin ihtiyacı:** alıcı tabanı yönetici nişi değil, Ar-Ge yapan herkes |
| K4 | **Hızlı para:** hizmet-önce gelir veya haftalar içinde satılabilir lisans |
| K5 | **Deterministik çekirdek asıl, LLM dar-görevli** (hesap/kayıt/versiyon motoru; YZ süs değil destek) |
| K6 | Argelog'un gerçek varlıklarını kullanır: alan bilgisi, hesap çekirdeği kodu, İSO 100 ilişkileri, **Kale erişimi** |
| K7 | **ARGELOG.AI vizyonunu besler:** veri → analiz → uzman onayı → doğrulanmış hafıza döngüsünü kurar |

## 3. Yeni Fikir Kümesi (teknik Ar-Ge'nin kendisine dönük)

| # | Fikir | Ne | K-filtre notu |
|---|---|---|---|
| Y1 | **Ar-Ge Defteri** ⭐ | Kapalı devre masaüstü deney/reçete kayıt ve kurumsal Ar-Ge hafıza sistemi (aşağıda detay) | 7/7 — amiral aday |
| Y2 | Kurumsal Ar-Ge Hafıza Motoru | Şirket içi teknik arşiv (raporlar, deney kayıtları, şartnameler) üzerinde tamamen yerel arama + soru-cevap ("şirket içi Google") | Güçlü; Y1'in doğal modülü — bağımsız da satılır |
| Y3 | Reçete/Formülasyon Sürüm Kontrolü | "Formülasyonun Git'i": reçete versiyonlama, fark görme, lab/üretim sonucu bağlama, sapma istatistiği — seramik/kimya/boya/gıda | Kale'nin tam ihtiyacı; Y1'in çekirdek modülü |
| Y4 | Deney Tasarım Sihirbazı (DoE-lite) | Mühendis için basit deney planlama + sonuç istatistiği; deterministik istatistik çekirdeği, LLM yalnız açıklama dili | Y1 üstüne v2 modülü |
| Y5 | Teknik Rapor Fabrikası | Deney/test verisinden tek tık Türkçe teknik rapor + TEYDEB/faaliyet raporu kanıt eki | Y1'in çıktı katmanı; tek başına da hizmet ürünü |
| Y6 | Üretim Sapma Günlüğü | Üretimdeki sapma/uygunsuzlukların kök-neden kayıt zinciri (hafif 8D/CAPA), Ar-Ge'ye geri besleme | Kalite ekiplerine yayılım; v2+ |

**Desen açık:** Y2, Y3, Y5 aslında Y1'in modülleri; Y4 ve Y6 doğal genişlemeleri. Yani yeniden değerlendirme tek bir amiral projeye yakınsıyor.

## 4. Önerilen Amiral Proje: **AR-GE DEFTERİ** (çalışma adı; "DENEY" / "LabOS" alternatif)

### 4.1 Tek cümle

Türkiye sanayisinin Ar-Ge'sini Word/Excel dağınıklığından kurtaran; kapalı devrede, sıradan bilgisayarda çalışan; deneyi, reçeteyi, laboratuvar ve üretim sonucunu tek yapılandırılmış zincirde kaydedip **kurumun aranabilir, sorgulanabilir, kanıt üreten Ar-Ge hafızasına** dönüştüren masaüstü sistem.

### 4.2 Ne yapar (çekirdek özellik seti — kolay kullanım önce)

- **Kayıt:** Deney/deneme kaydı sihirbazla: amaç → reçete/malzeme (versiyon zincirli) → proses parametreleri → ölçüm/lab sonucu → sonuç ve karar → uzman yorumu. Excel/CSV/fotoğraf sürükle-bırak; serbest notu **yerel küçük LLM şemaya yapılandırmayı önerir**, mühendis onaylar (dar görev, insan onaylı).
- **Hafıza:** Tamamen yerel arama + soru-cevap: "B-347 katkısıyla yaptığımız pişirimlerde küçülme ne çıkmıştı, kim çalışmıştı?" — kaynak kayıtlara bağlantılı cevap (CPU'da embedding + küçük model).
- **Kanıt:** Her kayıt zaman damgalı ve değişmez zincirde (hash) — buluş tarihi kanıtı, TEYDEB/faaliyet raporu için **faaliyet kanıt paketi tek tıkla** (5746 alan bilgimiz burada yan ürün olarak parlar), denetimde "bu projeyi gerçekten çalıştık" dosyası.
- **Analiz:** Reçete sürümleri arası fark + sonuç karşılaştırması, temel sapma istatistiği (deterministik); v2'de DoE-lite.
- **Rapor:** Kayıtlardan tek tık Türkçe teknik rapor/deney raporu (LLM yalnız dil katmanı, tüm sayılar kayıttan).
- **Kapalı devre yaşam döngüsü:** imzalı offline şablon/şema güncellemeleri; veri hiç dışarı çıkmaz.

### 4.3 Neden 7 kriteri de geçiyor

- **K1-K2:** Masaüstü, CPU-yalnız (kayıt/versiyon/arama zaten hafif; LLM görevleri batch ve dar), kurulumdan ilk kayda 15 dakika.
- **K3 — gerçek "herkes":** Her Ar-Ge merkezi, her teknopark firması, üniversite lab'ları, hatta tek mühendis. Bugünkü alternatif Word/Excel/OneNote dağınıklığı; global ELN'ler (Benchling, LabArchives, eLabFTW) bulut-öncelikli, İngilizce, biyoteknoloji-eğilimli ve KVKK-hassas sanayide zayıf. *Türkçe, kapalı devre, sanayi-odaklı masaüstü ELN kategorisi görünürde boş (doğrulama: keşif görüşmeleri + hızlı pazar taraması).*
- **K4 — hızlı para:** (a) **"Ar-Ge Arşivi İçeri Alma" hizmeti** — müşterinin dağınık geçmiş deney arşivini yapılandırılmış hafızaya dönüştürme (BAZ Hattı'nın retrospektif deseninin buradaki karşılığı; concierge, hemen faturalanır); (b) masaüstü lisans (düşük fiyat × geniş taban); (c) Kale reçete pilotu — U1-R süreciyle birebir.
- **K5:** Çekirdek deterministik (kayıt, versiyon zinciri, hash, istatistik); LLM üç dar görevde (not yapılandırma önerisi, arama-cevap, rapor dili) — ARGUS'ta kurduğumuz mimari felsefe aynen taşınır.
- **K6:** Kale = tasarım ortağı ve ilk pilot (reçete+lab verisi); 5746/TEYDEB bilgisi kanıt paketi modülünde; BAZ Hattı/immutable zincir mimarisi yeniden kullanılır.
- **K7 — ARGELOG.AI'nin ta kendisi:** Strateji dokümanındaki **şema moat'ı** (`reçete → proses → lab → üretim → sapma → uzman yorumu`) bu ürünün veri modelidir; Deney Döngüsü bu üründe yaşar; "müşteri-içi veri zekâsı lock-in"i her kayıtla büyür. Ajanlar (sapma analizi, reçete önerisi) bu hafızanın üstüne gelir.

### 4.4 Teknopark başvurusu için Ar-Ge niteliği (ön taslak)

- **AS-a:** Türkçe serbest teknik notların (sektör jargonlu) dar-görevli küçük modelle, CPU'da, şema-zorlamalı yapılandırılması — doğruluk/hız sınırlarının karakterizasyonu (ARGUS AS-5'in devamı, farklı alan).
- **AS-b:** Sektör-uyarlanabilir deney zinciri ontolojisi: tek çekirdek şemanın seramik/kimya/metal gibi alanlara kayıpsız özelleşmesi ve alanlar arası sorgulanabilirlik.
- **AS-c:** Değişmez, süpersedans-versiyonlu kayıt zincirinin (BAZ mimarisi) hukuki kanıt değeri taşıyan deney defteri olarak biçimselleştirilmesi (zaman damgası, bütünlük, erişim izi).
- **AS-d:** Küçük-örneklem deney serilerinde reçete-sonuç ilişkisinden sapma/anomali işaretleme (ARGUS AS-4 deseninin deney verisine taşınması).

### 4.5 Hızlı gelir iskeleti

| Basamak | Ürün | Zaman |
|---|---|---|
| 1 | Kale ile "Reçete Hafızası" ücretli keşif pilotu: bir reçete ailesinin geçmiş deney/lab arşivini şema v0'a içeri alma + retrospektif "sapmayı önceden görebilir miydik?" analizi | Hafta 2-8 |
| 2 | "Ar-Ge Arşivi İçeri Alma" concierge hizmeti (2-3 mevcut müşteriye) | Ay 2-4 |
| 3 | Masaüstü lisans v1 (kayıt+arama+kanıt paketi) + offline güncelleme aboneliği | Ay 5-8 |
| 4 | TEYDEB kanıt paketi modülü upsell; DoE-lite v2 | Ay 8+ |

### 4.6 ARGUS ne olacak?

Ölmesin — **konum değişsin:** hesap çekirdeği ve BAZ Hattı tasarımı değerli varlıklar. Üç seçenek (karar senin):

- **A) Ar-Ge Defteri amiral, ARGUS modül:** Teknopark başvurusu Ar-Ge Defteri üzerine kurulur; 5746 kanıt/uyum yetenekleri Defterin bir modülü olur; hesap çekirdeği o modülde yaşar. *(Önerim bu — "herkesin ihtiyacı" ve Kale enerjisiyle hizalı.)*
- **B) İki ayrı ürün, Defter önce:** Defter amiral proje; ARGUS hizmet-önce gelir planıyla (tarama/pilot) satılmaya devam eder, ürünleşmesi ertelenir.
- **C) ARGUS devam:** Mevcut başvuru korunur, Defter H2 keşfi olarak paralel yürür (önceki plan).

## 5. Sonraki Adım

Seçenek A onaylanırsa: teknopark başvuru formunu Ar-Ge Defteri üzerine yeniden kurarım (mevcut formun CPU/kapalı devre/kolay kullanım omurgası aynen taşınır — büyük kısmı hazır), Kale keşif pilotunun tek sayfalık kapsamını çıkarırım ve şema v0 taslağını yazarım.

---

*İlgili: `arge-proje-fikirleri.md` (v1 analizleri — pazar verileri geçerli), `argelog-ai-strateji.md` (şema moat'ı ve döngüler), `argus-teknopark-basvuru-formu.md` (taşınacak omurga), `argus-baz-hatti-tasarimi.md` (değişmez zincir mimarisi).*
