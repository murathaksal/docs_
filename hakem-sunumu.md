# HAKEM SUNUMU: Denetci.AI

*İstanbul Medeniyet Üniversitesi Teknopark A.Ş. proje değerlendirme sunumu.*

| Belge | İçerik |
|---|---|
| Bu dosya | 12 slaytın içeriği ve şema tarifleri. **Konuşma metinleri burada değil**, ayrı dosyadadır |
| [`hakem-sunumu-konusma-notlari.md`](hakem-sunumu-konusma-notlari.md) | **Sunum günü elde tutulacak teslim metni:** slayt başına süre, şemada neyi göstereceğiniz, çıpa cümle ve geçiş |
| [`hakem-sunumu-soru-cevap.md`](hakem-sunumu-soru-cevap.md) | Hakem heyetinin soracağı 43 zor soru ve savunma cevapları |
| [`ek-7-akademik-kaynakca.md`](ek-7-akademik-kaynakca.md) | Sunumdaki her literatür rakamının doğrulanmış künyesi |
| [`denetci-proje-bilgi-formu.md`](denetci-proje-bilgi-formu.md) | Kaynak belge |

---

## Sunum hakkında

**12 slayt, hedef süre 14 dakika 45 saniye + soru-cevap.** Onunda gerçek bir şema vardır; şemalar süsleme değil, sözle anlatılması uzun süren mekanizmaları gösterir.

**Slayt metni bilerek azdır.** Her slaytta bir iddia, bir giriş cümlesi, bir şema ve gerekiyorsa bir eşik şeridi bulunur. Madde listesi yoktur. Ayrıntının tamamı konuşma metnindedir; hakem heyeti slaytı okurken konuşmacıyı dinleyemez, ikisinden birini seçer.

**Konuşma metinleri bu dosyadan ayrılmıştır.** Zamanlama, şemada neyin gösterileceği, çıpa cümle ve geçişlerle birlikte [`hakem-sunumu-konusma-notlari.md`](hakem-sunumu-konusma-notlari.md) dosyasındadır; PowerPoint dosyasında da her slaydın konuşmacı notu alanına gömülüdür.

**Dört araştırma sorusu dört slayttadır** (5-8). Her birinin altında aynı yerde duran bir *başarısızlık eşiği* şeridi vardır: eşik tutmazsa soru olumsuz sonuçlandı diye raporlanır, eşik değiştirilmez.

**Kesilen içerik silinmedi.** Önceki sürümdeki ekip matrisi, bütçe kırılımı, rekabet analizi ve veri yönetimi ya bu 12 slayda sıkıştırıldı ya da aşağıdaki yedek slayt listesine taşındı.

---

## Slayt 1 — Denetci.AI

*01  ·  İstanbul Medeniyet Üniversitesi Teknopark · Proje değerlendirme*

*Denetçi Rolünde Nöro-Sembolik Yerel Yapay Zekâ*

> Hesabı motor yapar · bulguyu model inceler · kararı insan verir

- **Firma:** ARGELOG A.Ş.
- **Süre:** 12 ay
- **İş gücü:** 39 adam-ay · 4 kişi
- **Bütçe:** 7.000.000 ₺
- **Kapsam:** 5746 · 4691
- **Hazırlık:** THS 5 → 7

---

## Slayt 2 — Kapanmış dönem, kendi kural sürümüyle yeniden üretilemiyor

*02  ·  Problem*

5746 sayılı Kanun kapsamındaki 1.720 Ar-Ge ve Tasarım Merkezi ile 4691 kapsamındaki 13.452 bölge firması, personel başına yılda yaklaşık bir milyon TL'lik teşvik akışını elektronik tabloyla yönetmektedir. Elektronik tablo tek kural sürümü taşır.

**Şema.** Elektronik tabloda tek kural sürümü tüm dönemleri besler ve değişiklikte üzerine yazılır; önerilen sistemde her dönem kendi mühürlü kural sürümüne bağlıdır.

*Şema altı:* Elektronik tablo tek sürüm tutar ve değişiklikte üzerine yazar; kapanmış bir dönem bu nedenle denetimde yeniden üretilemez. Sorunun ikinci yarısı daha ağırdır: farkı yorumlayacak, sorgulayacak ve kanıt isteyecek uzman emeği kıt ve pahalıdır. T.C. Sanayi ve Teknoloji Bakanlığı istatistikleri, Haziran ve Ağustos 2026.

---

## Slayt 3 — Mevzuat alanında dil modeli hesap ve karar üretemez

*03  ·  Tasarım kararı*

Mali ve hukuki hesaplamalarda üretken yapay zekâ, yaygın olarak hesabı ve kararı üreten konumda denenmektedir. Hukuk alanında yapılan ölçümler bu konumun savunulabilir olmadığını göstermektedir.

**Şema.** Hukuk alanında ölçülmüş dayanaksız yanıt oranları: Llama 2 yüzde 88, ChatGPT-4 yüzde 58, hukuka özel ticari araçlar yüzde 17 ile 33 arası; projenin hedef eşiği yüzde 1 veya altı.

*Şema altı:* Erişim destekli ticari araçlar oranı düşürmekte ancak ortadan kaldırmamaktadır. Bir tutarın yüzde on yedi olasılıkla dayanaksız olması denetim ortamında kabul edilebilir değildir; bu nedenle modelin rolü daraltılmıştır. Dahl vd. 2024, Journal of Legal Analysis; Magesh vd. 2025, Journal of Empirical Legal Studies; Kalai vd. 2026, Nature. Künyeler EK‑7 bölüm 2.

---

## Slayt 4 — İş bölümü: motor hesaplar, model inceler, insan karar verir

*04  ·  İş bölümü*

Roller kesin çizgiyle ayrılmıştır. Model hiçbir aşamada tutar hesaplamaz; ayrım kod düzeyinde kuruludur ve denetim iziyle kanıtlanabilir.

**Şema.** Motor farkı üretir, model bulguyu inceler, doğrulama kapısı atıfları denetler, insan karar verir ve getirilen belgeyle motor yeniden koşar. Modelden tutara giden bir yol yoktur.

*Şema altı:* Çarpı işaretli kesik çizgi mimarinin taşıyıcı tercihidir: modelden tutara giden bir yol bulunmamaktadır. Bu nedenle modelin yanılması hatalı bir tutar değil, gereksiz bir inceleme adımı üretir. Yeminli Mali Müşavirin tasdik yetkisi ve sorumluluğu değişmez.

---

## Slayt 5 — Denetçi rolü dar kapsamlı bir modele öğretilebilir mi?

*05  ·  Araştırma Sorusu 1*

Bu göreve elle etiketli eğitim verisi üretmek ölçeklenebilir değildir. Önerilen yaklaşım, doğrulanmış deterministik motoru referans kaynağı olarak kullanmaktır.

**Şema.** Senaryo, enjeksiyon ve pilot verisi motordan geçerek fark imzası ve kural sürümü üretir; buradan eğitim çiftleri çıkar. Araştırma yönlendirme görevinde etiketi motorun yeniden koşumu otomatik olarak koyar.

*Şema altı:* Etiketin kaynağı model değil, 96 gerçek dönemde kuruş farksız doğrulanmış motordur. Özyineleme bulunmadığı için sentetik veriyle eğitimin bilinen çöküş mekanizması bu hatta oluşmaz.

> **Başarısızlık eşiği · ay 10 ve 12**
> Yönlendirme isabeti ≥ %70  |  ince ayarsız temel modele karşı ≥ 15 puan
> Uzmanın bulgularının ≥ %80'i yakalanır  |  soru nitelenme oranı ≥ %70

---

## Slayt 6 — Gerekçeler sembolik kural tabanına karşı kanıta bağlanabilir mi?

*06  ·  Araştırma Sorusu 2*

Dil modellerinin bilinen zayıflığı akıcı fakat dayanaksız iddia üretmeleridir. Mevzuat alanında bu, var olmayan bir maddeye atıf ya da ilgili dönemde yürürlükte olmayan bir kurala dayanma biçiminde ortaya çıkar.

**Şema.** Model bulguları doğrulama kapısında iki soruya tabi tutulur; geçenler kullanıcıya gider, elenenler ince ayar turuna olumsuz örnek olarak döner.

*Şema altı:* Kapı hiçbir tutarı gizlemez: motorun bulduğu fark her koşulda kullanıcıya ulaşır. Elenen şey tutar değil, modelin o fark üzerine yazdığı yorumdur. Dil modelleri kendi akıl yürütme hatasını düzeltemediği için doğrulamanın dışsal ve sembolik olması gerekmektedir.

> **Başarısızlık eşiği · ay 10**
> Atıf doğruluğu ≥ %98  |  desteksiz iddia ≤ %1

---

## Slayt 7 — Abdüktif kök-neden teşhisi: sembolik üretim, nöral sıralama

*07  ·  Araştırma Sorusu 3*

Farkı bulmak deterministiktir. Belirsizlik, farkın kök nedenine atanmasındadır; birden çok neden matematiksel olarak aynı fark görüntüsünü üretebilir.

**Şema.** Tek bir fark tutarı yedi ayrı kök nedenle açıklanabilir; sembolik katman bu kümeyi eksiksiz üretir, nöral katman sıralar ve kanıt belgesi ister, ayırt edilemeyen kalem belirsiz olarak raporlanır.

*Şema altı:* Klasik bir tanımlanabilirlik problemidir: yedi neden matematiksel olarak aynı fark görüntüsünü üretir. Sembolik katman doğruluğu, nöral katman verimliliği taşır. İki eşik farklı paydadadır ve bilerek kilitlenmiştir; zor vakaları belirsiz sınıfına atmak tutar payını yükseltir. Model tabanlı teşhis: Reiter 1987; de Kleer ve Williams 1987. Künyeler EK‑7 bölüm 6.

> **Başarısızlık eşiği · ay 10 ve 12**
> Kalem bazında ≥ %85  |  ilk üç hipotezde ≥ %90  |  belirsiz tutar payı ≤ %5

---

## Slayt 8 — Üç eksenli yürürlük tarihli sürümleme ve ifade edilebilirlik sınırı

*08  ·  Araştırma Sorusu 4*

Modelin her atfının doğrulanabilmesi, kural tabanının her dönem için o gün yürürlükte olan kuralı kesin olarak bilmesini gerektirir.

**Şema.** Parametre, hesap şeması ve bilgi tarihi eksenleri birbirinden bağımsız sürümlenir; as-of kesiti üç eksenden o tarihte geçerli olan sürümü seçer.

*Şema altı:* Üç eksen birbirinden bağımsız sürümlenir. Kapanmış bir dönemi yeniden üretmek, bu üç eksenin kesişiminden o tarihte geçerli olan sürümü seçebilmektir. Sorunun ikinci yarısı, rejime özgü mantığın ne kadarının kural dosyasına taşınabildiğidir; 4691 bunun sınama alanıdır.

> **Başarısızlık eşiği · ay 7 ve 8**
> YMM teyitli gerçek çapa 96 → ≥ 140  |  oranı doğrulanmamış ay için ne hesap ne rapor üretilir
> 4691 kurallarının ≥ %90'ı kod yazılmadan tanımlanmalı  |  kaçış ≤ 3

---

## Slayt 9 — Ölçüm düzeneği ve başarısızlık eşikleri

*09  ·  Ölçüm düzeneği*

Dört araştırma sorusunun tamamı, ölçümden önce sabitlenen yanlışlanabilir eşiklere bağlanmıştır.

**Şema.** Aynı kör test seti beş kolda koşulur: ince ayarlı model, ince ayarsız model, erişim destekli kol, alan dışı genel model ve uzman denetçi.

*Şema altı:* Üçüncü kol, erişim destekli üretimin ince ayar yerine geçip geçemeyeceğini tahmine değil ölçüme bağlar.

| Soru | Eşik | Ay |
|---|---|---|
| AS-1 | Yönlendirme ≥ %70; temel modele karşı ≥ 15 puan; uzman bulgularının ≥ %80'i | 10, 12 |
| AS-2 | Atıf doğruluğu ≥ %98; desteksiz iddia ≤ %1 | 10 |
| AS-3 | Kalem bazında ≥ %85; ilk üçte ≥ %90; belirsiz tutar ≤ %5 | 10, 12 |
| AS-4 | Çapa 96 → ≥ 140; kural dosyasıyla kapsama ≥ %90; kaçış ≤ 3 | 7, 8 |

> **Ön kayıt**
> Eşikler ve kör test seti ay 7'de mühürlenip TTO ve YMM nezdinde saklanır.
> Ölçümden sonra ne eşik ne payda değişir. Sızıntı kontrolü EK‑6 §4'te yazılıdır.

---

## Slayt 10 — İş paketleri, ölçüm kapıları ve kaynak dağılımı

*10  ·  İş planı*

Her iş paketinin adam-ayı, ay aralığı ve çıkış kriteri tanımlıdır. Hesap çekirdeği proje öncesinde geliştirilmiş ve başlangıç varlığı olarak beyan edilmiştir.

**Şema.** On iki aylık takvimde yedi iş paketi ve ay 7, 8, 10, 11 ile 12'deki ölçüm kapıları; koyu şerit denetçi modelin geliştirildiği İP5'tir.

*Şema altı:* Koyu şerit İP5'tir: denetçi rolündeki modelin geliştirildiği paket. Etiketlerdeki sayılar adam-aydır; toplam 39.

| Ekip · 4 kişi | Adam-ay | Bütçe · 7.000.000 ₺ | Pay |
|---|---|---|---|
| Proje yöneticisi | 6 | Proje personeli · 39 × 130.000 ₺ | %72 |
| Kıdemli geliştirici | 12 | YMM hizmeti · kural teyidi, uzman etiketleme | %8 |
| Yapay zekâ mühendisi | 12 | Donanım · 3 iş istasyonu, 2 referans makine | %4 |
| Analiz ve test uzmanı | 9 | Patent, marka, akademik danışmanlık | %4 |
| Toplam · 3,25 TZE | 39 | Seyahat, bulut GPU, lisans, sarf, öngörülemeyen | %12 |

---

## Slayt 11 — Başarısızlık senaryosu ve risk asimetrisi

*11  ·  Risk*

Nöral katmanın hedefe ulaşamaması hâlinde ne olacağı, mimarinin kendisinde tanımlıdır.

**Şema.** Model yanıldığında sonuç yalnızca gereksiz bir inceleme adımıdır ve tutar değişmez; motorun parametresi doğrulanmamışsa sert kural hesabı ve raporu tamamen durdurur.

*Şema altı:* Asimetri bir tasarım tercihidir. Nöral katmanın hatası ilerler fakat zarar vermez; sembolik katmanın teyitsizliği hiç ilerlemez. AS-1 tutmazsa olumsuz sonuçlu araştırma sorusu olarak raporlanır ve ürün sembolik katman üzerinden eksiksiz çalışmayı sürdürür.

---

## Slayt 12 — Proje çıktıları ve teknopark katkısı

*12  ·  Kapanış*

Proje sonunda dört somut çıktı bırakılacaktır.

| # | Çıktı | Kanıtı |
|---|---|---|
| 1 | Doğrulanmış zaman-farkındalıklı kural tabanı | YMM teyitli gerçek çapa 96 → en az 140; 5746 ve 4691 kural setleri |
| 2 | Denetçi model ve ölçüm düzeneği | Yönlendirme ≥ %70, atıf ≥ %98, grafik işlemcisiz çalışır |
| 3 | THS 7 prototip, iki referans vaka | Tüpraş ve Kale Seramik'te ücretli pilot; yazılı ihtiyaç görüşleri alındı |
| 4 | Fikri mülkiyet | Marka başvurusu; ay 9'da patentlenebilirlik ön değerlendirmesi |

> Araştırma sorusu düşerse bile ürün sembolik katman üzerinden eksiksiz çalışır.
> Hesabı motor yapar, bulguyu model inceler, kararı insan verir.

TTO'dan talebimiz: yapay zekâ tarafında akademisyen danışmanlığı; ay 7 ve ay 10'da bağımsız gözden geçirme. Bölgeye taahhüdümüz: 4 kişiyle başlayıp 6; beş bölge firmasına 4691 ön sürümü; iki seminer; TTO ile ortak bildiri.

---

# YEDEK SLAYTLAR

*Soru-cevapta açılmak üzere hazırlanır; ana akışta gösterilmez. Kaynakları ana belge ve eklerdir.*

| # | Yedek slayt | Hangi soruya cevap verir |
|---|---|---|
| Y1 | EK-4 kişi × iş paketi efor matrisi (satır 6/12/12/9, sütun 3/6/3/9/10/5/3) | "Bu işi kim yapacak, yapabilecek mi?" |
| Y2 | Bütçenin dokuz satırı, portal harcama kategorileriyle | "7 milyon TL neye gidiyor?" |
| Y3 | EK-1 rekabet karşılaştırma tablosu (Ö1-Ö4) | "Rakipler bunu yapmıyor mu?" |
| Y4 | Veri yönetimi: veri sorumlusu/işleyen, KVKK dayanağı, imha | "Bordro verisini hangi dayanakla işliyorsunuz?" |
| Y5 | Sorumluluk ve insan gözetimi: lisans sözleşmesi, arayüz kısıtı | "Yanlış beyan verilirse sorumlu kim?" |
| Y6 | Ekonomik değerin dört kanalı ve fiyat bandı | "Müşteri bunu neden ödesin?" |
| Y7 | Risk tablosu: yedi risk, erken uyarı ve önlem | "Ya gecikirse, ya pilot düşerse?" |
| Y8 | EK-6 veri hattı ve hacim tablosu | "Kaç örnekle eğitiyorsunuz?" |
| Y9 | 96 çapanın yıl × rejim × kalem kapsama matrisi | "Motor da bir yazılım, nasıl güveniyorsunuz?" |
| Y10 | Örneklem büyüklüğü ve istatistiksel test planı | "15 puanlık fark anlamlı mı?" |
| Y11 | Dört kapılı pilot akışı ve yedek pilot planı | "Pilotlar gerçekten olacak mı?" |
| Y12 | THS bileşen tablosu ve THS 7 kabul kanıtı | "Neden 5'ten 7'ye?" |

---

# SUNUM ÖNCESİ KARAR BEKLEYEN MADDELER

*Aşağıdaki maddeler sunum metninde yer alıyor ancak başvuru dosyasında henüz karşılığı yok ya da düzeltilmesi gereken bir kayıt var. Sunum günü çelişki üretmemesi için önceden karara bağlanmalıdır.*

## A. Dosyaya eklenmesi gereken taahhütler

| # | Sunumdaki ifade | Durum | Yapılacak |
|---|---|---|---|
| A1 | Kör setin bir kısmının **iki bağımsız YMM** tarafından etiketlenmesi ve uyum katsayısının (Cohen kappa) raporlanması. 12 slaytlık sürümde taahhüt olarak yer almaz; soru-cevap bankasında S8'de geçer | EK-6 §6 tek etiketleyici varsayıyor; 550.000 ₺'lik YMM kalemi buna göre kurulmuş | Taahhüt edilecekse EK-6 §6'ya ikinci etiketleyici eklenir ve YMM kalemi gözden geçirilir; edilmeyecekse S8 cevabından çıkarılır |
| A2 | **Beş karşılaştırma kolu** (erişim destekli kol ve sembolik taban çizgisi dâhil); slayt 9'da şema olarak gösteriliyor | Formda üç kol var: ince ayarlı, ince ayarsız, alan dışı | Formdaki Kazanım 1'e iki kol eklenmeli ya da slayt 9 üç kola indirilmeli |
| A3 | **Ay 2-4 fizibilite ölçümü ve karar kapısı** | Formda yok | İP5 tanımına eklenebilir; eklenmezse sunumda "planlıyoruz" olarak söylenir |
| A4 | **Eşiklerin ay 7'de mühürlenmesi** ve TTO/YMM nezdinde saklanması | Formda yok | TTO'dan talep edilen hizmetlere eklenebilir |
| A5 | **Ezberleme sınaması** ve dağıtılan model ağırlıklarının kuruluştan arındırılması | Formda ve EK-6'da yok | EK-6 §4'e eklenmesi önerilir; pilot kuruluşun hukuk birimi bunu soracaktır |
| A6 | **Bölgeye taahhütler** (6 kişi istihdam, 5 bölge firması, 2 seminer) | Formda yok | Taahhüt edilecekse forma işlenmeli; edilmeyecekse sunumdan çıkarılmalı |
| A7 | **Kaynak dönem kesişim taraması, karıştırılmış etiket kontrol koşumu ve tamamen kör tutulan bir pilot** | EK-6 §4 bu üç kontrolü içermiyor; "tamamen kör pilot" ise EK-6 §5 takvimiyle çelişiyor (ay 11'de her iki pilotun eğitim kısmı kullanılıyor) | Taahhüt edilecekse EK-6 §4 ve §5 buna göre güncellenmeli. Sunumdan çıkarıldı; slayt 9 doğrudan EK-6 §4'e atıf yapar, soru-cevap bankasında S10 da EK-6'ya indirildi |

## B. Düzeltilmesi gereken kayıtlar

| # | Sorun | Yapılacak |
|---|---|---|
| B1 | Portal kaydında "Toplam Personel: 2" yazıyor; ekip 4 kişi | Portalda 4'e çekilmeli. Heyet portal çıktısını ekranla karşılaştırabilir |
| B2 | Portal kaydında "Kiralanan Alan: 10 m²"; 4 kişide kişi başına 2,5 m² düşüyor | Alan ihtiyacı gözden geçirilmeli |
| B3 | Formda kural tabanı kapsamı "2019-2026"; proje 26.10.2026-25.10.2027 arası yürüyor ve ay 11'de cari dönem kontrolü yapılacak | Kapsam "2019'dan cari döneme" olarak düzeltilmeli; aksi hâlde 2027 dönemleri, formun kendi sert kuralı gereği hesaplanamaz |
| B4 | Formda "yedi ürün/hizmet kategorisi tarandı" deniyor ama beş kategori listeleniyor; EK-1'in yedi satırı bunlardan yalnızca dördüne karşılık geliyor | Formda "yedi ürün tarandı, dört rakip sınıfında toplandı; beşinci sınıf (genel amaçlı bulut araçları) taramaya değil mimari gerekçeye dayanır" biçiminde düzeltilmeli |
| B5 | Formda Tüpraş "aynı il" olarak işaretli | Pilot sahasının ili teyit edilmeli |
| B6 | Slayt 3'teki literatür rakamları (%58, %88, %17-33) formda geçmiyor | **EK-7 bu boşluğu kapatır.** Başvuru dosyasına ek olarak sunulmalıdır |

## C. Sunum öncesi son kontroller

1. **EK-1'i yeniden tara.** Rakip ürün siteleri Ağustos-Eylül 2026'dan bu yana değişmiş olabilir.
2. **EK-1'deki ölçüt sayısını düzelt.** Tabloda dört ölçüt (Ö1-Ö4) var ama metin iki yerde "üç ölçüt" diyor: Yöntem paragrafı ve Değerlendirme maddesi 1. Yedek slayt Y3 bu tabloyu ekrana getirdiği için heyet çelişkiyi görür.
3. **Niyet mektuplarını topla.** Kurumsal imza süreci 2-4 hafta sürüyor.
4. **EK-3'teki tutarları doldur.** Yer tutucu bırakılmış bir maliyet dayanağı, bütçe sorusunda savunulamaz.
5. **EK-4'teki özgeçmişleri doldur;** özellikle "diğer projelerdeki yük" alanını. Bu alan boşsa 39 adam-ay beyanı sorgulanır.
6. **Yapay zekâ mühendisinin istihdam durumunu netleştir.** Yedek slayt Y1'de ve İP5 anlatısında bu satır boş kalmamalı.
7. **Taban model lisansını kayda geçir.** Ticari kullanıma ve türev ağırlık dağıtımına izin veren bir aile seçilmeli; bu, ürünleştirmenin hukuki ön koşuludur.
