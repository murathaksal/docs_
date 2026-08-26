# Teknopark Proje Başvuru Dosyası (Taslak)

## ARGUS — Ar-Ge Teşvik Uyumu için Yapay Zekâ Destekli Doğrulama ve Hesaplama Platformu

*4691 sayılı Teknoloji Geliştirme Bölgeleri Kanunu kapsamında proje başvurusu taslağı — Argelog A.Ş., Ağustos 2026*

> Bu taslak, başvuru yapılacak teknoparkın kendi form şablonuna aktarılmak üzere hazırlanmıştır. Bölüm başlıkları yaygın TGB başvuru formatını izler; hakem heyeti değerlendirme kriterleri (Ar-Ge niteliği, teknolojik yenilik, ticarileşme) gözetilmiştir. "ARGUS" çalışma adıdır, değiştirilebilir.

---

## 1. Proje Kimliği

| Alan | Bilgi |
|---|---|
| Proje adı | ARGUS — Ar-Ge Teşvik Uyumu için Yapay Zekâ Destekli Doğrulama ve Hesaplama Platformu |
| Başvuru sahibi | Argelog Ar-Ge Merkezi Yönetim Danışmanlığı ve Yazılım Hizmetleri A.Ş. |
| Proje süresi | 12 ay (9 ay geliştirme + 3 ay saha doğrulama/sertleşme) |
| Teknoloji alanı | Yazılım / Yapay Zekâ — Doğal Dil İşleme, Kural Tabanlı Sistemler (NACE 62.01) |
| Tahmini bütçe | ~7,9 M TL + iki pilot genişletmesi ~0,5 M TL |
| THS (başlangıç → hedef) | THS 3 (kavram doğrulama) → THS 8 (gerçek ortamda kalifiye sistem) |
| Hedef pazar | Türkiye'deki 1.363 Ar-Ge Merkezi + 342 Tasarım Merkezi (5746) ve kurumsal teknopark firmaları (4691) |

## 2. Proje Özeti

5746 sayılı kanun kapsamındaki Ar-Ge ve Tasarım Merkezleri, her ay bordroyla iç içe geçen teşvik hesaplamaları (gelir vergisi stopajı teşviki, SGK işveren desteği, kurumlar vergisi indirimi) yapmak, yıllık faaliyet raporunu Mayıs sonuna kadar sunmak ve en geç iki yılda bir denetlenmek yükümlülüğü altındadır. Hatalı hesap veya eksik/tutarsız kayıt; teşvik geri ödemesi, üç ay durdurma ve belge iptali riski doğurur. Bu iş bugün Excel, YMM danışmanlığı ve parçalı bordro yazılımlarıyla, hataya açık ve emek-yoğun biçimde yürütülmektedir.

ARGUS; (a) mevzuat metinlerinden **versiyonlanabilir, çalıştırılabilir kural setleri** üreten ve mevzuat değişikliklerinde etki analizini otomatikleştiren bir kural motoru, (b) bordro/ERP verisiyle bütünleşen **kuruş mutabakatı hedefli teşvik hesaplama çekirdeği** ve (c) denetim öncesi eksik/tutarsız veriyi tespit eden, her bulgusunu mevzuat dayanağıyla açıklayan **büyük dil modeli (LLM) destekli hibrit doğrulama katmanı** geliştirmeyi amaçlayan bir Ar-Ge projesidir. Projenin araştırma boyutu, Türkçe mali-hukuki metinler üzerinde halüsinasyonsuz ve dayanak-gösterimli bilgi çıkarımı ile kural tabanlı ve olasılıksal (LLM) doğrulamanın açıklanabilir tek mimaride birleştirilmesidir. Çıktı, iki sanayi kuruluşunda (biri Kale grubu bünyesinde) sahada doğrulanacak ticari bir SaaS/on-prem üründür.

## 3. Firma Tanıtımı

Argelog, 2013'ten bu yana Türkiye'nin önde gelen İSO 100 sanayi kuruluşlarına inovasyon, teknoloji ve Ar-Ge yönetimi yazılımları sunan bir teknoloji firmasıdır. Ürün ailesi üç modülden oluşur: Ar-Ge Yönetimi (TÜBİTAK TEYDEB süreçleri, THS takibi, Ar-Ge Merkezi Faaliyet Raporu altyapısı, 5746 uyum kontrolleri), Teknoloji Yönetimi ve İnovasyon Yönetimi. SAHA İstanbul üyesidir. Bu proje, firmanın on yılı aşkın 5746/TEYDEB alan bilgisini ve müşteri tabanında birikmiş süreç verisini yapay zekâ destekli yeni bir ürün kategorisine taşımaktadır.

## 4. Projenin Amacı ve Hedefleri

**Amaç:** Ar-Ge/Tasarım Merkezlerinin 5746 teşvik ve raporlama yükümlülüklerini, denetlenebilir doğrulukta ve insan emeğini asgariye indirerek yöneten yapay zekâ destekli bir uyum platformu geliştirmek.

**Ölçülebilir hedefler:**
1. Teşvik hesaplama çekirdeğinin, pilot firmaların birer dönemlik gerçek verisinde YMM hesabıyla **kuruş düzeyinde mutabakat** sağlaması (tolerans: 0).
2. Doğrulama katmanının, bilinen hata enjekte edilmiş test setinde eksik/tutarsız kayıtların **≥ %90'ını** yakalaması; yanlış alarm oranının **≤ %10**'da kalması.
3. Her doğrulama bulgusunun ilgili mevzuat maddesine **dayanak bağlantısıyla** sunulması (dayanaksız bulgu üretimi: 0 toleransı — halüsinasyon kontrolü).
4. Bir mevzuat değişikliğinin kural setine yansıtılma süresinin, mevcut manuel pratiğe (günler) karşı **< 1 iş gününe** indirilmesi.
5. En az **2 bordro/ERP konnektörünün** (pilot firmaların kullandığı sistemler öncelikli) canlı veriyle çalışır durumda teslimi.
6. İki sanayi kuruluşunda ücretli pilot tamamlanması ve en az birinden yenileme/abonelik taahhüdü alınması.

## 5. Ar-Ge Niteliği ve Teknolojik Yenilik (Özgün Değer)

### 5.1 Teknik belirsizlikler ve araştırma soruları

Proje, rutin yazılım geliştirmenin ötesinde dört araştırma problemi içerir:

- **AS1 — Mevzuattan kurala çeviri (text-to-rule):** Türkçe mevzuat metinlerinden (kanun, yönetmelik, tebliğ, genelge) çalıştırılabilir hesaplama kurallarının yarı-otomatik çıkarımı ve her kuralın kaynak maddeyle izlenebilir bağının korunması. Türkçe mali-hukuki dil için bu problemin yayımlanmış çözümü yoktur; LLM destekli çıkarım + insan onaylı derleme hattı tasarlanacak ve doğruluğu ölçülecektir.
- **AS2 — Halüsinasyonsuz doğrulama:** LLM'lerin mali denetim bağlamında kullanımının önündeki temel engel, dayanaksız bulgu üretme riskidir. Proje; kural tabanlı kesin kontrollerle LLM'in bağlam-kısıtlı, yalnızca dayanak gösterebildiği bulguları raporlayabildiği **hibrit ve açıklanabilir bir doğrulama mimarisi** geliştirecek, "dayanaksız bulgu = 0" hedefini ölçülebilir kabul kriteri olarak tanımlayacaktır.
- **AS3 — Mevzuat değişikliği etki analizi:** Kural setlerinin zaman-versiyonlu tutulması (hangi dönem hangi kural setiyle hesaplanır) ve yeni bir düzenleme yayımlandığında etkilenen kuralların, müşterilerin ve geçmiş hesapların otomatik tespiti. Zamansal kural versiyonlama, mali mevzuat alanında özgün bir mühendislik problemidir.
- **AS4 — Heterojen bordro verisinde tutarlılık denetimi:** Farklı bordro/ERP şemalarından gelen verinin ortak modele normalize edilmesi ve proje-personel-zaman-teşvik zincirinde çapraz tutarlılık denetimi (ör. tam zamanlı eşdeğer hesabına giren personelin izin/görevlendirme kayıtlarıyla çelişkisi).

### 5.2 Mevcut duruma (state of the art) göre farklar

| Mevcut çözüm | Kapsamı | ARGUS farkı |
|---|---|---|
| Yerli teşvik yazılımları (ArgeMemory, Ar-GeNet) | Hesaplama/puantaj odaklı | LLM destekli denetim öncesi tutarsızlık tespiti ve dayanak-gösterimli bulgular yok; mevzuat değişikliği etki analizi yok |
| Bordro yazılımlarının teşvik modülleri (Logo vb.) | Bordro içi hesap | Ar-Ge süreç verisiyle (proje, faaliyet, THS) çapraz doğrulama yapamaz |
| YMM/danışmanlık hizmeti | Dönemsel, manuel | Sürekli izleme değil; ölçeklenmez; çıktı denetim izi üretmez |
| Global R&D tax otomasyon (Boast.ai, Neo.tax) | ABD/Kanada mevzuatı | Türk mevzuatını kapsamaz; Türkçe metin işleme yetenekleri yok |

Aramalarda, Türk mevzuatına özgü LLM tabanlı denetim öncesi doğrulama yapan yerli bir ürün tespit edilmemiştir; projenin bu katmanı ulusal düzeyde ilktir.

### 5.3 Projenin Ar-Ge çıktısı sayılma gerekçesi

Proje çıktısı; özgün veri modeli, zamansal kural motoru, Türkçe mali metin işleme bileşenleri ve hibrit doğrulama mimarisi içeren, teknik belirsizlikleri deneysel olarak giderilecek bir yazılım ürünüdür. Geliştirme sürecinde ölçüm setleri (hata enjeksiyonlu sentetik bordro verisi, mevzuat-kural eşleme altın seti) üretilecek; sonuçların akademik yayın/bildiri olarak paylaşılması hedeflenmektedir (en az 1 bildiri).

## 6. İş-Zaman Planı

| İP | Başlık | Aylar | Efor (AA) | Temel faaliyetler ve çıktılar |
|---|---|---|---|---|
| İP1 | Mevzuat analizi ve kural setinin çıkarılması | 1–3 | 4 | YMM/mevzuat uzmanıyla 5746 kural envanteri; AS1 text-to-rule deneyleri; **Ç1: onaylı kural kataloğu + çıkarım hattı prototipi** |
| İP2 | Zamansal kural motoru ve hesaplama çekirdeği | 2–6 | 8 | Versiyonlu kural motoru, teşvik hesaplama çekirdeği, birim test + altın set; **Ç2: kuruş-mutabakat testi geçen çekirdek** |
| İP3 | Bordro/ERP entegrasyonları | 4–7 | 5 | Ortak veri modeli, 2 konnektör (pilot firmaların sistemleri), veri normalizasyon katmanı; **Ç3: canlı veri akışı** |
| İP4 | Hibrit doğrulama katmanı ve denetim panosu | 5–8 | 5 | AS2/AS4 mimarisi, hata-enjeksiyon değerlendirme seti, denetim hazırlık panosu; **Ç4: ≥%90 yakalama / ≤%10 yanlış alarm raporu** |
| İP5 | Saha doğrulama — Pilot 1 (Kale) | 8–10 | 3 | Bir dönemlik gerçek veriyle paralel hesap, "tespit edilen risk / eksik teşvik" raporu, mutabakat; **Ç5: pilot 1 kabul raporu** |
| İP6 | Saha doğrulama — Pilot 2 + ürünleştirme | 10–12 | 3 | İkinci firmada tekrarlanabilirlik testi, fiyatlama doğrulaması, sertleşme, dokümantasyon; **Ç6: pilot 2 raporu + sürüm 1.0** |

Toplam efor: **28 adam-ay** (12 aya yayılmış, ortalama ~2,3 FTE + danışmanlık).

## 7. Proje Ekibi ve Personel Planı

| Rol | Kişi | Süre | Efor (AA) |
|---|---|---|---|
| Proje yöneticisi / ürün sahibi | 1 | 12 ay × 0,25 | 3 |
| Kıdemli arka uç geliştirici (kural motoru, hesaplama) | 2 | ay 1–12 | 14 |
| YZ/NLP mühendisi (AS1, AS2, AS4) | 1 | ay 1–10 | 7 |
| Ön yüz geliştirici (pano, iş akışları) | 1 | ay 4–9 × 0,5 | 3 |
| Test/kalite (altın setler, hata enjeksiyonu) | 1 | ay 5–12 × 0,5 | 1 (kısmi, İP içlerinde) |
| Mevzuat/YMM uzmanı | danışmanlık | ay 1–12 | (hizmet alımı) |

## 8. Bütçe

| Kalem | Tutar (TL) |
|---|---|
| Personel (28 AA × 250 bin ort. tam maliyet) | 7.000.000 |
| Mevzuat/YMM danışmanlığı (hizmet alımı) | 600.000 |
| Bulut altyapısı + LLM API kullanımı | 350.000 |
| Entegrasyon test ortamları ve yazılım lisansları | 300.000 |
| Beklenmedik giderler (~%5) | 400.000 |
| **Toplam** | **8.650.000** |

*Not:* İki pilotlu genişletilmiş kurgu bütçeye dahildir. Teknopark bünyesinde yürütülmesi hâlinde personel gelir vergisi ve SGK destekleri ile proje çıktısı yazılım satış gelirlerine 4691 kurumlar vergisi istisnası uygulanır; TÜBİTAK 1501/1507 desteğiyle birlikte kullanım durumunda mükerrer destek kurallarına göre kalemler ayrıştırılacaktır.

## 9. Riskler ve Önlemler

| Risk | Olasılık | Etki | Önlem / B planı |
|---|---|---|---|
| Mevzuat değişim hızının kural bakımını aşması | Orta | Yüksek | AS3 zamansal versiyonlama baştan mimaride; YMM danışmanıyla aylık mevzuat gözden geçirme; değişiklik izleme (Resmî Gazete) yarı-otomasyonu |
| LLM doğrulama katmanının hedef doğruluğa ulaşamaması | Orta | Orta | Hibrit mimari: kural tabanlı kontroller tek başına da ürünleşebilir; LLM katmanı kademeli devreye alınır (önce öneri modu, insan onaylı) |
| Bordro/ERP veri erişiminde gecikme | Orta | Orta | Pilot firmalarla veri erişim protokolü İP1'de imzalanır; konnektör önceliği pilotların gerçek sistemlerine göre belirlenir; dosya-tabanlı (CSV/e-bildirge) yedek içe aktarım yolu |
| KVKK / bordro verisi gizliliği | Düşük | Yüksek | Kişisel veri minimizasyonu, maskeleme, müşteri başına izolasyon; on-prem kurulum seçeneği; KVKK uyum görüşü alınması |
| Pilot firmaların takvim kayması | Orta | Düşük | İki bağımsız pilot (tek firmaya bağımlılık yok); pilotlar 2 ay kaydırılabilir tampon ile planlandı |
| Hesap hatasının müşteride mali sonuç doğurması | Düşük | Yüksek | "Kuruş mutabakatı" kabul kriteri; çift hesap (motor + YMM) doğrulama dönemi; sorumluluk sınırı sözleşmede "karar destek" konumu |

## 10. Ticarileşme Planı ve Pazar Potansiyeli

- **Pazar:** Türkiye'de 1.363 Ar-Ge Merkezi + 342 Tasarım Merkezi (2025 sonu); 5746 teşvikleri 31.12.2028'e kadar uzatılmış durumda. İkincil pazar: kurumsal ölçekli teknopark (4691) firmaları. Gerçekçi hedeflenebilir set: orta-büyük ölçekli 400–600 merkez.
- **Talep kanıtı:** İki sanayi kuruluşundan (biri Kale grubu bünyesinde) proje kapsamındaki ihtiyaca dair yazılı görüş alınmıştır; başvuru ekinde niyet mektubu (LOI) olarak sunulması hedeflenmektedir. Yerli rakiplerin (ArgeMemory, Ar-GeNet) varlığı kategori talebini ayrıca doğrulamaktadır.
- **Gelir modeli:** Personel sayısına kademeli yıllık abonelik + denetim öncesi "hazırlık taraması" paketi; pilotlarda abonelik ile "bulunan eksik teşvik üzerinden başarı primi" modelleri A/B test edilecektir.
- **Satış projeksiyonu (muhafazakâr):** Yıl 1 — 2 ücretli pilot + 3–5 abonelik; Yıl 2 — 12–18 müşteri; Yıl 3 — 30–40 müşteri. Mevcut Argelog müşteri tabanı (İSO 100) ilk satış kanalıdır; YMM/danışmanlık firmalarıyla kanal ortaklığı ikinci kanaldır.
- **Rekabet konumu:** Global oyuncular Türk mevzuatına giremez (yerel hendek); yerli rakiplere karşı fark, LLM destekli doğrulama katmanı ve Argelog platformundaki Ar-Ge süreç verisiyle çapraz denetimdir.

## 11. Fikri Mülkiyet ve Çıktılar

- Kaynak kod, veri modelleri ve kural derleme hattı Argelog mülkiyetinde; markalaşma (ARGUS) için marka başvurusu.
- AS1/AS2 mimarisi için patentlenebilirlik ön değerlendirmesi (proje ay 9'da); uygun bulunursa TÜRKPATENT başvurusu.
- Ölçüm setleri (anonimleştirilmiş hata-enjeksiyon değerlendirme seti) ve en az 1 akademik bildiri.
- Ticari çıktı: ARGUS v1.0 (SaaS + on-prem), 2 canlı konnektör, denetim hazırlık panosu.

## 12. Yaygın Etki

- Ar-Ge teşvik sisteminin doğru işlemesine katkı: hatalı teşvik kullanımının ve denetim kaynaklı geri ödemelerin azalması hem firmalar hem kamu açısından kazançtır.
- Ar-Ge merkezlerinde uyum için harcanan nitelikli mühendis/mali müşavir emeğinin Ar-Ge'nin kendisine kayması.
- Türkçe mali-hukuki metin işleme alanında yeniden kullanılabilir yöntem ve veri setleri (ulusal YZ ekosistemine katkı).
- Proje süresince 5+ nitelikli istihdam; ticarileşmeyle birlikte satış/destek istihdamı.

## 13. Başvuru Ekleri — Kontrol Listesi

- [ ] İki firmadan niyet mektubu (LOI) — keşif görüşmelerinde talep edilecek
- [ ] Proje ekibi özgeçmişleri
- [ ] Firma tanıtım dosyası ve mali tablolar
- [ ] Varsa: TÜBİTAK 1501/1507 başvuru/karar durumu (mükerrer destek beyanı)
- [ ] KVKK veri işleme değerlendirmesi (pilot veri protokolü taslağı)
- [ ] Teknoparkın kendi başvuru formu üzerinde bu içeriğin eşlenmesi

---

*Bu taslak, ana analiz dokümanındaki (arge-proje-fikirleri.md) #5 RegTech fikrinin market-fit analizi, bütçe/zaman planı ve iki saha sinyali üzerine inşa edilmiştir.*
