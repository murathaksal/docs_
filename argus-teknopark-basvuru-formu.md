# Teknopark Proje Başvuru Formu — ARGUS

*Teknoloji Geliştirme Bölgesi proje başvuru formu (standart portal formatı) — tüm başlıklar doldurulmuştur. Önceki Argelog.AI başvurusunun birebir başlık düzeni Drive erişimi açıldığında eşlenecektir.*

**Mimari ilkeler (sabit):**
1. **Asıl olan deterministik hesap motorlarıdır.** Teşvik hesabı ve uyum denetiminin çekirdeği, Argelog bünyesinde geliştirilmiş ve Bakanlık verisiyle kuruşuna kadar doğrulanmış saf hesap fonksiyonları ile kural tabanlı kontrollerdir.
2. **LLM yalnızca dar ve sınırlı görevlerde çalışır** — hesap yapmaz, karar vermez; tüm çıktıları insan onaylıdır.
3. **Tüm YZ işleme yereldir ve CPU-yalnız çalışır** — ürün, kapalı devre (internetsiz/izole ağ) ortamdaki sıradan kişisel bilgisayarlarda, GPU gerektirmeden çalışır teslim edilir; bordro verisi kurum dışına çıkmaz, harici LLM API kullanılmaz (KVKK + kapalı devre tasarım kısıtı).
4. **Kolay kullanım varsayılandır:** kurulum tek paketle, kullanım "dosyaları sürükle → sihirbazı izle → raporu al" akışıyla; BT projesi gerektirmez — hedef, ilk raporun kurulumdan sonraki ilk saat içinde alınmasıdır.

---

## 1. Proje Kimliği

| Alan | Bilgi |
|---|---|
| Proje adı | ARGUS — Ar-Ge Teşvik Uyumu için Doğrulanmış Hesap Motoru ve Yerel YZ Destekli Uyum Platformu |
| Başvuru sahibi | Argelog Ar-Ge Merkezi Yönetim Danışmanlığı ve Yazılım Hizmetleri A.Ş. |
| Proje süresi | 10 ay (7 ay geliştirme + 3 ay saha doğrulama/sertleşme) |
| Teknoloji alanı | Yazılım — Kurumsal Uyum/RegTech; Kural Tabanlı Sistemler; (sınırlı kapsamda) Yerel Doğal Dil İşleme (NACE 62.01) |
| Tahmini bütçe | ~7,95 M TL |
| THS (başlangıç → hedef) | Hesap çekirdeği THS 8 (sahada/Bakanlık verisiyle doğrulanmış); platform bütünü THS 5 → **THS 8** |
| Hedef pazar | Türkiye'deki 1.363 Ar-Ge Merkezi + 342 Tasarım Merkezi (5746) ve kurumsal teknopark firmaları (4691) |

## 2. Proje Özeti

5746 kapsamındaki Ar-Ge/Tasarım Merkezleri; aylık teşvik hesaplamaları (GV stopaj terkini, SGK işveren indirimleri, DV muafiyeti, KV indirimi), yıllık faaliyet raporu ve iki yılda bir denetim yükümlülüğü altındadır. Hata; teşvik geri ödemesi, durdurma ve belge iptali riski doğurur.

ARGUS'un çekirdeği **deterministik hesap motorudur**: Argelog bünyesinde önceden geliştirilmiş, Bakanlık doğrulaması Nisan 2026 verisiyle kuruşuna kadar doğrulanmış (96/96 çapa testi), mevzuat maddesi izlenebilirliği taşıyan saf hesap fonksiyonları (5746 m.3/a-b-d, 5510 m.81/i, KVK m.10/1-a ve m.32, 7555 ücret teşvik tavanı, SGK 2016-26 genelge sıralaması) proje başlangıç varlığı olarak devralınır. Projenin Ar-Ge içeriği bu çekirdeğin üzerine üç katman ekler: (a) **bitemporal kural/parametre katmanı** — hangi dönemin hangi mevzuat sürümüyle hesaplanacağının versiyonlanması ve mevzuat değişikliği etki analizi; (b) **çapraz tutarlılık denetim motoru** — bordro × PDKS × proje kayıtları × faaliyet raporu zincirinde kural tabanlı çelişki tespiti; (c) **dar-görevli yerel LLM katmanı** — yalnızca mevzuat değişikliği özetleme/kural taslağı önerisi, serbest metinli belge-kanıt eşleştirme ve bulgu açıklamalarının rapor diline dökülmesi görevlerinde, tamamen yerel çalışan ve tüm çıktıları insan onaylı küçük dil modelleri.

Projenin Ar-Ge ve market-fit kalbi **BAZ Hattı** alt sistemidir: yeni müşterinin geçmiş resmî beyanları (MUHSGK, e-Bildirge hizmet listeleri, tahakkuk fişleri) ile hesap girdileri (bordro, özlük, PDKS) yüklenir; her ay o ayın yürürlük-tarihli mevzuat parametreleriyle yeniden hesaplanır, beyan edilenle kademeli mutabakat kurulur, farklar kök nedene ve geri kazanım kanalına göre sınıflanır ve insan onaylı kapanışla her dönem güven skorlu, hash zincirli **immutable BAZ** snapshot'ına dondurulur. Ücretli pilotun teslimatı olan Retrospektif Mutabakat Raporu bu hattın çıktısıdır — onboarding, market-fit ölçümü ve ürünün kalıcı değeri (ileri dönem hesap referansı + denetim savunma dosyası) tek mekanizmada birleşir. (Ayrıntılı tasarım: `argus-baz-hatti-tasarimi.md`.)

**Ürün biçimi:** Kapalı devre ortamda, sıradan kişisel bilgisayarda (GPU'suz, CPU-yalnız) çalışan **masaüstü uygulama** — kurulumdan ilk rapora bir saat hedefiyle, "dosyaları sürükle → sihirbazı izle → raporu al" kolaylığında; mevzuat güncellemeleri imzalı offline paketlerle taşınır. Bu biçim ürünü yalnız büyük Ar-Ge merkezlerinin değil; savunma sanayii kapalı ağlarının, KVKK-hassas her kurumun ve SMMM/mali müşavir ofislerinin kullanabileceği "herkesin kurabildiği" bir araca dönüştürür. Çok kullanıcılı kurum sunucusu opsiyonel üst pakettir. Çıktı, iki sanayi kuruluşunda (biri Kale grubu bünyesinde) ücretli sahada doğrulanacaktır.

## 3. Firma Tanıtımı

Argelog, 2013'ten bu yana Türkiye'nin önde gelen İSO 100 sanayi kuruluşlarına inovasyon, teknoloji ve Ar-Ge yönetimi yazılımları sunar (Ar-Ge Yönetimi, Teknoloji Yönetimi, İnovasyon Yönetimi modülleri); SAHA İstanbul üyesidir. Projenin başlangıç varlığı olan teşvik hesap çekirdeği de dahil olmak üzere tüm yazılım varlıkları Argelog bünyesinde geliştirilmiştir.

## 4. Projenin Amacı ve Hedefleri

**Amaç:** Ar-Ge/Tasarım Merkezlerinin 5746 teşvik ve raporlama yükümlülüklerini, doğrulanmış deterministik hesap motorları ve kural tabanlı denetimle — yerel YZ'nin yalnızca dar destek görevlerinde kullanıldığı bir mimaride — denetlenebilir doğrulukta yöneten platformu geliştirmek.

**Ölçülebilir hedefler:**
1. **Retrospektif doğruluk kapısı:** Yürürlük-tarihli parametre tablosu 2022/07'ye kadar Resmî Gazete referanslı ve YMM teyitli doldurulur; her retrospektif yıl için YMM-doğrulamalı çapa dönemi **kuruş farksız** geçmeden o yıl müşteriye raporlanmaz (mevcut 96/96 çapa deseninin geriye genişletilmesi, hedef ≥300 çapa; parametresiz koşumda 96/96 birebir korunur — regresyonsuzluk kanıtı).
2. **Bazlama operasyonu:** Pilot firmada ≥12 dönem, veri odası açılışından itibaren ≤8 haftada (hedef 6) bazlanır; aynı girdi setinin yeniden yüklenmesi bit-özdeş kayıt ve özdeş hash üretir; herhangi bir baz versiyonu o günkü bilgi-durumuyla tek komutla ≤5 dakikada yeniden üretilir.
3. **Mutabakat kalitesi:** Fark kalemlerinin **≥%85'i otomatik sınıflanır**; sınıflandırılamaz + belirsiz (S3+S5) tutar payı **≤%5**; YMM oturum etiketleriyle yanlış-neden oranı **≤%10**; mevzuat-referanslı ≥60 senaryoluk kütüphanede sınıf doğruluğu ≥%90.
4. **Anomali tespiti:** Baz serisine enjekte edilen ≥20 mevzuat-referanslı sentetik hatanın ≥18'i yakalanır; temiz dönemlerde yanlış alarm ≤%5.
5. **Kalibrasyon kanıtı:** Pilot kapanışında protokolü baştan yazılı YMM **kör örneklem incelemesi** (dönem başına ≥20 kalem) A-seviye dönemlerde açıklanmamış maddi fark 0 gösterir.
6. LLM katmanında **dayanaksız çıktı 0**: her LLM önerisi kaynak referanslı ve insan onaylıdır. **CPU hedefi (AS-5):** damıtılmış öğrenci model, öğretmen doğruluğunun ≥%95'ine ulaşır; 16 GB RAM / 4 çekirdek GPU'suz referans makinede belge başına ≤30 sn; üç donanım sınıfında tekrarlanabilir.
6a. **Kolay kullanım hedefi:** temsili kullanıcı (BT desteği olmadan) kurulumdan ilk Denetim Hazırlık Skoru raporuna ≤1 saatte ulaşır; pilotlarda görevi tamamlama oranı ≥%80 ölçülür.
7. En az **2 bordro/ERP konnektörü** canlı veriyle çalışır; retrospektif belge içeri alma (MUHSGK XML ana yol) iç-toplam kabul kapısından geçer.
8. İki sanayi kuruluşunda ücretli pilot; kapanıştan 30 gün içinde en az birinden yazılı yenileme/abonelik taahhüdü.

## 5. Ar-Ge Niteliği, Yenilikçi ve Özgün Yönleri

**Proje başlangıç varlığı (background IP):** Argelog bünyesinde önceden geliştirilmiş teşvik hesap çekirdeği — 10 saf, deterministik, mevzuat-atıflı hesap fonksiyonu; parametrik mevzuat tablosu; 12 uyum kontrolü; çok kiracılı web platformu. Bu varlık projenin Ar-Ge konusu değildir; projenin THS başlangıcını yükselten kanıtlanmış temeldir ve tüm fikri hakları Argelog'a aittir.

**Projenin Ar-Ge içeriği — teknik belirsizlikler** (ayrıntı ve ölçüm protokolleri: `argus-baz-hatti-tasarimi.md` §8):

1. **AS-1 — Mevzuat değişikliklerinin parametre/girdi-semantiği katmanlaması ve bilgi-zamanlı retroaktif yeniden hesap:** Bitemporal tablolar tek başına ders kitabı malzemesidir; savunulan belirsizlik, Türk teşvik mevzuatındaki hangi değişikliğin salt parametre (KV oranı seyri, beş-puan imalat/diğer ayrışması), hangisinin **girdi semantiği** değişikliği olduğudur (2022 AGİ kaldırımı terkine konu matrah tanımını değiştirir; 7555 tavanının 01.08.2025 ay-ortası yürürlüğü dönem anahtarını yapısal kırar; 4691 rejiminde GV teşvikinin eğitim dereceli olmaması rejim dallanması ister). Şema + parametre + bilgi-zamanı birleşik sürümlemesinin, kuruşuna doğrulanmış çekirdeğin davranışını bozmadan temsil edilmesi ve düzeltme beyannamelerinin "hangi bilgi-tarihiyle hangi nüshaya karşı mutabakat" sorusunun biçimselleştirilmesi literatürde hazır cevabı olmayan kısımdır.
2. **AS-2 — Beyan-hesap farklarının nedensel zincir üzerinde abdüktif kök-neden teşhisi:** Farkı bulmak deterministiktir; belirsizlik farkın nedenine güvenilir atıftadır. Farklar kalemler arasında nedensel zincirle yayılır (matrah → GV terkini → KVK), birden çok hipotez aynı fark imzasını üretebilir ve kanun türü hataları ancak beyan-edilen/olması-gereken **karşı-olgusal çift hesapla** ayrışır. Araştırma içeriği: hangi fark imzasının hangi nedene tekil bağlanabildiğinin karakterizasyonu (identifiability), zincirleme farkların topolojik sırayla kök nedene indirgenmesi, ayırt edilemeyen hipotezlerin kanıtla "belirsiz" raporlanması. Tamamen deterministik ve kanıt üreten yapı, KVKK ve denetim-savunulabilirlik kısıtlarının doğrudan sonucudur.
3. **AS-3 — Güven-yayılımlı kısmi baz ve kalibre edilmiş doğrulanmışlık ölçüsü:** Eksik kaynakla kurulan kısmi bazda alan düzeyi güven etiketlerinin (TAM/KISMİ/YOK) hesap zinciri boyunca biçimsel yayılımı; dönem güven skorunun keyfî ağırlık değil **kalibre** bir ölçü olması (A ilan edilen dönemde sonradan maddi hata çıkma olasılığı gerçekten düşük olmalı); immutable hash zinciri ile "geçmişi değiştirmeden geçmişe düzeltme ekleme" çelişkisinin süpersedans versiyonlamayla çözümü.
4. **AS-4 — Küçük-örneklem baz serisinden ileriye dönük anomali tespiti:** Tek firma × 12-24 dönemlik seride neyin anomali sayılacağı açık problemdir; veri tek seri değil kişi×dönem panelidir, asgari ücret/zam mevsimselliği yürürlük-tarihli parametreyle ayrıştırılır, kural başına kesinlik/duyarlılık dengesi ölçüme bağlanır ("dosya doğruyken çok tutarsızlık buldu" yanlış-alarm riskine karşı).
5. **AS-5 — Görev-özel damıtılmış küçük modellerin CPU-yalnız kişisel bilgisayarda hedef doğrulukla çalıştırılması:** Ürün kapalı devre ortamdaki sıradan bilgisayarlarda (GPU'suz, 16 GB RAM) çalışmak zorundadır. Teknik belirsizlik: büyük öğretmen modelin dar görevlerdeki (Türkçe mali belge alan-çıkarımı, başlık eşleme) davranışının 1–4B sınıfı öğrenci modele **damıtma + 4-bit nicemleme + dilbilgisi-kısıtlı çözümleme** bileşimiyle, doğruluk kaybı sınırlanarak aktarılması; belge başına işleme süresinin batch hattında kabul edilebilir tutulması (önbellekleme, alan-bazlı kısa bağlam tasarımı). Türkçe mali-hukuki dar görevler için bu bileşimin doğruluk-hız-bellek sınırlarının karakterizasyonu yayımlanmış çözümü olmayan mühendislik araştırmasıdır. *Ölçülebilir hedef:* seçilen dar görevlerde öğrenci model, öğretmen modelin doğruluğunun **≥%95'ine** ulaşır; 16 GB RAM / 4 çekirdek CPU referans makinede belge başına işleme **≤30 sn** (batch), şema-geçersiz çıktı oranı ≤%1; üç farklı donanım sınıfında tekrarlanabilir.

*(Yerel LLM'in dar görevleri — belge alan-çıkarımı/başlık-eşleme önerisi, mevzuat değişikliği özeti, rapor dili — Ar-Ge iddiası olarak öne sürülmez; insan onaylı destek işlevleridir. Retrospektif belge içeri alma/format normalizasyonu da bilinçli olarak Ar-Ge değil, adlandırılmış geliştirme kalemi İP3a'dır.)*

**Mevcut duruma göre farklar:** Yerli teşvik yazılımları (ArgeMemory, Ar-GeNet) hesaplama/puantaj odaklıdır; Bakanlık-doğrulamalı açık test çapası, bitemporal mevzuat versiyonlama, çapraz kaynak denetim motoru ve yerel-LLM destekli mevzuat izleme katmanı hiçbirinde yoktur. Global ürünler (Boast.ai, Neo.tax) Türk mevzuatını kapsamaz.

## 6. Projede Kullanılacak Teknolojiler — Teknoloji Yığını

### 6.1 Katman katman teknoloji yığını

| Katman | Teknoloji | Gerekçe |
|---|---|---|
| **Hesap çekirdeği (devralınan, ⭐ asıl katman)** | Argelog'un firma içi geliştirdiği saf hesap fonksiyonları (Python, `Decimal` ROUND_HALF_UP aritmetiği): 5746/5510 SGK indirimleri, GV terkini (eğitim derecesi oranlı), DV muafiyeti, KVK net-yorum zinciri, 7555 ücret tavanı oranlama mantığı; deterministik (`hesapla(g)==hesapla(g)`), framework-bağımsız, immutable dönem snapshot'ları | Bakanlık doğrulaması Nisan 2026 verisiyle 96/96 çapa testi; mevzuat referansı fonksiyon docstring'lerinde — denetlenebilirlik hazır |
| **Mevzuat parametre katmanı → bitemporal genişletme (özgün geliştirme)** | Mevcut parametrik `mevzuat.py` tablosunun geçerlilik dönemi × yayım tarihi eksenli versiyonlu modele taşınması; kural DSL'i (YAML/JSON) + etki analizi motoru | AS1 — hiçbir oran/tutar koda gömülmez; dönem bazlı doğru sürümle hesap ve <1 iş günü mevzuat yansıtma hedefi |
| **Uyum/denetim motoru** | Mevcut 12 kontrolün (7 mantıksal + 5 mevzuat) genişletilebilir kural tabanlı denetim motoruna evrimi; çapraz kaynak kuralları (bordro × PDKS × proje × personel) | AS2 — ≥%90 yakalama / ≤%10 yanlış alarm hedefinin taşıyıcısı; denetçi-okunabilir kural tanımları |
| **Uygulama katmanı** | Python 3.12 + FastAPI + SQLAlchemy + Jinja2/HTMX (çekirdeğin mevcut mimarisi korunur); Pydantic girdi/çıktı modelleri; tek yönlü bağımlılık (web → store → io → core) | Kanıtlanmış lean mimari (~4,5K satır); Argelog platformuyla API düzeyinde entegrasyon |
| **YZ/NLP katmanı — dar görevli, tamamen yerel, CPU-yalnız** | Küçük açık ağırlıklı modeller (1–4B sınıfı; izin verici lisanslı adaylar — Apache-2.0 öncelikli — İP1'de CPU ölçümüyle seçilir); **görev-özel damıtma:** büyük öğretmen modelden dar göreve damıtılmış öğrenci modeller (AS-5). Yalnız üç görev: (1) belge alan-çıkarımı ve başlık-eşleme önerisi, (2) mevzuat değişikliği özeti, (3) bulgu açıklamalarının rapor diline dökülmesi — hepsi **batch** nitelikli (interaktif sohbet değil), CPU hızı yeterli. GBNF/kısıtlı çözümleme ile şema-zorlamalı çıktı; her öneri kaynak-atıflı ve insan onaylı. Embedding: küçük çok dilli açık model (CPU'da milisaniyeler) | **LLM hesap yapmaz, karar vermez.** Kapalı devre kısıtı: ürün internetsiz ortamda, sıradan kişisel bilgisayarda çalışır; harici API yok. Dar görev + küçük model + batch işleme = GPU'suz fizibilite |
| **LLM çalıştırma — CPU çıkarım altyapısı** | llama.cpp sınıfı CPU çıkarım motoru (AVX2/AVX-512, GGUF 4-bit nicemleme) veya ONNX Runtime; bellek eşlemeli model yükleme; görev kuyruklu batch işleme ve önbellekleme. **Asgari sistem hedefi: 4 çekirdek CPU + 16 GB RAM, GPU yok** — temsili donanım matrisinde (3-4 farklı sınıf kişisel bilgisayar) sürekli ölçüm | Müşteri donanım yatırımı sıfıra iner — "her bilgisayarda çalışır" hem satış hızlandırıcı hem kapalı devre (savunma/hassas veri) segmentlerinin ön şartı; damıtma/ince ayar eğitimleri geliştirme aşamasında kiralık bulut GPU'da yalnız sentetik+anonim veriyle yapılır |
| **Masaüstü dağıtım ve offline güncelleme** | Tek paketli masaüstü kurulum (Windows öncelikli; imzalı installer); yerel şifreli veri deposu; **imzalı offline güncelleme paketi** — mevzuat parametre/kural güncellemeleri kapalı devre ortama dosya/USB ile taşınır, imza doğrulaması ve sürüm damgasıyla uygulanır (mevzuat sürümü her raporda görünür) | Kapalı devre ortamda güncellenebilirlik ürünün yaşamsal özelliğidir; imzalı parametre paketi aboneliğin teslim biçimidir |
| **Veri katmanı** | PostgreSQL 16 (üretim; şema bazlı çok kiracılı izolasyon — mevcut multi-tenant yapı taşınır), Redis (kuyruk/önbellek), MinIO (belge deposu); pgvector (mevzuat korpusu embedding'leri) | Mevcut SQLAlchemy repository katmanı korunur; KVKK izolasyonu |
| **Entegrasyon katmanı** | Mevcut Excel/bordro şablon sihirbazı + PDKS içe aktarımı devralınır; üzerine 2 canlı bordro/ERP konnektörü (pilot firmaların sistemleri: Logo/Netsis/SAP adaptörleri), e-bildirge/muhtasar formatları, SFTP | İP3 — dosya tabanlı içe aktarım bugün çalışır durumda; konnektörler canlı akışa taşır |
| **Raporlama** | Mevcut Excel export + çalışma raporu PDF üretimi genişletilir: denetim hazırlık raporu, "risk/eksik teşvik" özeti, Bakanlık faaliyet raporu veri seti | Pilot teslimat formatları |
| **Güvenlik / KVKK** | Mevcut bcrypt auth + multi-tenant context üzerine: alan bazlı şifreleme, maskeleme, RBAC + SSO (OIDC), kapsamlı denetim izi (audit mevcut), veri minimizasyonu | Bordro verisi hassas kişisel veri; on-prem varsayılan seçenek |
| **DevOps / dağıtım** | Birincil dağıtım: imzalı masaüstü installer + offline güncelleme paketleri; Kurum sürümü sunucu opsiyonu için Docker/compose (mevcut altyapı korunur); GitHub Actions CI/CD; mevcut çapa testi (`dogrulama.py` 96/96), izolasyon testleri (16/16) ve CPU donanım matrisi ölçümleri CI'a bağlanır | Aynı çekirdekten masaüstü + kurum sunucusu; her değişiklikte kuruş-mutabakat regresyonu |
| **Kalite / değerlendirme** | Çapa test setinin pilot verileriyle genişletilmesi; hata-enjeksiyonlu sentetik bordro üreteci; LLM görevleri için ayrı skorlama düzeneği (şema geçerliliği, kaynak-atıf zorunluluğu) | Hedef 1-4'ün ölçülebilir kanıtı |

### 6.2 Özellik Seti ve Sürümler ("herkesin ihtiyacı" kademesi)

Özellik seti "işi fiilen yapan kişinin BT desteği olmadan kullanabildiği" ilkesine göre kademelenmiştir; her sürüm bir alt sürümün üstüne kurulur ve tek kod tabanından çıkar:

| Sürüm | Kime | Çekirdek özellikler |
|---|---|---|
| **ARGUS Masaüstü (çekirdek)** | Tek tüzel kişilikli her Ar-Ge/Tasarım Merkezi; mali işler/İK uzmanı | Sürükle-bırak bordro/beyanname yükleme (sihirbaz akışı); **Denetim Hazırlık Skoru** ve 23+ kural taraması; ay sonu tek tık teşvik kontrolü (dönem gölge hesabı); 7555 tavan kontrolü; Excel içeri/dışarı rapor; imzalı offline mevzuat güncellemesi; tümü CPU-yalnız, kapalı devrede |
| **ARGUS Pro** | Denetime hazırlanan / geçmişini doğrulamak isteyen merkezler | + BAZ Hattı retrospektif mutabakat (kişi×ay düzeyi), kök-neden sınıflandırmalı fark envanteri (S1–S5), düzeltme yol haritası çıktısı, güven skorlu baz sertifikası, tek komut denetim savunma dosyası, LLM belge yardımcıları (alan çıkarımı/başlık eşleme önerisi) |
| **ARGUS Kurum** | Çok tüzel kişilikli gruplar, savunma tedarik zinciri | + Çok kullanıcı/rol, çok firma; merkezi sunucu opsiyonu (aynı çekirdek); bordro/ERP canlı konnektörleri; kapalı ağ dağıtım paketi ve toplu offline güncelleme |
| **ARGUS SMMM/YMM** | Mali müşavir ve YMM ofisleri | Çok müvekkilli lisans: aynı masaüstü araç, müvekkil başına izole veri; ortak markalı rapor şablonu; meslek mensubunun kendi hizmetini güçlendiren "araç lisansı" modeli |

Katma değer cümlesi her sürümde aynıdır: *"Teşvikinizin kuruş doğruluğunu ve denetim savunmasını, veriniz bilgisayarınızdan çıkmadan, kurulumdan sonraki ilk saat içinde görün."*

### 6.3 Mimari özet

Konnektörler/içe aktarım → çok kiracılı platform → **deterministik hesap çekirdeği** (bitemporal parametre katmanıyla) dönem hesabını üretir → **kural tabanlı denetim motoru** çapraz tutarlılık bulgularını mevzuat atıflarıyla raporlar → **dar-görevli yerel LLM** yalnızca mevzuat izleme özeti, kanıt eşleştirme adayları ve rapor dili üretir (tamamı insan onaylı) → denetim hazırlık panosu ve resmi çıktılar. Kişisel veri hiçbir harici API'ye gönderilmez.

## 7. Projenin Katma Değer Unsurları ve Uygulanabilirliği

- **Uygulanabilirlik kanıtı güçlü:** Hesap çekirdeği bugün çalışır ve Bakanlık doğrulaması Nisan 2026 gerçek verisiyle kuruşuna kadar doğrulanmıştır (96/96 çapa testi) — projenin en riskli görünen kısmı fiilen tamamlanmış başlangıç varlığıdır. İki sanayi kuruluşundan yazılı ihtiyaç görüşü alınmıştır.
- **Ölçülebilir başarı kriterleri:** kuruş mutabakatı (tolerans 0); ≥%90 yakalama / ≤%10 yanlış alarm; mevzuat yansıtma <1 iş günü; LLM'de dayanaksız çıktı 0; 2 canlı konnektör.
- **KVKK-tam-uyum ayrıştırıcısı:** Veri kurum dışına çıkmaz; kurumsal BT/KVKK onayı hızlanır, savunma tedarik zincirine (SAHA) giriş ön şartı sağlanır.
- **Doğru araç doğru yerde:** Hesap ve denetim deterministik motorlarda, YZ yalnızca dar destek görevlerinde — "YZ hatası mali sonuç doğurur" riski mimari düzeyde dışlanmıştır.

## 8. İş-Zaman Planı

| İP | Başlık | Aylar | Efor (AA) | Çıktı |
|---|---|---|---|---|
| İP1 | Çekirdek devralma + **aylık dönem anahtarı ve imza genişletmesi** (davranış varsayılanlarla birebir korunur; 96/96 çapa parametresiz koşumla regresyonsuz); kural envanteri; küçük model aday havuzu (lisans denetimli) + CPU test donanım matrisi kurulumu ve ilk CPU ölçümleri | 1–2 | 5 | Entegre çekirdek; regresyonsuzluk kanıtı; CPU model karşılaştırma raporu |
| İP2 | **Yürürlük-tarihli parametre backfill'i** (2022/07'ye kadar, Resmî Gazete referanslı + YMM teyitli — pilot ön koşulu) + bilgi-zamanlı MevzuatSnapshot ve as-of yeniden üretim (AS-1); retrospektif yıl çapaları | 2–5 | 5 | Doğrulanmış parametre tablosu; ≥300 çapa; as-of kanıtı |
| İP3a | **Retrospektif belge içeri alma:** MUHSGK BDP-XML parser (ana yol) + Ar-Ge ek bildirimi çıkarımı + hizmet listesi/tahakkuk PDF çıkarıcı (iç-toplam kabul kapılı) + nüsha zinciri + Veri Kalite Karnesi *(Ar-Ge iddiası değil, geliştirme kalemi)* | 3–6 | 4 | Bazlanabilir dönem envanteri üreten içeri alma hattı |
| İP3b | Canlı bordro/ERP konnektörleri (2) | 4–7 | 2 | Canlı veri akışı |
| İP4 | Kademeli mutabakat + **abdüktif kök-neden sınıflandırıcı ve karşı-olgusal çift hesap** (AS-2) + K1–K14 kural zinciri + ≥60 senaryoluk kütüphaneyle kesinlik ayarı (çıkış kriteri) + anomali tespiti (AS-4) + görev-özel damıtma ve CPU-yalnız çıkarım optimizasyonu (AS-5) + denetim panosu ve masaüstü sihirbaz akışı | 4–7 | 6 | Sınıflandırıcı doğruluk raporu; yanlış-alarm ayar kanıtı |
| İP5 | Saha doğrulama deneyi — Pilot 1 (Kale): kapılı bazlama süreci, YMM mutabakat oturumları, kör değerlendirme protokolü (ön faz/sözleşme-KVKK ay 4–5'te, pilot dışında) | 6–8 | 2 | Pilot 1 kabul raporu; Retrospektif Mutabakat Raporu |
| İP6 | Pilot 2 (ikinci bordro ekosistemi — genelleme testi) + süpersedans senaryosu canlı kanıtı + yükleme portalı/otomatik karne + v1.0 | 8–10 | 1 | Pilot 2 raporu + ARGUS v1.0 |

Toplam: **25 adam-ay / 10 ay** (ort. ~2,5 FTE + danışmanlık). Pilot eforu concierge→araç dönüşümünü ölçer: Pilot 1 ≤40 adam-gün, Pilot 2 ≤15 adam-gün.

## 9. Proje Ekibi ve Personel Planı

| Rol | Kişi | Görev | Efor (AA) |
|---|---|---|---|
| Proje yöneticisi / ürün sahibi | 1 | Planlama, pilot koordinasyonu, kabul kriterleri | 2,5 |
| Kıdemli arka uç geliştirici | 2 | Bitemporal katman, denetim motoru, konnektörler | 12 |
| YZ/NLP mühendisi | 1 | Dar-görevli LLM katmanı, model değerlendirme, şema zorlama | 5 |
| Ön yüz geliştirici | 1 (yarı zamanlı) | Pano ve iş akışı arayüzleri (HTMX üzerine) | 3 |
| Test/kalite + MLOps | 1 (kısmi) | Çapa seti genişletme, hata enjeksiyonu, CPU çıkarım/paketleme altyapısı ve donanım matrisi ölçümleri | 2,5 |
| Mevzuat/YMM uzmanı | Hizmet alımı | Kural doğrulama, mutabakat denetimi | — |

## 10. Proje Bütçesi

| Kalem | Tutar (TL) |
|---|---|
| Personel (25 AA × 250.000 ort. tam maliyet) | 6.250.000 |
| Danışmanlık — mevzuat/YMM (hizmet alımı) | 500.000 |
| Bulut GPU kiralama — damıtma/ince ayar eğitimleri (yalnızca sentetik + anonim veriyle, geliştirme aşamasında) | 400.000 |
| CPU test donanım matrisi (3-4 temsili sınıf kişisel bilgisayar) | 150.000 |
| Entegrasyon test ortamları ve yazılım lisansları | 300.000 |
| Beklenmedik giderler (~%4,5) | 350.000 |
| **Toplam** | **7.950.000** |

*Notlar:* (1) Harici LLM API kalemi yoktur — tüm YZ işleme yereldir ve **üründe CPU-yalnız** çalışır; GPU yalnız geliştirme aşamasındaki damıtma/ince ayar eğitimlerinde kiralık kullanılır, ürüne GPU gereksinimi taşınmaz. (2) CPU-yalnız pivot, önceki plandaki GPU sunucu yatırımını (1,2 M TL) kaldırmış, bütçeyi ~8,7 → ~7,95 M TL'ye düşürmüştür. (3) Hesap çekirdeğinin hazır devralınması, süreyi 12→10 aya, eforu 30→25 AA'ya düşürmüştür.

## 11. Proje Çıktısının Ticarileştirilmesi ve Pazar Analizi

- **Hedef pazar (masaüstü biçimiyle genişletilmiş):** Çekirdek — 1.363 Ar-Ge Merkezi + 342 Tasarım Merkezi (teşvikler 31.12.2028'e uzatılmış; orta-büyük 400–600 merkez); ikinci halka — kurumsal teknopark (4691) firmaları ve **savunma sanayii kapalı ağları** (CPU-yalnız/kapalı devre biçimin doğrudan açtığı segment); üçüncü halka — **SMMM/YMM ofisleri** (binlerce ofis; müvekkilleri adına aynı masaüstü aracı kullanır — sunucu/BT projesi gerektirmeyen biçim bu segmenti ilk kez erişilebilir kılar).
- **Kolay kullanım = pazar uyumu:** "Her bilgisayarda çalışır, bir saatte ilk rapor" konumu; alıcı BT departmanı değil, işi fiilen yapan mali işler/İK uzmanı ve mali müşavirdir — satın alma sürtünmesi (sunucu, bulut izni, BT projesi onayı) tasarımla sıfırlanmıştır.
- **Rakip analizi:** Yerli — ArgeMemory, Ar-GeNet (hesaplama odaklı; Bakanlık-doğrulamalı açık test çapası, bitemporal versiyonlama ve denetim motoru yok); bordro yazılımı teşvik modülleri; YMM hizmeti. Global — Boast.ai, Neo.tax (Türk mevzuatı yok). Konum: doğrulanmış hesap çekirdeği + yerel mevzuat hendeği + KVKK-tam-uyum.
- **Gelir modeli:** Personel sayısına kademeli yıllık abonelik + denetim öncesi "hazırlık taraması" paketi; pilotlarda abonelik vs. başarı primi A/B testi.
- **Satış projeksiyonu (muhafazakâr):** Yıl 1 — 2 ücretli pilot + 3–5 abonelik; Yıl 2 — 12–18; Yıl 3 — 30–40 müşteri. Kanallar: Argelog İSO 100 müşteri tabanı ve danışmanlık ilişkileri; YMM kanal ortaklıkları.
- **Talep kanıtı:** İki sanayi firmasından yazılı ihtiyaç görüşü (LOI başvuru ekinde hedeflenir).
- **Büyüme vizyonu (ARGELOG.AI):** ARGUS, Argelog'un "kuruma özel Ar-Ge zekâ katmanı" (ARGELOG.AI) vizyonunun ilk üretim uygulamasıdır: kurumsal veri → analiz → uzman onayı → doğrulanmış sonuç → geri besleme döngüsünü uyum alanında kanıtlar. Aynı platform çekirdeği (olay/onay zinciri, sürümlü bilgi tabanı, model soyutlama, ajan manifesti) üzerinde sonraki aşamalarda deney/reçete döngüsü ve ek Ar-Ge ajanları (TRL, patent tarama, proje riski, teknoloji radarı) ticarileştirilecektir — bu vizyon projenin kapsamını değil, çıktısının pazar tavanını büyütür.

## 12. Riskler ve B Planı

| Risk | O/E | Önlem |
|---|---|---|
| Doğrulanmamış geçmiş parametreyle retro hesap → sahte bulgu | Orta/Çok yüksek | "Doğrulanmamış parametreli ay hesaplanamaz" motor seviyesinde sert kural; parametre backfill'i Resmî Gazete referanslı + YMM madde madde teyitli (İP2 ilk teslimatı, pilot ön koşulu); yıl başına çapa dönemi kuruş farksız geçmeden o yıl raporlanmaz |
| Yanlış alarm seli ("dosya doğruyken tutarsızlık buldu") | Orta/Yüksek | Kademeli mutabakat + firma muhasebe politikası profili + sürümlü tolerans bandı; S3/S5 sınıfları asla tutar iddiasına dönüşmez; kural kesinliği pilot öncesi ≥60 senaryoyla ayarlanır (İP4 çıkış kriteri); hiçbir rapor YMM oturumundan geçmeden müşteriye gitmez |
| Veri temini kilidi (beyanname XML'leri ve şifreler dış SMMM'de; SMMM kendi geçmiş işini yanlışlayacak araca isteksiz) | Orta/Yüksek | İki muhataplı talep paketi; sözleşme ekinde SMMM/YMM yetkilendirme yazısı; mali müşavir "denetlenen" değil **"rapor ortağı"** (bulgular önce ona, dil "hata" değil "fırsat"); XML yoksa tahakkuk fişi + hizmet listesi istisna yolu; sözleşmede kapsam daraltma hakkı |
| Tahsil edilebilirlik hayal kırıklığı (SGK'da geriye yararlanma ~6 ay — 5510 Ek m.17) | Orta/Orta | Rapor değer tanımı baştan üç kanallı: tahsil edilebilir (pencere içi) + önlenen yıllık koşan kayıp + risk azaltımı; aleyhte bulgular kendiliğinden düzeltme avantajlarıyla YMM eşliğinde sunulur; "bulgu ne olursa olsun rapor teslim edilir" sözleşmede |
| Mevzuat değişim hızının kural bakımını aşması | Orta/Yüksek | Bitemporal versiyonlama (AS-1) tam da bunun için; YMM ile aylık gözden geçirme; LLM destekli Resmî Gazete izleme (insan onaylı) |
| Çekirdek imza genişletmesinin 96/96 güvencesini eritmesi | Düşük/Yüksek | Opsiyonel parametre deseni; parametresiz koşumda birebir regresyon; migrasyon İP1'de adlandırılmış kalem ve İP5'in ön koşulu |
| Çapraz denetim motorunun hedef doğruluğa ulaşamaması | Orta/Orta | Kural seti kademeli genişler; ilk sürüm mevcut 12 doğrulanmış kontrolle çıkar |
| LLM dar görevlerinde düşük kalite | Düşük/Düşük | Mimari gereği LLM çıktısı hiçbir hesaba doğrudan etki etmez (insan onaylı öneri); en kötü durumda özellik kapatılır, ürün değeri korunur |
| Damıtılmış küçük modelin CPU'da hedef doğruluk/süreye ulaşamaması | Orta/Orta | Görev daha da daraltılır (alan-bazlı kısa bağlam); model kademesi 4B'ye çıkarılır (yine CPU'da); en kötü durumda ilgili LLM özelliği kapatılır — deterministik motor + kural katmanı ürün değerini tek başına taşır |
| Açık model lisans uyumsuzluğu (ticari dağıtımda kısıt) | Düşük/Orta | Aday havuzu izin verici lisanslı (Apache-2.0 öncelikli) modellerle sınırlanır; lisans denetimi İP1 model seçim kriteridir |
| Düşük donanımlı müşteri makinelerinde performans şikâyeti | Orta/Düşük | Asgari sistem gereksinimi açık yayımlanır; kurulumda donanım ön kontrolü; batch işler ilerleme göstergeli ve arka planda |
| Bordro/ERP veri erişiminde gecikme | Orta/Orta | Mevcut Excel/şablon içe aktarımı yedek yol; veri protokolleri İP1'de imzalanır |
| KVKK / veri gizliliği | Düşük/Yüksek | Tamamen yerel YZ; veri minimizasyonu, maskeleme, şifreleme, kiracı izolasyonu |
| Hesap hatasının mali sonucu | Düşük/Yüksek | Çekirdek Bakanlık-doğrulamalı + her değişiklikte 96/96 çapa regresyonu; kuruş mutabakat kabulü; sözleşmede "karar destek" konumu |

## 13. Fikri Mülkiyet ve Proje Çıktıları

- **Başlangıç varlığı beyanı:** Firma bünyesinde önceden geliştirilmiş teşvik hesap çekirdeği background IP olarak beyan edilir; proje kapsamında geliştirilen bitemporal katman, denetim motoru ve LLM katmanı dahil tüm fikri haklar Argelog mülkiyetindedir.
- ARGUS marka başvurusu; AS1/AS2 mimarisi için ay 8'de patentlenebilirlik ön değerlendirmesi.
- Anonimleştirilmiş değerlendirme setleri ve en az 1 akademik bildiri.
- Ticari çıktı: ARGUS v1.0 — kapalı devre CPU-yalnız masaüstü uygulama (Masaüstü/Pro sürümleri) + Kurum sunucu opsiyonu, 2 canlı konnektör, denetim hazırlık panosu, imzalı offline mevzuat güncelleme altyapısı.

## 14. Diğer Kamu Destekleri

TÜBİTAK 1501/1507 başvurusu planlanmaktadır; kabul hâlinde 4691 muafiyetleriyle mükerrer destek kurallarına göre kalem ayrıştırması yapılacaktır. (Başvuru anındaki durum bu bölümde beyan edilecektir.)

## 15. Firma Bilgileri

Argelog Ar-Ge Merkezi Yönetim Danışmanlığı ve Yazılım Hizmetleri A.Ş. — 2013, İstanbul (Üsküdar). İnovasyon, teknoloji ve Ar-Ge yönetimi yazılımları; müşteri tabanı İSO 100 sanayi kuruluşları; SAHA İstanbul üyesi. (Ticari sicil, vergi ve iletişim bilgileri form aktarımında eklenecektir.)

---

*Kaynaklar: `arge-proje-fikirleri.md` (#5 RegTech analizleri), `teknopark-proje-basvurusu-regtech.md` (önceki taslak) ve Argelog bünyesindeki teşvik hesap çekirdeği kod tabanı.*
