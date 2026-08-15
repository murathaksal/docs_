# Argelog için 10 Ar-Ge Proje Fikri

*Argelog'un pazarı, mevcut ürün altyapısı ve 2026 teknoloji trend analizleri temel alınarak hazırlanmıştır — Ağustos 2026*

---

## Arka Plan: Argelog'un Mevcut Konumu

Argelog, 2013'ten bu yana Türkiye'nin önde gelen İSO 100 firmalarına inovasyon, teknoloji ve Ar-Ge yönetimi yazılım çözümleri sunmaktadır. Platform üç ana modülden oluşur:

- **Ar-Ge Yönetimi Modülü:** Proje yönetimi, TÜBİTAK TEYDEB başvuru ve izleme desteği, THS (Teknoloji Hazırlık Seviyesi) takibi, Teknoloji Yol Haritası uyumu, Ar-Ge Merkezi Faaliyet Raporu altyapısı, veri doğrulama ve mevzuat uyum kontrolleri
- **Teknoloji Yönetimi Modülü:** Teknolojik mevcut durum analizi, operasyonel ve stratejik hedefler için yetkinlik tespiti, Ar-Ge/inovasyon çalışmalarının teknolojik gelişim katkısının yönetimi
- **İnovasyon Yönetimi Modülü:** Fikir yönetimi, iç girişimcilik, yarışma ve kampanyalar, açık inovasyon, girişimcilik ekosistemi takibi

Platformun güçlü yanları: **kurumsal hafıza** (doküman-veri yönetimi), **modüler mimari**, **veri odaklı karar destek** ve **mevzuat uyumu** (5746 sayılı kanun, TEYDEB süreçleri). Bu dört varlık, aşağıdaki proje fikirlerinin tamamında kaldıraç olarak kullanılmaktadır.

## Pazar ve Trend Özeti

| Sinyal | Veri |
|---|---|
| İnovasyon yönetimi yazılımı pazarı | 2026'da ~3,0 milyar USD → 2035'te ~46,7 milyar USD (CAGR ~%35) |
| Yapay zekâ entegrasyonu | 2025'te yeni kurulan platformların ~%61'i YZ destekli fikir değerlendirme içeriyor |
| Teknoloji kâşifliği (tech scouting) | YZ destekli patent/pazar zekâsının en hızlı büyüyen uygulaması (CAGR ~%22) |
| Kurumsal benimseme | Büyük işletmelerin %72'si dijital araçlarla desteklenen resmî inovasyon programı yürütüyor (2019'da %48) |
| Öne çıkan teknolojiler | LLM/RAG, agentic (otonom ajan) iş akışları, bilgi grafları, prediktif analitik, patent analitiği |

Türkiye özelinde: 5746 sayılı kanun kapsamındaki 1.300+ Ar-Ge/Tasarım Merkezi, TÜBİTAK TEYDEB programları ve teknopark ekosistemi, Argelog'un doğal pazarını oluşturur ve aşağıdaki fikirlerin çoğu bu kurumların zorunlu süreçlerine doğrudan değer üretir.

---

## Proje Fikirleri

### 1. Argelog Copilot — Kurumsal Hafıza Üzerinde LLM Tabanlı Ar-Ge Asistanı

**Ne:** Platformdaki proje kayıtları, faaliyet raporları ve doküman arşivi üzerinde RAG (Retrieval-Augmented Generation) mimarisiyle çalışan bir yapay zekâ asistanı. Kullanıcı doğal dilde soru sorar ("Geçen yıl kompozit malzeme alanında hangi projeleri yürüttük, çıktıları neydi?"), TEYDEB proje önerisi taslağı ürettirir, Ar-Ge Merkezi Faaliyet Raporu bölümlerini otomatik yazdırır.

**Neden şimdi:** LLM tabanlı kurumsal asistanlar 2026'nın en hızlı benimsenen kurumsal yazılım kategorisi; rakip global platformlar (ITONICS, Qmarkets) YZ asistanlarını temel özellik hâline getirdi.

**Altyapı uyumu:** Argelog'un kurumsal hafıza ve doküman-veri yönetimi altyapısı, RAG için gereken veri tabanını hazır sunuyor — en büyük giriş bariyeri zaten aşılmış durumda.

**Çıktılar:** Türkçe Ar-Ge terminolojisine ince ayarlı asistan, TEYDEB başvuru taslağı üreteci, faaliyet raporu otomasyonu.
**Destek uyumu:** TÜBİTAK 1501/1507 (yazılım Ar-Ge'si, doğal dil işleme bileşeni özgün değer taşır).

**Değerlendirme**
- **Teknoloji yığını:** LLM API (Claude / GPT sınıfı, Türkçe performansı yüksek bir model) + RAG mimarisi; embedding modeli ve vektör veri tabanı (pgvector / Qdrant); doküman işleme hattı (OCR, parçalama, meta veri çıkarımı); orkestrasyon katmanı (LangChain / Semantic Kernel); mevcut platforma mikroservis + API ile entegrasyon. KVKK ve kurumsal güvenlik gereksinimleri için on-prem/özel bulut LLM seçeneği (açık ağırlıklı modeller) planlanmalı.
- **Zorluk: Orta (3/5).** Bileşenler olgun ve bol örnekli; asıl zorluk Türkçe teknik metin kalitesi, halüsinasyon kontrolü (özellikle TEYDEB taslaklarında yanlış bilgi riski) ve müşteri başına veri izolasyonudur.
- **Veri bağımlılığı: Yüksek — ağırlıklı iç veri.** Kurumsal hafızadaki doküman ve proje kayıtları yeterli; dış veri gerekmez. Risk: bazı müşterilerde doküman arşivi dağınık/taranmamış olabilir; veri hazırlama (ingestion) hizmeti ürünün parçası yapılmalı.
- **Pazar potansiyeli: Çok yüksek.** Tüm mevcut müşteri tabanına satılabilir yatay üst modül; kurumsal YZ asistanları en hızlı benimsenen kategori. Kısa satış döngüsü, hızlı gelir; rakip platformlarda muadili var, bu yüzden aynı zamanda savunma amaçlı da (churn önleme) kritik.

### 2. YZ Destekli Fikir Değerlendirme ve Önceliklendirme Motoru

**Ne:** İnovasyon Yönetimi Modülü'ndeki fikir havuzuna gelen önerileri otomatik işleyen motor: mükerrer fikir tespiti (embedding tabanlı benzerlik), tematik kümeleme, stratejik hedeflerle otomatik eşleştirme ve geçmiş proje verilerinden öğrenen **başarı olasılığı skorlaması**.

**Neden şimdi:** YZ destekli fikir değerlendirme, yeni inovasyon platformlarının %61'inde standart; prediktif fikir değerlendirme pazar büyümesinin ana itici gücü olarak raporlanıyor.

**Altyapı uyumu:** Fikir havuzu, yarışma/kampanya verileri ve projeye dönüşen fikirlerin sonuç verileri (eğitim seti) platformda zaten birikmiş durumda — Argelog'un uzun süredir İSO 100 müşterileriyle çalışması, rakiplerin sahip olmadığı bir Türkçe eğitim verisi avantajı sağlar.

**Çıktılar:** Dedup + kümeleme servisi, strateji eşleştirme algoritması, açıklanabilir başarı skoru (fikir sahibine geri bildirim üretir).

**Değerlendirme**
- **Teknoloji yığını:** Embedding tabanlı benzerlik (çok dilli embedding modeli) + kümeleme (HDBSCAN/UMAP); başarı tahmini için gradyan artırma (XGBoost/LightGBM) veya ince ayarlı transformer sınıflandırıcı; açıklanabilirlik katmanı (SHAP); MLOps altyapısı (model versiyonlama, izleme — MLflow benzeri); mevcut fikir havuzu modülüne servis entegrasyonu.
- **Zorluk: Orta (2,5/5).** Dedup ve kümeleme düşük riskli, hızlı kazanım; başarı tahmini ise etiketli veri miktarına bağlı — teknik değil veri zorluğu. Açıklanabilir skor tasarımı (fikir sahibini küstürmeyen geri bildirim) ürün tasarımı emeği ister.
- **Veri bağımlılığı: Yüksek — iç, tarihsel etiketli veri.** Fikir → projeye dönüşüm → sonuç zinciri etiket setidir; yeni müşterilerde soğuk başlangıç sorunu var (kural tabanlı skorla başlayıp veriyle öğrenmeye geçen kademeli tasarım gerekir). Müşteriler arası ortak model KVKK/ticari gizlilik nedeniyle federated veya anonimleştirilmiş yaklaşım gerektirir.
- **Pazar potansiyeli: Yüksek.** YZ destekli fikir değerlendirme artık kategori standardı (%61 benimseme) — satış kazanmak için gerekli, tek başına prim getirmez ama İnovasyon Modülü'nün rekabet gücünü doğrudan belirler.

### 3. Agentic Teknoloji Kâşifi (Otonom Tech Scouting Ajanı)

**Ne:** Patent veri tabanları (TÜRKPATENT, EPO, WIPO), akademik yayınlar ve hibe/fon akışlarını sürekli tarayan otonom ajan sistemi. Üç öncü sinyali izler: patent başvuru hızı, atıf ivmesi ve kamu fon akışı. Müşterinin teknoloji yol haritasındaki alanlara göre kişiselleştirilmiş **zayıf sinyal uyarıları** ve trend radarı üretir.

**Neden şimdi:** Teknoloji kâşifliği, YZ destekli patent/pazar zekâsının en dinamik segmenti (CAGR ~%22); bir teknoloji danışmanlık raporlarına girmeden 12–18 ay önce patent ve yayın sinyallerinde görünür hâle geliyor. Agentic iş akışları 2026'nın belirleyici YZ mimarisi.

**Altyapı uyumu:** Teknoloji Yönetimi Modülü'ndeki teknoloji ağacı/yetkinlik haritası, ajanın neyi arayacağını belirleyen filtre olarak doğrudan kullanılır — genel bir tarayıcı değil, müşteriye özel kâşif olur.

**Çıktılar:** Çok kaynaklı veri toplama hattı, sinyal skorlama modeli, modül içi trend radarı ekranı.
**Destek uyumu:** TÜBİTAK 1501; TÜRKPATENT veri işbirliği potansiyeli.

**Değerlendirme**
- **Teknoloji yığını:** Agentic çerçeve (Claude Agent SDK / LangGraph) üzerinde planlama-arama-özetleme döngüsü; veri kaynakları: EPO OPS API, WIPO PATENTSCOPE, TÜRKPATENT, OpenAlex/Crossref (yayın+atıf), CORDIS ve TÜBİTAK destek duyuruları; arama/indeksleme (Elasticsearch/OpenSearch); patent sınıflandırma (CPC) ve konu modelleme; sinyal ivmesi için zaman serisi analizi; zamanlanmış hat orkestrasyonu (Airflow benzeri).
- **Zorluk: Yüksek (4/5).** Asıl yük veri mühendisliği: çok kaynaklı, formatları ve limitleri farklı API'lerin sürekli işletimi, sinyal/gürültü ayrımının doğrulanması ve işletim maliyeti (sürekli tarama + LLM çağrıları). Ajan mimarisi olgunlaşıyor ama üretim kalitesinde tutmak deneyim ister.
- **Veri bağımlılığı: Çok yüksek — ağırlıklı dış veri.** Patent ve yayın verileri açık API'lerle büyük ölçüde erişilebilir (EPO/OpenAlex ücretsiz katmanlar), ancak hacim büyüyünce ticari lisans maliyeti doğar; TÜRKPATENT'in programatik veri erişimi belirsiz — resmi işbirliği projenin kritik yol maddesi. İç bağımlılık düşük: müşterinin teknoloji ağacı filtre olarak yeter.
- **Pazar potansiyeli: Yüksek.** Segment %22 CAGR ile pazarın en hızlı büyüyeni; premium fiyatlanabilir ve Teknoloji Modülü'nü pasif envanterden canlı istihbarat ürününe çevirir. Risk: küresel oyuncular (PatSnap, ITONICS) güçlü — Türkçe kaynaklar, TÜRKPATENT verisi ve yerel destek programı sinyalleri farklılaşma alanıdır.

### 4. Kurumsal Ar-Ge Bilgi Grafı (Knowledge Graph)

**Ne:** Projeler, personel, yetkinlikler, teknolojiler, patentler, dokümanlar ve dış paydaşlar arasındaki ilişkileri tek bir graf modelinde birleştiren katman. Üzerinde: uzman bulma ("elektromanyetik uyumluluk deneyimi olan kim var?"), yetkinlik boşluğu analizi, proje-teknoloji-strateji izlenebilirliği ve graf tabanlı öneri sistemleri çalışır.

**Neden şimdi:** Bilgi grafları, LLM'lerin halüsinasyonunu azaltan ve kurumsal veriye yapı kazandıran temel teknoloji olarak patent analitiği ve foresight araçlarında hızla yaygınlaşıyor; GraphRAG mimarileri 2025–2026'da olgunlaştı.

**Altyapı uyumu:** Argelog'un üç modülü aynı varlıklar (proje, kişi, teknoloji, fikir) etrafında dönüyor ama ilişkiler bugün tablolarda örtük; graf katmanı bu veriyi yeni ürün özelliklerinin ortak zemini yapar. Fikir #1 (Copilot) ve #3'ün (Kâşif) isabetini doğrudan artırır — platformun sonraki beş yıllık YZ yol haritasının temel taşıdır.

**Çıktılar:** Graf veri modeli ve ETL hattı, uzman/yetkinlik arama, görsel keşif arayüzü.

**Değerlendirme**
- **Teknoloji yığını:** Graf veri tabanı (Neo4j / Memgraph, veya mevcut PostgreSQL üzerine Apache AGE ile düşük riskli başlangıç); LLM destekli varlık/ilişki çıkarımı (dokümanlardan NER); ontoloji/şema tasarımı (proje-kişi-teknoloji-patent-doküman); GraphRAG katmanı (Copilot'un isabetini artırmak için); görselleştirme (Cytoscape.js / D3).
- **Zorluk: Yüksek (4/5).** Teknoloji değil modelleme zorluğu: üç modülün örtük ilişkilerini tutarlı bir ontolojiye oturtmak, mevcut şemadan ETL ve veri kalitesi temizliği en büyük emek kalemi. Yanlış ontoloji seçimi sonraki tüm YZ özelliklerine taşınır — baştan iyi tasarım kritik.
- **Veri bağımlılığı: Yüksek — tamamen iç veri.** Dış kaynak gerekmez; mevcut platform verisi yeterli. Risk veri miktarı değil kalitesi: eksik/tutarsız kayıtlar grafa taşınmadan temizlenmeli. Bu yönüyle dış bağımlılık riski en düşük projelerden.
- **Pazar potansiyeli: Doğrudan orta, dolaylı çok yüksek.** Tek başına satılabilir bir modül değil, **çarpan altyapı**: Copilot'un (#1) doğruluğunu, Kâşif'in (#3) kişiselleştirmesini ve uzman bulma gibi özellikleri mümkün kılar. Yatırım getirisi diğer fikirlerin başarısı üzerinden ölçülmeli; platformun 5 yıllık YZ yol haritasının temelidir.

### 5. Mevzuat Uyum ve Teşvik Otomasyonu (Ar-Ge RegTech)

**Ne:** 5746 sayılı kanun kapsamındaki Ar-Ge/Tasarım Merkezi yükümlülüklerini uçtan uca otomatikleştiren modül: personel zaman takibi ile teşvik (gelir vergisi stopajı, SGK, kurumlar vergisi indirimi) hesaplamalarının otomasyonu, denetim öncesi eksik/tutarsız veri tespiti (LLM destekli belge doğrulama), mevzuat değişikliklerinin izlenip etki analizinin otomatik çıkarılması.

**Neden şimdi:** RegTech, kurumsal yazılımda en yüksek ödeme istekliliği olan kategorilerden; Türkiye'de Ar-Ge merkezi denetimleri sıkılaşırken merkezlerin en büyük operasyonel yükü uyum raporlamasıdır.

**Altyapı uyumu:** Argelog'un veri doğrulama ve mevzuat uyum kontrolleri özelliği zaten var — bu proje, mevcut kural tabanlı kontrolleri YZ destekli, mali boyutu da kapsayan tam otomasyona taşır. Rakiplerin (global platformların) Türk mevzuatını bilmemesi, Argelog'a savunulabilir yerel hendek kazandırır.

**Çıktılar:** Teşvik hesaplama motoru, denetim hazırlık panosu, mevzuat değişiklik izleyici.
**Destek uyumu:** TÜBİTAK 1507/1501.

**Değerlendirme**
- **Teknoloji yığını:** Versiyonlanabilir iş kuralları motoru (mevzuat değişimini kod değişikliği olmadan yönetmek için); bordro/ERP entegrasyon konnektörleri (Logo, SAP, Netsis, Mikro); LLM destekli belge doğrulama ve eksik/tutarsız veri tespiti; Resmî Gazete / mevzuat izleme tarayıcısı + değişiklik fark analizi (LLM özetleme); raporlama ve denetim izi katmanı.
- **Zorluk: Orta (3/5).** Teknik karmaşıklık orta; asıl zorluk alan bilgisidir — mali müşavirlik/YMM düzeyinde 5746 uzmanlığı ekibe dahil edilmeli ve mevzuat her değiştiğinde bakım yükü doğar (bu yük aynı zamanda abonelik gelirinin gerekçesidir). Hesaplama hatasının müşteriye mali sonucu olacağı için test/doğrulama disiplini yüksek tutulmalı.
- **Veri bağımlılığı: Orta.** Mevzuat kaynakları kamuya açık; kritik bağımlılık müşteri tarafında bordro/zaman verisi entegrasyonudur (ERP çeşitliliği entegrasyon emeğini belirler). Dış API riski yok.
- **Pazar potansiyeli: Çok yüksek (yerel), sınırlı (küresel).** 1.300+ Ar-Ge/Tasarım Merkezi'nin zorunlu ve acılı ihtiyacı; ödeme istekliliği yüksek (denetim riski + teşvik tutarları büyük), küresel rakiplerin giremeyeceği mevzuat hendeği var. Karşılığında pazar Türkiye ile sınırlı — ölçek tavanı bilinerek fiyatlanmalı.

### 6. Prediktif Proje Riski ve Portföy Optimizasyonu

**Ne:** Platformda biriken tarihsel proje verisinden (süre, bütçe, kaynak, THS ilerlemesi, sonuç) öğrenen ML modelleriyle: proje gecikme/bütçe aşımı erken uyarısı, portföy düzeyinde Monte Carlo simülasyonu, kaynak darboğazı tahmini ve "hangi proje karması stratejik hedefe en yüksek katkıyı verir" optimizasyonu.

**Neden şimdi:** Prediktif analitik, inovasyon yönetimi pazar raporlarında büyümenin üç ana sürücüsünden biri; Ar-Ge yöneticilerinin karar destek beklentisi tanımlayıcı raporlamadan öngörüye kaymış durumda.

**Altyapı uyumu:** Argelog'un "veri odaklı yönetim sistemi" konumlanmasının doğal bir üst basamağı; 10+ yıllık müşteri tabanındaki proje geçmişi, modellerin eğitimi için kritik ve taklit edilmesi zor bir varlık.

**Çıktılar:** Risk skorlama modeli, portföy simülasyon motoru, yönetici karar panosu.

**Değerlendirme**
- **Teknoloji yığını:** Klasik ML (gradyan artırma, gecikme tahmini için survival analizi); Monte Carlo simülasyon motoru; portföy optimizasyonu (OR-Tools / PuLP ile kısıt programlama); özellik mühendisliği hattı; yönetici panosu için BI/görselleştirme katmanı; model izleme ve yeniden eğitim (MLOps).
- **Zorluk: Orta-yüksek (3,5/5).** Modelleme teknikleri olgun; zorluk veri hacmi ve kalitesinde. Bir müşterinin kendi proje geçmişi model eğitmeye yetmeyebilir — müşteriler arası anonimleştirilmiş öğrenme (veya sektör bazlı önceden eğitilmiş modeller) tasarlanmalı, bu da gizlilik mühendisliği getirir. Tahminlerin güven aralığıyla ve açıklamayla sunulması (yanlış alarm yönetimi) ürünleşmenin kritik parçası.
- **Veri bağımlılığı: Çok yüksek — iç, uzun tarihsel veri.** En az 2–3 yıllık, sonuçlanmış proje geçmişi gerekir; Argelog'un 10+ yıllık kurulu tabanı burada gerçek ve taklit edilemez avantajdır. Yeni müşterilerde özellik ancak veri biriktikçe açılır (ürün kurgusunda beklenti yönetimi şart).
- **Pazar potansiyeli: Yüksek.** Prediktif analitik pazarın üç ana büyüme sürücüsünden biri; C-seviyeye (portföy kararı verenlere) hitap ettiği için sözleşme değerini yükseltir ve mevcut müşterilerde upsell ürünüdür. Veri kilidi etkisi (geçmiş veri platformda biriktikçe geçiş maliyeti artar) müşteri tutundurmayı güçlendirir.

### 7. Kanıta Dayalı Otomatik THS/TRL Değerlendirme Asistanı

**Ne:** Proje dokümanlarını (test raporları, prototip kayıtları, yayınlar) LLM ile analiz ederek Teknoloji Hazırlık Seviyesi değerlendirmesini kanıta bağlayan asistan. Her TRL iddiası için destekleyici kanıtı gösterir, eksik kanıtı işaretler, seviye geçişleri için gereken adımları önerir ve zaman içindeki THS ilerlemesini otomatik grafikler.

**Neden şimdi:** TRL değerlendirmesi hem TEYDEB süreçlerinde hem savunma/havacılık tedarik zincirlerinde (SAHA İstanbul ekosistemi) zorunlu hâle geliyor; bugün büyük ölçüde öznel ve elle yapılıyor. LLM'lerin belge anlama yeteneği bu işi otomatikleştirilebilir kıldı.

**Altyapı uyumu:** THS takibi Argelog'un mevcut Ar-Ge modülünün öne çıkan özelliği — bu proje onu "form doldurma"dan "denetlenebilir kanıt zinciri"ne dönüştürür ve savunma sanayii müşteri segmentinde farklılaşma yaratır.

**Çıktılar:** Kanıt-iddia eşleştirme motoru, TRL geçiş yol haritası üreteci, denetim izi raporu.

**Değerlendirme**
- **Teknoloji yığını:** LLM belge analizi + yapılandırılmış çıktı (TRL kriter şablonlarına karşı kanıt eşleştirme); RAG (proje doküman arşivi üzerinde); TRL kriter bilgi tabanı (NASA/AB/TÜBİTAK tanımları + sektörel uyarlamalar); denetim izi ve raporlama katmanı. Copilot (#1) ile aynı doküman işleme altyapısını paylaşır — marjinal maliyeti düşüktür.
- **Zorluk: Orta (2,5/5).** Kapsamı dar, problemi iyi tanımlı (TRL kriterleri standart ve kamuya açık) — 10 fikir içinde uygulanması en hızlı olanlardan. Zorluk, sektöre göre kanıt türlerinin değişmesi (yazılımda TRL ile donanımda TRL farklı görünür) ve değerlendirmenin "denetlenebilir" sayılması için insan onay adımının doğru kurgulanması.
- **Veri bağımlılığı: Orta — iç doküman verisi.** Proje dokümanları (test raporları, prototip kayıtları) yeterli; dış veri gerekmez. Etiketli TRL değerlendirme örneği az olsa da kriterlerin açık tanımlı olması few-shot/kural hibrit yaklaşımı mümkün kılar.
- **Pazar potansiyeli: Orta-yüksek (niş ama güçlü).** Yatay pazarı sınırlı; ancak savunma/havacılık tedarik zincirinde (SAHA İstanbul ekosistemi, ana yüklenici alt-yüklenici denetimleri) THS kanıtlama zorunluluğu keskinleşiyor — bu segmentte belirgin farklılaşma ve yeni müşteri kapısı. TEYDEB süreçlerinde de her başvuru sahibine dokunur.

### 8. Açık İnovasyon Eşleştirme Platformu (İhtiyaç–Çözüm Pazaryeri)

**Ne:** Kurumların teknoloji ihtiyaçlarını; startup'lar, üniversite araştırma grupları, teknoparklar ve tedarikçilerin yetkinlikleriyle embedding tabanlı anlamsal eşleştirmeyle buluşturan ağ katmanı. Müşteriler arası anonimleştirilmiş yetkinlik keşfi, ortak proje (konsorsiyum) kurulum sihirbazı ve TÜBİTAK/Ufuk Avrupa ortaklı çağrılarına eşleştirme içerir.

**Neden şimdi:** Açık inovasyon, inovasyon platformlarının en hızlı büyüyen kullanım senaryosu; Türkiye'de üniversite-sanayi işbirliği teşvikleri (YÖK, TÜBİTAK 1505) talebi artırıyor.

**Altyapı uyumu:** İnovasyon Yönetimi Modülü'ndeki açık inovasyon ve ekosistem takibi özelliklerinin ağ etkisi üreten hâli — Argelog'un İSO 100 müşteri portföyü, pazaryerinin "talep tarafını" ilk günden hazır getirir. Bu proje, Argelog'u araç satıcısından **ağ platformuna** dönüştürme potansiyeli taşır.

**Çıktılar:** Anlamsal eşleştirme motoru, anonim yetkinlik profili protokolü, konsorsiyum kurulum akışı.

**Değerlendirme**
- **Teknoloji yığını:** Embedding tabanlı anlamsal eşleştirme + LLM yeniden sıralama (ihtiyaç metni ↔ yetkinlik profili); çok kiracılı (multi-tenant) platform mimarisi ve kiracılar arası kontrollü veri paylaşım katmanı; anonimleştirme/açığa çıkarma (progressive disclosure) protokolü; profil zenginleştirme için dış kaynak entegrasyonları (teknopark firma rehberleri, üniversite araştırma envanterleri); çağrı eşleştirme için TÜBİTAK/Ufuk Avrupa duyuru tarayıcısı.
- **Zorluk: Yüksek (4/5) — teknikten çok iş modeli zorluğu.** Eşleştirme motoru orta zorlukta; asıl zorluk pazaryerinin soğuk başlangıcı (arz tarafını — startup/üniversite profillerini — sıfırdan kurmak), taraflar arası güven/gizlilik tasarımı ve platform operasyonudur. Teknik ekip kadar ekosistem geliştirme ekibi ister.
- **Veri bağımlılığı: Yüksek — dış ve ağ verisi.** Talep tarafı (kurumsal ihtiyaçlar) mevcut müşterilerden gelir; arz tarafı verisi (çözüm sağlayıcı profilleri) dışarıdan toplanmalı ve güncel tutulmalı. Veri ortaklıkları (teknoparklar, TTO'lar, SAHA İstanbul) projenin ön koşuludur.
- **Pazar potansiyeli: Çok yüksek potansiyel, yüksek risk.** Başarılı olursa Argelog'u araç satıcısından ağ etkisi olan platforma dönüştürür — 10 fikir içinde tavanı en yüksek olan budur; kazanan-hepsini-alır dinamiği erken hareket avantajını değerli kılar. Başarısızlık riski de en yüksek: ağ kurulamzsa eşleştirme değeri doğmaz. Aşamalı kurgu (önce mevcut müşteriler arası kapalı ağ, sonra dışa açılım) riski düşürür.

### 9. Fikrî Mülkiyet Zekâsı Modülü (Patent Analitiği + Fikir Sahipliği Güvencesi)

**Ne:** İki bileşen: (a) proje ve fikirler için **patentlenebilirlik ön analizi** — benzer patentlerin otomatik taranması, yenilik farkının LLM ile özetlenmesi, rakip patent portföylerinin izlenmesi (rakibin bugünkü başvuruları, 18–24 ay sonraki ürün yönünü gösterir); (b) fikir havuzuna giren önerilerin **kriptografik zaman damgasıyla** sahiplik kaydı (iç buluş bildirimi süreçleri ve 6769 sayılı SMK'daki çalışan buluşları yükümlülükleri için).

**Neden şimdi:** YZ destekli patent zekâsı pazarı 2035'e kadar ~8 milyar USD'ye büyüyor; patent analitiği bu pazarın en büyük segmenti. Fikir doğrulama + IP güvenliği entegrasyonu, pazar raporlarında belirgin trend olarak geçiyor.

**Altyapı uyumu:** Ar-Ge çıktısı → patent süreci bugün platformun dışında kalıyor; bu modül yaşam döngüsünü kapatır. Fikir #3'ün patent veri hattını yeniden kullanır.

**Çıktılar:** Patentlenebilirlik ön rapor üreteci, rakip portföy izleyici, buluş bildirimi + zaman damgası iş akışı.
**Destek uyumu:** TÜRKPATENT işbirliği; TÜBİTAK 1501.

**Değerlendirme**
- **Teknoloji yığını:** Patent API'leri (EPO OPS, WIPO, TÜRKPATENT) — #3 ile ortak veri hattı; patent-özel arama (CPC sınıflandırma + patent diline uyarlanmış embedding modelleri); LLM ile istem (claim) analizi ve yenilik farkı özetleme; rakip portföy izleme için zamanlanmış tarama; fikir sahipliği için RFC 3161 kriptografik zaman damgası (blockchain opsiyonel, zorunlu değil); buluş bildirimi iş akışı motoru.
- **Zorluk: Yüksek (4/5).** Patent dili ve istem yapısı özel NLP uzmanlığı ister; benzerlik aramasının kalitesi (gerçek öncül tekniği bulma) ürünün güvenilirliğini belirler. Kritik tasarım sınırı: çıktılar "ön analiz"dir, hukuki görüş değildir — sorumluluk çerçevesi ve patent vekilleriyle işbirliği modeli baştan kurulmalı. Zaman damgası bileşeni ise düşük zorluklu, hızlı kazanım.
- **Veri bağımlılığı: Çok yüksek — dış patent verisi.** #3 ile aynı lisans/erişim bağımlılıkları; iki proje birlikte planlanırsa veri maliyeti paylaşılır. İç bağımlılık düşük (fikir/proje metinleri mevcut).
- **Pazar potansiyeli: Yüksek.** YZ destekli patent zekâsı 2035'e doğru ~8 milyar USD'ye büyüyen pazarın en büyük segmenti; Türkiye'de kurumsal patent farkındalığı ve başvuru sayıları artıyor. Premium fiyatlanabilir; patent vekili firmalarla kanal ortaklığı (rekabet değil tamamlayıcılık) satışı hızlandırır. Buluş bildirimi + SMK uyum akışı, Ar-Ge merkezlerinin mevzuat kaynaklı somut ihtiyacıdır.

### 10. Stratejik Öngörü ve Senaryo Planlama Modülü (Foresight)

**Ne:** Teknoloji Yol Haritası özelliğinin üzerine kurulan öngörü katmanı: trend radarından (Fikir #3) beslenen **senaryo üretimi** (LLM destekli "eğer X teknolojisi 2029'da olgunlaşırsa portföyümüz nasıl etkilenir?" analizleri), yapılandırılmış uzman görüşü toplama (dijital Delphi), teknoloji yol haritasının senaryolara göre otomatik stres testi ve yönetim kuruluna sunulabilir öngörü raporları.

**Neden şimdi:** Senaryo planlama ve YZ destekli trend analizi modülleri, 2026 pazar raporlarında karar isabetini artıran öne çıkan yenilikler arasında; foresight, global rakiplerin (ITONICS vb.) ana farklılaşma alanı ve Argelog'un "strateji odaklı platform" konumlanmasıyla birebir örtüşüyor.

**Altyapı uyumu:** Teknoloji Yol Haritası + teknoloji olgunluk analizi + trend radarı verilerinin sentezi; üç modülün verisini tek stratejik ürüne dönüştürerek platformun C-seviyesindeki (CTO/CINO) değerini artırır.

**Çıktılar:** Senaryo üretim motoru, dijital Delphi aracı, yol haritası stres testi simülatörü.

**Değerlendirme**
- **Teknoloji yığını:** LLM tabanlı senaryo üretimi (yapılandırılmış senaryo şablonları + trend radar girdileri); dijital Delphi aracı (çok turlu anonim uzman anketi, yanıt sentezi LLM ile); yol haritası stres testi için kural/simülasyon motoru (senaryo parametreleri → portföy etkisi); trend radar görselleştirme; yönetim raporu üreteci. #3'ün sinyal verisi ve #6'nın simülasyon motoruyla ortak bileşenler kullanır.
- **Zorluk: Orta-yüksek (3,5/5).** Teknik bileşenler orta zorlukta; asıl zorluk çıktı kalitesinin öznelliği — üretilen senaryoların "yönetim kuruluna sunulabilir" derinlikte olması, genel geçer LLM metinlerinden ayrışması gerekir. Alan uzmanı (foresight metodolojisi) ile ürün ekibinin birlikte çalışması şart; değer kanıtı (ROI) diğer fikirlere göre daha zor ölçülür.
- **Veri bağımlılığı: Orta — karma.** Trend/sinyal verisi #3'ten beslenir (o olmadan dış trend kaynakları elle beslenmeli); uzman görüşü verisi Delphi turlarıyla platform içinde üretilir; iç yol haritası ve portföy verisi mevcut. #3 hayata geçmeden bağımsız çalışabilir ama gücü sınırlı kalır — sıralama açısından #3 sonrası konumlanmalı.
- **Pazar potansiyeli: Orta-yüksek.** Foresight, global rakiplerin (ITONICS vb.) ana farklılaşma ve premium fiyat alanı; alıcısı C-seviye (CTO/CINO) olduğundan sözleşme değerini büyütür ve Argelog'un danışmanlık hizmetleriyle paketlenerek (yazılım + metodoloji) satılmaya çok uygundur. Hacim ürünü değil, marj ve konumlandırma ürünüdür.

---

## Karşılaştırma Matrisi

| # | Proje | Temel teknoloji | Zorluk | Veri bağımlılığı | Pazar potansiyeli |
|---|---|---|---|---|---|
| 1 | Argelog Copilot | LLM + RAG, vektör DB | 🟡 3/5 | Yüksek (iç) | ⭐⭐⭐ Çok yüksek |
| 2 | Fikir Değerlendirme Motoru | Embedding, kümeleme, ML skorlama | 🟢 2,5/5 | Yüksek (iç, etiketli) | ⭐⭐ Yüksek |
| 3 | Agentic Teknoloji Kâşifi | Ajan çerçevesi, patent/yayın API'leri | 🔴 4/5 | Çok yüksek (dış) | ⭐⭐ Yüksek |
| 4 | Ar-Ge Bilgi Grafı | Graf DB, GraphRAG, ontoloji | 🔴 4/5 | Yüksek (iç) | ⭐ Orta (dolaylı çok yüksek) |
| 5 | RegTech Uyum Otomasyonu | Kural motoru, ERP entegrasyonu, LLM doğrulama | 🟡 3/5 | Orta | ⭐⭐⭐ Çok yüksek (yerel) |
| 6 | Prediktif Portföy | ML, Monte Carlo, optimizasyon | 🟡 3,5/5 | Çok yüksek (iç, tarihsel) | ⭐⭐ Yüksek |
| 7 | THS/TRL Asistanı | LLM belge analizi, kanıt eşleştirme | 🟢 2,5/5 | Orta (iç) | ⭐⭐ Orta-yüksek (niş) |
| 8 | Açık İnovasyon Ağı | Anlamsal eşleştirme, çok kiracılı mimari | 🔴 4/5 | Yüksek (dış, ağ) | ⭐⭐⭐ Çok yüksek (riskli) |
| 9 | IP Zekâsı | Patent NLP, CPC arama, zaman damgası | 🔴 4/5 | Çok yüksek (dış) | ⭐⭐ Yüksek |
| 10 | Foresight & Senaryo | LLM senaryo üretimi, Delphi, simülasyon | 🟡 3,5/5 | Orta (karma) | ⭐⭐ Orta-yüksek |

**Matristen çıkan stratejik okuma:**
- **En iyi zorluk/getiri oranı:** #2 ve #7 (düşük zorluk, hazır iç veri, net alıcı) ile #1 ve #5 (orta zorluk, çok yüksek pazar) — kısa vade portföyünün omurgası.
- **Dış veri bağımlılığı olan üçlü** (#3, #9 ve kısmen #8) ortak veri hattı üzerinde birlikte planlanmalı; patent API lisans maliyeti ve TÜRKPATENT erişimi tek seferde çözülürse üç ürünü birden besler.
- **#4 (Bilgi Grafı)** matriste doğrudan pazar puanı düşük görünse de #1, #3, #6 ve #10'un kalitesini belirleyen altyapıdır — kendi geliriyle değil, taşıdığı ürünlerin geliriyle değerlendirilmelidir.
- **Salt iç veriyle çalışan fikirler** (#1, #2, #4, #6, #7) dış lisans/API riski taşımaz ve Argelog'un birikmiş müşteri verisini hendeğe çevirir; dış veri gerektirenler ise pazar tavanı daha yüksek ama işletim maliyetli ürünlerdir — portföy iki grubu dengelemelidir.

## Önceliklendirme Önerisi

| Ufuk | Projeler | Gerekçe |
|---|---|---|
| **Kısa vade (0–12 ay)** | #1 Copilot, #2 Fikir Değerlendirme, #5 RegTech | Mevcut veri ve modüller üzerinde hızla ürünleşir; müşteriye görünür YZ değeri ve yerel mevzuat hendeği |
| **Orta vade (12–24 ay)** | #4 Bilgi Grafı, #6 Prediktif Portföy, #7 THS Asistanı | Graf katmanı sonraki tüm YZ özelliklerinin temelidir; tarihsel veri avantajını ürünleştirir |
| **Uzun vade (24+ ay)** | #3 Tech Scouting Ajanı, #9 IP Zekâsı, #8 Açık İnovasyon Ağı, #10 Foresight | Dış veri hatları ve ağ etkisi gerektirir; Argelog'u araçtan platforma taşır |

Projelerin tamamı TÜBİTAK 1501/1507 kapsamında desteklenebilir nitelikte yazılım Ar-Ge'si içerir; #3, #9 için TÜRKPATENT, #8 için teknopark/üniversite işbirlikleri başvuru gücünü artırır.

---

## Kaynaklar

- [Argelog – Çözümler](https://argelog.com.tr/cozumler) · [Hakkımızda](https://argelog.com.tr/hakkimizda) · [Ar-Ge Yönetimi](https://argelog.com.tr/arge-yonetimi) · [İnovasyon ve Teknoloji Yönetimi](https://argelog.com.tr/inovasyon-ve-teknoloji-yonetimi)
- [Innovation Management Software Market Report 2026 — Research and Markets](https://www.researchandmarkets.com/reports/6245152/innovation-management-software-market-report)
- [Innovation Management Software Market Analysis 2026 — Cognitive Market Research](https://www.cognitivemarketresearch.com/innovation-management-software-market-report)
- [AI Driven Innovation Software: The 2026 Enterprise Trend Report — Ideawake](https://ideawake.com/ai-driven-innovation-software-the-2026-enterprise-trend-report/)
- [Top 10 Best Innovation Management Software 2026 — ITONICS](https://www.itonics-innovation.com/blog/top-innovation-management-software)
- [AI in Patent & Market Intelligence Market — Fortune Business Insights](https://www.fortunebusinessinsights.com/ai-in-patent-market-intelligence-market-114122) · [Precedence Research](https://www.precedenceresearch.com/ai-in-patent-and-market-intelligence-market)
- [AI-Powered Technology Scouting — Traction Technology](https://www.tractiontechnology.com/blog/how-ai-is-transforming-technology-scouting)
- [Technology Scouting Software Market Forecast 2026-2034 — Verified Market Reports](https://www.verifiedmarketreports.com/product/technology-scouting-software-solution-market/)
