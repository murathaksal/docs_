# Teknopark Proje Başvuru Formu — ARGUS

*Teknoloji Geliştirme Bölgesi proje başvuru formu (standart portal formatı) — tüm başlıklar doldurulmuştur. Önceki Argelog.AI başvurusunun birebir başlık düzeni Drive erişimi açıldığında eşlenecektir.*

**Mimari ilkeler (sabit):**
1. **Asıl olan deterministik hesap motorlarıdır.** Teşvik hesabı ve uyum denetiminin çekirdeği, Argelog bünyesinde geliştirilmiş ve Bakanlık verisiyle kuruşuna kadar doğrulanmış saf hesap fonksiyonları ile kural tabanlı kontrollerdir.
2. **LLM yalnızca dar ve sınırlı görevlerde çalışır** — hesap yapmaz, karar vermez; tüm çıktıları insan onaylıdır.
3. **Tüm YZ işleme yereldir** — bordro verisi kurum dışına çıkmaz, harici LLM API kullanılmaz (KVKK tasarım kısıtı).

---

## 1. Proje Kimliği

| Alan | Bilgi |
|---|---|
| Proje adı | ARGUS — Ar-Ge Teşvik Uyumu için Doğrulanmış Hesap Motoru ve Yerel YZ Destekli Uyum Platformu |
| Başvuru sahibi | Argelog Ar-Ge Merkezi Yönetim Danışmanlığı ve Yazılım Hizmetleri A.Ş. |
| Proje süresi | 10 ay (7 ay geliştirme + 3 ay saha doğrulama/sertleşme) |
| Teknoloji alanı | Yazılım — Kurumsal Uyum/RegTech; Kural Tabanlı Sistemler; (sınırlı kapsamda) Yerel Doğal Dil İşleme (NACE 62.01) |
| Tahmini bütçe | ~8,45 M TL |
| THS (başlangıç → hedef) | Hesap çekirdeği THS 8 (sahada/Bakanlık verisiyle doğrulanmış); platform bütünü THS 5 → **THS 8** |
| Hedef pazar | Türkiye'deki 1.363 Ar-Ge Merkezi + 342 Tasarım Merkezi (5746) ve kurumsal teknopark firmaları (4691) |

## 2. Proje Özeti

5746 kapsamındaki Ar-Ge/Tasarım Merkezleri; aylık teşvik hesaplamaları (GV stopaj terkini, SGK işveren indirimleri, DV muafiyeti, KV indirimi), yıllık faaliyet raporu ve iki yılda bir denetim yükümlülüğü altındadır. Hata; teşvik geri ödemesi, durdurma ve belge iptali riski doğurur.

ARGUS'un çekirdeği **deterministik hesap motorudur**: Argelog bünyesinde önceden geliştirilmiş, Bakanlık doğrulaması Nisan 2026 verisiyle kuruşuna kadar doğrulanmış (96/96 çapa testi), mevzuat maddesi izlenebilirliği taşıyan saf hesap fonksiyonları (5746 m.3/a-b-d, 5510 m.81/i, KVK m.10/1-a ve m.32, 7555 ücret teşvik tavanı, SGK 2016-26 genelge sıralaması) proje başlangıç varlığı olarak devralınır. Projenin Ar-Ge içeriği bu çekirdeğin üzerine üç katman ekler: (a) **bitemporal kural/parametre katmanı** — hangi dönemin hangi mevzuat sürümüyle hesaplanacağının versiyonlanması ve mevzuat değişikliği etki analizi; (b) **çapraz tutarlılık denetim motoru** — bordro × PDKS × proje kayıtları × faaliyet raporu zincirinde kural tabanlı çelişki tespiti; (c) **dar-görevli yerel LLM katmanı** — yalnızca mevzuat değişikliği özetleme/kural taslağı önerisi, serbest metinli belge-kanıt eşleştirme ve bulgu açıklamalarının rapor diline dökülmesi görevlerinde, tamamen yerel çalışan ve tüm çıktıları insan onaylı küçük dil modelleri.

Çıktı, iki sanayi kuruluşunda (biri Kale grubu bünyesinde) ücretli sahada doğrulanacak SaaS + on-prem üründür.

## 3. Firma Tanıtımı

Argelog, 2013'ten bu yana Türkiye'nin önde gelen İSO 100 sanayi kuruluşlarına inovasyon, teknoloji ve Ar-Ge yönetimi yazılımları sunar (Ar-Ge Yönetimi, Teknoloji Yönetimi, İnovasyon Yönetimi modülleri); SAHA İstanbul üyesidir. Projenin başlangıç varlığı olan teşvik hesap çekirdeği de dahil olmak üzere tüm yazılım varlıkları Argelog bünyesinde geliştirilmiştir.

## 4. Projenin Amacı ve Hedefleri

**Amaç:** Ar-Ge/Tasarım Merkezlerinin 5746 teşvik ve raporlama yükümlülüklerini, doğrulanmış deterministik hesap motorları ve kural tabanlı denetimle — yerel YZ'nin yalnızca dar destek görevlerinde kullanıldığı bir mimaride — denetlenebilir doğrulukta yöneten platformu geliştirmek.

**Ölçülebilir hedefler:**
1. Hesap motorunun pilot firmaların birer dönemlik gerçek verisinde YMM hesabıyla **kuruş mutabakatı** (tolerans 0) — çekirdek için mevcut 96/96 çapa testi setinin pilot verileriyle genişletilmesi.
2. Çapraz tutarlılık denetiminin, hata enjekte edilmiş test setinde eksik/tutarsız kayıtların **≥%90'ını** yakalaması; yanlış alarm **≤%10**.
3. Bir mevzuat değişikliğinin versiyonlu parametre/kural setine yansıtılma süresi **<1 iş günü**; geçmiş dönem hesapları etkilenmeden (bitemporal izolasyon) yeni dönem doğru sürümle hesaplanması.
4. LLM katmanında **dayanaksız çıktı 0**: her LLM önerisi kaynak referansı taşır ve insan onayından geçmeden hiçbir kural/rapor içeriğine dönüşmez.
5. En az **2 bordro/ERP konnektörünün** (pilot firmaların sistemleri) canlı veriyle çalışması.
6. İki sanayi kuruluşunda ücretli pilot; en az birinden yenileme/abonelik taahhüdü.

## 5. Ar-Ge Niteliği, Yenilikçi ve Özgün Yönleri

**Proje başlangıç varlığı (background IP):** Argelog bünyesinde önceden geliştirilmiş teşvik hesap çekirdeği — 10 saf, deterministik, mevzuat-atıflı hesap fonksiyonu; parametrik mevzuat tablosu; 12 uyum kontrolü; çok kiracılı web platformu. Bu varlık projenin Ar-Ge konusu değildir; projenin THS başlangıcını yükselten kanıtlanmış temeldir ve tüm fikri hakları Argelog'a aittir.

**Projenin Ar-Ge içeriği — teknik belirsizlikler:**

1. **Bitemporal mevzuat versiyonlama ve etki analizi (AS1):** Mevcut çekirdek parametrik ancak tek-sürümlüdür. Geçerlilik dönemi × yayım tarihi eksenlerinde versiyonlanan kural/parametre modeli; bir düzenleme değiştiğinde etkilenen dönem, müşteri ve geçmiş hesapların otomatik tespiti; kapanmış dönem snapshot'larının değişmezlik garantisiyle birlikte yeniden hesap senaryoları. Mali mevzuat alanında özgün mühendislik problemidir.
2. **Çapraz kaynak tutarlılık denetimi (AS2):** Mevcut 12 kontrolün; bordro × PDKS × proje/faaliyet kayıtları × personel nitelik verisi zincirinde çelişki tespit eden genişletilebilir bir denetim motoruna dönüştürülmesi (ör. tam zamanlı eşdeğer hesabına giren personelin izin/görevlendirme kayıtlarıyla çelişkisi; destek personeli %10 sınırının dönemsel simülasyonu). Kural DSL'i ile denetçi tarafından okunabilir kontrol tanımları.
3. **Mevzuattan kural taslağına yarı-otomatik çeviri (AS3 — LLM, dar görev):** Resmî Gazete/tebliğ metinlerinden değişiklik özetinin ve parametre/kural değişiklik taslağının yerel LLM ile üretilmesi; taslak, mevzuat uzmanı onayından geçmeden hiçbir hesaba etki etmez. Araştırma sorusu: küçük (8–14B) yerel modellerin Türkçe mevzuat metninde, kısıtlı çözümleme (constrained decoding) ve şema zorlamasıyla güvenilir yapılandırılmış çıktı üretme sınırları.
4. **Serbest metinli kanıt-kayıt eşleştirme (AS4 — LLM, dar görev):** Denetim dosyasındaki serbest metinli belgelerin (görevlendirme yazıları, proje raporları) yapılandırılmış kayıtlarla eşleştirilip eksik kanıtın işaretlenmesi — çıktı yalnızca "insan incelemesi için aday" statüsündedir.

**Mevcut duruma göre farklar:** Yerli teşvik yazılımları (ArgeMemory, Ar-GeNet) hesaplama/puantaj odaklıdır; Bakanlık-doğrulamalı açık test çapası, bitemporal mevzuat versiyonlama, çapraz kaynak denetim motoru ve yerel-LLM destekli mevzuat izleme katmanı hiçbirinde yoktur. Global ürünler (Boast.ai, Neo.tax) Türk mevzuatını kapsamaz.

## 6. Projede Kullanılacak Teknolojiler — Teknoloji Yığını

### 6.1 Katman katman teknoloji yığını

| Katman | Teknoloji | Gerekçe |
|---|---|---|
| **Hesap çekirdeği (devralınan, ⭐ asıl katman)** | Argelog'un firma içi geliştirdiği saf hesap fonksiyonları (Python, `Decimal` ROUND_HALF_UP aritmetiği): 5746/5510 SGK indirimleri, GV terkini (eğitim derecesi oranlı), DV muafiyeti, KVK net-yorum zinciri, 7555 ücret tavanı oranlama mantığı; deterministik (`hesapla(g)==hesapla(g)`), framework-bağımsız, immutable dönem snapshot'ları | Bakanlık doğrulaması Nisan 2026 verisiyle 96/96 çapa testi; mevzuat referansı fonksiyon docstring'lerinde — denetlenebilirlik hazır |
| **Mevzuat parametre katmanı → bitemporal genişletme (özgün geliştirme)** | Mevcut parametrik `mevzuat.py` tablosunun geçerlilik dönemi × yayım tarihi eksenli versiyonlu modele taşınması; kural DSL'i (YAML/JSON) + etki analizi motoru | AS1 — hiçbir oran/tutar koda gömülmez; dönem bazlı doğru sürümle hesap ve <1 iş günü mevzuat yansıtma hedefi |
| **Uyum/denetim motoru** | Mevcut 12 kontrolün (7 mantıksal + 5 mevzuat) genişletilebilir kural tabanlı denetim motoruna evrimi; çapraz kaynak kuralları (bordro × PDKS × proje × personel) | AS2 — ≥%90 yakalama / ≤%10 yanlış alarm hedefinin taşıyıcısı; denetçi-okunabilir kural tanımları |
| **Uygulama katmanı** | Python 3.12 + FastAPI + SQLAlchemy + Jinja2/HTMX (çekirdeğin mevcut mimarisi korunur); Pydantic girdi/çıktı modelleri; tek yönlü bağımlılık (web → store → io → core) | Kanıtlanmış lean mimari (~4,5K satır); Argelog platformuyla API düzeyinde entegrasyon |
| **YZ/NLP katmanı — dar görevli, tamamen yerel** | Küçük açık ağırlıklı modeller birincil (8–14B sınıfı; Qwen3 ailesi aday, İP1'de ölçümle seçim); yalnız üç görev: (1) mevzuat değişikliği özet + kural taslağı önerisi, (2) serbest metin kanıt-kayıt eşleştirme, (3) bulgu açıklamalarının rapor diline dökülmesi. Kısıtlı çözümleme (xgrammar/outlines) ile şema-zorlamalı çıktı; her öneri kaynak-atıflı ve insan onaylı. Embedding: BGE-M3 sınıfı (açık) | **LLM hesap yapmaz, karar vermez.** KVKK kısıtı: tüm işleme yerel; harici LLM API'ye veri gönderilmez. Dar görev + küçük model = düşük donanım ve düşük risk |
| **LLM sunum ve GPU altyapısı** | vLLM + AWQ/FP8 nicemleme; geliştirme ve müşteri kurulumu hedefi: **tek 48GB GPU'lu sunucu** (8–14B nicemlenmiş model için rahat sığar) | Dar-görevli tasarım GPU ihtiyacını tek sunucuya indirir; bulut GPU yalnızca yük testinde (sentetik/anonim veri) |
| **Veri katmanı** | PostgreSQL 16 (üretim; şema bazlı çok kiracılı izolasyon — mevcut multi-tenant yapı taşınır), Redis (kuyruk/önbellek), MinIO (belge deposu); pgvector (mevzuat korpusu embedding'leri) | Mevcut SQLAlchemy repository katmanı korunur; KVKK izolasyonu |
| **Entegrasyon katmanı** | Mevcut Excel/bordro şablon sihirbazı + PDKS içe aktarımı devralınır; üzerine 2 canlı bordro/ERP konnektörü (pilot firmaların sistemleri: Logo/Netsis/SAP adaptörleri), e-bildirge/muhtasar formatları, SFTP | İP3 — dosya tabanlı içe aktarım bugün çalışır durumda; konnektörler canlı akışa taşır |
| **Raporlama** | Mevcut Excel export + çalışma raporu PDF üretimi genişletilir: denetim hazırlık raporu, "risk/eksik teşvik" özeti, Bakanlık faaliyet raporu veri seti | Pilot teslimat formatları |
| **Güvenlik / KVKK** | Mevcut bcrypt auth + multi-tenant context üzerine: alan bazlı şifreleme, maskeleme, RBAC + SSO (OIDC), kapsamlı denetim izi (audit mevcut), veri minimizasyonu | Bordro verisi hassas kişisel veri; on-prem varsayılan seçenek |
| **DevOps / dağıtım** | Docker + docker-compose (mevcut), AWS dağıtım betikleri (mevcut) + on-prem kurulum paketi; GitHub Actions CI/CD; mevcut çapa testi (`dogrulama.py` 96/96) ve izolasyon testleri (16/16) CI'a bağlanır | Aynı imajla SaaS ve on-prem; her değişiklikte kuruş-mutabakat regresyonu |
| **Kalite / değerlendirme** | Çapa test setinin pilot verileriyle genişletilmesi; hata-enjeksiyonlu sentetik bordro üreteci; LLM görevleri için ayrı skorlama düzeneği (şema geçerliliği, kaynak-atıf zorunluluğu) | Hedef 1-4'ün ölçülebilir kanıtı |

### 6.2 Mimari özet

Konnektörler/içe aktarım → çok kiracılı platform → **deterministik hesap çekirdeği** (bitemporal parametre katmanıyla) dönem hesabını üretir → **kural tabanlı denetim motoru** çapraz tutarlılık bulgularını mevzuat atıflarıyla raporlar → **dar-görevli yerel LLM** yalnızca mevzuat izleme özeti, kanıt eşleştirme adayları ve rapor dili üretir (tamamı insan onaylı) → denetim hazırlık panosu ve resmi çıktılar. Kişisel veri hiçbir harici API'ye gönderilmez.

## 7. Projenin Katma Değer Unsurları ve Uygulanabilirliği

- **Uygulanabilirlik kanıtı güçlü:** Hesap çekirdeği bugün çalışır ve Bakanlık doğrulaması Nisan 2026 gerçek verisiyle kuruşuna kadar doğrulanmıştır (96/96 çapa testi) — projenin en riskli görünen kısmı fiilen tamamlanmış başlangıç varlığıdır. İki sanayi kuruluşundan yazılı ihtiyaç görüşü alınmıştır.
- **Ölçülebilir başarı kriterleri:** kuruş mutabakatı (tolerans 0); ≥%90 yakalama / ≤%10 yanlış alarm; mevzuat yansıtma <1 iş günü; LLM'de dayanaksız çıktı 0; 2 canlı konnektör.
- **KVKK-tam-uyum ayrıştırıcısı:** Veri kurum dışına çıkmaz; kurumsal BT/KVKK onayı hızlanır, savunma tedarik zincirine (SAHA) giriş ön şartı sağlanır.
- **Doğru araç doğru yerde:** Hesap ve denetim deterministik motorlarda, YZ yalnızca dar destek görevlerinde — "YZ hatası mali sonuç doğurur" riski mimari düzeyde dışlanmıştır.

## 8. İş-Zaman Planı

| İP | Başlık | Aylar | Efor (AA) | Çıktı |
|---|---|---|---|---|
| İP1 | Çekirdek devralma ve mimari birleşim: mevcut hesap çekirdeğinin Argelog platform bağlamına taşınması; kural envanteri; yerel model değerlendirme havuzu + GPU kurulumu | 1–2 | 4 | Entegre çekirdek + model karşılaştırma raporu |
| İP2 | Bitemporal mevzuat parametre/kural katmanı + etki analizi (AS1) | 2–5 | 5 | Versiyonlu hesap; <1 iş günü yansıtma testi |
| İP3 | Bordro/ERP konnektörleri (2) ve veri normalizasyonu | 3–6 | 4 | Canlı veri akışı |
| İP4 | Çapraz tutarlılık denetim motoru (AS2) + dar-görevli LLM katmanı (AS3/AS4) + denetim panosu | 4–7 | 6 | ≥%90/≤%10 raporu; şema-zorlamalı LLM değerlendirmesi |
| İP5 | Saha doğrulama — Pilot 1 (Kale), on-prem kurulum | 6–8 | 3 | Pilot 1 kabul raporu, "risk/eksik teşvik" çıktısı |
| İP6 | Saha doğrulama — Pilot 2, fiyat doğrulama, sürüm 1.0 | 8–10 | 3 | Pilot 2 raporu + ARGUS v1.0 |

Toplam: **25 adam-ay / 10 ay** (ort. ~2,5 FTE + danışmanlık).

## 9. Proje Ekibi ve Personel Planı

| Rol | Kişi | Görev | Efor (AA) |
|---|---|---|---|
| Proje yöneticisi / ürün sahibi | 1 | Planlama, pilot koordinasyonu, kabul kriterleri | 2,5 |
| Kıdemli arka uç geliştirici | 2 | Bitemporal katman, denetim motoru, konnektörler | 12 |
| YZ/NLP mühendisi | 1 | Dar-görevli LLM katmanı, model değerlendirme, şema zorlama | 5 |
| Ön yüz geliştirici | 1 (yarı zamanlı) | Pano ve iş akışı arayüzleri (HTMX üzerine) | 3 |
| Test/kalite + MLOps | 1 (kısmi) | Çapa seti genişletme, hata enjeksiyonu, GPU/vLLM altyapısı | 2,5 |
| Mevzuat/YMM uzmanı | Hizmet alımı | Kural doğrulama, mutabakat denetimi | — |

## 10. Proje Bütçesi

| Kalem | Tutar (TL) |
|---|---|
| Personel (25 AA × 250.000 ort. tam maliyet) | 6.250.000 |
| Danışmanlık — mevzuat/YMM (hizmet alımı) | 500.000 |
| GPU sunucu — geliştirme/test (1× 48GB GPU'lu sunucu) | 1.200.000 |
| Bulut GPU kiralama (yalnızca yük testleri, sentetik/anonim veri) | 100.000 |
| Entegrasyon test ortamları ve yazılım lisansları | 300.000 |
| Beklenmedik giderler (~%4) | 350.000 |
| **Toplam** | **8.700.000** |

*Notlar:* (1) Harici LLM API kalemi yoktur — tüm YZ işleme yereldir. (2) Dar-görevli küçük model tasarımı GPU ihtiyacını tek sunucuya indirmiştir; sunucu proje sonrası sürekli geliştirme/test altyapısıdır (makine-teçhizat, amortismana tabi). (3) Hesap çekirdeğinin hazır devralınması, önceki plana göre süreyi 12→10 aya, eforu 30→25 AA'ya düşürmüştür.

## 11. Proje Çıktısının Ticarileştirilmesi ve Pazar Analizi

- **Hedef pazar:** 1.363 Ar-Ge Merkezi + 342 Tasarım Merkezi; teşvikler 31.12.2028'e kadar uzatılmış; gerçekçi hedeflenebilir set orta-büyük 400–600 merkez; ikincil pazar kurumsal teknopark (4691) firmaları.
- **Rakip analizi:** Yerli — ArgeMemory, Ar-GeNet (hesaplama odaklı; Bakanlık-doğrulamalı açık test çapası, bitemporal versiyonlama ve denetim motoru yok); bordro yazılımı teşvik modülleri; YMM hizmeti. Global — Boast.ai, Neo.tax (Türk mevzuatı yok). Konum: doğrulanmış hesap çekirdeği + yerel mevzuat hendeği + KVKK-tam-uyum.
- **Gelir modeli:** Personel sayısına kademeli yıllık abonelik + denetim öncesi "hazırlık taraması" paketi; pilotlarda abonelik vs. başarı primi A/B testi.
- **Satış projeksiyonu (muhafazakâr):** Yıl 1 — 2 ücretli pilot + 3–5 abonelik; Yıl 2 — 12–18; Yıl 3 — 30–40 müşteri. Kanallar: Argelog İSO 100 müşteri tabanı ve danışmanlık ilişkileri; YMM kanal ortaklıkları.
- **Talep kanıtı:** İki sanayi firmasından yazılı ihtiyaç görüşü (LOI başvuru ekinde hedeflenir).

## 12. Riskler ve B Planı

| Risk | O/E | Önlem |
|---|---|---|
| Mevzuat değişim hızının kural bakımını aşması | Orta/Yüksek | Bitemporal versiyonlama (AS1) tam da bunun için; YMM ile aylık gözden geçirme; LLM destekli Resmî Gazete izleme (insan onaylı) |
| Çapraz denetim motorunun hedef doğruluğa ulaşamaması | Orta/Orta | Kural seti kademeli genişler; ilk sürüm mevcut 12 doğrulanmış kontrolle çıkar |
| LLM dar görevlerinde düşük kalite | Düşük/Düşük | Mimari gereği LLM çıktısı hiçbir hesaba doğrudan etki etmez (insan onaylı öneri); en kötü durumda özellik kapatılır, ürün değeri korunur |
| GPU tedarik/maliyet | Düşük/Orta | Tek sunucu ihtiyacı; erken satın alma; müşteri kurulumlarında donanımı müşterinin tedarik seçeneği |
| Bordro/ERP veri erişiminde gecikme | Orta/Orta | Mevcut Excel/şablon içe aktarımı yedek yol; veri protokolleri İP1'de imzalanır |
| KVKK / veri gizliliği | Düşük/Yüksek | Tamamen yerel YZ; veri minimizasyonu, maskeleme, şifreleme, kiracı izolasyonu |
| Hesap hatasının mali sonucu | Düşük/Yüksek | Çekirdek Bakanlık-doğrulamalı + her değişiklikte 96/96 çapa regresyonu; kuruş mutabakat kabulü; sözleşmede "karar destek" konumu |

## 13. Fikri Mülkiyet ve Proje Çıktıları

- **Başlangıç varlığı beyanı:** Firma bünyesinde önceden geliştirilmiş teşvik hesap çekirdeği background IP olarak beyan edilir; proje kapsamında geliştirilen bitemporal katman, denetim motoru ve LLM katmanı dahil tüm fikri haklar Argelog mülkiyetindedir.
- ARGUS marka başvurusu; AS1/AS2 mimarisi için ay 8'de patentlenebilirlik ön değerlendirmesi.
- Anonimleştirilmiş değerlendirme setleri ve en az 1 akademik bildiri.
- Ticari çıktı: ARGUS v1.0 (SaaS + on-prem), 2 canlı konnektör, denetim hazırlık panosu.

## 14. Diğer Kamu Destekleri

TÜBİTAK 1501/1507 başvurusu planlanmaktadır; kabul hâlinde 4691 muafiyetleriyle mükerrer destek kurallarına göre kalem ayrıştırması yapılacaktır. (Başvuru anındaki durum bu bölümde beyan edilecektir.)

## 15. Firma Bilgileri

Argelog Ar-Ge Merkezi Yönetim Danışmanlığı ve Yazılım Hizmetleri A.Ş. — 2013, İstanbul (Üsküdar). İnovasyon, teknoloji ve Ar-Ge yönetimi yazılımları; müşteri tabanı İSO 100 sanayi kuruluşları; SAHA İstanbul üyesi. (Ticari sicil, vergi ve iletişim bilgileri form aktarımında eklenecektir.)

---

*Kaynaklar: `arge-proje-fikirleri.md` (#5 RegTech analizleri), `teknopark-proje-basvurusu-regtech.md` (önceki taslak) ve Argelog bünyesindeki teşvik hesap çekirdeği kod tabanı.*
