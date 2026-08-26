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

---

## Market-Fit Analizi

Her fikir, Türkiye pazarı özelinde web araştırmasıyla (rakipler, mevzuat sinyalleri, talep kanıtları) ayrı ayrı analiz edildi; skorlar fikirler arası karşılaştırılabilirlik için tek kalemden normalize edildi.

**Skala:** Acı şiddeti — 5: zorunlu/yakıcı ihtiyaç … 1: hoş-olur. PMF riski — 5: talep tamamen varsayımsal … 1: neredeyse garanti talep. *Hiçbir fikir acıda 5 almadı; her acı bugün danışman + Excel + genel LLM üçlüsüyle "yeterince iyi" gideriliyor — bu, tüm portföyün ortak gerçeğidir.*

### Market-Fit Özet Matrisi

| # | Fikir | Acı şiddeti | PMF riski | Alıcı persona | Ödeme kancası |
|---|---|---|---|---|---|
| 5 | RegTech | **4/5** | **2/5** 🟢 | Ar-Ge Md. + CFO | Teşvik iptali/geri ödeme riski (sigorta değeri) |
| 1 | Copilot | 3/5 | 3/5 🟢 | Ar-Ge Merkezi Müdürü | Zorunlu yıllık rapor + TEYDEB yükü |
| 2 | Fikir Motoru | 2/5 | 3/5 🟡 | İnovasyon Yöneticisi | Komite iş yükü, program güvenilirliği |
| 7 | THS Asistanı | 3/5 | 4/5 🟡 | Ar-Ge/Program Direktörü | TEYDEB ön değerlendirme + SSB/EYDEP pratiği |
| 9 | IP Zekâsı | 3/5 | 4/5 🟡 | Ar-Ge Dir. / IP Yöneticisi | 6769 SMK çalışan buluşu yükümlülüğü |
| 3 | Teknoloji Kâşifi | 2/5 | 4/5 🔴 | Teknoloji/Strateji Müdürü | Yol haritasını kanıtla savunma |
| 4 | Bilgi Grafı | 2/5 | 4/5 🔴 | Ar-Ge Direktörü / CTO | Personel devriyle bilgi kaybı |
| 6 | Prediktif Portföy | 2/5 | 4/5 🔴 | PMO/Program Direktörü | Gecikme cezaları, portföy raporu |
| 8 | Açık İnovasyon Ağı | 2/5 | 4/5 🔴 | İnovasyon/İş Gel. Direktörü | Konsorsiyum ortağı bulma (dönemsel) |
| 10 | Foresight | 2/5 | 4/5 🔴 | Strateji Direktörü / GMY | YK'ya "geleceğe hazırız" hikâyesi |

**PMF olasılığı en yüksek üçlü: #5 → #1 → #2. En riskli üçlü: #10, #8, #4.**

### Fikir Bazında Market-Fit Detayı

**#1 Copilot** — Hedef: 1.300+ Ar-Ge/Tasarım Merkezi; gerçekçi ilk küme mevcut müşteriler + düzenli TEYDEB başvurucusu ~100-200 hesap. Alternatifler: teşvik danışmanları, Word şablonları ve giderek artan genel ChatGPT kullanımı; TEYDEB/5746 formatına özel Türkçe rakip ürün aramalarda bulunamadı. Ödeme: bağımsız üründe düşük, mevcut lisansa %25-40 "AI eklentisi" olarak yüksek; on-prem kurulumda premium. **En büyük risk: "ChatGPT yeter" ikamesi** — fark, kurumsal arşiv entegrasyonu ve format doğruluğuyla kanıtlanmalı. Talep kanıtı güçlü: TÜBİTAK'ın Üretken YZ kullanım rehberi yayınlaması başvurularda YZ'yi meşrulaştırdı; Horizon Europe 2025'ten beri YZ kullanım beyanı istiyor; globalde Grantable/Grant Assistant kategoriyi doğruladı. Doğrulama: 5-8 müşteriyle ücretli pilot ön-satışı (3+ ödeme taahhüdü hedefi); ürün yazmadan danışman+LLM ile concierge TEYDEB önerisi üretimi.

**#2 Fikir Motoru** — Hedef: aktif öneri programı olan ~150-300 kuruluş (İSO 500 ∩ Ar-Ge merkezleri). Alternatifler ciddi: globalde Qmarkets/ITONICS/Brightidea'da bu yetenek standartlaştı; Türkiye'de innoCentrum pazar lideri, oneri.io YZ ile mükerrer tespiti zaten pazarlıyor. **En büyük risk: "ürün değil özellik"** — ayrı ödeme istekliliği oluşmayabilir; ikincisi başarı skoru için cold-start. Konumlandırma savunma amaçlı olmalı: innoCentrum/oneri.io'ya karşı İnovasyon Modülü'nün elde tutma hattı; ayrıştırıcı, Ar-Ge modülündeki geçmiş TEYDEB/proje verisinden gelen başarı skoru. Doğrulama: 5-10 müşterinin gerçek fikir havuzuyla PoC (komite süresindeki azalmayı ölç); fiyat etiketli LOI kampanyası (10 görüşmede 3 yazılı niyet).

**#3 Teknoloji Kâşifi** — Hedef: teknoloji yönetimi olgunluğu olan ~150-300 firma; Argelog'un erişebildiği çekirdek ~30-80 hesap. Acı normalize edilerek 2'ye çekildi: teknoloji izleme mevzuatla zorunlu değil, patent vekillerinin ucuz manuel izlemesi ve ücretsiz Espacenet "yeterince iyi". Globalde kategori kalabalık (PatSnap, Questel, Cypris — $20-80K/yıl); Türkiye'de yerli SaaS rakip bulunamadı, ama bu boşluk kanıtlanmış yazılım talebinin zayıflığına da işaret. Dolaylı kanca: 5746 performans göstergelerindeki patent kriteri; savunmada STM ThinkTech'in varlığı segment talebini gösteriyor. **Satış biçimi kritik: self-servis SaaS değil, danışmanlıkla paketlenmiş "yönetilen scouting raporu".** Doğrulama: yarı-manuel aylık zayıf sinyal raporunu 3 ay ücretli pilot olarak sat (>%50 yenileme hedefi); mevcut Teknoloji Radarı ekranına fake-door "Ajan Uyarıları" butonu.

**#4 Bilgi Grafı** — Hedef: 100+ Ar-Ge personelli çok-projeli yapılar (~150-250 firma). Acı gerçek ama kronik/gizli: "uzman bulamama"nın maliyeti hissediliyor ama bütçe önceliği almıyor; alıcı "graf altyapısı" değil somut senaryo satın alır. **En büyük risk: altyapı katmanının tek başına bütçelenmemesi + Microsoft 365 Copilot/Glean gibi genel amaçlı araçların aynı ihtiyacı "bedavaya yakın" karşılaması.** Türkiye'de Ar-Ge'ye özel rakip yok, ama talep de şimdilik varsayımsal. Market-fit açısından doğru konum: müşteriye satılan ürün değil, #1/#3/#6'yı güçlendiren iç altyapı; dışa dönük yüzü yalnızca "uzman bulma + denetim izlenebilirliği" senaryoları olmalı. Doğrulama: "son uzman bulamadığınızda maliyeti ne oldu?" görüşmeleri (3 LOI hedefi); tek müşteride 4-6 haftalık ücretli PoC.

**#5 RegTech** — **Portföyün en güçlü market-fit'i.** Tek fikir ki acısı mevzuata bağlı: faaliyet raporu Mayıs sonu zorunlu, merkezler en geç 2 yılda bir denetleniyor, eksiklikte 3 ay durdurma/belge iptali/teşvik geri ödemesi var; teşvikler 2028 sonuna kadar uzatıldı (pazar garantili). Alıcı çift başlı: Ar-Ge Müdürü + CFO — "sigorta + tasarruf" argümanı bütçe açtırıyor. Dikkat: pazar boş değil — ArgeMemory (Vertex) ve Ar-GeNet zaten 5746/4691 hesaplama satıyor; farklılaşma LLM tabanlı denetim öncesi tutarsızlık tespiti ve mevzuat etki analizi katmanında (bu katmanın yerli muadili bulunamadı). Globalde Boast.ai/Neo.tax kategoriyi doğruladı. **En büyük risk: mevcut araçların "yeterince iyi" görülmesi** — YMM'lerle rekabet değil ortaklık kurgusu şart. Doğrulama: 2-3 müşterinin dönemlik bordro/teşvik verisiyle "tespit edilen risk/eksik teşvik: X TL" concierge raporu (rapora ödeme = gerçek WTP testi); "5746 denetim hazırlık" webinarı (30 günde 20+ nitelikli demo talebi hedefi).

**#6 Prediktif Portföy** — Hedef: 20+ eşzamanlı proje yürüten ~150-300 firma. Acı normalize edilerek 2'ye indi: yakıcı olduğu savunma ana yüklenicilerinde sorun zaten Primavera Risk/Safran + Monte Carlo pratiğiyle çözülmüş; orta segment ise eksikliği dert etmiyor. **En büyük risk: veri kıtlığı** — tek merkezin onlarca projelik tarihçesi "öğrenen ML" vaadini besleyemez, ürün kural tabanlı simülasyona geriler ve nPlan (750.000+ takvimle eğitilmiş) tarzı gerçek ML ile arasındaki fark güven sorunu yaratır; savunmada müşteriler arası veri havuzlama fiilen imkânsız. Doğrulama önce gelsin: 3-5 müşterinin geçmiş verisiyle retrospektif "gecikmeyi tahmin edebilir miydik?" analizi — hem veri yeterliliğini hem tahmin değerini ürün yazmadan ölçer.

**#7 THS Asistanı** — Hedef: SAHA'nın 1.000+ üyesi içinde aktif ürün geliştiren ~250-400 firma; çekirdek, ana yüklenici (ASELSAN/TUSAŞ/ROKETSAN) alt tedarikçileri. Mevzuat kancası yarım: THS beyanı 2020'den beri TEYDEB ön değerlendirme kriteri ve SSB kılavuz yayınlamış/EYDEP değerlendiriyor — ama **kanıta dayalı denetlenebilir zincir henüz hiçbir kurumca zorunlu değil; ürünün çekirdek vaadi bu zorunluluk gelmeden "hoş-olur"da kalabilir (en büyük risk).** Acı dönemsel (başvuru/denetim anları), bugün TÜBİTAK'ın Excel soru setleri + danışmanla çözülüyor; alternatiflerin ucuz/bedava olması fiyat çıpasını düşürüyor. İkinci engel: savunma verisinde bulut LLM kabul edilmez — on-prem mimari şart. Doğrulama: EYDEP danışmanlarıyla kanal ortaklığı görüşmesi; gerçek test raporları üzerinden yarı-manuel ücretli THS raporu satışı.

**#8 Açık İnovasyon Ağı** — Acı normalize edilerek 2'ye indi: ortak bulma ihtiyacı kanıtlı (SAHA EXPO'da 25.000+ B2B görüşme planı, TÜBİTAK'ın eşleştirme etkinlikleri) ama dönemsel ve **ücretsiz/kamu sübvanseli ikamelerle gideriliyor: İSTKA destekli Zemin360, Here2Next, AB'nin ücretsiz Funding&Tenders/B2Match araçları, SAHA'nın kendi yerlileştirme portalı.** En büyük risk: soğuk başlangıç + bedava rakipler — ücretli talep bugün büyük ölçüde varsayımsal. Market-fit'e giden yol bağımsız pazaryeri değil: mevcut ürüne gömülü "çağrı-yetkinlik eşleştirme radarı" (paraya bağlanan tek kanca TÜBİTAK/UA çağrıları ve savunmada yerlileştirme taraması). Doğrulama: 3-5 müşteriye elle yapılan ücretli "teknoloji tarama raporu" (50-100 bin TL); TTO ortaklı pilotta arz tarafının profil doldurma oranı (<%20 = soğuk başlangıç doğrulandı).

**#9 IP Zekâsı** — Hedef: düzenli patent başvurusu yapan ~200-400 firma (patent aktivitesi az sayıda büyük firmada yoğun — 2025'te Türk Telekom tek başına 921 başvuru). Mevzuat kancası gerçek ama baskısı zayıf: 6769 SMK çalışan buluşu bildirimi + 4 aylık hak talebi süresi dava riski doğuruyor, ama çoğu firma e-posta/Excel + vekille idare ediyor. **En büyük risk: IP işinin "vekile devredilmiş dış hizmet" olarak görülmesi** — vekil ücretsiz ön araştırmayla modülü gereksizleştirebilir. Doğru kurgu: vekillerle rekabet değil kanal ortaklığı; zaman damgası bileşeni emtia (TÜBİTAK zaman damgası zaten ucuz), değer SMK uyum iş akışı + faaliyet raporu patent göstergesi entegrasyonunda. Doğrulama: 15-20 müşteriyle bildirim süreci/vekil harcaması sayısallaştırma görüşmesi; ücretli "patentlenebilirlik ön analizi + süreç kurulumu" concierge paketi.

**#10 Foresight** — Hedef en dar segment: foresight fonksiyonu kurabilecek ~50-150 kurum (1.300+ Ar-Ge merkezinin büyük çoğunluğu alıcı değil). **İki yapısal sorun: talep proje bazlı ve süreksiz (kurumlar senaryo çalışmasını 2-3 yılda bir danışmanlık projesi olarak alıyor — EY, Istanbul Foresight Institute, MindEx bu talebi bugün danışmanlıkla topluyor) ve çekirdek vaat genel amaçlı LLM'lerle neredeyse bedavaya taklit edilebilir.** Ayrıca alıcı persona (strateji ofisi) Argelog'un alıştığı Ar-Ge Müdürü'nden farklı — yeni satış kası gerekir. Uygun model salt SaaS değil: 6-12 aylık ücretli foresight projesi içine gömülü platform, sonra Teknoloji Modülü'ne eklenti lisans. Doğrulama ilk adımı acımasız olmalı: müşterilere "son 3 yılda foresight'a fiilen para harcadınız mı, kime, ne kadar?" — harcama geçmişi yoksa talep varsayımsaldır.

### Portföy Düzeyi Market-Fit Çıkarımları

1. **Acıyı belirleyen tek tutarlı eksen mevzuat kancası:** 5746 denetim/geri ödeme riskine bağlanan RegTech (#5) tek başına 4 seviyesinde; zorunlu ama dönemsel yükümlülüğe dayananlar (#1, #7, #9) 3'te; düzenleyici tetikleyicisi olmayan verimlilik fikirleri (#2, #3, #4, #6, #8, #10) 2'de kümeleniyor.
2. **On fikrin tamamı mevcut tabana upsell** — bu Argelog'un kanal gücüyle örtüşüyor ama ortak zayıflık: #5 hariç neredeyse hiçbiri bağımsız bütçe kalemi açtıramıyor. Doğru fiyatlama, tek tek ürünler değil mevcut üç modüle %20-40 bandında "AI katmanı" eklentileri; bu da gelir tavanını mevcut müşteri sayısına bağlıyor — büyüme için müşteri adedi de artmalı.
3. **Tekrarlayan en büyük PMF riski rekabet değil ikame:** genel amaçlı LLM'ler (#1, #2, #10'un çekirdek vaadini bedavaya taklit ediyor), ücretsiz/kamu sübvanseli platformlar (#8) ve mevcut dış hizmet sağlayıcılar — danışmanlar, YMM'ler, patent vekilleri (#5, #7, #9). Savunulabilir tek ayrıştırıcı, Argelog modüllerinde halihazırda biriken kurum içi proje/fikir/teşvik verisi; bu avantajın en somut olduğu fikirler #5 ve #1.
4. **Analitik/ML iddialı fikirler (#4, #6, kısmen #3) ortak cold-start sorunu paylaşıyor:** müşteri başına tarihsel veri "öğrenen sistem" vaadini besleyecek hacimde değil. Bunlar önce ürün olarak değil, hibrit modele uygun "yönetilen danışmanlık raporu" formatında test edilmeli; ürünleştirme kararı pilot yenileme oranına ertelenmeli.
5. **Çekirdek-çevre yapısı:** önce #5 ile zorunlu-tekrarlayan acıya çapa at, #1'i aynı alıcıya doküman katmanı olarak bindir, #2'yi İnovasyon Modülü'nün savunma hattı (innoCentrum/oneri.io'ya karşı) olarak konumla. #8 ve #10 Argelog'un satış modeliyle yapısal uyumsuz (biri iki taraflı pazaryeri, diğeri farklı alıcı persona) — en son ele alınmalı.

### Sahadan İlk Doğrulama Sinyali: Kale (#1, #5, #9)

Kale'den gelen görüş, #1 (Copilot), #5 (RegTech) ve #9 (IP Zekâsı) için bu bağlamda ihtiyaçları olduğu yönünde — analizden sonra gelen ilk gerçek saha talebi.

**Sinyalin anlamı:** Üçlünün seçimi rastgele değil; market-fit analizindeki mevzuat kancalı grubun (acı 3-4 bandı) tam kendisi ve üçü de **aynı alıcı personada** birleşiyor (Ar-Ge Merkezi yönetimi + mali işler/hukuk). Birlikte tutarlı bir **"Ar-Ge Merkezi Uyum ve Üretkenlik Paketi"** oluşturuyorlar: #5 zorunlu uyum çekirdeği, #1 aynı verinin üzerine doküman üretim katmanı, #9 Ar-Ge çıktısının IP tarafını kapatan halka. Tek platform + tek satış görüşmesi + tek pilot ile üçü birden test edilebilir.

**Fikir bazında ne değişti:**
- **#9 için en kritik güncelleme:** PMF riski "talep büyük ölçüde varsayımsal" gerekçesiyle 4/5'ti — Kale görüşü bu fikir için ilk somut talep beyanı. Görüşmede vekil harcaması ve buluş bildirim hacmi sayısallaştırılırsa risk okuması aşağı çekilebilir.
- **#1 için:** "ChatGPT yeter" ikame riskine karşı ilk kurumsal karşı-kanıt — demek ki genel LLM'ler bu ihtiyacı kapatmıyor. Kale'nin kendi arşiviyle concierge pilot için ideal aday.
- **#5 için:** Zaten en güçlü PMF'ye sahipti; sinyal, dokümandaki 1 numaralı doğrulama deneyini (yapılandırılmış görüşme) doğrudan başlatma fırsatı verdi.

*Not: Tek hesabın beyanı pazar geneli PMF skorlarını değiştirmez; skorlar korunuyor. Değişen şey doğrulama yolu: Kale, "design partner" adayı olarak deney sürecini aylarca kısaltır ve pilot sonucu (yenileme + referans) diğer İSO 100 hesaplara satışın kanıtı olur.*

**Önerilen hamle — keşif görüşmesi soru seti** (doğrulama deneylerinden derlenmiş):
1. **#5:** Teşvik hesabı ve denetim hazırlığına bugün kim, kaç saat harcıyor? Son denetimde ne çıktı? Hangi araç kullanılıyor (ArgeMemory/Ar-GeNet/Excel/YMM)? — rekabet istihbaratı için de kritik.
2. **#1:** TEYDEB önerilerini ve faaliyet raporunu kim yazıyor, yıllık danışman maliyeti ne? KVKK/bilgi güvenliği tarafında on-prem şartı var mı? (Savunma bağlantılı işlerde bulut LLM engeli baştan netleşmeli.)
3. **#9:** Son 2 yılda kaç buluş bildirimi ve patent başvurusu yapıldı, vekile yıllık ödeme ne? 6769 SMK çalışan buluşu süreci bugün nasıl yönetiliyor (e-posta/Excel mi)?
4. **Ödeme testi:** Görüşme, ücretli pilot teklifiyle kapanmalı — ücretsiz PoC değil. Ödeme taahhüdü, analizdeki tüm doğrulama deneylerinin ortak eşiği.

**Pilot kurgusu önerisi (8-12 hafta, ücretli):** #5'ten başla — bir dönemlik bordro/teşvik verisiyle "tespit edilen risk / eksik teşvik: X TL" raporu (concierge, ürün yazmadan); üzerine #1'den bir faaliyet raporu bölümü + bir TEYDEB önerisi taslağı üretimi; #9'dan buluş bildirimi iş akışının kurulumu. Çıkış kriterleri: pilot ücretinin ödenmesi, yenileme niyeti ve referans olma onayı.

### İkinci Sinyal: #5 İçin İkinci Görüş

#5 (RegTech) için ikinci bir firmadan da bu yönde ihtiyaç görüşü geldi — **#5 artık portföyde iki bağımsız saha sinyali olan tek fikir** ve çekirdek proje statüsü kesinleşti. Bu, zaten en düşük olan PMF riskini (2/5) teyit ediyor; ancak doğrulama eşiği değişmedi: iki görüş de henüz ödeme değil, gerçek test hâlâ ücretli pilot.

**İkinci sinyalin somut etkileri:**
1. **Pilot kurgusu güçleniyor:** İki aday, sıralı iki pilot demek — Kale ile başla, ikinci firmayı 4-6 hafta arayla ardına al. İkinci pilot, ilkinin bulgularının **tekrarlanabilirlik testi** olur: aynı concierge rapor formatı farklı bir bordro düzeninde de değer üretiyorsa ürünleştirme kararı sağlam zemine oturur.
2. **İP3 (bordro entegrasyonları) gereksinimi gerçek veriyle netleşir:** İki firmanın kullandığı bordro/ERP sistemleri farklıysa, plandaki "2 konnektör" hedefi iki gerçek müşteriyle test edilir — test ortamı ihtiyacı azalır, konnektör önceliği varsayımla değil sahayla belirlenir. Keşif görüşmelerinde her iki firmanın bordro sistemi mutlaka öğrenilmeli.
3. **Fiyatlama A/B testi imkânı:** İki hesapta iki farklı fiyat noktası/paket denenebilir (ör. yıllık abonelik vs. abonelik + bulunan eksik teşvik üzerinden başarı primi) — tek hesapla yapılamayan ödeme istekliliği ölçümü.
4. **TÜBİTAK başvurusu güçlenir:** İki sanayi firmasından niyet mektubu (LOI), 1501/1507 önerisinin ticarileşme/yaygın etki bölümünü somutlaştırır — görüşmelerin hedeflerinden biri yazılı LOI olmalı.
5. **Program takvimine etki:** #5'in kapsamı ve önceliği değişmiyor (zaten programın ilk projesi); değişen, İP5'in tek pilot yerine iki pilotu kapsaması — ikinci pilot ay 9-11'e denk gelir ve efora ~2 adam-ay eklenir (bütçe etkisi ~0,5 M TL, pilot geliriyle karşılanabilir).

## Önceliklendirme Önerisi

| Ufuk | Projeler | Gerekçe |
|---|---|---|
| **Kısa vade (0–12 ay)** | #1 Copilot, #2 Fikir Değerlendirme, #5 RegTech | Mevcut veri ve modüller üzerinde hızla ürünleşir; müşteriye görünür YZ değeri ve yerel mevzuat hendeği |
| **Orta vade (12–24 ay)** | #4 Bilgi Grafı, #6 Prediktif Portföy, #7 THS Asistanı | Graf katmanı sonraki tüm YZ özelliklerinin temelidir; tarihsel veri avantajını ürünleştirir |
| **Uzun vade (24+ ay)** | #3 Tech Scouting Ajanı, #9 IP Zekâsı, #8 Açık İnovasyon Ağı, #10 Foresight | Dış veri hatları ve ağ etkisi gerektirir; Argelog'u araçtan platforma taşır |

Projelerin tamamı TÜBİTAK 1501/1507 kapsamında desteklenebilir nitelikte yazılım Ar-Ge'si içerir; #3, #9 için TÜRKPATENT, #8 için teknopark/üniversite işbirlikleri başvuru gücünü artırır.

**Market-fit analiziyle güncellenen sıralama:** Kısa vade üçlüsü doğrulandı ancak iç sırası değişti — giriş noktası #5 (RegTech) olmalı (tek zorunlu-tekrarlayan acı, en düşük PMF riski), #1 (Copilot) aynı alıcıya ikinci katman olarak bindirilmeli, #2 savunma amaçlı (rekabete karşı) konumlanmalı. #8 ve #10, teknik yol haritasında "uzun vade"de dursa da market-fit açısından portföyün en riskli fikirleri: ikisi de önce ucuz doğrulama deneylerinden geçmeden yatırım almamalı.

---

## Proje Seçimi: Gereksinim, Bütçe ve Zaman Planı

### Varsayımlar

Tüm hesaplar şu varsayımlara dayanır; değişirse tablolar orantılı güncellenmelidir:

- **Adam-ay tam maliyeti: ortalama 250 bin TL** (2026 ikinci yarı; brüt ücret + işveren yükleri + genel gider payı; kıdem karışımına göre 180–350 bin TL bandı). Argelog ~10 kişilik ekip olduğundan aynı anda **en fazla 1,5–2 projelik kapasite** (4–6 FTE geliştirme) gerçekçidir — plan buna göre kademelidir.
- **LLM/bulut işletimi** geliştirme döneminde proje başına aylık 30–60 bin TL; canlıda müşteri sayısıyla ölçeklenir (fiyatlamaya maliyet+marj olarak yansıtılmalı).
- **TÜBİTAK finansmanı:** Argelog KOBİ olduğundan 1507/1501 kapsamında destek oranı ~%75; çağrı bütçe üst limitleri dönemsel değiştiği için başvuru öncesi güncel çağrı duyurusundan teyit edilmeli. Büyük bütçeli projeler gerekirse faz bölünerek ayrı projeler hâlinde sunulur.

### Tüm Portföy: Kaba Efor, Süre ve Bütçe

| # | Proje | Süre (MVP) | Efor (adam-ay) | Bütçe bandı | Not |
|---|---|---|---|---|---|
| 5 | RegTech | 9 ay | 22–26 | 6,5–8 M TL | + mevzuat/YMM danışmanlığı dahil |
| 1 | Copilot | 9 ay | 18–22 | 5,5–7 M TL | on-prem GPU opsiyonu +1,5–2 M TL |
| 9 | IP Zekâsı | 8 ay | 15–18 | 4,5–5,5 M TL | SMK iş akışı 2 ayda ayrılabilir quick-win |
| 2 | Fikir Motoru | 6–8 ay | 12–16 | 3,5–4,5 M TL | dedup/kümeleme ilk 3 ayda çıkar |
| 7 | THS Asistanı | 6–8 ay | 12–16 | 3,5–4,5 M TL | on-prem şartı bütçeyi artırır |
| 10 | Foresight | 8–10 ay | 16–20 | 5–6 M TL | danışmanlık projesine gömülü başlamalı |
| 6 | Prediktif Portföy | 9–12 ay | 18–24 | 5,5–7 M TL | önce retrospektif veri analizi (1 ay, ~300 bin TL) |
| 4 | Bilgi Grafı | 10–12 ay | 24–30 | 7–9 M TL | ontoloji tasarımı dahil; altyapı yatırımı |
| 3 | Teknoloji Kâşifi | 12–15 ay | 30–40 | 9–12 M TL | + yıllık 1,5–2 M TL veri/işletim gideri |
| 8 | Açık İnovasyon Ağı | 12–18 ay | 30–40 | 9–12 M TL | + ekosistem geliştirme ekibi (yazılım dışı) |

**Seçim okuması:** Kale sinyali alan üçlü (#5+#1+#9) toplamda ~55–66 adam-ay ve 16,5–20,5 M TL — TÜBİTAK %75 desteğiyle net yük ~4–5 M TL'ye iner ve üçü aynı alıcıya satıldığı için tek ticari kanalla geri kazanılır. Aynı bütçeyle #3 veya #8'den yalnızca biri yapılabilirdi ve ikisinin de PMF riski 4/5. Seçim net: **program = #5 → #9 (quick-win) → #1.**

### Seçilen Üçlü: Detay Planlar

#### #5 RegTech — 9 ay, 22–26 adam-ay, 6,5–8 M TL

**MVP gereksinimleri (kapsam içi):** 5746 teşvik hesaplama motoru (stopaj, SGK, KV indirimi; versiyonlanabilir kural seti); personel zaman/proje eşleştirmesinden teşvik matrahı üretimi; en az 2 bordro entegrasyonu (Logo + 1 diğeri; Kale'nin kullandığı sistem öncelikli); denetim hazırlık panosu (eksik/tutarsız veri tespiti — önce kural tabanlı, LLM doğrulama ay 6+); faaliyet raporu veri tutarlılık kontrolü. **Kapsam dışı (v2):** 4691 teknopark modu, mevzuat değişikliği otomatik etki analizi, ERP çeşitliliğinin tamamı.

| İş paketi | Aylar | Efor (AA) |
|---|---|---|
| İP1 — Mevzuat kural setinin çıkarılması ve doğrulanması (YMM danışmanıyla) | 1–3 | 4 |
| İP2 — Hesaplama motoru + kural motoru altyapısı | 2–6 | 8 |
| İP3 — Bordro entegrasyonları (2 konnektör) | 4–7 | 5 |
| İP4 — Denetim hazırlık panosu + LLM belge doğrulama | 5–8 | 5 |
| İP5 — Kale pilotu: gerçek dönem verisiyle paralel hesap + "risk/eksik teşvik" raporu | 7–9 | 3 |

**Bütçe:** personel 24 AA × 250 bin = 6,0 M; YMM/mevzuat danışmanlığı 0,6 M; bulut/LLM 0,35 M; entegrasyon test ortamları ve lisanslar 0,3 M; beklenmedik %10 ≈ **toplam ~7,9 M TL**. Kritik kabul testi: motorun çıktısı, Kale'nin bir döneminde YMM hesabıyla kuruş düzeyinde mutabık kalmalı.

#### #9 IP Zekâsı — 8 ay, 15–18 adam-ay, 4,5–5,5 M TL

**Gereksinimler — iki fazlı:** **Faz A (ay 1–2, quick-win):** 6769 SMK çalışan buluşu bildirim iş akışı (bildirim formu, 4 aylık yasal süre takibi, onay zinciri, RFC 3161 zaman damgası, faaliyet raporu patent göstergesine otomatik besleme) — mevcut platform altyapısıyla yazılır, Kale'ye 2. ayın sonunda canlı gösterilir. **Faz B (ay 3–8):** patentlenebilirlik ön analizi (EPO OPS + PATENTSCOPE + TÜRKPATENT taraması, benzerlik araması, LLM yenilik farkı özeti) ve rakip portföy izleme (aylık otomatik rapor).

| İş paketi | Aylar | Efor (AA) |
|---|---|---|
| İP1 — SMK buluş bildirimi iş akışı + zaman damgası (Faz A) | 1–2 | 3 |
| İP2 — Patent veri hattı (EPO/WIPO/TÜRKPATENT erişimi) | 3–5 | 4 |
| İP3 — Benzerlik araması + LLM yenilik farkı raporu | 4–7 | 5 |
| İP4 — Rakip portföy izleme + Kale pilotu (gerçek buluş bildirimleriyle) | 6–8 | 3 |

**Bütçe:** personel 15 AA × 250 bin = 3,75 M; patent vekili danışmanlığı (rapor kalitesi doğrulama) 0,3 M; veri erişimi (EPO OPS ücretsiz; olası ticari tamamlayıcı) 0,4 M; bulut/LLM 0,25 M; beklenmedik %10 ≈ **toplam ~5,2 M TL**. Not: İP2 hattı ileride #3'e (Teknoloji Kâşifi) doğrudan taşınır — bütçenin bir kısmı gelecek projenin ön yatırımıdır.

#### #1 Copilot — 9 ay, 18–22 adam-ay, 5,5–7 M TL

**MVP gereksinimleri (kapsam içi):** doküman işleme hattı (mevcut modüllerdeki proje kayıtları + yüklenen arşiv; OCR, parçalama, erişim yetkisine saygılı indeksleme); RAG tabanlı Türkçe soru-cevap (kaynak gösterimli — halüsinasyon kontrolü için zorunlu); faaliyet raporu bölüm taslağı üretimi (Bakanlık formatına şablonlu); TEYDEB öneri taslağı asistanı (bölüm bölüm, insan onaylı akış); müşteri başına veri izolasyonu. **Kapsam dışı (v2):** on-prem LLM (pilot bulutta KVKK uyumlu başlar; Kale görüşmesinde on-prem şartı çıkarsa +2 ay ve +1,5–2 M TL GPU sunucu bütçelenir), çok dilli destek, otomatik gönderim.

| İş paketi | Aylar | Efor (AA) |
|---|---|---|
| İP1 — Doküman işleme ve indeksleme hattı | 1–3 | 5 |
| İP2 — RAG çekirdeği + kaynak gösterimli Türkçe QA | 2–5 | 5 |
| İP3 — Faaliyet raporu + TEYDEB taslak üreteçleri | 4–7 | 5 |
| İP4 — Değerlendirme seti (kalite ölçümü), KVKK/güvenlik sertleşmesi | 6–8 | 3 |
| İP5 — Kale pilotu: kendi arşivleriyle canlı kullanım, 1 gerçek TEYDEB önerisi | 7–9 | 2 |

**Bütçe:** personel 20 AA × 250 bin = 5,0 M; LLM API/bulut 0,5 M; embedding/vektör altyapısı 0,15 M; veri hazırlama danışmanlığı (Kale arşiv taraması) 0,2 M; beklenmedik %10 ≈ **toplam ~6,5 M TL** (+on-prem opsiyonu ayrı kalem).

### Birleşik Program Takvimi (18 ay)

Kapasite kısıtı (4–6 FTE) nedeniyle üç proje kademeli yürür; #5 ile #9-Faz A paralel başlar, #1 ekip #5'ten boşaldıkça devreye girer:

| Ay | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| #5 RegTech | ██ | ██ | ██ | ██ | ██ | ██ | ██ | ██ | ██ | | | | | | | | | |
| #9 Faz A (SMK) | ██ | ██ | | | | | | | | | | | | | | | | |
| #9 Faz B (patent) | | | | | | | | | | ██ | ██ | ██ | ██ | ██ | ██ | | | |
| #1 Copilot | | | | | | | ██ | ██ | ██ | ██ | ██ | ██ | ██ | ██ | ██ | | | |
| Kale pilotları | | ▒▒ | | | | | ▒▒ | ▒▒ | ▒▒ | | | | ▒▒ | ▒▒ | ▒▒ | ▒▒ | | |
| Ticarileşme (diğer hesaplara satış) | | | | | | | | | | ▒▒ | ▒▒ | ▒▒ | ▒▒ | ▒▒ | ▒▒ | ██ | ██ | ██ |

**Kilometre taşları:** Ay 2 — SMK iş akışı Kale'de canlı (ilk görünür teslimat); Ay 9 — RegTech MVP + Kale mutabakat testi; Ay 12 — Copilot ilk gerçek TEYDEB önerisi; Ay 15 — üç ürün pilotta doğrulanmış; Ay 16–18 — referanslı satış kampanyası.

**Program bütçesi ve finansman:** Toplam ~19,6 M TL (üç projenin toplamı) / 18 ay. TÜBİTAK kurgusu: #5 ve #1 ayrı 1501/1507 projeleri, #9 daha küçük bütçesiyle 1507'ye uygun; %75 destek gerçekleşirse net öz kaynak yükü **~5 M TL** (aylık ~280 bin TL) — Kale pilot gelirleri (hedef: proje başına 0,3–0,8 M TL) ve mevcut nakit akışıyla taşınabilir düzey. Başvuru takvimi programın 1.–2. ayında tamamlanmalı; destek kararı beklenmeden Faz A (SMK) öz kaynakla başlatılmalı ki Kale ivmesi kaçmasın.

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
