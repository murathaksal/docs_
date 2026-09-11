# PROJE BİLGİ FORMU: Denetci

*İstanbul Medeniyet Üniversitesi Teknopark A.Ş. Proje Bilgi Formu (Döküman No: A-R-01224) başlıklarına göre doldurulmuştur. Hakem heyeti ve teknopark yönetimi diline uygun yazılmış; kısaltmalar ilk kullanımda açılmış, mutlak nitelikli rekabet iddialarından kaçınılmış, her sayısal hedef metrik tanımı, test seti ve ölçüm ayı üçlüsüne bağlanmıştır.*

---

## Kimlik Bilgileri

| Alan | Değer |
|---|---|
| Firma Unvanı | ARGELOG ARGE MERKEZİ YÖNETİM DANIŞMANLIĞI VE YAZILIM HİZMETLERİ A.Ş. |
| Proje Adı | **Denetci**: Ar-Ge Teşvik Beyanlarının Bağımsız Denetimi İçin Denetçi Rolünde Yerel Yapay Zekâ Sistemi |
| Proje Kodu | ARGELOG-002 |
| Proje Yöneticisi | Murat Haksal |
| Proje Süresi | 12 Ay |
| Proje Başlangıç / Tahmini Bitiş Tarihi | 26.10.2026 / 25.10.2027 *(portal kaydına göre; ay numaraları bu başlangıca göredir: ay 7 = Nisan 2027, ay 10 = Temmuz 2027, ay 12 = Ekim 2027)* |
| Tahmini Proje Bütçesi | 7.000.000,00 ₺ |
| Ar-Ge İş Gücü | 31 Adam/Ay |
| Destek/Geliştirme İş Gücü | 8 Adam/Ay |
| Toplam İş Gücü | 39 Adam/Ay |
| Toplam Personel | 4 kişi (ortalama 3,25 tam zaman eşdeğeri; 39 ÷ 12 = 3,25) |
| Projenin Sektörü | Yazılım / Bilişim Teknolojileri (yapay zekâ uygulamaları) |
| İlişkili Sektörler | İmalat sanayii Ar-Ge/Tasarım Merkezleri; teknoloji geliştirme bölgesi firmaları; mali müşavirlik ve denetim hizmetleri |
| NACE Kodu | 62.01, Bilgisayar Programlama Faaliyetleri |

## Teknolojik Hazırlık Seviyesi

**Mevcut Teknoloji Hazırlık Seviyesi: THS 5.** *Açıklama:* Sistemin sembolik bileşeni olan deterministik teşvik hesaplama motoru firmamız bünyesinde daha önce geliştirilmiş ve T.C. Sanayi ve Teknoloji Bakanlığı'nın yayımladığı gerçek dönem verisi üzerinde iç doğrulamadan (96 adet çapa testinin tamamı kuruş farksız) geçirilmiştir; bu bileşen ilgili ortamda doğrulanmış durumdadır. Sistemin yapay zekâ bileşeni olan denetçi rolündeki dar kapsamlı dil modeli ise henüz laboratuvar düzeyinde deneysel kanıt aşamasındadır (THS 3); zaman-farkındalıklı kural tabanı ve geçmiş beyan mutabakat altsistemi bütünleşik sistem olarak doğrulanmamıştır. Bütünleşik sistem için beyan edilen seviye, en olgun bileşene değil bileşenlerin bütünleşme durumuna göre THS 5 olarak verilmiştir.

**Hedef Teknoloji Hazırlık Seviyesi: THS 7.** *Açıklama:* Proje sonunda sistem, iki sanayi kuruluşunda gerçek bordro ve beyan verisiyle, kendi işletme ortamlarında çalıştırılmış prototip düzeyinde (operasyonel ortamda gösterilmiş sistem) olacaktır; denetçi rolündeki model bu ortamda, uzman denetçiyle kör karşılaştırmalı olarak ölçülmüş olacaktır. THS 8 (tamamlanmış ve kalifiye edilmiş sistem) proje sonrası ilk 12 aylık ticarileşme fazının hedefidir; iki pilotla proje süresi içinde THS 8 iddia edilmesi gerçekçi bulunmamıştır.

## Anahtar Kelimeler

Nöro-sembolik yapay zekâ; denetçi rolünde dar kapsamlı dil modeli; deterministik referansla (oracle) üretilen eğitim verisi; denetimli ince ayar (SFT); abdüktif kök-neden teşhisi; kanıta bağlı gerekçelendirme; sembolik doğrulama kapısı; zaman-farkındalıklı kural tabanı; 5746 sayılı Kanun Ar-Ge teşvikleri; 4691 sayılı Kanun istisnaları; geçmiş beyan mutabakatı; denetim savunma dosyası; grafik işlemcisiz yerel çıkarım; kapalı devre çalışma; veri gizliliği (KVKK)

## Proje Özeti

**Denetci, bir Ar-Ge/Tasarım Merkezinin veya teknoloji geliştirme bölgesi firmasının geçmiş ve cari dönem teşvik/istisna beyanlarını, mevzuatın o tarihte yürürlükte olan hâliyle bağımsız olarak yeniden hesaplayan deterministik bir motor ile bu motorun bulgularını bir denetçi gibi inceleyen, sorgulayan ve kanıt isteyen yerel bir dil modelini tek sistemde birleştiren nöro-sembolik yapay zekâ sistemidir. Sistem, beyan ile hesap arasındaki her farkı tutar ve kök nedeniyle raporlar; mutabık kalınan dönemleri insan onayıyla mühürler; her rakamı mevzuat maddesine bağlı denetim savunma dosyasına dönüştürür ve bordro verisi kurum dışına hiç çıkmadan, grafik işlemcisiz sıradan bir bilgisayarda çalışır.**

5746 sayılı Araştırma, Geliştirme ve Tasarım Faaliyetlerinin Desteklenmesi Hakkında Kanun kapsamındaki 1.300'ü aşkın Ar-Ge ve Tasarım Merkezi ile 4691 sayılı Teknoloji Geliştirme Bölgeleri Kanunu kapsamındaki firmalar; her ay bordroyla iç içe geçen teşvik ve istisna hesaplamaları yapmak, yıllık raporlama sunmak ve düzenli aralıklarla denetlenmek yükümlülüğündedir. Bu hesaplar bugün ağırlıkla elektronik tablolar ve dönemsel mali müşavirlik hizmetiyle yürütülmektedir. Elektronik tablo bugünün oranlarıyla üzerine yazıldığı için, denetimde üç yıl önceki bir rakamın hangi mevzuat sürümüyle nasıl kurulduğunu gösteren bir kayıt bulunmamaktadır. Daha önemlisi, bir fark bulunduğunda onun ne anlama geldiğini yorumlamak, doğru soruyu sormak ve hangi belgeye bakılacağını belirlemek tamamen uzman emeğine bağlıdır; bu emek kıt, pahalı ve ölçeklenemezdir.

Projenin çözdüğü sorun iki katmanlıdır. Birinci katman, bordronun ürettiği hesabın yerine geçmek değil, **aynı hesabın bağımsız olarak yeniden kurulabilmesidir.** Bu yetenek iki yönde birden çalışır:

- **Geriye dönük (geçmiş dönemler):** Geçmiş 12-24 dönemin her biri, kendi yürürlük tarihli kural sürümüyle yeniden hesaplanır; beyan ile hesap arasındaki fark kuruş bazında ve kök nedeniyle gösterilir, ayırt edilemeyen durumlar dürüstçe "belirsiz" olarak raporlanır ve mutabık kalınan dönem denetimde savunulabilir biçimde mühürlenir.
- **Cari dönemde (gelinen aylar):** Kapanan her ay için, tahakkuk kesinleşmeden bağımsız bir kontrol hesabı yapılır; bordro çıktısıyla karşılaştırılarak sapmalar beyandan **önce** görülür. Böylece ürün yılda bir kez kullanılan bir denetim aracı değil, her bordro döneminde çalışan sürekli bir kontrol katmanı hâline gelir.

İkinci katman ve projenin Ar-Ge ağırlığının bulunduğu yer, **denetçi emeğinin yapay zekâya devridir.** Deterministik motorun üzerinde, yapay zekâ **denetçi rolünü üstlenen dar kapsamlı bir dil modeli** olarak konumlanır: motorun ürettiği her farkı bir denetçinin gözüyle inceler, bulgunun ne anlama geldiğini mevzuat maddesi atfıyla açıklar, bir denetçinin soracağı soruları sorar, hangi kanıt belgesinin isteneceğini belirler ve araştırmayı o belgeye yönlendirir; getirilen belgeyle motor yeniden çalıştırılır ve döngü kapanır. Model iş bölümünün hesap tarafına hiçbir zaman girmez: **hesabı motor yapar, bulguyu model inceler, kararı insan verir.** Modelin ürettiği her atıf ve her iddia, motorun kural tabanına karşı sembolik olarak doğrulanır; kural tabanında karşılığı olmayan bir iddia kullanıcıya ulaşmadan elenir. Model, elle etiketlenmiş veriyle değil, doğrulanmış deterministik motorun kendi çıktısından üretilen denetim verisiyle eğitilir (EK-6); böylece sistem kendi kullanımı sırasında kendi eğitim verisini biriktirir. Yeminli Mali Müşavirin tasdik yetkisi ve sorumluluğu değişmez.

Bu mimari tercih, alandaki yaygın eğilimin tersidir. Mali ve hukuki hesaplamalarda üretken yapay zekâ genellikle hesabı ve kararı üreten konumda denenmekte, bunun sonucu olarak doğrulanamayan çıktılar ve denetim karşısında savunulamayan sonuçlar ortaya çıkmaktadır. Bu projede yapay zekânın rolü bilinçli olarak daraltılmış ve **sembolik bir motorla çevrelenmiştir**: model yalnızca inceler, sorar ve yönlendirir; doğruluğu motor, yetkiyi insan taşır. Projenin araştırma sorusu, bu iş bölümü altında 1-4 milyar parametre sınıfında, grafik işlemcisiz bir bilgisayarda çalışan yerel bir modelin uzman denetçinin ön inceleme yükünü ölçülebilir biçimde üstlenip üstlenemeyeceğidir.

Ürün, internet bağlantısı olmayan (kapalı devre) ortamlardaki sıradan kişisel bilgisayarlarda, grafik işlemci gerektirmeden, yalnızca merkezi işlemciyle çalışır; bordro verisi kurum dışına hiçbir koşulda çıkmaz ve 6698 sayılı Kişisel Verilerin Korunması Kanunu (KVKK) yükümlülükleri tasarım düzeyinde karşılanır. Mevzuat güncellemeleri elektronik imzalı çevrimdışı paketlerle dağıtılır.

Proje kapsamı bilinçli olarak **tek mevzuat ailesiyle**, yani 5746 (Ar-Ge ve Tasarım Merkezleri) ve kardeş rejimi 4691 (Teknoloji Geliştirme Bölgeleri) ile sınırlanmıştır. Bu iki rejim ayrı müşteri segmentleri değildir; **çok sayıda kuruluşta bir arada bulunur**: aynı firma, tesisinde Ar-Ge Merkezi işletirken teknoloji geliştirme bölgesinde de ofis/şirket bulundurabilir. 5746 sayılı Kanun'un 4. maddesi, aynı kazanç üzerinden 4691 istisnasından ayrıca yararlanılmasını yasaklamaktadır (mükerrer yararlanma yasağı). Dolayısıyla personelin, ücretin ve kazancın rejimler arasında doğru paylaştırılması, her kalemin tek bir rejim altında beyan edilmesi ve bu ayrımın denetimde belgelenebilmesi gerekir. Sistem, iki rejimi yalnız ayrı ayrı hesaplamakla kalmaz, **aralarındaki sınırı da denetler**.

İki sanayi kuruluşundan projeye ilişkin yazılı ihtiyaç görüşü alınmış olup, her ikisiyle ücretli saha pilotu planlanmaktadır.

**Katma değer (iki cümlelik sıralama):** *Geri kazanım toplantıyı açar, denetim savunulabilirliği sözleşmeyi kapatır.* Geçmiş dönem mutabakatı, eksik yararlanılmış teşvikleri tutar ve kök nedeniyle ortaya çıkarır (tahsil edilebilirlik, ilgili zamanaşımı pencerelerine ve yazılı mali müşavirlik/hukuk teyidine tabidir; farklar iki yönlüdür ve fazla yararlanma bulgusu geri ödeme riski olarak raporlanır). Denetim savunma dosyası, düzenli denetimlerde her rakamın hangi mevzuat maddesi ve hangi kural sürümüyle kurulduğunu belgeler. Üçüncü ve süreklilik sağlayan kanal cari dönem kontrolüdür: ürün her bordro döneminde çalıştığı için hata denetimde değil oluştuğu ay yakalanır. Denetçi rolündeki model ise bu değerin ölçeklenme koşuludur: bugün her farkın yorumlanması ve hangi belgeye bakılacağının belirlenmesi uzman saati gerektirir; model bu ön inceleme işini üstlendiğinde uzman yalnızca karar noktasına çağrılır ve aynı ekip çok daha fazla dönem ve kuruluşu denetleyebilir. İkincil ticari kaldıraç satın alma sürtünmesinin ortadan kalkmasıdır: veri kurum dışına çıkmadığı için bulut onayı, bilgi güvenliği anketi, harici veri işleyici sözleşmesi ve bilgi işlem proje onayı satın alma zincirinden düşer.

## Projenin Hedefleri

- ☑ Üretim Maliyetlerini ve Giderlerini Düşürme *(teşvik kayıplarının azaltılması; uyum için harcanan nitelikli iş gücünün azaltılması)*
- ☑ Ürün Kalitesi ve Standardını Yükseltme *(beyan ve raporlamada denetlenebilir doğruluk standardı)*
- ☑ Üründe veya Üretim Yöntemlerinde Yenilik Geliştirme
- ☑ Yeni Ürüne Yönelik Araştırma

## Hedeflenen Kazanım ve Sonuçlar

*Her hedef; metrik tanımı, test seti ve ölçüm ayı ile birlikte verilmiştir. Ölçümler kabul testleri ve Yeminli Mali Müşavir (YMM) eşliğinde yapılacak bağımsız örneklem incelemeleriyle doğrulanacaktır. İlk üç kazanım projenin yapay zekâ bileşenine, sonraki ikisi sembolik kural tabanına, son ikisi ürün ve saha doğrulamasına aittir.*

1. **Denetçi rolünü üstlenen dar kapsamlı model (ay 10 laboratuvar, ay 12 saha):** Deterministik motorun çıktısıyla üretilen denetim verisi (EK-6) üzerinde ince ayarlanan 1-4 milyar parametre sınıfındaki modelin; bulgu yorumlama, denetçi sorusu üretme ve araştırma yönlendirme görevlerindeki başarımı. *Metrik:* araştırma yönlendirme isabeti ≥%70 (önerilen belgenin, farkı gerçekten çözen belge olma oranı); ince ayarsız aynı modele karşı ≥15 puan, alan-dışı genel bir modele karşı ölçülebilir üstünlük; ürettiği denetçi sorularının, kör değerlendirmede YMM tarafından "bir denetçinin soracağı soru" olarak nitelenme oranı ≥%70; uzman denetçinin aynı fark envanterinde bulduğu bulguların ≥%80'ini yakalaması (kör karşılaştırma); 16 GB bellekli, grafik işlemcisiz referans bilgisayarda bulgu başına ≤30 saniye. *Test seti:* eğitimde kullanılmamış kör fark envanteri + YMM etiketli doğrulama örneklemi + pilot kuruluşların gerçek fark envanteri.
2. **Kanıta bağlılık ve sembolik doğrulama kapısı (ay 10):** Modelin ürettiği her mevzuat atfının, kural sürümü referansının ve belge talebinin, kural tabanına karşı otomatik olarak doğrulanması. *Metrik:* kullanıcıya ulaşan bulgularda atıf doğruluğu ≥%98 (atıf yapılan madde gerçekten var ve ilgili dönemde yürürlükte); kapıdan elenen bulgu oranı raporlanır ve ince ayar turları boyunca düşer; kural tabanında karşılığı olmayan, kullanıcıya ulaşmış iddia (desteksiz iddia) oranı ≤%1; modelin ürettiği hiçbir çıktının tutar hesabına girmediği kod düzeyinde ayrım ve denetim iziyle kanıtlanır. *Test seti:* kör fark envanteri; her bulgu için atıfların YMM tarafından örneklemle teyidi.
3. **Fark kök-neden teşhisi ve hipotez sıralama (ay 10 laboratuvar, ay 12 saha):** Sembolik hipotez üretimi ile modelin hipotez sıralama ve kanıt talebi görevlerinin birlikte ölçülmesi. *Metrik:* fark **kalemlerinin** ≥%85'i doğru kök-neden sınıfına atanır; doğru kök nedenin modelin sıraladığı ilk üç hipotez içinde bulunma oranı ≥%90; sınıflandırılamayan ve "belirsiz" etiketli **tutar** payı ≤%5. *Test seti:* hata enjeksiyonlu, YMM etiketli, bilinen tek ve çoklu kök neden içeren ≥400 vakalık kalibrasyon seti + mevzuat referanslı ≥60 senaryoluk kütüphane + iki pilotun gerçek fark envanteri.
4. **Zaman-farkındalıklı kural tabanı ve yeniden hesap (ay 7):** 2019-2026 arası her ay için, ilgili dönemde yürürlükte olan parametre ve hesap şeması ile yeniden hesap yapılabilmesi; modelin dayanacağı kural tabanının doğrulanmış olması. *Metrik:* parametresiz koşumda mevcut 96 gerçek çapada regresyon sayısı 0; şema kıran en az 6 tarihli mevzuat olayının (2022 asgari geçim indirimi kaldırımı, 01.08.2025 ay-ortası ücret tavanı yürürlüğü dâhil) doğru dönem sınırıyla uygulanması; YMM teyitli gerçek regresyon çapası 96'dan **≥140'a** çıkarılır ve sentetik kural kapsama vakası ≥400 üretilir (iki sayaç ayrı raporlanır, toplanmaz). *Test seti:* YMM teyitli gerçek beyan dönemleri.
5. **Rejimden bağımsızlık ve rejim sınırı denetimi (ay 8):** 4691 kural seti, çekirdek hesap motorunun kaynak koduna dokunulmadan yalnızca bildirimsel kural dosyalarıyla yazılır. *Metrik:* bildirimsel kapsama oranı ≥%90; çekirdek kodda rejime özgü kaçış kancası ≤3 (her biri mevzuat maddesiyle gerekçelendirilir); 5746 tarafında regresyon 0; 4691 tarafında ≥24 gerçek çapa; iki rejimi bir arada işleten bir kuruluş senaryosunda, aynı kazanç/ücret üzerinden çifte istisna talebi içeren enjekte edilmiş vakaların tamamı (≥20 vaka) tespit edilir ve mevzuat maddesi atfıyla raporlanır.
6. **Cari dönem kontrol hesabı (ay 11):** Pilot kuruluşlarda, kapanan aylar için tahakkuk kesinleşmeden bağımsız kontrol hesabının çalıştırılması. *Metrik:* pilot başına en az 3 cari dönemde kontrol hesabı üretilir; bordro çıktısıyla karşılaştırma raporu tahakkuk tarihinden önce teslim edilir; tespit edilen sapmaların mali müşavir/YMM tarafından değerlendirilme oranı raporlanır. *Test seti:* pilot kuruluşların canlı bordro dönemleri.
7. **Saha doğrulaması (ay 12):** İki sanayi kuruluşunda ücretli, dört kapılı saha pilotunun tamamlanması; kurulumdan ilk rapora bir saat içinde ulaşılması (bilgi işlem desteği olmadan, pilotlarda görev tamamlama oranı ≥%80); en az bir kuruluştan yazılı yenileme/abonelik taahhüdü.

## Hedef Kitle

- ☑ TGB Dışında Bulunan Kurum / Kuruluş *(birincil: 5746 kapsamındaki Ar-Ge ve Tasarım Merkezleri)*
- ☑ TGB İçinde Bulunan Kurum / Kuruluş *(4691 kapsamındaki teknoloji geliştirme bölgesi firmaları; 4691 kural seti proje kapsamında ayrı bir iş paketiyle (İP3) geliştirilmektedir; İstanbul Medeniyet Üniversitesi Teknopark bölge firmaları ürünün ilk kullanıcı adaylarıdır. Bölge firması olup aynı zamanda Ar-Ge Merkezi işleten kuruluşlar için rejim sınırı denetimi de sunulmaktadır.)*
- ☑ Sipariş Üzerine *(geçmiş dönem mutabakat hizmeti)*
- ☑ Kendi Firmamız

## Hedef Lokasyon

- ☑ İl içi, ☑ İl dışı *(Türkiye genelinde Ar-Ge/Tasarım Merkezleri ve teknoloji geliştirme bölgesi firmaları)*

## Projenin Nitelikleri

- ☑ Yeni Bir Ürün veya Hizmet Üretilmesi
- ☑ Verimliliği Artıran Yeni Ürün / Süreç Geliştirmesi
- ☑ Ülke bazında teknolojik olarak yeni ürün üretim süreci
- ☑ Yeni teknoloji geliştirme *(denetçi rolündeki nöro-sembolik model ve deterministik referansla veri üretim yöntemi)*
- ☑ Yeni teknolojinin ülke koşullarına uyarlanması

## Ar-Ge Yönü

Proje, rutin yazılım geliştirmenin ötesinde **dört** teknik belirsizlik üzerinde çalışacaktır. İlk üçü sistemin yapay zekâ bileşenine, dördüncüsü bu bileşenin dayandığı sembolik kural tabanına aittir. Dördünün de düşebilir (yanlışlanabilir) bir ölçütü vardır; ölçütü sağlanamayan soru, proje sonunda başarısız olarak raporlanacaktır.

**AS-1: Denetçi rolü, deterministik bir motorun kendi çıktısıyla eğitilen dar kapsamlı ve yerel bir dil modeline öğretilebilir mi?** Deterministik motor bir farkı bulur ve kök neden adaylarını üretir; ancak bir denetçinin bu bulgu karşısında yaptığı üç iş daha vardır: bulgunun **ne anlama geldiğini** yorumlamak, bulguyu **sorgulayacak soruları** sormak ve o farkı çözmek için **hangi kanıt belgesinin isteneceğini** belirlemek. Bugün bu işleri uzman yapar ve projenin ölçeklenmesinin önündeki asıl darboğaz budur. Projenin tezi, bu denetçi rolünün 1-4 milyar parametre sınıfında, grafik işlemcisiz bir bilgisayarda çalışan bir modele öğretilebileceğidir. Araştırma sorusu üç katmanlıdır.

*(a) Eğitim verisi nereden gelir?* Bu göreve etiketli eğitim verisi üretmek klasik anlamda mümkün değildir; alan uzmanının binlerce örneği elle etiketlemesi gerekirdi. Projenin önerdiği yaklaşım, **doğrulanmış deterministik motoru bir referans kaynağı (oracle) olarak kullanmaktır**: motorun ürettiği fark imzaları, karşı-olgusal çift hesap sonuçları, uygulanan kural sürümü ve insan onayıyla kapanan mutabakat kararları birlikte denetimli eğitim çiftleri oluşturur. Araştırma yönlendirme görevinde etiket, önerilen belge getirildiğinde motorun farkı çözüp çözmediğine göre motor tarafından otomatik üretilir. Böylece eğitim verisi, ürünün kendi çalışması sırasında ve elle etiketleme olmadan birikir. Bu üretim hattının tasarımı, ürettiği verinin yeterliliği ve sentetik veriden gerçek pilot verisine aktarımın ne ölçüde gerçekleştiği açık araştırma problemleridir; hattın kaynakları, görev tanımları, sızıntı ve kalite denetimleri EK-6'da ayrıntılandırılmıştır.

*(b) Dar kapsamlı denetimli ince ayar (SFT) ne kadar kazandırır ve nerede durur?* Küçük bir modelin, ince ayarsız aynı modele ve alan-dışı genel bir modele karşı; bulgu yorumlama, denetçi sorusu üretme ve araştırma yönlendirme görevlerinde ölçülebilir üstünlük sağlayıp sağlamadığı deneysel olarak sınanacaktır. Aynı düzenekte, modelin başarımının veri kaynağına (sentetik senaryo, hata enjeksiyonu, gerçek pilot kaydı) ve veri hacmine göre nasıl değiştiği ölçülerek, hangi eşikten sonra ek verinin kazanç getirmediği belirlenecektir. *(Not: ince ayar, nicemleme ve şema-zorlamalı çözümleme tekniklerinin kendisi olgun araçlardır ve Ar-Ge iddiası bunların uygulanması değildir; iddia, denetim verisinin deterministik referanstan üretilmesi ve bu dar görevde ölçülebilir kazanç elde edilip edilemeyeceğidir.)*

*(c) Döngü nasıl kapanır?* Modelin çıktısı bir hesap değil, bir **denetçi bulgusudur**: "bu fark şu kural sürümünün uygulanmamasıyla tutarlı; şu dönemin şu belgesi istenmeli", "şu hipotez şu kayıtla ayrıştırılabilir; kuruluşa şu soru sorulmalı". Bu bulgu üzerine ilgili belge getirilir, deterministik motor yeniden çalıştırılır ve sonuç modeli değil **motoru** doğrular; motorun yeni sonucu modele yeniden bulgu olarak döner ve inceleme, fark kapanana ya da "belirsiz" olarak insana devredilene kadar sürer. Yanlış bir bulgu yalnızca gereksiz bir inceleme adımı doğurur, hatalı bir tutar üretmez. Bu asimetri, yapay zekânın denetim ortamında güvenle kullanılabilmesinin tasarım koşuludur.
*Ölçüt (ay 10 laboratuvar, ay 12 saha):* Yukarıdaki Kazanım 1'de tanımlanan metrikler.

**AS-2: Küçük bir modelin ürettiği gerekçeler, sembolik bir kural tabanına karşı doğrulanarak kanıta bağlı tutulabilir mi?** Dil modellerinin bilinen zayıflığı, akıcı fakat dayanaksız iddia üretmeleridir; mevzuat alanında bu, var olmayan bir maddeye atıf ya da ilgili dönemde yürürlükte olmayan bir kurala dayanma biçiminde ortaya çıkar ve denetim ortamında kabul edilemez. Bu projede modelin her çıktısı şema-zorlamalı yapıda üretilir ve içindeki her atıf (mevzuat maddesi, kural sürümü, dönem, belge türü) motorun zaman-farkındalıklı kural tabanına karşı **sembolik olarak doğrulanır**; karşılığı olmayan atıf içeren bulgu kullanıcıya ulaşmadan elenir ve eleme kaydı modelin bir sonraki ince ayar turuna olumsuz örnek olarak döner. Araştırma sorusu, bu doğrulama kapısının (i) desteksiz iddiaları hangi oranda yakaladığı, (ii) doğru bulguları hangi oranda haksız yere elediği ve (iii) eleme kayıtlarıyla eğitilen modelin dayanaksız iddia oranının ince ayar turları boyunca düşüp düşmediğidir. Bu, küçük bir modelin açıklamalarının bir sembolik motorla "kanıta bağlı" tutulup tutulamayacağının deneysel sınamasıdır.
*Ölçüt (ay 10):* Yukarıdaki Kazanım 2'de tanımlanan metrikler.

**AS-3: Beyan ile yeniden hesap arasındaki farkların abdüktif kök-neden teşhisi: sembolik hipotez üretimi ile nöral hipotez sıralamanın birleştirilmesi.** Farkı *bulmak* deterministiktir ve rutin yazılımdır; belirsizlik farkın *nedenine* güvenilir biçimde atanmasındadır. Problem klasik bir tanımlanabilirlik (identifiability) problemidir: yuvarlama, kapsam-personel farkı, gün/kısmi çalışma, üst sınır bağlaması, oran farkı, veri eksiği ve gerçek hata gibi birden çok kök neden matematiksel olarak *aynı* fark görüntüsünü üretebilir; üstelik farklar hesap kalemleri arasında zincirleme yayılır. Projede teşhis iki katmanda kurulur. Sembolik katman, karşılaştırmalı çift hesap ve hipotez taramasıyla farkı açıklayabilecek hipotez kümesini eksiksiz ve kanıtlı biçimde üretir; ayırt edilemeyen kümeler "belirsiz" olarak işaretlenir. Nöral katman (denetçi rolündeki model), bu kümeyi kuruluşun bağlamına (belge envanteri, önceki dönem kararları, personel yapısı) göre sıralar ve kümeyi daraltacak kanıt belgesini ister. Araştırma sorusu, sembolik katmanın ürettiği hipotez kümesinin ne ölçüde daraltılabildiği ve nöral sıralamanın, uzmanın sıralamasına ne ölçüde yaklaştığıdır; sembolik katman doğruluğu, nöral katman ise verimliliği taşır.
*Ölçüt (ay 10 laboratuvar, ay 12 saha):* Yukarıdaki Kazanım 3'te tanımlanan metrikler.

**AS-4: Modelin dayanacağı sembolik kural tabanı: üç eksenli yürürlük tarihli sürümleme ve bir teşvik rejiminin bildirimsel kural olarak ifade edilebilirlik sınırı.** Denetçi modelin her atfının doğrulanabilmesi, kural tabanının her dönem için "o gün yürürlükte olan" kuralı kesin olarak bilmesini gerektirir. Mevzuat değişikliklerinin bir kısmı yalnızca bir oranı değiştirir; bir kısmı hesaba giren büyüklüğün *tanımını* değiştirir. 2022'de asgari geçim indiriminin kaldırılması ücret istisnası matrahının tanımını değiştirmiştir (parametre değil, şema kırılması); 7555 sayılı düzenlemenin ücret tavanı 01.08.2025'te ay ortasında yürürlüğe girerek dönem anahtarının kendisini kırmıştır. Üçüncü eksen olarak, aynı döneme ait düzeltme beyannameleri farklı *bilgi tarihleriyle* birden çok geçerli sürüm yaratır. Parametre, hesap şeması ve bilgi tarihi eksenlerinin birlikte sürümlenmesi ve kapanmış bir dönemin o günkü bilgi durumuyla yeniden üretilebilmesi, bu alanda hazır bir çözümü bulunmayan bir bilgi temsili problemidir.

Sorunun ikinci katmanı, rejime özgü mantığın ne kadarının koddan çıkarılıp bildirimsel kural dosyalarına taşınabildiğidir; bu sınır tasarım öncesinde bilinemez, ölçülerek bulunur. 4691 uygun bir sınama alanıdır: ücret gelir vergisi istisnası eğitim derecesinden bağımsız işler, kazanç istisnası matrahı farklı kurulur; yani rejim yalnız parametrede değil mantıkta ayrışır. İki rejimin **aynı kuruluşta bir arada bulunması** ise kural tabanının "hangi kalem hangi rejime ait" sorusunu da çözmesini gerektirir: personelin ve ücretin rejimler arasında paylaştırılması, aynı kazanç üzerinden çifte istisna talebinin engellenmesi (5746 md. 4 mükerrer yararlanma yasağı) ve bu ayrımın denetimde belgelenebilmesi. Bu, iki kural setinin toplamı değil, aralarındaki **sınır koşullarının** bildirimsel olarak modellenmesidir.
*Ölçüt (ay 7 ve ay 8):* Yukarıdaki Kazanım 4 ve 5'te tanımlanan metrikler.

**Ar-Ge iddiası olmayan, geliştirme kalemi olarak beyan edilenler:** Belge içeri alma ve format normalizasyonu; masaüstü ürünleştirme, kurulum sihirbazı ve arayüzler; imzalı çevrimdışı güncelleme mekanizması; ince ayar, nicemleme ve şema-zorlamalı çözümlemenin araç düzeyinde uygulanması. Bu bileşenler proje için gereklidir ancak tek başlarına teknik belirsizlik içermedikleri için araştırma sorusu olarak öne sürülmemektedir.

## Yenilikçi ve Teknolojik Yön

**1. Yapay zekânın hesaplayıcı değil denetçi olarak konumlandırıldığı nöro-sembolik mimari.** Yaygın eğilim, mali ve hukuki hesaplamalarda üretken yapay zekânın karar üretici konumda kullanılmasıdır. Bu projede yapay zekâ **hesap yapmaz, karar vermez**; deterministik motorun sonucunu bir denetçi gibi inceler, bulguyu yorumlar, soru sorar, kanıt ister ve araştırmayı yönlendirir. Roller kesin çizgiyle ayrılmıştır: hesabı motor yapar, bulguyu model inceler, kararı insan verir. Bu iş bölümü, yapay zekânın denetim ortamında tekrarlanabilir ve savunulabilir biçimde kullanılmasının koşuludur ve projenin özgün mimari tercihidir.

**2. Kendi eğitim verisini üreten sistem.** Modelin eğitim verisi, doğrulanmış deterministik motorun kendi çıktısından üretilir; araştırma yönlendirme görevinde etiketi motor otomatik olarak koyar. Sistem, her pilot ve her mutabakat oturumuyla kendi denetim verisini biriktirir; elle etiketleme darboğazı ortadan kalkar ve model, ürün kullanıldıkça iyileşir.

**3. Kanıta bağlı gerekçelendirme ve sembolik doğrulama kapısı.** Modelin her atfı ve her belge talebi, zaman-farkındalıklı kural tabanına karşı doğrulanır; dayanaksız iddia kullanıcıya ulaşmaz ve eleme kaydı modelin eğitimine geri döner. Bu, dil modellerinin bilinen dayanaksız iddia sorununa, alanın sembolik bilgisiyle verilmiş yapısal bir cevaptır.

**4. Grafik işlemcisiz, kapalı devre yerel çıkarım.** Denetçi rolündeki model, internet bağlantısı olmayan ortamlardaki sıradan kişisel bilgisayarlarda, grafik işlemci gerektirmeden çalışır. Bordro ve personel verisi kurum dışına hiçbir koşulda çıkmaz; mevzuat güncellemeleri ve model güncellemeleri elektronik imzalı çevrimdışı paketlerle taşınır. Bu, veri egemenliği ve kapalı ağ gereksinimi olan kuruluşlar için ürünü erişilebilir kılan teknolojik tercihtir ve ek donanım yatırımı gerektirmez.

**5. Zaman-farkındalıklı kural tabanı.** Yaygın uygulamada mevzuat parametreleri yazılıma tek sürüm hâlinde gömülür; değişiklik geldiğinde eski değerlerin üzerine yazılır ve geçmiş dönem yeniden üretilemez hâle gelir. Bu projede parametre, hesap şeması ve bilgi tarihi ayrı eksenlerde sürümlenir; her hesap ve modelin her atfı, ilgili dönemde yürürlükte olan kural sürümüne ve kaynağı olan mevzuat maddesine bağlı kalır. Ürünün çıktısı bir tutar değil, **tutarın gerekçesidir**.

**6. Rejim sınırı denetimi.** İki teşvik rejimini bir arada yürüten kuruluşlarda personel, ücret ve kazancın rejimler arasında paylaştırılması ile mükerrer yararlanma kontrolü, ayrı ayrı hesaplama yapan çözümlerin kapsamadığı bir yetenektir; bu proje söz konusu sınırı denetlenebilir bir kural katmanı olarak modellemektedir.

**7. Kullanım kolaylığının teknolojik gereklilik olarak ele alınması.** Hedef kullanıcı bilgi işlem personeli değil, mali işler ve insan kaynakları uzmanıdır. Kurulumdan ilk rapora bir saat içinde ulaşılması ölçülebilir bir kabul kriteri olarak tanımlanmıştır.

Bu unsurların ayrı ayrı değil **bir arada** bulunması, kamuya açık ürün materyalleri üzerinden yürütülen taramada (EK-1) rastlanmayan bileşimi oluşturmaktadır.

## Proje Ortaklığı

- ☑ Üniversite işbirliği ile yürütülen proje *(İstanbul Medeniyet Üniversitesi öğretim üyelerinden Teknoloji Transfer Ofisi aracılığıyla yapay zekâ, makine öğrenmesi ve doğal dil işleme alanında akademik danışmanlık talep edilecektir: nöro-sembolik denetçi mimarisinin, deterministik referansla veri üretim hattının ve değerlendirme düzeneğinin yöntemsel değerlendirilmesi)*
- ☑ Aynı ildeki firmaların işbirliği ile yürütülen proje *(Tüpraş; saha pilotu)*
- ☑ Farklı ildeki firmaların işbirliği ile yürütülen proje *(Kale Seramik; saha pilotu)*
- ☑ TTO işbirliği ile yürütülen proje *(akademisyen danışmanlığı ve proje değerlendirme)*

## Proje Kapsamında Teknoparktan Talep Edilen Hizmetler

- **Danışmanlık Hizmetleri:** TEKNOLOJİ TRANSFERİ; PAZARLAMA; PATENT; MARKA TESCİL; MUAFİYET UYGULAMALARI *(KDV istisnası ve 4691 muafiyetleri)*
- **Teknik Hizmetler:** EĞİTİM; İNTERNET SERVİSLERİ

## Proje Kapsamında TTO'dan Talep Edilen Hizmetler

- **AKADEMİSYEN DANIŞMANLIĞI**: Yapay zekâ, makine öğrenmesi ve doğal dil işleme alanında; denetçi rolündeki dar kapsamlı modelin eğitim veri hattı, değerlendirme düzeneği (kör karşılaştırma, kanıta bağlılık ölçümü) ve nöro-sembolik doğrulama kapısının yöntemsel değerlendirilmesi. Ayrıca, uygun bulunması hâlinde AS-1 ve AS-2 sonuçlarının ulusal bir yapay zekâ konferansında ortak bildiri olarak sunulması.
- **PROJE DEĞERLENDİRME**: Ara dönem çıktılarının (ay 7 ve ay 10 ölçüm noktaları) bağımsız gözden geçirilmesi.

## Teknoparkta Etkileşimde Bulunulan/Bulunulabilecek Firmalar

Proje, bölge firmalarıyla üç biçimde etkileşim öngörmektedir:

1. **Kullanıcı ve erken geri bildirim kaynağı olarak:** Bölgede faaliyet gösteren firmalar 4691 kapsamında istisna ve muafiyet hesabı yükümlülüğü taşıdığından, ürünün doğrudan hedef kullanıcısıdır. 4691 kural setinin geliştirildiği İP3 aşamasında, gönüllü bölge firmalarından kullanılabilirlik geri bildirimi ve (gizlilik sözleşmesi çerçevesinde) anonimleştirilmiş örnek hesap senaryoları talep edilmesi planlanmaktadır.
2. **Mali müşavirlik/denetim hizmeti veren bölge firmalarıyla:** Varsa, kural setlerinin teyidi ve raporlama çıktılarının uygulamadaki karşılığının değerlendirilmesi konusunda iş birliği.
3. **Yazılım geliştiren bölge firmalarıyla:** Veri içe aktarım formatları ve bordro sistemleri entegrasyonu konusunda deneyim paylaşımı.

*(Etkileşim kurulacak firma adları, bölge yönetiminin yönlendirmesi ve ilgili firmaların onayı ile başvuru sürecinde netleştirilecektir.)*

## Finansman Kaynakları

- ☑ Öz Sermaye *(birincil)*
- ☐ Kamu Destekleri *(bu başvuruda işaretlenmemiştir; ileride TÜBİTAK-TEYDEB başvurusu yapılması hâlinde 4691 muafiyetleriyle mükerrer destek kurallarına göre kalem ayrıştırması yapılacaktır)*

## Proje Ar-Ge Aşamaları

- ☑ Kavram Geliştirme
- ☑ Teknolojik/Teknik ve Ekonomik Yapılabilirlik Etüdü
- ☑ Bir Yenilik Unsuru İçeren Yazılım Geliştirme
- ☑ Yeni ya da İyileştirilmiş Ürün ya da Süreçler İçin Prototip Geliştirme
- ☑ Patent ve Lisans Çalışmaları

## Bölge Dışı Görevlendirme Süresi ve Gerekçesi

Talep edilen süre: **240 saat.** *Gerekçe:* Kişisel veri kurum dışına çıkarılamadığı için saha pilotları, müşteri sanayi kuruluşlarının kendi tesislerinde kurulum ve doğrulama gerektirmektedir; bordro sistemi veri aktarım testleri de müşteri ortamında yürütülecektir.

## Proje Detayı

**Problem:** 5746 sayılı Kanun kapsamındaki Ar-Ge ve Tasarım Merkezleri, her ay bordroyla iç içe geçen teşvik hesaplamaları (gelir vergisi stopajı teşviki, sigorta primi işveren desteği, damga vergisi istisnası, kurumlar vergisi indirimi) yapmak ve düzenli aralıklarla denetlenmek yükümlülüğündedir; 4691 kapsamındaki teknoloji geliştirme bölgesi firmaları da aynı nitelikte aylık istisna hesapları ve bildirimleriyle yükümlüdür. Hesaplar ağırlıkla elektronik tablo ve dönemsel mali müşavirlik hizmetiyle yürütülmekte; geçmiş bir dönemin, o dönemin kurallarıyla yeniden kurulabilmesini sağlayan bir kayıt tutulmamaktadır. Bir fark bulunduğunda onu yorumlayacak, sorgulayacak ve kanıt isteyecek uzman emeği kıt ve pahalıdır; bu nedenle hatalar çoğunlukla denetimde, düzeltme maliyetinin en yüksek olduğu anda ortaya çıkar. Hatalı veya eksik hesap; teşvik iadesi, belge iptali ve eksik yararlanma riski doğurmaktadır.

**Çözüm mimarisi (nöro-sembolik sistem):** *Sembolik katman:* (1) *Deterministik hesap çekirdeği*: her fonksiyonu mevzuat maddesine atıflı, aynı girdiyle her zaman aynı sonucu üreten, kapanan dönemleri değiştirilemez biçimde mühürleyen hesap motoru (firmamızın önceden geliştirdiği, gerçek dönem verisiyle iç doğrulaması tamamlanmış çekirdek üzerine kurulur). (2) *Zaman-farkındalıklı kural tabanı*: parametre, hesap şeması ve bilgi tarihi eksenlerinde sürümlenen bildirimsel kural setleri; 5746 ve 4691 bu tabanın iki uygulaması olup iki rejimi bir arada işleten kuruluşlar için rejim sınırı denetimi bu katmanda kurulur. (3) *Geçmiş beyan mutabakatı ve sembolik teşhis*: kuruluşun geçmiş resmî beyanları (Muhtasar ve Prim Hizmet Beyannamesi, Sosyal Güvenlik Kurumu hizmet listeleri, tahakkuk fişleri) ile bordro verisi sisteme alınır; her dönem kendi kurallarıyla yeniden hesaplanır, farklar için hipotez kümesi kanıtlarıyla üretilir ve insan onayıyla kapanan dönemler bütünlük zinciri korunan değişmez kayıtlara dönüştürülür. *Nöral katman:* (4) *Denetçi rolündeki dar kapsamlı yerel model*: sembolik katmanın bulgularını inceleyen, yorumlayan, hipotezleri sıralayan, denetçi sorusu üreten ve kanıt belgesi isteyen; motorun kendi çıktısından üretilen denetim verisiyle (EK-6) ince ayarlanmış, grafik işlemcisiz çalışan küçük model. *Bağlantı katmanı:* (5) *Sembolik doğrulama kapısı ve döngü*: modelin her atfı kural tabanına karşı doğrulanır, dayanaksız bulgu elenir ve eleme kaydı eğitime döner; kabul edilen bulgu üzerine belge getirilir, motor yeniden koşar ve döngü fark kapanana ya da insana devredilene kadar sürer. (6) *Masaüstü ürün ve çevrimdışı güncelleme*: tek paketle kurulan, grafik işlemci gerektirmeyen uygulama; mevzuat ve model güncellemeleri elektronik imzalı dosya paketleriyle taşınır.

**İş paketleri:** Her paketin adam-ayı, ayı, çıkış kriteri ve Ar-Ge/geliştirme etiketi aşağıdadır; adam-ayı tanımlanmamış hiçbir taahhüt yoktur.

| İP | Kapsam | Ay | Adam/Ay | Nitelik | Çıkış kriteri |
|---|---|---|---|---|---|
| İP1 | Çekirdek devralma; yarıyıl → aylık dönem çözünürlüğü; opsiyonel parametre imzası deseniyle "davranış varsayılanlarla birebir korunur" ilkesi; YMM imzalı regresyon protokolü | 1-2 | 3 | Ar-Ge (AS-4 ön koşulu) | Parametresiz koşumda 96/96 kuruş farksız, sıfır regresyon *(İP7 pilotlarının ön koşuludur)* |
| İP2 | Üç eksenli yürürlük tarihli kural tabanı; Resmî Gazete referanslı ve YMM madde madde teyitli geçmişe dönük parametre tablosu; as-of yeniden üretim; kural tabanının model tarafından sorgulanabilir arayüzü | 1-7 | 6 | Ar-Ge (AS-4) | Gerçek çapa 96 → ≥140; "doğrulanmamış parametreli ay hesaplanamaz ve raporlanamaz" motor seviyesinde sert kural |
| İP3 | 4691 kardeş kural seti (çekirdek koda dokunulmadan, bildirimsel kural dosyalarıyla); rejim sınırı kuralları | 5-8 | 3 | Ar-Ge (AS-4) | Bildirimsel kapsama ≥%90; kaçış kancası ≤3; 5746'da sıfır regresyon; 4691'de ≥24 gerçek çapa; ≥20 çifte istisna vakasının tamamı yakalanır |
| İP4 | Retrospektif belge içeri alma *(alt kalem: geliştirme)*; kademeli mutabakat; çapraz tutarlılık kural zinciri; sembolik hipotez üretimi ve karşı-olgusal çift hesap; ≥60 senaryoluk mevzuat referanslı kütüphane; ≥400 vakalık hata enjeksiyonlu kalibrasyon seti; insan onaylı mühürlü baz | 4-10 | 9 | Ar-Ge (AS-3) | Kalem bazında ≥%85 doğru sınıflandırma; belirsiz tutar payı ≤%5; senaryo ve enjeksiyon setleri İP5'e teslim |
| İP5 | Denetçi rolündeki dar kapsamlı model: motor çıktısından denetim verisi üretim hattı (EK-6); bulgu yorumlama, denetçi sorusu üretme, hipotez sıralama, araştırma yönlendirme ve belge alan çıkarımı görevlerinde denetimli ince ayar (SFT); şema-zorlamalı çıktı ve sembolik doğrulama kapısı; eleme kayıtlarıyla ikinci ince ayar turu; ince ayarsız ve alan-dışı modellere karşı kör karşılaştırma; grafik işlemcisiz çıkarım optimizasyonu | 6-12 | 10 | Ar-Ge (AS-1, AS-2) | Yönlendirme isabeti ≥%70; temel modele karşı ≥15 puan; atıf doğruluğu ≥%98; desteksiz iddia ≤%1; ilk üç hipotezde doğru neden ≥%90; bulgu başına ≤30 sn |
| İP6 | Masaüstü ürünleştirme; imzalı çevrimdışı mevzuat ve model güncellemesi; denetim savunma dosyası çıktısı; kurulum sihirbazı; dosya tabanlı içe aktarım; 12 aylık teşvik projeksiyonu raporu | 8-12 | 5 | **Ar-Ge iddiası değil; geliştirme** | Kurulumdan ilk rapora ≤1 saat; görev tamamlama ≥%80 |
| İP7 | İki ücretli, dört kapılı saha pilotu (veri odası → veri kalite karnesi → retroaktif mutabakat ve denetçi model kör karşılaştırması → yönetim sunumu ve baz sertifikası); sertleştirme; v1.0 | 9-12 | 3 | Destek | Pilot kapanış raporları; uzman-model kör karşılaştırma raporu; en az bir yenileme taahhüdü |
| | **Toplam** | **12 ay** | **39** | *(31 Ar-Ge + 8 geliştirme/destek)* | |

**Proje ekibi:** Proje yöneticisi; bir kıdemli yazılım geliştirici (hesap çekirdeği, kural tabanı ve mutabakat motoru); bir tam zamanlı yapay zekâ/doğal dil işleme mühendisi (İP5 iş paketinin yöneticisi; denetim verisi üretim hattı, denetçi rolündeki modelin ince ayarı, doğrulama kapısı ve değerlendirme düzeneği); bir analiz ve test-altyapı uzmanı (belge yapılarının ve mutabakat vakalarının analizi, senaryo ve enjeksiyon setlerinin kurulması, çapa/regresyon test altyapısı, imzalı güncelleme ve kapalı devre kurulum doğrulaması). Arayüz geliştirme kıdemli geliştirici tarafından üstlenilecektir (4 kişi, ortalama 3,25 tam zaman eşdeğeri; kıdemli geliştirici ve yapay zekâ mühendisi tam zamanlı; efor dağılımı **EK-4**). Yapay zekâ tarafında akademik danışmanlık Teknoloji Transfer Ofisi aracılığıyla, mevzuat doğrulaması YMM'den hizmet alımıyla sağlanacaktır. Firmamız 2013'ten bu yana 5746 süreçleri alanında sanayi kuruluşlarına yazılım geliştirmekte olup projenin sembolik çekirdeği bu birikimle üretilmiş ve gerçek dönem verisiyle iç doğrulaması tamamlanmıştır; bu sayede projenin Ar-Ge eforu, çalışan bir motorun üzerine yapay zekâ bileşenini kurmaya ayrılabilmektedir.

**Bütçe kırılımı (7.000.000 ₺):** *Satırlar, teknopark portalındaki "Proje Bütçe Kalemi" harcama kategorileriyle birebir eşleşecek biçimde düzenlenmiştir; portala aynı dokuz satır girilir.*

| Harcama | Portal harcama kategorisi | Tutar (₺) |
|---|---|---|
| Proje personeli: 39 adam/ay × 130.000 ₺ (brüt ücret + işveren maliyeti + genel gider payı; kırılım ve dayanak: **EK-3**) | Personel Giderleri | 5.070.000 |
| Yeminli Mali Müşavirlik hizmeti: 5746 ve 4691 kural setlerinin madde madde teyidi, geçmiş parametre tablosunun doğrulanması, senaryo kütüphanesinin teyidi, iki pilotta mutabakat denetimi ve denetçi model kör değerlendirmesinde uzman etiketleme; geriye dönük düzeltme pencerelerine ilişkin yazılı hukuk görüşü | Hizmet Alımları | 550.000 |
| Denetimli ince ayar eğitimleri için kısa süreli bulut grafik işlemci kiralama *(yalnızca sentetik ve anonimleştirilmiş veriyle; kişisel veri hiçbir koşulda dışarı çıkmaz)* | Hizmet Alımları | 200.000 |
| Patent ön değerlendirmesi ve başvurusu (patent vekili), marka tescili, yapay zekâ alanında akademik danışmanlık | Hizmet Alımları | 250.000 |
| Yazılım lisansları, kod imzalama sertifikası ve çevrimdışı güncelleme imza altyapısı, test ve model değerlendirme araçları | Hizmet Alımları | 200.000 |
| 3 geliştirici iş istasyonu ve 2 referans test bilgisayarı (4 çekirdek, 16 GB bellek, grafik işlemcisiz) | Makina ve Teçhizat Giderleri | 300.000 |
| Pilot saha ziyaretleri (iki sanayi kuruluşunun tesisleri) ve yapay zekâ alanında dış eğitim/konferans katılım seyahatleri | Seyahat Giderleri | 230.000 |
| Test ve veri ortamı sarf malzemeleri, harici depolama ortamı, çevrimdışı güncelleme paketi taşıyıcı ortamları, ofis sarf giderleri | Sarf Giderleri | 50.000 |
| Öngörülemeyen giderler payı *(firma genel gideri personel birim maliyetine dâhildir; bu kalemde tekrarlanmaz)* | Genel Giderler | 150.000 |
| **Toplam** | | **7.000.000** |

*Bursiyer Giderleri ile Temsil ve Tanıtma Giderleri kategorilerinde bu projede harcama öngörülmemektedir.*

**Başlıca riskler ve önlemleri:** (1) *Denetçi modelin hedef başarıma ulaşamaması*: model hiçbir aşamada hesap yapmadığı için başarısızlığı hatalı tutar üretmez; yalnızca ön incelemenin insan tarafından yapılmaya devam etmesi anlamına gelir. Bu durumda AS-1 olumsuz sonuçlu araştırma sorusu olarak, veri kaynağı ve hacim etkisi ölçümleriyle birlikte raporlanır; ürün sembolik katman üzerinden eksiksiz çalışmayı sürdürür. (2) *Modelin dayanaksız iddia üretmesi*: sembolik doğrulama kapısı, kural tabanında karşılığı olmayan atıf içeren her bulguyu kullanıcıya ulaşmadan eler; kapı başarımı ayrı ölçülür (Kazanım 2) ve eleme kayıtları eğitime geri döner. (3) *Denetim verisinin yetersiz kalması veya sentetik veriden gerçek veriye aktarımın zayıf olması*: veri üretim hattı (EK-6) dört kaynaktan beslenir; kaynak bazlı başarım ölçümü hangi kaynağın eksik olduğunu gösterir; pilot verisi eğitim ve kör test olarak kuruluş ve dönem bazında ayrılır. (4) *Geçmiş dönem parametrelerinin hatalı kurulması*: hiçbir dönem, Resmî Gazete referanslı ve YMM teyitli parametre seti ile yıl bazında kuruş farksız örnek doğrulama tamamlanmadan hesaplanmaz ve raporlanmaz (motor seviyesinde sert kural). (5) *Kök-neden teşhisinde yanlış alarm*: kesinlik ayarı pilot öncesinde ≥60 senaryoluk mevzuat referanslı kütüphaneyle yapılır ve İP4'ün çıkış kriteridir; ayırt edilemeyen kalemler tek nedene zorlanmaz, "belirsiz" raporlanır. (6) *Çekirdek imza genişletmesinin mevcut doğrulamayı bozması*: opsiyonel parametre deseni kullanılır; parametresiz koşumda 96/96 birebir korunur ve bu, pilotların ön koşuludur. (7) *Pilot kuruluşlardan veri temininde gecikme*: veri talepleri firma ve mali müşaviri olmak üzere iki muhataplı protokole bağlanır; dosya tabanlı yedek aktarım yolu mevcuttur. (8) *Grafik işlemcisiz çıkarım süresinin hedefi aşması*: model boyutu ve nicemleme düzeyi referans bilgisayarda ölçülerek seçilir; süre hedefi tutmazsa bulgu üretimi arka planda toplu işlem olarak çalıştırılır ve kullanıcı akışı etkilenmez.

## Proje Çıktılarına Yönelik Bilgiler

**Proje Çıktılarında Kullanılacak Sektör:** İmalat sanayii Ar-Ge/Tasarım Merkezleri (otomotiv, beyaz eşya, seramik, kimya, elektronik dâhil); teknoloji geliştirme bölgesi firmaları; mali müşavirlik ve denetim hizmetleri.

**Patent Çıktısı Var Mı:** Var *(hedeflenmektedir)*. Deterministik bir motorun çıktısından denetim verisi üretilerek denetçi rolündeki bir modelin eğitilmesi ve sembolik doğrulama kapısıyla kapatılan inceleme döngüsü yöntemi ile üç eksenli yürürlük tarihli kural sürümleme yöntemi için projenin 9. ayında patentlenebilirlik ön değerlendirmesi yapılacak; uygun bulunması hâlinde Türk Patent ve Marka Kurumu'na başvurulacaktır. "Denetci" markası için tescil başvurusu planlanmaktadır.

**Çevreye Etkileri:** Ürünün grafik işlemci gerektirmeyen, mevcut kişisel bilgisayarlarda çalışan mimarisi, yapay zekâ kullanımının enerji ayak izini bulut tabanlı alternatiflere kıyasla önemli ölçüde düşürür ve ek donanım yatırımı ile elektronik atık oluşturmaz.

**Sürdürülebilirlik:** Ürünün yaşam döngüsü mevzuata bağlıdır: teşvik mevzuatı düzenli olarak değiştiği için imzalı çevrimdışı güncelleme aboneliği hem sürekli gelir hem sürekli geliştirme döngüsü yaratır. Kural katmanı mimarisi, ileride yeni teşvik rejimlerinin bildirimsel kural setleri olarak eklenmesine açıktır; bu genişleme proje kapsamında değil, ticarileşme fazının yol haritasındadır.

**Ekonomik Değeri:** Ar-Ge personeli başına yıllık teşvik tutarı yaklaşık bir milyon TL mertebesindedir; 150 kişilik bir merkezde yıllık teşvik akışı yüz milyon TL düzeyine ulaşır ve bugün büyük ölçüde elektronik tabloda yönetilmektedir. Ürünün ekonomik değeri dört kanaldan ölçülür: (1) geçmiş dönemlerden geri kazanılabilir tutarlar, (2) önlenen kayıp ve denetim riski (teşvik iadesi, belge iptali), (3) uyum için harcanan nitelikli iş gücünün Ar-Ge'nin kendisine kayması, (4) denetçi rolündeki yapay zekâ bileşeni sayesinde bir uzmanın aynı sürede çok daha fazla dönem ve kuruluşu inceleyebilmesi. Fiyat, teorik teşvik hacmine değil, müşterinin hâlihazırda ödediği mali müşavirlik ve danışmanlık harcamasının üzerine eklenen marjinal tutara çıpalanır ve pilotlarda ölçülür. İlk fiyat bandı olarak yıllık toplam sahip olma bedeli 75 personele kadar olan merkezlerde 0,3-0,5 milyon TL, 76-200 personelli merkezlerde 0,5-0,9 milyon TL öngörülmektedir; geçmiş dönem mutabakat hizmeti ayrıca proje bazlı fiyatlanır.

Ticarileşme stratejisi beş adımlıdır. (1) Proje içindeki iki ücretli pilot (Tüpraş ve Kale Seramik) referans vaka çalışmasına dönüştürülür; ilk satışın kanıtı projenin kendi çıktısıdır. (2) Firmamızın 2013'ten bu yana 5746 alanında hizmet verdiği sanayi kuruluşu portföyü ilk satış kanalıdır; ürün bu kuruluşlara mevcut ilişki üzerinden sunulur. (3) Yeminli ve serbest mali müşavirlik ofisleri çarpan kanalıdır: ürün YMM'nin yetkisini almaz, onun tasdik işini belgeli ve hızlı hâle getirir; bu nedenle rakip değil dağıtım ortağı olarak konumlanır. (4) İstanbul Medeniyet Üniversitesi Teknopark başta olmak üzere teknoloji geliştirme bölgesi firmaları 4691 kural setinin doğrudan alıcısıdır ve bölge yönetimleriyle iş birliği içinde ulaşılır. (5) Hizmet-önce gelir modeli uygulanır: geçmiş dönem mutabakat hizmeti kapıyı açar ve ilk faturayı üretir, yıllık lisans ve güncelleme aboneliği sürekliliği sağlar.

Orta vadede (proje sonrası ilk 12-24 ay) iki pilotun aboneliğe dönmesi ve 8-12 yeni kuruluşun kazanılması hedeflenmektedir. Uzun vadede (3-5 yıl) 60-100 kuruluşluk abonelik tabanı ve ortalama 0,5 milyon TL yıllık bedelle 30-50 milyon TL yıllık yinelenen gelir hedeflenmektedir. Bu hedefler öngörüdür; hata oranı, geri kazanım büyüklüğü ve fiyat kabulüne ilişkin varsayımlar pilotlarda ölçülecek hipotez olarak etiketlenmiştir. Firma açısından ürün geliri, danışmanlık gelirinden bağımsız ve kişi sayısına bağlı olmadan ölçeklenen ilk gelir kalemidir. Ürün Türk mevzuatına özgü olduğundan ihracat hedefi yoktur; kural tabanı mimarisi ileride yeni teşvik rejimlerinin eklenmesine açıktır ve bu, proje sonrası büyüme yoludur.

**Alınacak Dış Hizmetler:** (1) Yeminli Mali Müşavirlik hizmeti: 5746 ve 4691 kural setlerinin madde madde teyidi, 2019-2026 geçmiş parametre tablosunun Resmî Gazete referanslı doğrulanması, mevzuat referanslı senaryo kütüphanesinin yazımı, iki pilotta mutabakat denetimi ve denetçi modelin kör değerlendirmesinde uzman etiketleme; ayrıca geriye dönük düzeltme pencerelerine ilişkin yazılı hukuk görüşü (bütçe: 550.000 TL). (2) Denetimli ince ayar eğitimleri için kısa süreli bulut grafik işlemci kiralama; yalnızca sentetik ve anonimleştirilmiş veriyle, kişisel veri hiçbir koşulda kurum dışına çıkmaz (200.000 TL). (3) Patent ön değerlendirmesi ve başvurusu için patent vekili, marka tescili ve Teknoloji Transfer Ofisi aracılığıyla yapay zekâ, makine öğrenmesi ve doğal dil işleme alanında akademik danışmanlık (250.000 TL). Yazılım geliştirme, model eğitimi ve değerlendirme işleri dışarıdan hizmet olarak alınmaz; proje ekibi tarafından yürütülür.

**Projenin Müşterisi:** Birincil müşteri kitlesi üç durumu kapsar: (a) yalnız 5746 sayılı Kanun kapsamında Ar-Ge veya Tasarım Merkezi işleten sanayi kuruluşları, (b) yalnız 4691 sayılı Kanun kapsamında teknoloji geliştirme bölgesinde faaliyet gösteren firmalar, (c) her ikisini bir arada yürüten kuruluşlar. Üçüncü grup, rejim sınırı ve mükerrer yararlanma denetimi ihtiyacı nedeniyle ürünün en yüksek değer ürettiği ve en az ikame edilebilir olduğu segmenttir. Kuruluş içindeki alıcı ve kullanıcı, mali işler direktörü, Ar-Ge merkezi müdürü ve insan kaynakları/bordro sorumlusudur; bilgi işlem birimi kurulum için gerekmez.

İkincil müşteri, mali müşavirlik ve Yeminli Mali Müşavirlik ofisleridir; ürün bu ofislerin tasdik ve raporlama işini belgeli hâle getirdiğinden hem kullanıcı hem dağıtım kanalıdır.

Sipariş üzerine nitelik: Proje kapsamındaki geçmiş dönem mutabakat hizmeti sipariş üzerine sunulur. Tüpraş ve Kale Seramik'ten projeye ilişkin yazılı ihtiyaç görüşü alınmış olup her iki kuruluşla ücretli saha pilotu planlanmaktadır; niyet mektupları başvuru ekinde sunulmaktadır. Bu iki kuruluş ürünün ilk müşterisi ve referans vakasıdır.

Kendi firmamız da müşteridir: Firmamızın 5746 danışmanlık hizmet kolu, ürünü kendi müşterilerinin geçmiş dönem mutabakatında ve cari dönem kontrolünde kullanacaktır.

Projenin İstanbul Medeniyet Üniversitesi Teknopark bünyesinde yürütülmesi, 4691 kapsamındaki ilk kullanıcılara bölge içinden ulaşılmasına ve bölge firmalarına doğrudan fayda üretilmesine imkân verir; bölge firmaları 4691 kural setinin ilk kullanıcı adaylarıdır.

**Hedef Pazar, Pazarın Lokal veya Globalliği:** Pazar yereldir (Türkiye); ürün Türk teşvik mevzuatına özgüdür ve yurt dışı genişleme proje hedefi değildir. Sektör olarak imalat sanayii (otomotiv, beyaz eşya, seramik, kimya, enerji, elektronik) Ar-Ge ve Tasarım Merkezleri, teknoloji geliştirme bölgesi firmaları ve mali müşavirlik/denetim hizmetleri hedeflenmektedir. Kullanıcı segmentleri: mali işler yöneticileri, Ar-Ge merkezi yöneticileri, bordro/insan kaynakları uzmanları ve YMM/SMMM ofisleri.

Pazar büyüklüğü, T.C. Sanayi ve Teknoloji Bakanlığı Ar-Ge Teşvikleri Genel Müdürlüğü'nün yayımladığı istatistiklere dayanır. Haziran 2026 itibarıyla Türkiye'de 1.373 Ar-Ge Merkezi ve 347 Tasarım Merkezi faaliyettedir (toplam 1.720 kuruluş). Ağustos 2026 itibarıyla 113 teknoloji geliştirme bölgesinde 13.452 firma faaliyet göstermekte ve 134.686 personel istihdam edilmektedir. Toplam adreslenebilir pazar bu iki kümenin birleşimidir; iki küme ayrık değildir, çok sayıda kuruluş her iki rejimde birden yer aldığından büyüklük iki sayının toplamı olarak değil kesişim dikkate alınarak değerlendirilmektedir. Hizmet edilebilir pazar, aylık teşvik hacmi bağımsız kontrolü ekonomik kılan kuruluşlardır: 30 ve üzeri Ar-Ge/Tasarım personeli olan merkezler ile bölge içinde 10 ve üzeri istisna kapsamında personel çalıştıran firmalar; firmamızın saha deneyimine dayalı tahminle 2.500-3.500 kuruluş. Bunun içinde iki rejimi bir arada yürüten kuruluşlar en yüksek değerli segmenttir.

Mevcut pay: Ürün yenidir, pazar payı sıfırdır. Firmamız 2013'ten bu yana 5746 süreçleri alanında sanayi kuruluşlarına hizmet vermekte olup mevcut danışmanlık portföyü ilk satış tabanını oluşturur. Hedef pay: proje sonrası ilk 12-24 ayda 10-14 kuruluş (iki pilot dâhil); 3-5 yılda 60-100 kuruluş, yani hizmet edilebilir pazarın yaklaşık yüzde 2-4'ü ve iki rejimi bir arada yürüten yüksek değerli segmentte daha yüksek bir oran. Coğrafi öncelik İstanbul ve Marmara'dır; Ar-Ge merkezlerinin ve teknoloji geliştirme bölgesi firmalarının en yoğun bulunduğu bölgedir ve iki pilot da bu bölgededir. Küresel pazar hedeflenmediğinden yerelleştirme ve kültürel uyarlama stratejisi gerekmez; ürün tamamen Türkçe mevzuat ve belge yapılarıyla çalışır.

Referanslar: T.C. Sanayi ve Teknoloji Bakanlığı, Ar-Ge ve Tasarım Merkezleri İstatistikleri (sanayi.gov.tr, Haziran 2026); T.C. Sanayi ve Teknoloji Bakanlığı, Teknoloji Geliştirme Bölgeleri İstatistikî Bilgiler (sanayi.gov.tr, Ağustos 2026).

## Rekabet Analizi

Ağustos-Eylül 2026'da kamuya açık ürün web siteleri ve tanıtım materyalleri üzerinden yedi ürün/hizmet kategorisi taranmıştır (ayrıntılı liste ve yöntem başvuru ekinde, EK-1). Rakipler ve nitelikleri:

(1) Yerli 5746/4691 hesaplama yazılımları: ArgeMemory (Vertex Group; 5746 ve 4691 hesaplama süreçlerinin otomasyonu), Ar-GeNet (bulut tabanlı teşvik bordrosu ve beyan işlemleri), Kolay Teşvik ve SMMM Teşvik (kanun numarası bazlı teşvik hesabı). Bu ürünler ileriye dönük aylık hesabı üretmeye odaklanır; kamuya açık materyallerinde geçmiş beyanın bağımsız yeniden hesaplanması, yürürlük tarihli kural sürümleme ve rejim sınırı denetimi ilan edilmemiştir. Ar-GeNet bulut tabanlı olduğundan kapalı devre gereksinimi olan kuruluşlarda kullanılamaz.

(2) Bordro ve kurumsal kaynak planlama paketlerinin teşvik modülleri (Logo, Mikro, Netsis, Luca vb.): Bordro içinde ileriye dönük hesap yaparlar; tek sürümlü kural tablosuyla çalıştıkları için geçmiş bir dönemi kendi kural sürümüyle yeniden kuramazlar ve hesabı üreten sistemin kendisi olduklarından bağımsız kontrol hesabı sunmazlar. Ürünümüz bu paketlerin yerini almaz, çıktısını bağımsız olarak doğrular.

(3) Yeminli Mali Müşavirlik ve Ar-Ge teşvik danışmanlığı hizmetleri (büyük denetim firmaları ve uzman danışmanlıklar): Dönemsel, elle yürütülen tasdik ve rapor hizmetidir; yazılım ürünü değildir. Bu kanal rakip değil tamamlayıcıdır; ürün YMM'nin tasdik işini belgeli hâle getirir ve dağıtım ortağı olarak konumlanır.

(4) Yurt dışı Ar-Ge vergi teşviki otomasyon ürünleri (Boast.ai, Neo.tax, Clarus R+D vb.): Kendi ülke mevzuatlarına özgüdür ve bulut tabanlıdır; Türk mevzuatında karşılığı yoktur.

(5) Genel amaçlı bulut yapay zekâ araçları: Bordro verisinin kurum dışına çıkmasını gerektirdiğinden ve ürettikleri açıklamalar bir kural tabanına karşı doğrulanmadığından denetim ortamında kullanılamaz.

Pazar payları: Bu alanda kamuya açık pazar payı verisi yoktur; yerli yazılım sağlayıcıları kurulum sayılarını ilan etmemektedir. Firmamızın saha gözlemine göre pazarın büyük çoğunluğunda hesap hâlâ elektronik tablo ve dönemsel danışmanlıkla yürütülmektedir; asıl ikame edilen şey bir rakip yazılım değil, bu elle yürütülen süreçtir.

Projenin iddiası kategori boşluğu değil, özellik bileşimidir: incelenen ürünlerin kamuya açık materyallerinde geçmiş beyan mutabakatı, yürürlük tarihli kural sürümleme, kapalı devre çalışma, iki rejimi bir arada yürüten kuruluşlar için rejim sınırı denetimi ve bulguları inceleyip kanıt isteyen yerel bir yapay zekâ bileşeninin bir arada ilan edildiği bir çözüme rastlanmamıştır. Ürünlerin ilan edilmemiş yetenekleri bulunabileceğinden bu tespit kamuya açık materyalle sınırlıdır ve mutlak üstünlük iddiası içermez. Rekabet konumu beş dayanağa oturur: gerçek dönem verisiyle doğrulanmış deterministik hesap çekirdeği, zaman-farkındalıklı kural tabanı, rejim sınırı ve mükerrer yararlanma denetimi, verinin kurum dışına çıkmadığı kapalı devre çalışma modeli ve denetçi rolünü üstlenen, kanıta bağlı tutulan yerel yapay zekâ bileşeni. Sipariş üzerine nitelik: geçmiş dönem mutabakat hizmeti için Tüpraş ve Kale Seramik'ten yazılı ihtiyaç görüşü alınmıştır.

## Fikri Sınai ve Mülkiyet Hakları

| Başvuru/Yayın Numarası | Belge Adı | Koruma Tipi |
|---|---|---|
| *(planlanan)* | "Denetci" marka tescil başvurusu | Marka |
| *(değerlendirilecek)* | Deterministik motor çıktısından denetim verisi üretimi ve sembolik doğrulama kapısıyla kapatılan denetçi model döngüsü yöntemi | Patent (ön değerlendirme ay 9) |
| *(değerlendirilecek)* | Üç eksenli yürürlük tarihli kural sürümleme yöntemi | Patent (ön değerlendirme ay 9) |

Projede geliştirilen tüm yazılım, veri modelleri ve yöntemlerin fikri hakları firmamıza aittir; proje öncesinde firma bünyesinde geliştirilen hesap çekirdeği başlangıç varlığı olarak beyan edilir.

## Alınan Ar-Ge Destekleri

| Kurum Adı | Destek Tipi | Destek Dönemi |
|---|---|---|
| *(beyan edilecek)* | - | - |

## Projeye Ait Ürünler

| Ürün Adı | Ürün Tipi |
|---|---|
| Denetci Masaüstü: 5746 ve 4691 kural setleriyle **cari dönem bağımsız kontrol hesabı** (her bordro döneminde, tahakkuk kesinleşmeden fark raporu), mevzuat maddesi atıflı raporlama, 12 aylık teşvik projeksiyonu; geçmiş beyan mutabakatı, kök-neden teşhisi, **denetçi rolündeki yerel yapay zekâ bileşeni** (bulgu yorumu, denetçi soruları, kanıt talebi), mühürlü baz ve denetim savunma dosyası yetenekleri personel kademesine göre açılır | Yazılım (masaüstü uygulama, yerel yapay zekâ bileşenli) |
| Mevzuat güncelleme aboneliği: elektronik imzalı çevrimdışı kural paketleriyle dağıtım | Hizmet (abonelik) |
| Geçmiş dönem mutabakat hizmeti: 12-24 dönemlik retroaktif yeniden hesap ve YMM eşliğinde kapanış raporu | Hizmet (proje bazlı) |

*Sipariş formu iki satırdır: (1) yıllık lisans + güncelleme aboneliği, (2) geçmiş dönem mutabakat hizmeti. Yetenek kademeleri ayrı ürün olarak satılmaz.*

## Proje Ekipman Listesi

| Ekipman | Adet | Amaç |
|---|---|---|
| Geliştirici iş istasyonu | 3 | Yazılım geliştirme |
| Referans test bilgisayarı (asgari sistem: 4 çekirdek, 16 GB bellek, grafik işlemcisiz) | 2 | Ürünün hedef donanımda doğrulanması ve kapalı devre kurulum senaryolarının sınanması (ağdan yalıtılmış ortam sanal makineyle karşılanır) |

## Başvuru Ekleri

| Ek | İçerik |
|---|---|
| **EK-1** | Rekabet analizi: incelenen ürün listesi, tarama yöntemi ve karşılaştırma ölçütleri |
| **EK-2** | Pilot kuruluşlardan alınacak niyet mektupları (iki adet; şablon ve toplama süreci) |
| **EK-3** | Personel birim maliyeti dayanağı: ekip kıdem dağılımı ve maliyet kırılımı |
| **EK-4** | Proje ekibi ve özgeçmişler: roller, efor dağılımı ve nitelik beyanı |
| **EK-5** | Firma tanıtım dosyası, referanslar, mali tablolar ve proje finansman beyanı |
| **EK-6** | Denetçi rolündeki dar kapsamlı modelin eğitim verisi üretim yöntemi: kaynaklar, görev tanımları, hacim ve kalite denetimleri (AS-1, AS-2 ve İP5 dayanağı) |

---

### Portala Aktarım Durumu *(bu bölüm forma aktarılmaz)*

Portal çıktısı (07.09.2026 16:32) ile bu belge karşılaştırılmıştır. Metin alanlarının çoğu (Proje Özeti, Kazanımlar, Ar-Ge Yönü, Yenilikçi Yön, Proje Detayı) portala aktarılmış ve bu belgeyle birebir uyumludur. Boş kalan alanlar ve girilecek değerler `portal-doldurma-kontrol-listesi.md` dosyasında alan alan verilmiştir. Kalan tutarsızlıklar: "Toplam Personel: 2" ve "Kiralanan Alan: 10 m²" kayıtları 4 kişilik ekiple çelişmektedir; personel kaydı 4 olarak güncellenmeli, alan ihtiyacı (kişi başına 2,5 m²'ye düşer) gözden geçirilmelidir.
