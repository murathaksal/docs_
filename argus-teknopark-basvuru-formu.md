# Teknopark Proje Başvuru Formu — ARGUS

*Teknoloji Geliştirme Bölgesi proje başvuru formu (standart portal formatı) — tüm başlıklar doldurulmuştur. Önceki Argelog.AI başvurusunun birebir başlık düzeni Drive erişimi açıldığında eşlenecektir.*

---

## 1. Proje Adı

**ARGUS — Ar-Ge Teşvik Uyumu için Yapay Zekâ Destekli Doğrulama ve Hesaplama Platformu**

## 2. Proje Süresi

12 ay (9 ay geliştirme + 3 ay saha doğrulama/sertleşme)

## 3. Teknoloji Alanı

- Birincil: **Yazılım — Yapay Zekâ / Doğal Dil İşleme** (Türkçe mali-hukuki metin işleme)
- İkincil: **Kurumsal Yazılım — Karar Destek ve İş Kuralları Sistemleri**
- NACE: 62.01 — Bilgisayar programlama faaliyetleri

## 4. Proje Konusu ve Amacı

5746 sayılı kanun kapsamındaki 1.363 Ar-Ge Merkezi ve 342 Tasarım Merkezi; her ay bordroyla iç içe geçen teşvik hesaplamaları (gelir vergisi stopajı teşviki, SGK işveren desteği, kurumlar vergisi indirimi) yapmak, yıllık faaliyet raporunu Mayıs sonuna kadar sunmak ve en geç iki yılda bir denetlenmek yükümlülüğü altındadır. Hatalı hesap veya eksik/tutarsız kayıt; teşvik geri ödemesi, üç ay durdurma ve belge iptali riski doğurur. Bu süreçler bugün Excel, YMM danışmanlığı ve parçalı bordro yazılımlarıyla, hataya açık ve emek-yoğun biçimde yürütülmektedir.

Projenin amacı; mevzuat metinlerinden çalıştırılabilir ve versiyonlanabilir kural setleri üreten, bordro/ERP verisiyle bütünleşerek kuruş mutabakatı hedefli teşvik hesaplaması yapan ve denetim öncesi eksik/tutarsız kayıtları büyük dil modeli (LLM) destekli hibrit bir mimariyle, her bulguyu mevzuat dayanağıyla birlikte raporlayarak tespit eden bir uyum platformu geliştirmektir.

## 5. Projenin Ar-Ge Niteliği, Yenilikçi ve Özgün Yönleri

Proje, rutin yazılım geliştirmenin ötesinde dört teknik belirsizlik/araştırma sorusu içerir:

1. **Mevzuattan kurala çeviri (text-to-rule):** Türkçe mevzuat metinlerinden (kanun, yönetmelik, tebliğ) çalıştırılabilir hesaplama kurallarının yarı-otomatik çıkarımı ve her kuralın kaynak maddeyle izlenebilir bağının korunması. Türkçe mali-hukuki dil için yayımlanmış bir çözüm yoktur.
2. **Halüsinasyonsuz doğrulama:** Kural tabanlı kesin kontroller ile LLM'in yalnızca dayanak gösterebildiği bulguları raporlayabildiği hibrit, açıklanabilir doğrulama mimarisi; "dayanaksız bulgu = 0" ölçülebilir kabul kriteridir.
3. **Zamansal kural versiyonlama ve mevzuat değişikliği etki analizi:** Hangi dönemin hangi kural setiyle hesaplanacağının bitemporal modellenmesi; yeni düzenleme yayımlandığında etkilenen kural, müşteri ve geçmiş hesapların otomatik tespiti.
4. **Heterojen bordro verisinde çapraz tutarlılık denetimi:** Farklı bordro/ERP şemalarının ortak modele normalize edilmesi ve proje-personel-zaman-teşvik zincirinde çelişki tespiti.

**Mevcut duruma göre farklar:** Yerli teşvik yazılımları (ArgeMemory, Ar-GeNet) hesaplama/puantaj odaklıdır; LLM destekli dayanak-gösterimli denetim öncesi doğrulama ve mevzuat değişikliği etki analizi katmanı hiçbirinde yoktur. Global R&D-tax otomasyon ürünleri (Boast.ai, Neo.tax) ABD/Kanada mevzuatına özeldir. Projenin doğrulama katmanı ulusal düzeyde ilktir.

## 6. Projede Kullanılacak Teknolojiler — Teknoloji Yığını

### 6.1 Katman katman teknoloji yığını

| Katman | Teknoloji | Gerekçe |
|---|---|---|
| **Ön yüz** | React 18 + TypeScript, Vite, TailwindCSS; grafikler için Recharts | Kurumsal panolarda yaygın, bileşen ekosistemi olgun; mevcut Argelog platform ön yüzüyle ortak bileşen kütüphanesi kurulacak |
| **API / uygulama katmanı** | .NET 8 (C#) Web API — mevcut Argelog platform yığınıyla hizalanır; REST + kısmi gRPC (konnektör iletişimi) | Kurumsal müşteri BT onaylarında güçlü; decimal hassasiyetli mali hesap için olgun tip sistemi |
| **Kural motoru (özgün geliştirme)** | YAML/JSON tabanlı kural tanım dili (DSL) + özel yürütme motoru; bitemporal versiyonlama (geçerlilik dönemi × yayım tarihi); karşılaştırma değerlendirmesi için NRules | Projenin Ar-Ge çekirdeği; hazır kural motorları zamansal mevzuat versiyonlamayı desteklemediği için özgün geliştirilir |
| **Hesaplama çekirdeği** | Deterministik decimal aritmetik; event-sourcing ile her hesabın denetim izi; property-based test (FsCheck) + altın set regresyonu | "Kuruş mutabakatı" kabul kriteri ve denetlenebilirlik zorunluluğu |
| **YZ/NLP katmanı** | Birincil: Claude API (Sonnet 5 — analiz; Haiku 4.5 — yüksek hacimli ön eleme, maliyet kademelemesi). RAG: mevzuat korpusu üzerinde embedding tabanlı erişim + zorunlu dayanak-atıflı yapılandırılmış çıktı (tool use/structured output). On-prem seçeneği: açık ağırlıklı Türkçe-yetkin model (Qwen/Llama sınıfı) + vLLM sunumu | AS1/AS2 araştırma soruları; bulut LLM kabul etmeyen müşteriler için mimari eşdeğerlik |
| **Vektör arama / mevzuat deposu** | PostgreSQL 16 + pgvector (mevzuat maddeleri, embedding'ler, kural-madde bağları tek veri tabanında) | Ayrı vektör DB işletim yükü olmadan dayanak-izlenebilirliği; bitemporal şema ile aynı yerde |
| **Veri katmanı** | PostgreSQL 16 (şema-bazlı çok kiracılı izolasyon), Redis (önbellek/kuyruk), MinIO (S3-uyumlu belge deposu — bordro dosyaları, kanıt belgeleri) | KVKK gereği müşteri başına izolasyon; on-prem'de aynı yığın değişmeden kurulur |
| **Entegrasyon katmanı** | Konnektör çerçevesi: Logo/Netsis/Mikro/SAP bordro sistemleri için adaptörler (REST/DB görünümü/dosya); e-bildirge, muhtasar-prim XML/CSV içe aktarım; SFTP toplu aktarım; webhook'lar | İP3 kapsamı; pilot firmaların gerçek sistemleri konnektör önceliğini belirler |
| **Raporlama** | Şablon tabanlı PDF/Excel üretimi (Bakanlık faaliyet raporu formatı, denetim hazırlık raporu, "risk / eksik teşvik" özeti) | Ç5/Ç6 pilot teslimatlarının çıktı formatı |
| **Güvenlik / KVKK** | Alan bazlı şifreleme (kimlik/ücret verileri), maskeleme, RBAC + SSO (OIDC/SAML — kurumsal AD entegrasyonu), kapsamlı denetim logu, veri minimizasyonu | Bordro verisi hassas kişisel veri; kurumsal BT/KVKK onay süreçlerinin ön şartı |
| **DevOps / dağıtım** | Docker; SaaS için Kubernetes, on-prem için K3s/Compose paketi + Helm; GitHub Actions CI/CD; Terraform (IaC); OpenTelemetry + Prometheus/Grafana izleme | Aynı imajın SaaS ve on-prem dağıtımı — iki pazarın tek kod tabanından beslenmesi |
| **Kalite / değerlendirme altyapısı** | Hata-enjeksiyonlu sentetik bordro veri seti üreteci; mevzuat-kural eşleme altın seti; doğrulama katmanı için otomatik skorlama düzeneği (yakalama/yanlış alarm ölçümü) | Hedef 2-3'ün (≥%90 yakalama, ≤%10 yanlış alarm, dayanaksız bulgu=0) ölçülebilir kanıtı |

### 6.2 Mimari özet

Çok kiracılı web platformu → konnektörlerle bordro/ERP verisi normalize edilir → bitemporal kural motoru dönem bazlı teşvik hesabını üretir (deterministik, denetim izli) → hibrit doğrulama katmanı (kural kontrolleri + dayanak-kısıtlı LLM) tutarsızlıkları mevzuat atıflarıyla raporlar → denetim hazırlık panosu ve resmi rapor çıktıları. Tüm YZ çıktıları insan onaylı akışa bağlıdır; sistem "karar destek" konumundadır.

## 7. Projenin Katma Değer Unsurları ve Uygulanabilirliği

- **Ölçülebilir başarı kriterleri:** YMM hesabıyla kuruş mutabakatı (tolerans 0); hata-enjeksiyon setinde ≥%90 yakalama / ≤%10 yanlış alarm; dayanaksız bulgu 0; mevzuat değişikliğinin kural setine yansıması <1 iş günü; 2 canlı bordro konnektörü.
- **Uygulanabilirlik kanıtı:** İki sanayi kuruluşundan (biri Kale grubu bünyesinde) yazılı ihtiyaç görüşü alınmıştır; her ikisiyle ücretli saha pilotu proje planına dahildir (İP5-İP6).
- **Firma yetkinliği:** Argelog 2013'ten beri 5746/TEYDEB alanında İSO 100 firmalarına yazılım geliştirmektedir; alan bilgisi ve müşteri verisi erişimi mevcuttur.

## 8. İş Paketleri ve Zaman Planlaması

| İP | Başlık | Aylar | Efor (AA) | Çıktı |
|---|---|---|---|---|
| İP1 | Mevzuat analizi, kural envanteri, text-to-rule deneyleri | 1–3 | 4 | Onaylı kural kataloğu + çıkarım hattı prototipi |
| İP2 | Bitemporal kural motoru ve hesaplama çekirdeği | 2–6 | 8 | Kuruş-mutabakat testi geçen çekirdek |
| İP3 | Bordro/ERP konnektörleri (2 adet) ve veri normalizasyonu | 4–7 | 5 | Canlı veri akışı |
| İP4 | Hibrit doğrulama katmanı + denetim hazırlık panosu | 5–8 | 5 | ≥%90 yakalama / ≤%10 yanlış alarm raporu |
| İP5 | Saha doğrulama — Pilot 1 (Kale) | 8–10 | 3 | Pilot 1 kabul raporu, "risk/eksik teşvik" çıktısı |
| İP6 | Saha doğrulama — Pilot 2, fiyat doğrulama, sürüm 1.0 | 10–12 | 3 | Pilot 2 raporu + ARGUS v1.0 |

Toplam: **28 adam-ay / 12 ay** (ort. ~2,3 FTE + danışmanlık).

## 9. Proje Personeli

| Rol | Kişi | Görev | Efor (AA) |
|---|---|---|---|
| Proje yöneticisi / ürün sahibi | 1 | Planlama, pilot koordinasyonu, kabul kriterleri | 3 |
| Kıdemli arka uç geliştirici | 2 | Kural motoru, hesaplama çekirdeği, konnektörler | 14 |
| YZ/NLP mühendisi | 1 | Text-to-rule, doğrulama katmanı, değerlendirme düzeneği | 7 |
| Ön yüz geliştirici | 1 (yarı zamanlı) | Pano ve iş akışı arayüzleri | 3 |
| Test/kalite uzmanı | 1 (kısmi) | Altın setler, hata enjeksiyonu, regresyon | 1 |
| Mevzuat/YMM uzmanı | Hizmet alımı | Kural doğrulama, mutabakat denetimi | — |

## 10. Proje Bütçesi

| Kalem | Tutar (TL) |
|---|---|
| Personel (28 AA × 250.000 ort. tam maliyet) | 7.000.000 |
| Danışmanlık — mevzuat/YMM (hizmet alımı) | 600.000 |
| Bulut altyapısı + LLM API kullanımı | 350.000 |
| Entegrasyon test ortamları ve yazılım lisansları | 300.000 |
| Beklenmedik giderler (~%5) | 400.000 |
| **Toplam** | **8.650.000** |

## 11. Proje Çıktısının Ticarileştirilmesi ve Pazar Analizi

- **Hedef pazar:** 1.363 Ar-Ge Merkezi + 342 Tasarım Merkezi (2025 sonu); teşvikler 31.12.2028'e kadar uzatılmış durumda; gerçekçi hedeflenebilir set orta-büyük ölçekli 400–600 merkez. İkincil pazar: kurumsal teknopark (4691) firmaları.
- **Rakip analizi:** Yerli — ArgeMemory, Ar-GeNet (hesaplama odaklı; YZ doğrulama katmanı yok); bordro yazılımlarının teşvik modülleri; YMM/danışmanlık hizmetleri. Global — Boast.ai, Neo.tax (Türk mevzuatını kapsamaz). Konum: yerli mevzuat hendeği + YZ doğrulama farkı.
- **Gelir modeli:** Personel sayısına kademeli yıllık abonelik + denetim öncesi "hazırlık taraması" paketi; pilotlarda abonelik ile başarı primi modeli A/B test edilecektir.
- **Satış projeksiyonu (muhafazakâr):** Yıl 1 — 2 ücretli pilot + 3–5 abonelik; Yıl 2 — 12–18 müşteri; Yıl 3 — 30–40 müşteri. Kanallar: mevcut İSO 100 müşteri tabanı, YMM/danışmanlık firmalarıyla kanal ortaklığı.
- **Talep kanıtı:** İki sanayi firmasından yazılı ihtiyaç görüşü; niyet mektupları başvuru ekinde sunulacaktır.

## 12. Riskler ve B Planı

| Risk | O/E | Önlem |
|---|---|---|
| Mevzuat değişim hızının kural bakımını aşması | Orta/Yüksek | Bitemporal versiyonlama baştan mimaride; YMM ile aylık gözden geçirme; Resmî Gazete izleme yarı-otomasyonu |
| LLM doğrulamanın hedef doğruluğa ulaşamaması | Orta/Orta | Hibrit mimari: kural tabanlı kontroller tek başına ürünleşebilir; LLM katmanı önce öneri modunda, insan onaylı devreye alınır |
| Bordro/ERP veri erişiminde gecikme | Orta/Orta | Veri erişim protokolleri İP1'de imzalanır; dosya-tabanlı yedek içe aktarım yolu |
| KVKK / veri gizliliği | Düşük/Yüksek | Veri minimizasyonu, maskeleme, şifreleme, müşteri başına izolasyon, on-prem seçenek |
| Pilot takvim kayması | Orta/Düşük | İki bağımsız pilot; 2 ay tampon |
| Hesap hatasının mali sonucu | Düşük/Yüksek | Kuruş mutabakatı kriteri; çift hesap doğrulama dönemi; sözleşmede "karar destek" konumu |

## 13. Fikri Mülkiyet ve Proje Çıktıları

Kaynak kod, veri modelleri ve kural derleme hattı Argelog mülkiyetinde; ARGUS marka başvurusu. AS1/AS2 mimarisi için ay 9'da patentlenebilirlik ön değerlendirmesi; uygun bulunursa TÜRKPATENT başvurusu. Anonimleştirilmiş değerlendirme setleri ve en az 1 akademik bildiri. Ticari çıktı: ARGUS v1.0 (SaaS + on-prem), 2 canlı konnektör, denetim hazırlık panosu.

## 14. Diğer Kamu Destekleri

TÜBİTAK 1501/1507 başvurusu planlanmaktadır; kabul hâlinde 4691 muafiyetleriyle mükerrer destek kurallarına göre kalem ayrıştırması yapılacaktır. (Başvuru anındaki durum bu bölümde beyan edilecektir.)

## 15. Firma Bilgileri

Argelog Ar-Ge Merkezi Yönetim Danışmanlığı ve Yazılım Hizmetleri A.Ş. — 2013, İstanbul (Üsküdar). İnovasyon, teknoloji ve Ar-Ge yönetimi yazılımları; müşteri tabanı İSO 100 sanayi kuruluşları; SAHA İstanbul üyesi. Ürünler: Ar-Ge Yönetimi, Teknoloji Yönetimi, İnovasyon Yönetimi modülleri. (Ticari sicil, vergi ve iletişim bilgileri form aktarımında eklenecektir.)

---

*Kaynak analizler: `arge-proje-fikirleri.md` (#5 RegTech — market-fit, bütçe/zaman) ve `teknopark-proje-basvurusu-regtech.md` (genişletilmiş taslak).*
