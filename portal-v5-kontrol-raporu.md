# Portal Form v5 Kontrol Raporu

*11.09.2026 11:33 tarihli portal çıktısı (14 sayfa), `denetci-proje-bilgi-formu.md` ve eklerle karşılaştırılmıştır. Bulgular üç grupta verilmiştir: (A) hatalı girilmiş alanlar, (B) hâlâ boş alanlar, (C) belge içi çelişkiler. Her madde başlık ve içerik olarak yazılmıştır.*

---

## A. Hatalı girilmiş alanlar

### A1. Proje Bütçesi: üç satır eksik, üç tutar yanlış

Girilen toplam **6.220.000,00 ₺**, olması gereken **7.000.000,00 ₺**. Fark 780.000 ₺.

**Eksik üç satır eklenmelidir:**

| Harcama Kategorisi | Harcama Adı | Tutar |
|---|---|---|
| Hizmet Alımları | Patent, marka tescili ve akademik danışmanlık | 250.000,00 |
| Hizmet Alımları | Yazılım lisansları, kod imzalama sertifikası ve imza altyapısı | 200.000,00 |
| Makina ve Teçhizat Giderleri | 3 geliştirici iş istasyonu ve 2 referans test bilgisayarı | 300.000,00 |

**Üç satırın tutarı düzeltilmelidir:**

| Harcama Adı | Girilen | Olması gereken |
|---|---|---|
| Bulut GPU-grafik işlemci kiralama | 250.000,00 | **200.000,00** |
| Öngörülemeyen pay | 100.000,00 | **150.000,00** |
| Pilot saha ziyaretleri, konferans | 200.000,00 | **230.000,00** |

*Not: Bulut grafik işlemci satırındaki 250.000 ₺, önceki mesajımızdaki bir yazım hatasından kaynaklanmıştır; doğru tutar 200.000 ₺'dir.*

### A2. Kimlik alanları: iş gücü değerleri yanlış

| Alan | Girilen | Olması gereken |
|---|---|---|
| Ar-Ge İş Gücü | 4 Adam/Ay | **31 Adam/Ay** |
| Destek İş Gücü | 0 Adam/Ay | **8 Adam/Ay** |
| Toplam İş Gücü | 4 Adam/Ay | **39 Adam/Ay** |
| Tahmini Proje Bütçesi | 6.220.000,00 ₺ | **7.000.000,00 ₺** (A1 düzeltilince) |
| Toplam Personel | 2 | **4** (Proje Ekibi ekranında 4 kişi kayıtlı) |

"Toplam Proje İş Gücü: 48 Adam/Ay" alanı sistem tarafından 4 kişi × 12 ay olarak hesaplanmış görünmektedir. Beyan ettiğimiz efor 39 adam/aydır, çünkü ekip üyelerinin bir kısmı kısmi zamanlıdır. Proje Ekibi ekranında kişi bazında çalışma oranı girilebiliyorsa oranlar (1,0 / 1,0 / 0,75 / 0,5) girilmeli; girilemiyorsa 48 ile 39 arasındaki farkın gerekçesi Proje Detayı metnindeki ekip paragrafında zaten açıklanmıştır ve bölge yönetimine sözlü olarak da belirtilmelidir.

### A3. Proje Detayı: eski sürüm yapıştırılmış

Portaldaki İş Paketleri tablosu, ekip paragrafı ve bütçe kırılımı **bir önceki sürümdendir**. Belirtiler: İP tablosu toplamı "36 (28 Ar-Ge + 8)", İP4 8 adam/ay, İP5 8 adam/ay; ekip paragrafı "ortalama 3 tam zaman eşdeğeri"; bütçe kırılımı "6.600.000 ₺" ve yedi satır.

Güncel metin `denetci-proje-bilgi-formu.md` dosyasının **"Proje Detayı"** başlığı altındadır ve şunları içerir: İP toplamı 39 (31 Ar-Ge + 8), İP4 9, İP5 10 adam/ay; ekip paragrafında "tam zamanlı yapay zekâ/doğal dil işleme mühendisi" ve "ortalama 3,25 tam zaman eşdeğeri"; bütçe kırılımı 7.000.000 ₺ ve portal kategorileriyle eşleşen dokuz satır. **Bu bölümün tamamı silinip güncel metin yeniden yapıştırılmalıdır.**

### A4. Anahtar Kelimeler: fazla kısa

Girilen: "5746, 4691, Mevzuata Uyum, Yapay Zeka Denetim". Bu dört kelime projenin yapay zekâ yönünü hakeme göstermez. Önerilen tam liste (formdaki "Anahtar Kelimeler" başlığı):

> Nöro-sembolik yapay zekâ; denetçi rolünde dar kapsamlı dil modeli; deterministik referansla (oracle) üretilen eğitim verisi; denetimli ince ayar (SFT); abdüktif kök-neden teşhisi; kanıta bağlı gerekçelendirme; sembolik doğrulama kapısı; zaman-farkındalıklı kural tabanı; 5746 sayılı Kanun Ar-Ge teşvikleri; 4691 sayılı Kanun istisnaları; geçmiş beyan mutabakatı; denetim savunma dosyası; grafik işlemcisiz yerel çıkarım; kapalı devre çalışma; veri gizliliği (KVKK)

Alan karakter sınırlıysa ilk sekiz kavram önceliklidir.

### A5. İşaretlenmemiş veya yanlış işaretlenmiş kutular

| Başlık | Durum | Yapılacak |
|---|---|---|
| Hedef Kitle: Kendi Firmamız | işaretsiz | **İşaretlenmeli** (firmanın danışmanlık kolu ürünü kullanacak; "Projenin Müşterisi" metninde de yazılı) |
| Projenin Nitelikleri: Yeni teknoloji geliştirme | işaretsiz | **İşaretlenmeli** (projenin Ar-Ge yönü yapay zekâ ağırlıklıdır) |
| Ar-Ge Aşamaları: Prototip Geliştirme | işaretsiz | **İşaretlenmeli** (hedef THS 7 prototipin gerçek ortamda denenmesidir) |
| Ar-Ge Aşamaları: Prototip ile İlişkili Sınai Mühendislik | işaretli | **Kaldırılmalı** (yazılım projesinde sınai mühendislik kalemi hakemden açıklama sorusu getirir) |
| Teknoparktan Talep: PATENT | işaretsiz | **İşaretlenmeli** (patent ön değerlendirmesi bütçede ve FSMH tablosunda var) |
| Teknoparktan Talep: MARKA TESCİL | işaretsiz | **İşaretlenmeli** ("Denetci.AI" marka başvurusu planlanıyor) |
| Teknoparktan Talep: MUAFİYET UYGULAMALARI | işaretsiz | **İşaretlenmeli** (KDV istisnası değerlendirme talebi işaretli) |
| Patent Çıktısı Var Mı | "Yok" | **"Var"** seçilmeli; açıklama metni formdaki "Patent Çıktısı Var Mı" paragrafıdır |

---

## B. Hâlâ boş olan alanlar

| # | Başlık | Girilecek içerik |
|---|---|---|
| B1 | İlişkili Sektörler (kimlik) | İmalat sanayii Ar-Ge/Tasarım Merkezleri; teknoloji geliştirme bölgesi firmaları; mali müşavirlik ve denetim hizmetleri |
| B2 | Proje Tahmini Bitiş Tarihi | 25.10.2027 (başlangıç 26.10.2026 + 12 ay) |
| B3 | Proje TGB Başlangıç Tarihi | Bölge yönetiminin onay tarihi; 26.10.2026 önerilir |
| B4 | Proje Çıktılarında Kullanılacak Sektör | İmalat sanayii Ar-Ge/Tasarım Merkezleri (otomotiv, beyaz eşya, seramik, kimya, enerji, elektronik dâhil); teknoloji geliştirme bölgesi firmaları; mali müşavirlik ve denetim hizmetleri |
| B5 | Çevreye Etkileri | Formdaki "Çevreye Etkileri" paragrafı |
| B6 | Sürdürülebilirlik | Formdaki "Sürdürülebilirlik" paragrafı |
| B7 | Fikri Sınai ve Mülkiyet Hakları tablosu | Üç satır: "Denetci.AI" marka başvurusu (Marka); denetim verisi üretimi ve doğrulama kapısı yöntemi (Patent, ön değerlendirme ay 9); üç eksenli kural sürümleme yöntemi (Patent, ön değerlendirme ay 9) |
| B8 | Projeye Ait Ürünler tablosu | Üç satır: Denetci.AI Masaüstü (Yazılım); mevzuat ve model güncelleme aboneliği (Hizmet); geçmiş dönem mutabakat hizmeti (Hizmet). Tam metinler `portal-doldurma-kontrol-listesi.md` A7'de |
| B9 | Proje Ekipman Listesi (sayfa 14) | İki satır: 3 adet geliştirici iş istasyonu; 2 adet referans test bilgisayarı (4 çekirdek, 16 GB bellek, grafik işlemcisiz). Bütçedeki Makina ve Teçhizat satırıyla tutarlı olmalıdır |

---

## C. Belge içi çelişkiler

### C1. Model boyutu üç yerde farklı (hakemin ilk yakalayacağı çelişki)

| Yer | Yazan |
|---|---|
| Proje Özeti | **4-16 milyar** parametre |
| Hedeflenen Kazanım 1 | **1-4 milyar** parametre |
| Ar-Ge Yönü AS-1 | **1-4 milyar** parametre |

Üçü aynı olmalıdır. Teknik olarak 1-4 milyar sınıfı, 16 GB bellekli ve grafik işlemcisiz bir bilgisayarda bulgu başına 30 saniye hedefiyle tutarlıdır. 16 milyar parametreli bir model nicemlenmiş hâlde yaklaşık 9-10 GB bellek kaplar ve aynı donanımda bulgu başına birkaç dakikaya çıkar; bu durumda hem 16 GB bellek hem 30 saniye hedefi savunulamaz hâle gelir. **Öneri: her üç yerde 1-4 milyar kalsın.** Daha büyük model ısrar ediliyorsa üç metin, bellek hedefi (32 GB) ve süre hedefi (bulgu başına 2-3 dakika) birlikte değiştirilmelidir; bu, "sıradan bilgisayarda çalışır" iddiasını zayıflatır.

### C2. Proje adı Özet metniyle uyumsuz

Kimlik alanında ad **"Denetci.AI"**, Proje Özeti metni ise "**Denetci**, bir Ar-Ge/Tasarım Merkezinin..." diye başlıyor. Özet metnindeki ad "Denetci.AI" olarak düzeltilmeli; marka tescil satırı ve ürün adı da aynı yazımı kullanmalıdır. *(Bizim belgelerimizde de aynı güncellemeyi yapabiliriz; onay verirseniz tüm dosyalarda "Denetci.AI" yaparım.)*

### C3. Proje Ekibi ile EK-3/EK-4 uyuşmuyor

Portaldaki ekip: Murat Haksal (Proje Yöneticisi & Yapay Zeka), Mesut Çakır (Backend Yazılımcı), Hatice Betül Haksal (Analist), Bengü Bayyurt Çetin (Analist, sözleşmeli).

Eklerdeki ekip: proje yöneticisi (6 adam/ay), kıdemli yazılım geliştirici (12), **tam zamanlı yapay zekâ/doğal dil işleme mühendisi** (12), analiz ve test-altyapı uzmanı (9).

İki fark önemlidir. Birincisi, portalda ayrı bir yapay zekâ mühendisi yoktur; proje yöneticisi bu rolü de üstlenmiştir. Yapay zekâ ağırlıklı bir projede tek kişinin hem yönetim hem model geliştirme yapması, hakemin soracağı ilk sorudur. İkincisi, portalda iki analist vardır, eklerde bir analiz/test uzmanı. **Karar gerekiyor:** ya ekler gerçek ekibe göre yeniden yazılır (Murat Haksal yönetim + yapay zekâ, iki analist arasında efor bölüştürülür), ya da portaldaki ekip kaydına yapay zekâ tarafını taşıyacak dördüncü bir rol eklenir. Söyleyin, hangisini istiyorsanız EK-3 ve EK-4'ü ona göre düzenleyeyim.

### C4. Ar-Ge Merkezi sayısı iki yerde farklı

Proje Özeti "1.300'ü aşkın Ar-Ge ve Tasarım Merkezi" diyor; Hedef Pazar metni Bakanlık istatistiğine dayanarak "1.373 Ar-Ge Merkezi ve 347 Tasarım Merkezi (toplam 1.720)" diyor. Özet metnindeki ifade **"1.700'ü aşkın Ar-Ge ve Tasarım Merkezi"** olarak düzeltilmelidir.

### C5. Niyet mektupları henüz ekli değil

"Projenin Müşterisi" metni "niyet mektupları başvuru ekinde sunulmaktadır" diyor ve Tüpraş ile Kale Seramik adları üç ayrı alanda geçiyor. Mektuplar imzalı olarak eklenmeden bu cümle taahhüt niteliği taşır. Mektuplar başvuruya yetişmeyecekse cümle "yazılı ihtiyaç görüşü alınmıştır; imzalı niyet mektupları değerlendirme sürecinde sunulacaktır" biçiminde yumuşatılmalıdır.
