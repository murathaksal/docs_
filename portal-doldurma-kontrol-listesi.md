# Portal Doldurma Kontrol Listesi

*Teknopark portalındaki Proje Bilgi Formu çıktısı (Döküman No A-R-01224, 07.09.2026 16:32, 12 sayfa) ile `denetci-proje-bilgi-formu.md` karşılaştırılmıştır. Bu belge üç bölümden oluşur: (A) boş kalan alanlar ve girilecek değerler, (B) portal ile form metni arasındaki farklar ve alınan kararlar, (C) hakem heyetinin ilk bakacağı tutarlılık noktaları. Uzun metinler için ilgili başlık gösterilmiştir; o başlığın altındaki metin portala aynen yapıştırılır (biçimlendirme düşer, sorun değildir).*

---

## A. Boş alanlar ve girilecek değerler

### A1. Kimlik alanları (sayfa 2)

| Portal alanı | Mevcut | Girilecek değer |
|---|---|---|
| Proje Yöneticisi | boş | Murat Haksal |
| Tahmini Proje Bütçesi | 0,00 ₺ | 7.000.000,00 ₺ |
| Ar-Ge İş Gücü | 0 | 31 Adam/Ay |
| Destek İş Gücü | 0 | 8 Adam/Ay |
| Toplam İş Gücü | 0 | 39 Adam/Ay |
| Toplam Proje İş Gücü | 0 | 39 Adam/Ay |
| Proje Tahmini Bitiş Tarihi | boş | 25.10.2027 (başlangıç 26.10.2026 + 12 ay) |
| Proje TGB Başlangıç Tarihi | boş | Bölge yönetiminin onay tarihine göre; 26.10.2026 önerilir |
| Toplam Personel | 2 | 4 |
| Kiralanan Alan | 10,00 m² | Gözden geçirilecek; 4 kişiyle kişi başına 2,5 m² düşer (bkz. C2) |
| İlişkili Sektörler | boş | İmalat sanayii Ar-Ge/Tasarım Merkezleri; teknoloji geliştirme bölgesi firmaları; mali müşavirlik ve denetim hizmetleri |
| Mevcut THS Açıklama | boş | Formdaki **"Teknolojik Hazırlık Seviyesi"** başlığı, "Mevcut" paragrafı |
| Hedef THS Açıklama | boş | Aynı başlık, "Hedef" paragrafı |
| Anahtar Kelimeler | boş | Formdaki **"Anahtar Kelimeler"** başlığındaki liste |

Teknoloji alanları portalda seçili: 1.2.15, 1.2.2, 1.2.3 Yapay Zeka, 1.2.6, 1.2.8; diğer 1.3.14. Bu seçim yeni yapay zekâ çerçevesiyle uyumludur; listede "makine öğrenmesi" veya "doğal dil işleme" gibi ayrı bir kod varsa eklenmesi önerilir.

### A2. Teknoparkta Etkileşimde Bulunulan/Bulunulabilecek Firmalar (sayfa 8, boş)

Formdaki **"Teknoparkta Etkileşimde Bulunulan/Bulunulabilecek Firmalar"** başlığının altındaki üç madde ve kapanış notu aynen girilir.

### A3. Bölge Dışı Görevlendirme (sayfa 8, "0 saat")

| Alan | Girilecek değer |
|---|---|
| Talep edilen süre | 240 saat |
| Gerekçe | Kişisel veri kurum dışına çıkarılamadığı için saha pilotları, müşteri sanayi kuruluşlarının kendi tesislerinde kurulum ve doğrulama gerektirmektedir; bordro sistemi veri aktarım testleri de müşteri ortamında yürütülecektir. |

### A4. Proje Çıktılarına Yönelik Bilgiler (sayfa 10-11, tamamı boş)

*Ekonomik Değeri, Alınacak Dış Hizmetler, Projenin Müşterisi, Hedef Pazar ve Rekabet Analizi alanları için, portalın yönlendirme metinlerine göre genişletilmiş ve karakter sınırı denetlenmiş metinler `portal-ekonomik-deger-metinleri.md` dosyasındadır; oradan yapıştırılır.*

| Portal alanı | Girilecek değer |
|---|---|
| Proje Çıktılarında Kullanılacak Sektör | İmalat sanayii Ar-Ge/Tasarım Merkezleri (otomotiv, beyaz eşya, seramik, kimya, enerji, elektronik dâhil); teknoloji geliştirme bölgesi firmaları; mali müşavirlik ve denetim hizmetleri |
| Patent Çıktısı Var Mı | Portalda **"Yok"** görünüyor → **"Var"** seçilecek; açıklama formdaki "Patent Çıktısı Var Mı" paragrafı |
| Çevreye Etkileri | Formdaki aynı adlı paragraf |
| Sürdürülebilirlik | Formdaki aynı adlı paragraf |
| Ekonomik Değeri | Formdaki aynı adlı paragraf |
| Alınacak Dış Hizmetler | Formdaki aynı adlı paragraf |
| Projenin Müşterisi | Formdaki aynı adlı paragraf |
| Hedef Pazar, Lokal/Global | Formdaki aynı adlı paragraf |
| Rekabet Analizi | Formdaki **"Rekabet Analizi"** başlığındaki paragraf |

### A4b. Proje Bütçesi ekranı (Proje Bütçe Kalemi penceresi)

**Önce:** Ekranda duran iki deneme satırı (`test` / Personel Giderleri / 100,00 ve `test` / Hizmet Alımları / 1,00) **silinmelidir**; "Planlanan Tahmini Bütçe" alanı şu an 101,00 ₺ görünmektedir ve doğru toplam girildiğinde 7.000.000,00 ₺ olacaktır.

**Sonra:** "Ekle" ile aşağıdaki dokuz satır girilir. Her satırda önce Harcama Kategorisi seçilir, sonra Harcama açıklaması ve Tutar yazılır. Açıklamalar kısa tutulmuştur; alan uzun metni kabul etmezse parantez içleri çıkarılabilir.

| # | Harcama Kategorisi | Harcama (açıklama) | Tutarı (TL) |
|---|---|---|---|
| 1 | Personel Giderleri | Proje personeli: 39 adam/ay x 130.000 TL (brüt ücret, işveren maliyeti ve genel gider payı dâhil; dayanak EK-3) | 5.070.000,00 |
| 2 | Hizmet Alımları | Yeminli Mali Müşavirlik hizmeti ve yazılı hukuk görüşü: kural setlerinin madde madde teyidi, geçmiş parametre tablosunun doğrulanması, pilot mutabakat denetimi, uzman etiketleme | 550.000,00 |
| 3 | Hizmet Alımları | Denetimli ince ayar eğitimleri için kısa süreli bulut grafik işlemci kiralama (yalnızca sentetik ve anonimleştirilmiş veriyle) | 200.000,00 |
| 4 | Hizmet Alımları | Patent ön değerlendirmesi ve başvurusu, marka tescili, yapay zekâ alanında akademik danışmanlık | 250.000,00 |
| 5 | Hizmet Alımları | Yazılım lisansları, kod imzalama sertifikası, çevrimdışı güncelleme imza altyapısı, test ve model değerlendirme araçları | 200.000,00 |
| 6 | Makina ve Teçhizat Giderleri | 3 geliştirici iş istasyonu ve 2 referans test bilgisayarı (4 çekirdek, 16 GB bellek, grafik işlemcisiz) | 300.000,00 |
| 7 | Seyahat Giderleri | Pilot saha ziyaretleri (iki sanayi kuruluşunun tesisleri) ve yapay zekâ alanında dış eğitim/konferans seyahatleri | 230.000,00 |
| 8 | Sarf Giderleri | Test ve veri ortamı sarf malzemeleri, harici depolama ortamı, çevrimdışı güncelleme paketi taşıyıcı ortamları, ofis sarf giderleri | 50.000,00 |
| 9 | Genel Giderler | Öngörülemeyen giderler payı (firma genel gideri personel birim maliyetine dâhil olduğundan bu kalemde tekrarlanmaz) | 150.000,00 |
| | | **Toplam** | **7.000.000,00** |

Notlar:

- **Bursiyer Giderleri** ve **Temsil ve Tanıtma Giderleri** kategorilerinde harcama öngörülmemiştir. Bursiyer kalemi, Teknoloji Transfer Ofisi aracılığıyla bir lisansüstü öğrenci projeye dâhil edilirse üniversite iş birliği beyanını güçlendirir; bu tercih edilirse personel kaleminden aktarım yapılarak bütçe toplamı korunur.
- Yazılım lisansları portalda **Hizmet Alımları** altına yazılmıştır; bölge yönetimi süreli lisansları Sarf Giderleri altında istiyorsa 5. satır o kategoriye alınabilir, toplam değişmez.
- Bu dokuz satır, `denetci-proje-bilgi-formu.md` içindeki bütçe kırılımı tablosuyla birebir aynıdır; kimlik alanındaki "Tahmini Proje Bütçesi" değeri de 7.000.000,00 ₺ olmalıdır.

### A5. Fikri Sınai ve Mülkiyet Hakları tablosu (sayfa 11, boş)

| Başvuru/Yayın Numarası | Belge Adı | Koruma Tipi |
|---|---|---|
| (planlanan) | "Denetci" marka tescil başvurusu | Marka |
| (değerlendirilecek) | Deterministik motor çıktısından denetim verisi üretimi ve sembolik doğrulama kapısıyla kapatılan denetçi model döngüsü yöntemi | Patent (ön değerlendirme ay 9) |
| (değerlendirilecek) | Üç eksenli yürürlük tarihli kural sürümleme yöntemi | Patent (ön değerlendirme ay 9) |

### A6. Alınan Ar-Ge Destekleri tablosu (sayfa 11, boş)

Daha önce alınmış destek varsa (TÜBİTAK, KOSGEB vb.) kurum adı, destek tipi ve dönemiyle girilir; yoksa boş bırakılır. Boş bırakılıyorsa formdaki "(beyan edilecek)" satırı da kaldırılmalıdır.

### A7. Projeye Ait Ürünler tablosu (sayfa 11, boş)

| Ürün Adı | Ürün Tipi |
|---|---|
| Denetci Masaüstü: 5746 ve 4691 kural setleriyle cari dönem bağımsız kontrol hesabı, mevzuat maddesi atıflı raporlama, 12 aylık teşvik projeksiyonu; geçmiş beyan mutabakatı, kök-neden teşhisi, denetçi rolündeki yerel yapay zekâ bileşeni, mühürlü baz ve denetim savunma dosyası | Yazılım (masaüstü uygulama, yerel yapay zekâ bileşenli) |
| Mevzuat güncelleme aboneliği: elektronik imzalı çevrimdışı kural ve model paketleriyle dağıtım | Hizmet (abonelik) |
| Geçmiş dönem mutabakat hizmeti: 12-24 dönemlik retroaktif yeniden hesap ve YMM eşliğinde kapanış raporu | Hizmet (proje bazlı) |

### A8. Proje Ekipman Listesi (sayfa 12, boş)

| Ekipman | Adet | Amaç |
|---|---|---|
| Geliştirici iş istasyonu | 3 | Yazılım geliştirme ve model ince ayar deneylerinin hazırlanması |
| Referans test bilgisayarı (4 çekirdek, 16 GB bellek, grafik işlemcisiz) | 2 | Ürünün ve denetçi modelin hedef donanımda doğrulanması; kapalı devre kurulum senaryolarının sınanması |

---

## B. Portal ile form metni arasındaki farklar ve kararlar

| Alan | Portalda | Form metninde (eski) | Karar |
|---|---|---|---|
| Hedef Kitle: Kendi Firmamız | işaretsiz | işaretli | Portalda **işaretlenmeli**; firma kendi danışmanlık kolunda ürünü kullanacaktır. |
| Projenin Nitelikleri: Yeni teknoloji geliştirme | işaretsiz | yoktu | Portalda **işaretlenmeli**; Ar-Ge yönü artık yapay zekâ ağırlıklıdır. Form metnine eklendi. |
| Proje Ortaklığı | Aynı il: Tüpraş; Farklı il: Kale Seramik; TTO; Üniversite | yalnız Üniversite ve Farklı il | Form metni portala göre güncellendi. **Dikkat:** Tüpraş'ın pilot sahası Kocaeli'deki tesis/Ar-Ge Merkezi ise "aynı il" değil "farklı il" olmalıdır; pilotun İstanbul ofisinde yürütülmesi planlanmıyorsa düzeltilmelidir. |
| Teknoparktan talep edilen danışmanlık hizmetleri | Teknoloji Transferi, Pazarlama | Muafiyet, Proje dosyası, Patent, Marka | Birleştirildi: portalda **Patent, Marka Tescil ve Muafiyet Uygulamaları** da işaretlenmeli (patent hedefi ve KDV istisnası talebi var). Form metni güncellendi. |
| Finansman: Kamu Destekleri | işaretsiz | işaretli | Portal esas alındı; form metninde işaret kaldırıldı, TÜBİTAK olasılığı not olarak bırakıldı. |
| Ar-Ge Aşamaları: Prototip Geliştirme | işaretsiz | işaretli | Portalda **işaretlenmeli**; hedef THS 7 prototipin gerçek ortamda denenmesidir. |
| Ar-Ge Aşamaları: Prototip ile ilişkili Sınai Mühendislik | işaretli | yoktu | Yazılım projesinde sınai mühendislik kalemi hakem için açıklama gerektirir; **işaretin kaldırılması** önerilir. |
| Patent Çıktısı | Yok | Var | Portalda **Var** seçilmeli (bkz. A4). |
| Proje adı | "Denetci" | "Denetci: … Yerel Yapay Zekâ Sistemi" | Portalda kısa ad yeterlidir; uzun ad Proje Özeti'nin ilk cümlesinde zaten geçmektedir. Değişiklik gerekmez. |

---

## C. Hakem heyetinin ilk bakacağı tutarlılık noktaları

1. **Proje adı:** Portalın bütçe ekranında proje adı **"Denetci.AI"** görünmektedir; Proje Bilgi Formu çıktısında ve hazırladığımız belgelerde ad **"Denetci"**dir. İki kayıt aynı olmalıdır. "Denetci.AI" tercih edilirse marka tescil başvurusu da bu adla yapılmalı ve belgelerdeki ad güncellenmelidir.
2. **Bütçe deneme satırları:** Bütçe ekranındaki iki `test` satırı silinmeden başvuru gönderilmemelidir.
3. **Personel ve iş gücü:** Toplam Personel 4, iş gücü 39 adam/ay (ortalama 3,25 TZE). Portaldaki "2 personel" kaydı bu beyanla çelişir; mutlaka güncellenmelidir.
4. **Kiralanan alan:** 10 m² ile 4 kişi, kişi başına 2,5 m² demektir. Ekip aynı anda bölgede bulunmayacaksa (proje yöneticisi yarı zamanlı, saha pilotları bölge dışında) bu durum "Bölge Dışı Görevlendirme" gerekçesinde ve gerekirse bölge yönetimine yazılı olarak açıklanmalı; aksi hâlde alan büyütülmelidir.
5. **Takvim:** Başlangıç 26.10.2026 ise ay 7 Nisan 2027, ay 10 Temmuz 2027, ay 12 Ekim 2027'dir. Kazanımlardaki "2019-2026 arası her ay" ifadesi başlangıç tarihiyle uyumludur.
6. **Bütçe:** Üç yerde aynı olmalıdır: kimlik alanındaki "Tahmini Proje Bütçesi", Proje Bütçesi ekranındaki dokuz satırın toplamı ("Planlanan Tahmini Bütçe") ve Proje Detayı metnindeki bütçe kırılımı tablosu. Üçü de 7.000.000,00 ₺'dir.
7. **KDV istisnası talebi (3065 sayılı Kanun geçici 20. madde):** İşaretlidir. Ürün "yazılım" teslimi olduğundan uygundur; ancak "geçmiş dönem mutabakat hizmeti" bir hizmet teslimidir ve istisna kapsamı yönünden mali müşavirle ayrıca teyit edilmelidir.
8. **Ekler:** Portalda ek yükleme alanı varsa EK-1'den EK-6'ya kadar tüm ekler PDF olarak yüklenmeli; yoksa başvuru dosyasına basılı eklenmelidir. EK-2 niyet mektupları Tüpraş ve Kale Seramik'ten imzalı alınmış olmalıdır.
