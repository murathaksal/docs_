# PROJE BİLGİ FORMU — Denetci

*İstanbul Medeniyet Üniversitesi Teknopark A.Ş. Proje Bilgi Formu (Döküman No: A-R-01224) başlıklarına göre doldurulmuştur; portala aktarım için hazırdır. Hakem heyeti ve teknopark yönetimi diline uygun yazılmış; kısaltmalar ilk kullanımda açılmış, iç çalışma adları ve gayriresmî kaynaklar kullanılmamıştır.*

---

## Kimlik Bilgileri

| Alan | Değer |
|---|---|
| Firma Unvanı | ARGELOG ARGE MERKEZİ YÖNETİM DANIŞMANLIĞI VE YAZILIM HİZMETLERİ A.Ş. |
| Proje Adı | **Denetci** — Kapalı Devre Ortamlar için Çok Mevzuatlı, Denetlenebilir Hesap ve Uyum Yazılımı |
| Proje Kodu | ARGELOG-002 |
| Proje Yöneticisi | Murat Haksal |
| Proje Süresi | 10 Ay |
| Tahmini Proje Bütçesi | 9.000.000,00 ₺ |
| Ar-Ge İş Gücü | 28 Adam/Ay |
| Destek İş Gücü | 2 Adam/Ay |
| Toplam İş Gücü | 30 Adam/Ay |
| Projenin Sektörü | Yazılım / Bilişim Teknolojileri *(portalda "Ambalaj" görünüyor — düzeltilmeli)* |
| İlişkili Sektörler | Seramik, Demir-Çelik, Alüminyum, Metal Eşya (hedef kullanıcı sektörleri); Mali Müşavirlik ve Denetim Hizmetleri |
| NACE Kodu | 62.01 — Bilgisayar Programlama Faaliyetleri |

## Teknolojik Hazırlık Seviyesi

**Mevcut Teknoloji Hazırlık Seviyesi: THS 5** — *Açıklama:* Projenin çekirdeğini oluşturan deterministik teşvik hesaplama motoru firmamız bünyesinde daha önce geliştirilmiş; T.C. Sanayi ve Teknoloji Bakanlığı'nın yayımladığı gerçek dönem verisi üzerinde iç doğrulamadan (96 adet çapa testinin tamamı kuruş farksız) geçirilmiştir. Bileşen düzeyinde ilgili ortam doğrulaması tamamlanmış; ancak çok mevzuatlı kural katmanı, geçmiş beyan mutabakat altsistemi ve yerel yapay zekâ bileşenleri henüz bütünleşik sistem olarak doğrulanmamıştır.

**Hedef Teknoloji Hazırlık Seviyesi: THS 8** — *Açıklama:* Proje sonunda sistem, iki sanayi kuruluşunda ücretli saha pilotlarıyla gerçek üretim/bordro verisi üzerinde doğrulanmış, tamamlanmış ve kalifiye edilmiş ticari sürüm (v1.0) olarak teslim edilecektir.

## Anahtar Kelimeler

Mevzuat uyum yazılımı; deterministik hesaplama motoru; 5746 sayılı Kanun Ar-Ge teşvikleri; Sınırda Karbon Düzenleme Mekanizması (SKDM/CBAM); gömülü emisyon hesabı; kapalı devre yazılım; yerel yapay zekâ; büyük dil modeli damıtma; denetim izi; veri gizliliği (KVKK)

## Proje Özeti

Sanayi kuruluşları, hesaplamaları denetim karşısında savunulması gereken iki ayrı mevzuat yükümlülüğüyle karşı karşıyadır: (1) 5746 sayılı Araştırma, Geliştirme ve Tasarım Faaliyetlerinin Desteklenmesi Hakkında Kanun kapsamındaki aylık teşvik hesaplamaları ve yıllık raporlama; (2) Avrupa Birliği'nin (AB) 2023/956 sayılı Tüzükle kurduğu ve 2026'da mali yükümlülük dönemine giren Sınırda Karbon Düzenleme Mekanizması (SKDM) kapsamında, AB'ye ihraç edilen ürünler için gömülü emisyon beyanı. Her iki alanda da hesaplamalar bugün ağırlıkla elektronik tablolar ve dönemsel danışmanlıkla, hataya açık biçimde yürütülmektedir; hatalı hesap teşvik iadesi, belge iptali veya sınırda ek mali yük riski doğurmaktadır.

Denetci projesi, bu iki mevzuat rejimini tek bir **çok mevzuatlı, deterministik ve denetlenebilir hesap platformunda** birleştiren bir yazılım geliştirmeyi amaçlamaktadır. Platformun çekirdeği; her hesabın mevzuat maddesine izlenebilir bağını koruyan, yürürlük tarihine göre sürümlenen kural setleriyle çalışan deterministik hesap motorudur. Yapay zekâ bileşenleri yalnızca dar ve sınırlı görevlerde (belge alan çıkarımı, mevzuat değişikliği özeti, rapor dili) kullanılır; hesap yapmaz, karar vermez ve tüm önerileri insan onayından geçer. Ürün; internet bağlantısı olmayan (kapalı devre) ortamlardaki sıradan kişisel bilgisayarlarda, grafik işlemci (GPU) gerektirmeden, yalnızca merkezi işlemciyle (CPU) çalışacak biçimde tasarlanmıştır — bu sayede bordro ve üretim verisi kurum dışına hiçbir koşulda çıkmaz ve 6698 sayılı Kişisel Verilerin Korunması Kanunu (KVKK) yükümlülükleri tasarım düzeyinde karşılanır. Mevzuat güncellemeleri, elektronik imzalı çevrimdışı paketlerle dağıtılır.

Proje süresince ilk mevzuat rejimi (5746) için geçmiş beyanların sisteme yüklenip yeniden hesaplanarak mutabakatının kurulduğu ve doğrulanmış sonuçların ileriye dönük hesaplara temel oluşturduğu bir altsistem geliştirilecek; ikinci rejim (SKDM) için seramik sektöründe ürün bazlı gömülü emisyon hesabı, sanayi ortağımızın gerçek üretim ve enerji verisiyle doğrulanacaktır. İki sanayi kuruluşundan projeye ilişkin yazılı ihtiyaç görüşü alınmıştır.

## Projenin Hedefleri

- ☑ Üretim Maliyetlerini ve Giderlerini Düşürme *(teşvik kayıplarının ve sınırda karbon maliyetinin azaltılması; uyum için harcanan nitelikli iş gücünün azaltılması)*
- ☑ Ürün Kalitesi ve Standardını Yükseltme *(beyan ve raporlamada denetlenebilir doğruluk standardı)*
- ☑ Üründe veya Üretim Yöntemlerinde Yenilik Geliştirme *(kapalı devre ortamda CPU ile çalışan yerel yapay zekâ destekli uyum yazılımı kategorisi)*
- ☑ Yeni Ürüne Yönelik Araştırma
- ☐ İthalat İhtiyacını Durdurma *(dolaylı: yabancı bulut tabanlı yazılımlara bağımlılığın önlenmesi)*

## Hedeflenen Kazanım ve Sonuçlar

1. Yürürlük tarihine göre sürümlenen, iki mevzuat rejimini (5746 ve SKDM) aynı çekirdekte çalıştıran hesap motoru; mevcut 96 çapa testinin geriye dönük yıllara genişletilmesi (hedef: 300'ün üzerinde doğrulama çapası, kuruş farksız).
2. Geçmiş beyanların yüklenmesi, yeniden hesaplanması ve beyan edilenle mutabakatının kurulması; farkların kök nedenine göre sınıflandırılması (hedef: farkların en az %85'inin otomatik sınıflandırılması, yanlış neden atama oranının %10'un altında tutulması).
3. Yerel yapay zekâ bileşenlerinin, 16 GB bellekli ve 4 çekirdekli, grafik işlemcisiz referans bilgisayarda belge başına 30 saniyenin altında, referans büyük modelin doğruluğunun en az %95'ine ulaşarak çalışması.
4. Seramik sektöründe ürün bazlı gömülü emisyon hesabının gerçek üretim verisiyle doğrulanması ve SKDM beyan dosyası çıktı formatının üretilmesi.
5. Kurulumdan ilk rapora bir saat içinde ulaşılabilen, bilgi işlem desteği gerektirmeyen kullanım kolaylığı (pilotlarda görev tamamlama oranı en az %80).
6. İki sanayi kuruluşunda ücretli saha pilotu ve en az birinden yenileme/abonelik taahhüdü.

## Hedef Kitle

- ☑ TGB Dışında Bulunan Kurum / Kuruluş *(birincil: 5746 kapsamındaki Ar-Ge ve Tasarım Merkezleri; AB'ye ihracat yapan sanayi kuruluşları)*
- ☑ TGB İçinde Bulunan Kurum / Kuruluş *(4691 kapsamındaki teknoloji geliştirme bölgesi firmaları)*
- ☑ Sipariş Üzerine *(kurum sürümü ve kapalı ağ kurulumları)*
- ☑ Kendi Firmamız *(mevcut müşteri tabanına ek modül)*

## Hedef Lokasyon

- ☑ İl içi — ☑ İl dışı *(Türkiye genelinde Ar-Ge/Tasarım Merkezleri ve ihracatçı sanayi kuruluşları)*
- ☑ Yurt dışı *(orta vadede: SKDM yükümlülüğü taşıyan diğer üçüncü ülke ihracatçıları)*

## Projenin Nitelikleri

- ☑ Yeni Bir Ürün veya Hizmet Üretilmesi
- ☑ Ülke bazında teknolojik olarak yeni ürün üretim süreci *(kapalı devre ortamda yalnızca CPU ile çalışan, çok mevzuatlı yerel yapay zekâ destekli uyum yazılımı kategorisinde yerli ürün tespit edilmemiştir)*
- ☑ İhraç edilebilecek ürün geliştirilmesi
- ☑ Verimliliği Artıran Yeni Ürün / Süreç Geliştirmesi
- ☑ Yeni teknolojinin ülke koşullarına uyarlanması *(büyük dil modeli damıtma ve nicemleme tekniklerinin Türkçe mali-teknik belgelere ve kapalı devre kısıtlarına uyarlanması)*

## Ar-Ge Yönü, Yenilikçi ve Teknolojik Yön

Proje, rutin yazılım geliştirmenin ötesinde beş teknik belirsizlik üzerinde çalışacaktır:

1. **Mevzuat değişikliklerinin katmanlı sürümlenmesi:** Mevzuat değişikliklerinin bir kısmı yalnızca parametre (oran, tutar) değişikliğidir; bir kısmı ise hesaba giren büyüklüklerin tanımını değiştirir (örneğin ücret istisnası rejiminin değişmesi veya bir üst sınırın yıl ortasında yürürlüğe girmesi). Parametre, şema ve bilgi-tarihi eksenlerinin birlikte sürümlenmesi ve geçmiş dönemlerin o dönemde yürürlükte olan kurallarla, bugünkü bilgiyle yeniden üretilebilir biçimde hesaplanması, yayımlanmış hazır çözümü bulunmayan bir tasarım problemidir. Aynı yaklaşım ikinci mevzuat rejiminde (SKDM emisyon faktörleri ve kapsam genişlemeleri) sınanarak genellenebilirliği gösterilecektir.
2. **Beyan-hesap farklarının kök nedenine güvenilir atıf:** Farkı bulmak deterministiktir; belirsizlik, farkın nedenine (yuvarlama, yöntem farkı, veri eksiği, gerçek hata) güvenilir biçimde atanmasındadır. Farklar hesap kalemleri arasında zincirleme yayıldığından ve birden çok neden aynı fark görüntüsünü üretebildiğinden; karşılaştırmalı çift hesap, hipotez taraması ve ayırt edilemeyen durumların dürüstçe "belirsiz" raporlanması üzerine kurulu bir teşhis çerçevesi geliştirilecektir.
3. **Eksik veriyle güven dereceli sonuç üretimi:** Geçmiş dönem belgelerinin bir kısmı temin edilemediğinde, hangi sonucun hangi güven düzeyiyle raporlanabileceğinin biçimsel bir modele bağlanması; güven düzeyinin hesap zinciri boyunca tutarlı yayılımı ve sonradan gelen veriyle sonuçların izlenebilir biçimde güncellenmesi.
4. **Küçük örneklemde sapma tespiti:** Tek bir kuruluşun 12-24 dönemlik verisinde neyin anormal sayılacağının; asgari ücret ve mevzuat değişimi etkileri ayrıştırılarak, yanlış alarm oranı düşük tutularak belirlenmesi.
5. **Büyük dil modellerinin kapalı devre, yalnızca CPU ile çalışan bilgisayarlara taşınması:** Büyük bir öğretmen modelin dar görevlerdeki (Türkçe mali/teknik belge alan çıkarımı) davranışının; bilgi damıtma, 4-bit nicemleme ve dilbilgisi kısıtlı çözümleme teknikleriyle 1-4 milyar parametre sınıfındaki öğrenci modele, doğruluk kaybı sınırlanarak aktarılması ve sıradan kişisel bilgisayarda kabul edilebilir sürede çalıştırılması. Türkçe mali-teknik dar görevler için bu bileşimin doğruluk-hız-bellek sınırlarının ortaya konması özgün mühendislik araştırmasıdır.

Yapay zekânın hesap ve karar süreçlerinden bilinçli olarak dışlanması (yalnızca insan onaylı destek görevleri) hem denetim güvenilirliği hem KVKK uyumu açısından projenin ayırt edici tasarım tercihidir; bu yaklaşım, uluslararası analist kuruluşların 2026 öngörülerinde öne çıkan alan-özgü küçük modeller, veri egemenliği ve kural tabanlı-üretken karma mimariler eğilimleriyle uyumludur.

## Proje Ortaklığı

- ☑ Üniversite işbirliği ile yürütülen proje *(İstanbul Medeniyet Üniversitesi öğretim üyelerinden akademik danışmanlık talep edilecektir — Teknoloji Transfer Ofisi aracılığıyla)*
- ☑ Farklı ildeki firmaların işbirliği ile yürütülen proje *(saha pilotu yürütülecek sanayi kuruluşları)*

## Proje Kapsamında Teknoparktan Talep Edilen Hizmetler

- Danışmanlık: MUAFİYET UYGULAMALARI; AR-GE PROJE TEKLİF DOSYASININ HAZIRLANMASI; PATENT; MARKA TESCİL; FİNANSMAN; İHRACAT *(SKDM tarafında AB pazarına satış için)*
- Teknik Hizmetler: EĞİTİM; İNTERNET SERVİSLERİ; KALİTE GÜVENCE
- TTO: AKADEMİSYEN DANIŞMANLIĞI; PROJE DEĞERLENDİRME

## Finansman Kaynakları

- ☑ Öz Sermaye *(birincil)*
- ☑ Kamu Destekleri *(TÜBİTAK-TEYDEB 1501/1507 başvurusu planlanmaktadır; kabul hâlinde 4691 muafiyetleriyle mükerrer destek kurallarına göre kalem ayrıştırması yapılacaktır)*

## Proje Ar-Ge Aşamaları

- ☑ Kavram Geliştirme
- ☑ Teknolojik/Teknik ve Ekonomik Yapılabilirlik Etüdü
- ☑ Bir Yenilik Unsuru İçeren Yazılım Geliştirme
- ☑ Yeni ya da İyileştirilmiş Ürün ya da Süreçler İçin Prototip Geliştirme
- ☑ Patent ve Lisans Çalışmaları *(proje ortasında patentlenebilirlik ön değerlendirmesi)*

## Bölge Dışı Görevlendirme Süresi ve Gerekçesi

Talep edilen süre: 480 saat. *Gerekçe:* Saha pilotları, kişisel verinin kurum dışına çıkarılamaması nedeniyle müşteri sanayi kuruluşlarının kendi tesislerinde kurulum ve doğrulama gerektirmektedir; ayrıca bordro/kurumsal kaynak planlaması entegrasyon testleri müşteri ortamında yürütülecektir.

## Proje Detayı

**Problem:** 5746 sayılı Kanun kapsamındaki 1.300'ü aşkın Ar-Ge ve Tasarım Merkezi; her ay bordroyla iç içe geçen teşvik hesaplamaları (gelir vergisi stopajı teşviki, sigorta primi işveren desteği, damga vergisi istisnası, kurumlar vergisi indirimi) yapmak, yıllık faaliyet raporu sunmak ve en geç iki yılda bir denetlenmek yükümlülüğündedir. Eş zamanlı olarak, AB'ye ihracat yapan çelik, alüminyum, çimento ve genişleyen kapsamla birlikte çok sayıda sanayi ürünü üreticisi, SKDM kapsamında ürün bazlı gömülü emisyon beyanı vermekle yükümlü hâle gelmiştir. Her iki alanda hesaplar bugün elektronik tablolar ve dönemsel danışmanlıkla yürütülmekte; hata, teşvik iadesi/belge iptali veya sınırda ek maliyet riski doğurmaktadır.

**Çözüm mimarisi:** (1) *Deterministik hesap çekirdeği* — her fonksiyonu mevzuat maddesine atıflı, aynı girdiyle her zaman aynı sonucu üreten, kapanan dönemleri değiştirilemez biçimde mühürleyen hesap motoru (firmamızın önceden geliştirdiği, Bakanlık verisiyle iç doğrulaması tamamlanmış çekirdek üzerine kurulur). (2) *Yürürlük tarihli kural katmanı* — hangi dönemin hangi mevzuat sürümüyle hesaplanacağını yöneten, değişikliklerde etki analizi üreten sürümleme altyapısı; 5746 ve SKDM kural setleri bu katmanın iki uygulamasıdır. (3) *Geçmiş beyan mutabakatı ve temel oluşturma altsistemi* — kuruluşun geçmiş resmî beyanları (Muhtasar ve Prim Hizmet Beyannamesi, Sosyal Güvenlik Kurumu hizmet listeleri, tahakkuk fişleri) ile bordro verisi sisteme alınır; her dönem o dönemin kurallarıyla yeniden hesaplanır, beyan edilenle kademeli mutabakat kurulur, farklar kök nedenine göre sınıflandırılır ve insan onayıyla kapanan dönemler, bütünlük zinciri (özet değeri/hash) korunan değişmez kayıtlara dönüştürülerek ileriye dönük hesapların ve denetim savunmasının temelini oluşturur. (4) *Dar görevli yerel yapay zekâ katmanı* — yalnızca belge alan çıkarımı önerisi, mevzuat değişikliği özeti ve rapor dili görevlerinde; tamamen yerel, yalnızca CPU ile ve insan onaylı çalışır. (5) *Masaüstü ürün ve çevrimdışı güncelleme* — tek paketle kurulan uygulama; mevzuat güncellemeleri elektronik imzalı dosya paketleriyle kapalı devre ortama taşınır.

**İş planı (özet):** İlk iki ayda mevcut çekirdek devralınır ve aylık dönem çözünürlüğüne genişletilir (mevcut doğrulama testleri birebir korunarak); 2-5. aylarda geçmişe dönük mevzuat parametre tablosu resmî kaynak referanslı ve Yeminli Mali Müşavir (YMM) teyitli olarak kurulur; 3-7. aylarda belge içeri alma, bordro entegrasyonları, mutabakat ve sınıflandırma motoru geliştirilir; 5-10. aylarda SKDM kural seti karbon/sürdürülebilirlik uzmanı teyidiyle kurulur ve seramik üretim verisiyle doğrulanır; 6-10. aylarda iki sanayi kuruluşunda ücretli saha pilotları yürütülür ve v1.0 yayımlanır.

## Proje Çıktılarına Yönelik Bilgiler

**Proje Çıktılarında Kullanılacak Sektör:** Birincil kullanıcılar imalat sanayii Ar-Ge/Tasarım Merkezleri (otomotiv, beyaz eşya, seramik, kimya, elektronik dahil) ile AB'ye ihracat yapan çelik/alüminyum/seramik/metal üreticileri; ayrıca mali müşavirlik ve denetim hizmetleri sektörü (çok müşterili sürüm).

**Patent Çıktısı Var Mı:** Var *(hedeflenmektedir)*. Yürürlük tarihli kural sürümleme ve fark kök-neden teşhis yöntemleri için proje ortasında patentlenebilirlik ön değerlendirmesi yapılacak; uygun bulunması hâlinde Türk Patent ve Marka Kurumu'na başvurulacaktır. "Denetci" markası için tescil başvurusu planlanmaktadır.

**Çevreye Etkileri:** Doğrudan olumlu katkı: SKDM modülü, üreticilerin ürün bazlı karbon emisyonlarını doğru ölçüp raporlamasını sağlayarak emisyon azaltım kararlarına güvenilir veri tabanı oluşturur. Ürünün grafik işlemci gerektirmeyen, mevcut kişisel bilgisayarlarda çalışan mimarisi, yapay zekâ kullanımının enerji ayak izini bulut tabanlı alternatiflere kıyasla önemli ölçüde düşürür ve ek donanım yatırımı/elektronik atık oluşturmaz.

**Sürdürülebilirlik:** Ürünün yaşam döngüsü mevzuata bağlıdır ve iki rejim birbirini dengeler: 5746 teşvik sistemi ile SKDM'nin kademeli genişleme takvimi, güncelleme aboneliği üzerinden sürekli gelir ve sürekli geliştirme döngüsü yaratır. Mevzuat güncellemelerinin imzalı paketlerle dağıtımı, ürünün kapalı devre ortamlarda dahi güncel kalmasını sağlar. Platform mimarisi üçüncü ve sonraki mevzuat rejimlerinin (örneğin ulusal emisyon ticaret sistemi) eklenmesine açıktır.

**Ekonomik Değeri:** Orta ölçekli (150 Ar-Ge personelli) bir merkezin yönettiği yıllık teşvik tutarı yüz milyon TL mertebesindedir; düşük oranlı bir hata bile yıllık milyonlarca TL kayıp veya iade riski demektir. SKDM tarafında hatalı emisyon beyanı, sınırda doğrudan ek maliyet oluşturur. Ürün; önlenen kayıp, geri kazanılabilir tutarlar ve denetim riskinin azaltılması üzerinden, yıllık bedelinin birkaç katı ölçülebilir değer üretir. Firma açısından üç gelir kalemi öngörülmektedir: masaüstü lisans ve güncelleme aboneliği, geçmiş dönem mutabakat/denetim hazırlık hizmetleri ve kurum sürümü kurulumları.

**Alınacak Dış Hizmetler:** Yeminli Mali Müşavirlik hizmeti (5746 kural setinin madde madde teyidi ve pilot mutabakat denetimi); karbon/sürdürülebilirlik danışmanlığı (SKDM metodolojisinin teyidi); kısa süreli bulut grafik işlemci kiralama (yalnızca model damıtma eğitimlerinde, sentetik ve anonim veriyle).

**Projenin Müşterisi:** Birincil: 5746 kapsamındaki Ar-Ge ve Tasarım Merkezi yöneten sanayi kuruluşları (Türkiye'de 1.300'ü aşkın merkez) ve AB'ye ihracat yapan üreticiler. İkincil: savunma sanayii tedarik zincirindeki kapalı ağ ortamları; mali müşavirlik/YMM ofisleri (çok müşterili sürüm). İki sanayi kuruluşundan yazılı ihtiyaç görüşü alınmış olup pilot çalışmalar bu kuruluşlarla planlanmaktadır.

**Hedef Pazar, Pazarın Lokal veya Globalliği:** Başlangıçta ulusal (Türkiye'deki Ar-Ge/Tasarım Merkezleri ve ihracatçılar); SKDM modülüyle birlikte bölgesel/küresel genişleme potansiyeli (AB'ye ihracat yapan tüm üçüncü ülke üreticileri aynı yükümlülüğe tabidir — ürün mimarisi çok dilli kullanıma uygundur).

## Rekabet Analizi

Yurt içinde 5746 hesaplama alanında puantaj/bordro odaklı yazılımlar mevcuttur; ancak bunlarda geçmiş beyan mutabakatı, yürürlük tarihli kural sürümleme, denetim savunma dosyası üretimi ve yerel yapay zekâ destekli belge işleme yetenekleri bulunmamaktadır. SKDM tarafında yurt içi arz ağırlıkla danışmanlık raporu biçimindedir; denetlenebilir, deterministik yerli bir hesap yazılımı tespit edilmemiştir. Yurt dışındaki Ar-Ge vergi teşviki otomasyon ürünleri kendi ülke mevzuatlarına özgüdür ve Türk mevzuatını kapsamaz; kurumsal yapay zekâ ürünleri ise ağırlıkla bulut tabanlıdır ve kapalı devre/veri egemenliği gereksinimlerini karşılamaz. Projenin rekabet konumu üç dayanağa oturur: doğrulanmış deterministik hesap çekirdeği, iki mevzuat rejimini tek platformda birleştiren mimari ve verinin kurum dışına çıkmadığı kapalı devre çalışma modeli.

## Fikri Sınai ve Mülkiyet Hakları

| Başvuru/Yayın Numarası | Belge Adı | Koruma Tipi |
|---|---|---|
| *(planlanan)* | "Denetci" marka tescil başvurusu | Marka |
| *(değerlendirilecek)* | Yürürlük tarihli kural sürümleme ve fark kök-neden teşhis yöntemi | Patent (ön değerlendirme proje ay 8'de) |

Projede geliştirilen tüm yazılım, veri modelleri ve yöntemlerin fikri hakları firmamıza aittir; proje öncesinde firma bünyesinde geliştirilen hesap çekirdeği başlangıç varlığı olarak beyan edilir.

## Alınan Ar-Ge Destekleri

| Kurum Adı | Destek Tipi | Destek Dönemi |
|---|---|---|
| *(beyan edilecek)* | — | — |

*Not: TÜBİTAK-TEYDEB 1501/1507 başvurusu planlanmaktadır; başvuru anındaki durum bu tabloda beyan edilecektir.*

## Projeye Ait Ürünler

| Ürün Adı | Ürün Tipi |
|---|---|
| Denetci Masaüstü (5746 uyum ve hesap) | Yazılım — masaüstü uygulama |
| Denetci Pro (geçmiş dönem mutabakatı ve denetim savunma dosyası) | Yazılım — modül |
| Denetci SKDM (gömülü emisyon hesabı ve beyan dosyası) | Yazılım — modül |
| Denetci Kurum (çok kullanıcılı/çok firmalı sürüm, kapalı ağ dağıtımı) | Yazılım — sunucu sürümü |
| Mevzuat güncelleme aboneliği (imzalı çevrimdışı paket) | Hizmet — abonelik |

## Proje Ekipman Listesi

| Ekipman | Adet | Amaç |
|---|---|---|
| Geliştirici iş istasyonu | 3 | Yazılım geliştirme |
| CPU test bilgisayarları (farklı donanım sınıflarında) | 4 | Yerel yapay zekâ bileşenlerinin hedef donanım matrisinde doğrulanması (asgari sistem: 4 çekirdek, 16 GB bellek, grafik işlemcisiz) |
| Test sunucusu (kurum sürümü doğrulaması) | 1 | Çok kullanıcılı sürüm testleri |
| Ağdan yalıtılmış test ortamı donanımı | 1 takım | Kapalı devre kurulum ve imzalı güncelleme senaryolarının doğrulanması |

---

*Not — portalda düzeltilmesi gerekenler: (1) "Projenin Sektörü" alanı "Ambalaj" görünmektedir; "Yazılım" olarak düzeltilmelidir. (2) Kimlik alanlarındaki süre/bütçe/iş gücü değerleri bu dokümandaki değerlerle güncellenmelidir. Kaynak analizler: `argus-teknopark-basvuru-formu.md` (teknik omurga), `argus-baz-hatti-tasarimi.md`, `argus-gelir-plani.md`.*
