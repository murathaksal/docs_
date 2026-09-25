# Hakem Toplantısı Sonrası Düzeltme Raporu (Portal Çıktısı v8)

*Bu rapor, 25.09.2026 10:13 tarihli portal çıktısını (Proje Bilgi Formu, 14 sayfa) hakem heyetinin geri bildirimine göre inceler. Heyetin üç notu vardır: (1) metinde yazım hataları var; (2) bütçe sunumda 7 milyon ₺, form metinlerinde ise farklı; (3) 1-4 milyar parametreli modelin "30 saniyenin altında cevap vermesi" hedefinin ucu çok açık. Her madde için portalın hangi sayfasında ve hangi alanında ne yazdığı, yerine ne yazılacağı gösterilmiştir. Karşılaştırmada `denetci-proje-bilgi-formu.md` (ana belge), EK-3, EK-4 ve EK-7 esas alınmıştır.*

---

## Özet

| # | Konu | Durum | Kök neden |
|---|---|---|---|
| 1 | **Bütçe** | Formda üç ayrı toplam var: **6.470.000 ₺** (kimlik alanı ve bütçe tablosu), **6.600.000 ₺** (Proje Detayı metni) ve sunumdaki **7.000.000 ₺** | Proje Bütçesi tablosu ve Proje Detayı metni eski sürümde kalmış |
| 2 | **1-4 milyar / 30 sn** | Proje Özeti'nde model boyutu hâlâ "4-16 milyar". 30 sn ölçütü tanımsız, risk (8) ise ölçütü yanlışlanamaz kılıyor | Ölçüt, EK-7'deki iki kademeli model kararı forma yansıtılmadan yazılmış |
| 3 | **Yazım** | Firmanın düzeltebileceği 9 madde, portal şablonuna ait 5 madde | Bir kısmı ana belgede de var; ana belgeden yeniden yapıştırılınca hatalar geri gelir |
| 4 | **Eski sürüm kalıntıları** | İş paketi adam-ayları, senaryo sayısı, Ar-Ge merkezi sayısı, patent kutuları | Proje Detayı ve Hedeflenen Kazanımlar alanları ana belgenin güncel hâliyle yenilenmemiş |
| 5 | **Karar gerekiyor** | Proje Ekibi ekranında 6 kişi var, bütün metinler ise 4 kişi diyor. Ayrıca portalın iş gücü alanları beklenenden farklı hesaplıyor | §5 |

**Ana bulgu:** Hakemin gördüğü farkların çoğunun nedeni aynıdır. Portaldaki **Proje Detayı**, **Hedeflenen Kazanım ve Sonuçlar** ve **Proje Bütçesi** alanları, ana belgenin 11.09.2026 sonrasındaki güncel hâline göre güncellenmemiştir. `portal-v5-kontrol-raporu.md` dosyasındaki A1, A3, A4, A5, B2, B7, B8, B9, C1 ve C4 maddeleri v8'de de açıktır.

---

## 1. Bütçe: tek toplam, 7.000.000 ₺

### 1.1 Bütçenin geçtiği yerler

| Yer (portal sayfası, alan) | Şu an | Olması gereken |
|---|---|---|
| s. 2, Kimlik: Tahmini Proje Bütçesi | 6.470.000,00 ₺ | **7.000.000,00 ₺**. v5 ve v8'de bu alan bütçe tablosunun toplamına eşit, yani tablo düzelince kendiliğinden güncellenmesi beklenir. Güncellenmezse elle girilmelidir |
| s. 10, Proje Detayı: "Bütçe kırılımı (6.600.000 ₺)" | 6.600.000 ₺, 7 satır, 36 adam/ay | **7.000.000 ₺, 9 satır, 39 adam/ay** (bkz. §1.3) |
| s. 11, Proje Bütçesi tablosu | 6.470.000 ₺, 7 satır | **7.000.000 ₺, 9 satır** (bkz. §1.2) |
| s. 12, Alınacak Dış Hizmetler | 550.000 / 200.000 / 250.000 TL | Doğru, değişmeyecek. Bütçe tablosundaki GPU satırı bu metne göre düzeltilir |
| s. 14, Proje Ekipman Listesi | boş | 2 satır (bkz. §1.4) |

### 1.2 Proje Bütçesi tablosu (s. 11), satır satır

| # | Harcama Kategorisi | Harcama Adı | Şu an | Olması gereken | İşlem |
|---|---|---|---|---|---|
| 1 | Personel Giderleri | 39 Adam Ay | 5.070.000,00 | 5.070.000,00 | değişmeyecek |
| 2 | Hizmet Alımları | YMM hizmeti ve hukuk görüşü | 550.000,00 | 550.000,00 | değişmeyecek |
| 3 | Hizmet Alımları | Bulut GPU-grafik işlemci kiralama | 250.000,00 | **200.000,00** | tutar düzeltilecek |
| 4 | Hizmet Alımları | Patent, marka tescili ve akademik danışmanlık | 250.000,00 | 250.000,00 | değişmeyecek |
| 5 | Hizmet Alımları | Yazılım lisansları, kod imzalama sertifikası ve imza altyapısı | yok | **200.000,00** | **eklenecek** |
| 6 | Makina ve Teçhizat Giderleri | 3 geliştirici iş istasyonu ve 2 referans test bilgisayarı | yok | **300.000,00** | **eklenecek** |
| 7 | Seyahat Giderleri | Pilot saha ziyaretleri, konferans | 200.000,00 | **230.000,00** | tutar düzeltilecek |
| 8 | Sarf Giderleri | Test ortamı ve ofis sarf | 50.000,00 | 50.000,00 | değişmeyecek |
| 9 | Genel Giderler | Öngörülemeyen pay | 100.000,00 | **150.000,00** | tutar düzeltilecek |
| | | **Toplam** | **6.470.000,00** | **7.000.000,00** | |

*Sağlama:* 6.470.000 − 50.000 + 200.000 + 300.000 + 30.000 + 50.000 = 7.000.000.

### 1.3 Proje Detayı içindeki bütçe kırılımı (s. 10)

Bu paragrafın başlığı ve yedi satırı eski sürümdendir. Değişecek satırlar:

| Şu an | Olması gereken |
|---|---|
| "Bütçe kırılımı (6.600.000 ₺)" | "Bütçe kırılımı (7.000.000 ₺)" |
| "Personel: 36 adam/ay × 130.000 ₺ … 4.680.000" | "Proje personeli: 39 adam/ay × 130.000 ₺ … 5.070.000" |
| "Pilot saha seyahati, dış eğitim/etkinlik ve öngörülemeyen giderler … 420.000" | Üç satıra bölünür: Seyahat **230.000**; Sarf **50.000**; Öngörülemeyen giderler payı **150.000** (toplam 430.000) |
| "Donanım: 3 geliştirici iş istasyonu + 2 referans test bilgisayarı 300.000" | Tutar aynı kalır, referans bilgisayarın tanımı eklenir: "(4 çekirdek, 16 GB bellek, grafik işlemcisiz)". §2'deki süre ölçütü bu makineye bağlanacaktır |

YMM (550.000), lisans (200.000), patent/akademik danışmanlık (250.000) ve bulut GPU (200.000) satırları değişmez. **En kısa yol:** bu bloğu silin ve ana belgedeki "Bütçe kırılımı (7.000.000 ₺)" tablosunu olduğu gibi yapıştırın. Bu tablo, portalın harcama kategorileriyle birebir eşleşen dokuz satırdan oluşur.

### 1.4 Proje Ekipman Listesi (s. 14)

| Ekipman | Adet | Not |
|---|---|---|
| Geliştirici iş istasyonu | 3 | Bütçe tablosu satır 6 |
| Referans test bilgisayarı (4 fiziksel çekirdekli x86-64 işlemci, 16 GB bellek, grafik işlemcisiz) | 2 | Kazanım 1'deki süre ölçümü bu makinelerde yapılır |

### 1.5 Bütçeye bağlı adam/ay rakamları

| Yer | Şu an | Olması gereken |
|---|---|---|
| s. 2, Kimlik: Ar-Ge / Destek / Toplam İş Gücü | 6 / 0 / 6 | Toplamda 39 adam/ay verecek değerler (bkz. §5.2) |
| s. 2, Toplam Proje İş Gücü | 72 | **39** |
| s. 9, İP tablosu: İP4 / İP5 / Toplam | 8 / 8 / "36 (28 Ar-Ge + 8)" | **9 / 10 / "39 (31 Ar-Ge + 8)"** (sunumda da İP5 10 adam-ay olarak anlatıldı) |
| s. 9, Ekip paragrafı | "ortalama 3 tam zaman eşdeğeri" | "ortalama 3,25 tam zaman eşdeğeri" (39 ÷ 12) |
| s. 11, Bütçe tablosu, Personel satırı | 39 Adam Ay | doğru |

---

## 2. 1-4 milyar parametreli model ve "30 saniye" ölçütü

### 2.1 Çelişki: Proje Özeti'nde farklı model boyutu

**s. 3, Proje Özeti:** "…4-16 milyar parametre sınıfında, grafik işlemcisiz bir bilgisayarda çalışan yerel bir modelin…" ifadesi **"1-4 milyar parametre sınıfında"** olarak düzeltilmelidir. Kazanım 1 (s. 4) ve AS-1 (s. 5) zaten 1-4 milyar diyor. 16 milyar parametreli bir model nicemlenmiş hâlde bile yaklaşık 9-10 GB yer kaplar ve 16 GB bellekli, grafik işlemcisiz bir makinede bulgu başına dakikalar sürer; yani bu ifade 30 sn hedefini baştan geçersiz kılıyor.

### 2.2 Ucun açık kaldığı noktalar

Kazanım 1'deki mevcut ifade şöyledir: *"16 GB bellekli, grafik işlemcisiz referans bilgisayarda bulgu başına ≤30 saniye."* Bu ifadenin altı açık ucu var:

| Açık uç | Neden sorun | Nasıl kapatılır |
|---|---|---|
| **Hangi model?** | 1-4 milyar bandı içinde hız yaklaşık 4 kat değişir. EK-7'ye göre doğruluk hedefleri 4 milyarlık *kalite kademesinde*, 30 sn hedefi ise 1,7 milyarlık *etkileşim kademesinde* tutuyor. Yani iki hedef iki ayrı modelle "tutturulmuş" gösterilebilir | Eşikler kademe bazında ayrı yazılır |
| **Süreye neler dâhil?** | Girdi işleme (ön-doldurma), doğrulama kapısı ve model yükleme süresinin dâhil olup olmadığı belirsiz. EK-7 §3 bu soruyu "Faz 0'da netleşecek" diyerek açık bırakıyor | Uçtan uca süre; model yükleme ayrı raporlanır |
| **Girdi/çıktı uzunluğu** | Süre, işlenen simge sayısıyla doğrusal artar ve şu an bir sınır yok | En fazla 2.500 girdi ve 250 çıktı simgesi (EK-7'deki Kapı K1 profili) |
| **Hangi istatistik?** | Ortalama mı, medyan mı, en kötü durum mu belli değil | Kör test setinin tamamında %95'lik dilim; medyan ayrıca raporlanır |
| **Hangi donanım?** | "16 GB, grafik işlemcisiz" ifadesi işlemciyi tanımlamıyor; 4 çekirdekli makineyle 16 çekirdekli makine arasında kat kat fark var | 4 fiziksel çekirdekli x86-64 işlemci (AVX2), 16 GB çift kanal bellek, çıkarım yazılımının sürümü sabit |
| **Kaçış maddesi** | Risk (8) şöyle diyor: "süre hedefi tutmazsa bulgu üretimi arka planda toplu işlem olarak çalıştırılır ve kullanıcı akışı etkilenmez". Bu hâliyle ölçüt hiçbir koşulda başarısız olamaz, yani yanlışlanamaz. Oysa formun geri kalanı her ölçütü yanlışlanabilir olarak tanımlıyor | Hedef tutmazsa olumsuz sonuç olarak raporlanır |

### 2.3 Yerine yazılacak metinler

**(a) s. 4, Kazanım 1:** "…bulguların ≥%80'ini yakalaması (kör karşılaştırma); 16 GB bellekli, grafik işlemcisiz referans bilgisayarda bulgu başına ≤30 saniye." cümlesinde noktalı virgülden sonraki kısım silinir. Yerine şu metin yazılır:

> …bulguların ≥%80'ini yakalaması (kör karşılaştırma). *Yanıt süresi:* Model, aynı aileden ve aynı eğitim hattından çıkan iki kademede ölçülür (EK-7). Yukarıdaki başarım eşikleri **kalite kademesi** (en fazla 4 milyar parametre) için geçerlidir; bu kademe arka planda toplu çalışır ve referans bilgisayarda saatte en az 40 bulgu işler. Kullanıcının ekranda beklediği **etkileşim kademesinde** (en fazla 2 milyar parametre) bir bulgunun uçtan uca süresi, kör test setinin tamamında %95'lik dilimde ≤30 saniyedir; bu kademenin araştırma yönlendirme isabeti, aynı sette kalite kademesinin en az %90'ı düzeyindedir. Süre; girdinin işlenmesi (toplam girdi ≤2.500 simge, ortak sistem istemi önbellekte), şema-zorlamalı çıktı üretimi (≤250 simge) ve sembolik doğrulama kapısı dâhil ölçülür; modelin belleğe ilk yüklenme süresi ayrıca raporlanır. Süre ve başarım aynı nicemlenmiş model dosyasıyla ölçülür. *Referans bilgisayar:* 4 fiziksel çekirdekli x86-64 işlemci (AVX2), 16 GB çift kanal bellek, grafik işlemcisiz; çıkarım yazılımının sürümü sabitlenir.

**(b) s. 9, İP5 çıkış kriteri:** "bulgu başına ≤30 sn" ifadesinin yerine şu yazılır: "etkileşim kademesinde uçtan uca süre %95'lik dilimde ≤30 sn; kalite kademesinde saatte ≥40 bulgu (tanımlar Kazanım 1'de)".

**(c) s. 10, risk (8):** Maddenin tamamı şu metinle değiştirilir:

> (8) *Grafik işlemcisiz çıkarım süresinin hedefi aşması*: model boyutu ve nicemleme düzeyi referans bilgisayarda ölçülerek seçilir (EK-7, ölçüm protokolü). Etkileşim kademesi süre ölçütünü sağlayamazsa ürün bulguları arka planda toplu işlemle üretmeye devam eder; ancak bu durumda Kazanım 1'in süre ölçütü karşılanmamış sayılır ve ölçülen süre dağılımıyla birlikte olumsuz sonuç olarak raporlanır.

**(d) s. 5, AS-1 (isteğe bağlı, tutarlılık için önerilir):** "1-4 milyar parametre sınıfında" ifadesinden sonra "(etkileşim kademesi en fazla 2, kalite kademesi en fazla 4 milyar; EK-7)" eklenir.

### 2.4 Sayıların dayanağı ve onayınızı gerektiren noktalar

- **30 sn ve 1,7 milyar:** EK-7 §3'teki tahmine göre 250 simgelik çıktı 13-21 saniyede üretilir; kalan süre girdi işleme ve doğrulama kapısı için bırakılmıştır. 4 milyarlık model aynı çıktıyı 28-50 saniyede üretir ve buna girdi işleme de eklenir. Bu nedenle kalite kademesine süre hedefi değil, iş hacmi hedefi konmuştur. Saatte 40 bulgu, bulgu başına ortalama 90 saniye demektir ve EK-7'deki tahmin bandının güvenli tarafında kalır.
- **Bu sayılar tahmindir.** Kesin değerler EK-7 Faz 1'de (Kapı K1) referans makinede ölçülecektir. Forma girmeden önce iki eşiği onaylamanız gerekiyor: **saatte en az 40 bulgu** ve **%90 koruma oranı**. Daha az bağlayıcı bir seçenek de var: %90 şartının yerine "etkileşim kademesinin başarımı aynı kör sette ayrıca raporlanır" yazılabilir. Ancak bu durumda hakem "hızlı model işe yarıyor mu?" sorusunu yeniden sorabilir.
- **Önerilmeyen seçenek: tek model, tek eşik.** 4 milyarlık model 30 saniyeyi tutturamaz (EK-7 §3). Bütün doğruluk eşiklerini 1,7 milyarlık modelle taahhüt etmek ise AS-1'in olumsuz sonuçlanma riskini gereksiz yere artırır.

---

## 3. Yazım hataları ve dil birliği

| # | Yer (sayfa, alan) | Şu an | Düzeltme | Ana belgede de var mı? |
|---|---|---|---|---|
| Y1 | s. 4, Kazanım 4 | "2022 asgari geçim indirimi **kaldırımı**" | "…asgari geçim indiriminin **kaldırılması**". Kaldırım "yaya yolu" demektir | **Evet**, satır 73 |
| Y2 | s. 10, Proje Ekibi, Mesut Çakır'ın görev adı | "Backend **Yazilimci**" | "**Kıdemli Yazılım Geliştirici**". Hem "ı" harfleri düzelir hem de Proje Detayı'ndaki rol adıyla aynı olur | Hayır (portal kaydı) |
| Y3 | s. 3, Proje Özeti ilk paragraf ("nöro-sembolik yapay **zeka** sistemidir"); s. 3, Anahtar Kelimeler; s. 10, Proje Ekibi görev adları ("Yapay Zeka") | "zeka" | "**zekâ**". Metnin kalanında 21 yerde "zekâ" yazılı; yazım tek biçimde olmalı. Proje adında portal şapkalı harfi kabul etmiyorsa ad olduğu gibi bırakılabilir, çünkü üst yazı da bu alandan üretiliyor | Hayır |
| Y4 | s. 3, Anahtar Kelimeler | "Denetim Savunma dosyası" | "denetim savunma dosyası" (büyük/küçük harf birliği). Liste de kısa, bkz. §4 T6 | Hayır |
| Y5 | s. 2, Mevcut THS açıklaması | "mutabakat **altsistemi**" | "mutabakat **alt sistemi**" (TDK'ye göre ayrı yazılır) | **Evet**, satır 28 |
| Y6 | s. 9, İP2 kapsamı | "**as-of** yeniden üretim" | "geçmiş bir tarihteki bilgi durumuyla (as-of) yeniden üretim". Türkçe metinde açıklamasız tek İngilizce terim | **Evet**, satır 196 |
| Y7 | s. 4, Proje Özeti sonu | "Katma değer **(iki cümlelik sıralama)**: Geri kazanım toplantıyı açar, denetim savunulabilirliği sözleşmeyi kapatır." | Başlık yalnızca "Katma değer:" olmalı. Cümle şöyle değiştirilmeli: "Ürünün ilk değeri geçmiş dönemlerden geri kazanım, kalıcı değeri denetimde savunulabilirliktir." Parantez içindeki ifade bir taslak notu; "toplantıyı açar / sözleşmeyi kapatır" ise satış dili ve hakem formuna uymuyor | **Evet**, satır 57 |
| Y8 | s. 13, Rekabet Analizi, ilk cümle | "**yedi** ürün/hizmet **kategorisi** taranmıştır" ama sonrasında beş grup sayılıyor | "yedi ürün ve hizmet kalemi taranmış (EK-1), genel amaçlı bulut yapay zekâ araçlarıyla birlikte beş grupta değerlendirilmiştir" | **Evet**, satır 263 |
| Y9 | s. 11, Ekonomik Değeri | "150 kişilik bir merkezde yıllık teşvik akışı **yüz milyon TL düzeyine ulaşır**" | 150 × ~1 milyon = ~150 milyon; ifade "yüz milyon TL'yi aşar" olmalı | **Evet**, satır 235 |

**Portal şablonuna ait hatalar (firma düzeltemez):** "Proje **Kampsamında** Teknoparktan Talep Edilen Hizmetler" (s. 7), "**Labaravutar**" ve "**Yapıılabilirlik**" (s. 8), "**Döküman** No" (s. 2), "Fikri **Sinai**" (s. 13). Bunlar teknoparkın form etiketleridir. Hakem sorarsa böyle açıklanabilir; istenirse teknopark yönetimine de bildirilebilir.

---

## 4. Eski sürümden kalan diğer farklar (hakem söylemedi, kökleri aynı)

| # | Yer | Şu an | Olması gereken |
|---|---|---|---|
| T1 | s. 3, Proje Özeti | "**1.300'ü** aşkın Ar-Ge ve Tasarım Merkezi" | "**1.700'ü** aşkın". Aynı formun Hedef Pazar bölümü (s. 12) ve sunum 1.720 diyor |
| T2 | s. 4 Kazanım 3; s. 9 İP4; s. 10 risk (5) | "≥**60** senaryoluk kütüphane" | "≥**150** senaryoluk". İP4'e ayrıca "(senaryo başına en fazla 12 parametrik türetme)" ve "≥40 farklı hata tipli enjeksiyon kalibrasyon seti" ifadeleri eklenir (ana belgede R1 düzeltmesi) |
| T3 | s. 4, Kazanım 1 ve 2 | Örneklem büyüklüğü yazılmamış | Ana belgedeki "asgari 400 kalem / 150 kalem, örneklem gerekçesi" ve "≥300 atıf / ≥400 bulgu" cümleleri eklenir |
| T4 | s. 9, Ekip paragrafı | "bir yapay zekâ/doğal dil işleme mühendisi" | "bir **tam zamanlı** yapay zekâ/doğal dil işleme mühendisi"; parantez içi "(4 kişi, ortalama 3,25 tam zaman eşdeğeri; kıdemli geliştirici ve yapay zekâ mühendisi tam zamanlı; efor dağılımı EK-4)". *§5.1'deki karara bağlı* |
| T5 | s. 11, Patent Çıktısı Var Mı | "Yok" | "**Var**". s. 8'de "Patent ve Lisans Çalışmaları" işaretli, bütçede de patent satırı var; "Yok" bunlarla çelişiyor |
| T6 | s. 3, Anahtar Kelimeler | 4 kavram | Ana belgedeki 15 kavramlık liste. Karakter sınırı varsa ilk sekiz kavram girilir |
| T7 | s. 7, Teknoparktan Talep: PATENT, MARKA TESCİL | işaretsiz | İşaretlenmeli |
| T8 | s. 8, Ar-Ge Aşamaları: Prototip Geliştirme | işaretsiz | İşaretlenmeli (hedef THS 7, prototipin gerçek ortamda denenmesidir) |
| T9 | s. 2, İlişkili Sektörler | "**Ambalaj**, Petrol ve Petrol Ürünleri, Yazılım" | "Ambalaj" hiçbir pilotla ilişkili değil. Kale Seramik pilotuna karşılık gelen "**Seramik ve Refrakter**" seçilmeli (bu seçenek portal listesinde var, s. 11) |
| T10 | s. 2, Proje Tahmini Bitiş Tarihi | boş | 25.10.2027 |
| T11 | s. 13, Fikri Sınai ve Mülkiyet Hakları; Projeye Ait Ürünler | boş | `portal-doldurma-kontrol-listesi.md` A7 ve v5 raporu B7-B8'deki satırlar |
| T12 | s. 7, Proje Ortaklığı | Tüpraş "aynı il" | Pilot sahası Kocaeli ise "farklı il" olmalı (teyit edilecek) |

---

## 5. Karar gerektiren iki konu

### 5.1 Ekip 4 kişi mi, 6 kişi mi?

Portaldaki **Proje Ekibi** ekranında (s. 10) 6 kişi var: Murat Haksal (Proje Yöneticisi & Yapay Zeka), Mesut Çakır (Backend Yazılımcı), Hatice Betül Haksal (Analist), Bengü Bayyurt Çetin (Analist, sözleşmeli), Kazım Yıldırım (Yapay Zeka, sözleşmeli), Necati Koray Koçabaş (Veri Uzmanı & Yapay Zeka, sözleşmeli). Buna karşılık Proje Detayı metni, EK-3, EK-4 ve sunum **4 kişi, 39 adam-ay, 3,25 tam zaman eşdeğeri** diyor. Kimlik alanındaki "Toplam Personel" ise hâlâ **2**.

| Seçenek | Yapılacaklar | Değerlendirme |
|---|---|---|
| **A: 4 kişi (önerilen)** | Proje Ekibi'nde EK-4'teki dört rolü taşıyan kişiler kalır: proje yöneticisi, kıdemli yazılım geliştirici, tam zamanlı yapay zekâ mühendisi ve analiz/test uzmanı. Diğer iki kişi işe başladıklarında ekibe eklenir. Murat Haksal'ın görev adı "Proje Yöneticisi" olur, yapay zekâ rolü ayrı bir kişiye geçer. Toplam Personel 4 olur | Bütçe, adam-ay ve EK-3/EK-4 hiç değişmez. Sunumdaki "4 kişiyle başlayıp 6" beyanıyla da tutarlıdır. Ancak dört kişiden hangilerinin kalacağına siz karar vermelisiniz |
| B: 6 kişi | EK-3, EK-4 efor matrisi, Proje Detayı ekip paragrafı, Toplam Personel ve sunumdaki "4 kişi" ifadeleri 6 kişiye göre yeniden yazılır | 39 adam-ay 6 kişiye bölünürse kişi başına ortalama 0,54 tam zaman eşdeğeri düşer ve hakem "ekip kısmi zamanlı mı?" diye sorar. Adam-ay artırılırsa bütçe 7 milyonu aşar |

Kiralanan alan 10 m² olduğu için kişi başına 4 kişide 2,5 m², 6 kişide 1,7 m² düşer. Karar ne olursa olsun alan ihtiyacı gözden geçirilmelidir.

### 5.2 Portalın iş gücü alanları nasıl hesaplıyor?

Portal "Toplam Proje İş Gücü" alanını görünüşe göre **süreyle çarparak** hesaplıyor: v5'te 4 girilince 48, v8'de 6 girilince 72 çıktı (her ikisi de × 12). Bu nedenle "Ar-Ge İş Gücü (Adam/Ay)" alanı toplam adam/ay'ı değil, **aylık ortalama iş gücünü** bekliyor olabilir. v5 raporundaki "31 / 8 / 39 girin" önerisi (A2) bu alanları toplam kabul ediyordu. Bu durumda o öneri uygulanırsa toplam 39 × 12 = 468 adam/ay çıkar.

**Ne yapılmalı:** Hedef, "Toplam Proje İş Gücü" alanında **39** görmek.
1. Ar-Ge **2,58**, Destek **0,67** (toplam **3,25**) girin ve Toplam Proje İş Gücü'nün 39'a düştüğünü kontrol edin (31 ÷ 12 ve 8 ÷ 12).
2. Portal ondalık sayı kabul etmiyorsa hiçbir tam sayı 39'u vermez. Bu durumda teknopark yönetimine alanın nasıl doldurulması gerektiğini sorun. Onların cevabına kadar 39 adam-ay beyanının Proje Detayı ve bütçe tablosunda açıkça yazılı olduğunu belirtin.
3. v8'deki eşitlik (iş gücü 6 = ekip 6 kişi) portalın ekip sayısını mı yoksa iş gücü alanını mı çarptığını ayırt etmeye yetmiyor. İlk denemedeki sonuç bunu netleştirecektir.

---

## 6. Uygulama sırası ve son kontrol

1. **Kararlar:** §5.1 (ekip) ve §2.4 (iki eşik) kararlarını verin.
2. **Proje Bütçesi tablosu:** §1.2'deki dokuz satırı girin ve kimlik alanında 7.000.000 ₺ göründüğünü kontrol edin.
3. **Kimlik alanları:** iş gücü (§5.2), Toplam Personel, bitiş tarihi, İlişkili Sektörler (T9).
4. **Proje Detayı:** alanın tamamını silin ve ana belgedeki güncel metni yapıştırın. Yapıştırmadan önce ana belgeye şu düzeltmeleri işleyin: Y1, Y5, Y6, §2.3 (b) ve (c). Yoksa hatalar geri gelir.
5. **Hedeflenen Kazanım ve Sonuçlar:** ana belgeden yeniden yapıştırın, ardından Kazanım 1'e §2.3 (a) metnini, Kazanım 4'e Y1 düzeltmesini uygulayın.
6. **Proje Özeti:** T1 (1.700), §2.1 (1-4 milyar), Y3 (zekâ) ve Y7 (katma değer satırı).
7. **Kutular ve tablolar:** T5, T7, T8, T11, ekipman listesi (§1.4), Proje Ekibi görev adları (Y2, Y3).
8. **Son kontrol:** yeni PDF çıktısını alın ve aşağıdaki ifadeleri arayın. **Hiçbiri bulunmamalıdır:**

   `6.470` · `6.600` · `36 adam` · `4.680` · `420.000` · `4-16 milyar` · `60 senaryo` · `1.300` · `kaldırımı` · `Yazilimci` · `altsistem` · `iki cümlelik` · `(28 Ar-Ge` · `yapay zeka` *(bu sonuncusu yalnızca proje adında ve portalın "Ana Teknoloji Alanı" listesinde kalabilir)*

   Aşağıdakiler ise **bulunmalıdır:** `7.000.000` (en az iki yerde), `39 (31 Ar-Ge + 8)`, `%95'lik dilim`, `1.700'ü aşkın`.

---

## 7. Repodaki belgelere yansıması

Bu rapor yalnızca yapılacakları listeler; belgelerde henüz değişiklik yapılmamıştır. §2.4'teki eşikler onaylandıktan sonra şu belgeler güncellenmelidir:

| Belge | Değişiklik |
|---|---|
| `denetci-proje-bilgi-formu.md` | Y1, Y5, Y6, Y7, Y8, Y9; Kazanım 1 süre tanımı, İP5 çıkış kriteri, risk (8) (§2.3); proje adını portaldaki adla eşitleme (portal: "Denetci.AI - Denetçi Rolünde Yerel Yapay Zeka Sistemi", ana belge: "Denetci.AI: Denetçi Rolünde Nöro-Sembolik Yerel Yapay Zekâ"; hakem portaldaki adı gördü) |
| `ek-7-denetci-model-secimi.md` | §3'teki "Faz 0'da netleştirilecek iki tanım" maddesinin (a) şıkkı artık yanıtlandı: süreye ön-doldurma dâhil. Kapı K1'e %95'lik dilim ve kalite kademesi için iş hacmi hedefi eklenir |
| `hakem-sunumu-soru-cevap.md` S13 | Cevaptaki "3 milyar parametre, 300 simge" ifadesi 1,7 milyar / 250 simge ile, "son çare arka planda toplu işlem" ifadesi de risk (8)'in yeni hâliyle ("tutmazsa olumsuz raporlanır") uyumlu hâle getirilir |
| `ek-3`, `ek-4` | Yalnızca §5.1'de B seçeneği seçilirse güncellenir |
