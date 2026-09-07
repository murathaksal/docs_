# PROJE BİLGİ FORMU — Denetci

*İstanbul Medeniyet Üniversitesi Teknopark A.Ş. Proje Bilgi Formu (Döküman No: A-R-01224) başlıklarına göre doldurulmuştur. Hakem heyeti ve teknopark yönetimi diline uygun yazılmış; kısaltmalar ilk kullanımda açılmış, mutlak nitelikli rekabet iddialarından kaçınılmış, her sayısal hedef metrik tanımı + test seti + ölçüm ayı üçlüsüne bağlanmıştır.*

---

## Kimlik Bilgileri

| Alan | Değer |
|---|---|
| Firma Unvanı | ARGELOG ARGE MERKEZİ YÖNETİM DANIŞMANLIĞI VE YAZILIM HİZMETLERİ A.Ş. |
| Proje Adı | **Denetci** — Ar-Ge Teşvik Beyanlarının Bağımsız Yeniden Hesaplanması ve Denetim Savunma Dosyası Yazılımı |
| Proje Kodu | ARGELOG-002 |
| Proje Yöneticisi | Murat Haksal |
| Proje Süresi | 12 Ay |
| Tahmini Proje Bütçesi | 7.500.000,00 ₺ |
| Ar-Ge İş Gücü | 19 Adam/Ay |
| Destek/Geliştirme İş Gücü | 6 Adam/Ay |
| Toplam İş Gücü | 25 Adam/Ay |
| Toplam Personel | 5 kişi (ortalama 2,1 tam zaman eşdeğeri; 25 ÷ 12 = 2,08) |
| Projenin Sektörü | Yazılım / Bilişim Teknolojileri |
| İlişkili Sektörler | İmalat sanayii Ar-Ge/Tasarım Merkezleri; teknoloji geliştirme bölgesi firmaları; mali müşavirlik ve denetim hizmetleri |
| NACE Kodu | 62.01 — Bilgisayar Programlama Faaliyetleri |

## Teknolojik Hazırlık Seviyesi

**Mevcut Teknoloji Hazırlık Seviyesi: THS 5** — *Açıklama:* Projenin çekirdeğini oluşturan deterministik teşvik hesaplama motoru firmamız bünyesinde daha önce geliştirilmiş; T.C. Sanayi ve Teknoloji Bakanlığı'nın yayımladığı gerçek dönem verisi üzerinde iç doğrulamadan (96 adet çapa testinin tamamı kuruş farksız) geçirilmiştir. Bileşen düzeyinde ilgili ortam doğrulaması tamamlanmıştır; zaman-farkındalıklı kural katmanı ve geçmiş beyan mutabakat altsistemi henüz bütünleşik sistem olarak doğrulanmamıştır.

**Hedef Teknoloji Hazırlık Seviyesi: THS 7** — *Açıklama:* Proje sonunda sistem, iki sanayi kuruluşunda gerçek bordro ve beyan verisiyle, kendi işletme ortamlarında çalıştırılmış prototip düzeyinde (operasyonel ortamda gösterilmiş sistem) olacaktır. THS 8 (tamamlanmış ve kalifiye edilmiş sistem) proje sonrası ilk 12 aylık ticarileşme fazının hedefidir; iki pilotla proje süresi içinde THS 8 iddia edilmesi gerçekçi bulunmamıştır.

## Anahtar Kelimeler

Mevzuat uyum yazılımı; deterministik hesaplama motoru; 5746 sayılı Kanun Ar-Ge teşvikleri; 4691 sayılı Kanun istisnaları; zaman-farkındalıklı kural sürümleme; geçmiş beyan mutabakatı; kök-neden teşhisi; denetim savunma dosyası; kapalı devre yazılım; veri gizliliği (KVKK)

## Proje Özeti

**Denetci, bir Ar-Ge/Tasarım Merkezinin veya teknoloji geliştirme bölgesi firmasının geçmiş ve cari dönem teşvik/istisna beyanlarını mevzuatın o tarihte yürürlükte olan hâliyle bağımsız ve deterministik olarak yeniden hesaplayan, beyan ile hesap arasındaki her farkı tutar ve kök nedeniyle raporlayan, mutabık kalınan dönemleri insan onayıyla mühürleyip her rakamı mevzuat maddesine bağlı denetim savunma dosyasına dönüştüren; bordro verisi kurum dışına hiç çıkmadan sıradan bir bilgisayarda çalışan masaüstü yazılımdır.**

5746 sayılı Araştırma, Geliştirme ve Tasarım Faaliyetlerinin Desteklenmesi Hakkında Kanun kapsamındaki 1.300'ü aşkın Ar-Ge ve Tasarım Merkezi ile 4691 sayılı Teknoloji Geliştirme Bölgeleri Kanunu kapsamındaki firmalar; her ay bordroyla iç içe geçen teşvik ve istisna hesaplamaları yapmak, yıllık raporlama sunmak ve düzenli aralıklarla denetlenmek yükümlülüğündedir. Bu hesaplar bugün ağırlıkla elektronik tablolar ve dönemsel mali müşavirlik hizmetiyle yürütülmektedir. Yapı gereği, elektronik tablo bugünün oranlarıyla üzerine yazıldığı için, denetimde üç yıl önceki bir rakamın hangi mevzuat sürümüyle nasıl kurulduğunu gösteren bir kayıt bulunmamaktadır.

Projenin çözdüğü sorun, bordronun ürettiği hesabın yerine geçmek değil — **aynı hesabın bağımsız olarak yeniden kurulabilmesidir.** Bu yetenek iki yönde birden çalışır:

- **Geriye dönük (geçmiş dönemler):** Geçmiş 12-24 dönemin her biri, kendi yürürlük tarihli kural sürümüyle yeniden hesaplanır; beyan ile hesap arasındaki fark kuruş bazında ve kök nedeniyle gösterilir, ayırt edilemeyen durumlar dürüstçe "belirsiz" olarak raporlanır ve mutabık kalınan dönem denetimde savunulabilir biçimde mühürlenir.
- **Cari dönemde (gelinen aylar):** Kapanan her ay için, tahakkuk kesinleşmeden bağımsız bir kontrol hesabı yapılır; bordro çıktısıyla karşılaştırılarak sapmalar beyandan **önce** görülür. Böylece ürün yılda bir kez kullanılan bir denetim aracı değil, her bordro döneminde çalışan sürekli bir kontrol katmanı hâline gelir; hata denetimde değil oluştuğu ay yakalanır ve düzeltme maliyeti asgariye iner.

Bordro ve kurumsal kaynak planlama paketlerinin teşvik modülleri bu iki işlevi yapısal olarak yerine getiremez: tek sürümlü kural tablosuyla çalışırlar (geçmişi kendi kural sürümüyle kuramazlar) ve hesabı üreten sistemin kendisi olduklarından bağımsız bir kontrol hesabı sunmazlar. Denetci, bordro yazılımının yerini almaz; onun çıktısını bağımsız olarak doğrular.

Platformun çekirdeği, her hesabın mevzuat maddesine izlenebilir bağını koruyan, yürürlük tarihine göre sürümlenen kural setleriyle çalışan deterministik hesap motorudur. Yapay zekâ yalnızca tek bir dar görevde (belge alan çıkarımı önerisi) kullanılır; **hesap yapmaz, karar vermez ve tüm önerileri insan onayından geçer.** Ürün, internet bağlantısı olmayan (kapalı devre) ortamlardaki sıradan kişisel bilgisayarlarda, grafik işlemci gerektirmeden, yalnızca merkezi işlemciyle çalışır; bordro verisi kurum dışına hiçbir koşulda çıkmaz ve 6698 sayılı Kişisel Verilerin Korunması Kanunu (KVKK) yükümlülükleri tasarım düzeyinde karşılanır. Mevzuat güncellemeleri, elektronik imzalı çevrimdışı paketlerle dağıtılır.

Proje kapsamı bilinçli olarak **tek mevzuat ailesiyle** — 5746 (Ar-Ge ve Tasarım Merkezleri) ve kardeş rejimi 4691 (Teknoloji Geliştirme Bölgeleri) — sınırlanmıştır. Bu iki rejim ayrı müşteri segmentleri değildir; **çok sayıda kuruluşta bir arada bulunur**: aynı firma, tesisinde Ar-Ge Merkezi işletirken teknoloji geliştirme bölgesinde de ofis/şirket bulundurabilir. Bu durum, hesaplama açısından iki rejimi ayrı ayrı desteklemekten daha zor bir problem doğurur: 5746 sayılı Kanun'un 4. maddesi, aynı kazanç üzerinden 4691 istisnasından ayrıca yararlanılmasını yasaklamaktadır (mükerrer yararlanma yasağı). Dolayısıyla personelin, ücretin ve kazancın rejimler arasında doğru paylaştırılması; her kalemin tek bir rejim altında beyan edilmesi ve bu ayrımın denetimde belgelenebilmesi gerekir. Ürün, iki rejimi yalnız ayrı ayrı hesaplamakla kalmaz, **aralarındaki sınırı da denetler**.

İki sanayi kuruluşundan projeye ilişkin yazılı ihtiyaç görüşü alınmış olup, her ikisiyle ücretli saha pilotu planlanmaktadır.

**Katma değer — iki cümlelik sıralama:** *Geri kazanım toplantıyı açar, denetim savunulabilirliği sözleşmeyi kapatır.* Geçmiş dönem mutabakatı, eksik yararlanılmış teşvikleri tutar ve kök nedeniyle ortaya çıkarır (tahsil edilebilirlik, ilgili zamanaşımı pencerelerine ve yazılı mali müşavirlik/hukuk teyidine tabidir; farklar iki yönlüdür — fazla yararlanma bulgusu geri ödeme riski olarak raporlanır). Denetim savunma dosyası ise, düzenli denetimlerde her rakamın hangi mevzuat maddesi ve hangi kural sürümüyle kurulduğunu belgeler. Üçüncü ve süreklilik sağlayan kanal, cari dönem kontrolüdür: ürün her bordro döneminde çalıştığı için hata denetimde değil oluştuğu ay yakalanır; bu, hem yıllık abonelik gerekçesinin hem de ürünün günlük kullanımının dayanağıdır. İkincil ticari kaldıraç mühendislik değil satın alma sürtünmesidir: veri kurum dışına çıkmadığı için bulut onayı, bilgi güvenliği anketi, harici veri işleyici sözleşmesi ve bilgi işlem proje onayı satın alma zincirinden düşer.

## Projenin Hedefleri

- ☑ Üretim Maliyetlerini ve Giderlerini Düşürme *(teşvik kayıplarının azaltılması; uyum için harcanan nitelikli iş gücünün azaltılması)*
- ☑ Ürün Kalitesi ve Standardını Yükseltme *(beyan ve raporlamada denetlenebilir doğruluk standardı)*
- ☑ Üründe veya Üretim Yöntemlerinde Yenilik Geliştirme
- ☑ Yeni Ürüne Yönelik Araştırma

## Hedeflenen Kazanım ve Sonuçlar

*Her hedef; metrik tanımı, test seti ve ölçüm ayı ile birlikte verilmiştir. Ölçümler kabul testleri ve Yeminli Mali Müşavir (YMM) eşliğinde yapılacak bağımsız örneklem incelemeleriyle doğrulanacaktır.*

1. **Zaman-farkındalıklı yeniden hesap (ay 7):** 2019-2026 arası her ay için, ilgili dönemde yürürlükte olan parametre ve hesap şeması ile yeniden hesap yapılabilmesi. *Metrik:* parametresiz koşumda mevcut 96 gerçek çapada regresyon sayısı 0; şema kıran en az 6 tarihli mevzuat olayının (2022 asgari geçim indirimi kaldırımı, 01.08.2025 ay-ortası ücret tavanı yürürlüğü dâhil) doğru dönem sınırıyla uygulanması. *Test seti:* YMM teyitli gerçek beyan dönemleri.
2. **Doğrulama çapası genişletmesi (ay 7):** Gerçek beyan kaynaklı, YMM teyitli regresyon çapası mevcut 96'dan **≥140'a** çıkarılır (dönem × rejim). *Ayrıca* sentetik kural kapsama vakası ≥400 üretilir. Bu iki sayaç ayrı raporlanır, hiçbir koşulda toplanmaz.
3. **Fark kök-neden teşhisi (ay 10 laboratuvar, ay 12 saha):** *Metrik:* fark **kalemlerinin** ≥%85'i doğru kök-neden sınıfına otomatik atanır; sınıflandırılamayan ve "belirsiz" etiketli **tutar** payı ≤%5. *Test seti:* hata enjeksiyonlu, YMM etiketli, bilinen tek ve çoklu kök neden içeren ≥400 vakalık kalibrasyon seti + mevzuat referanslı ≥60 senaryoluk kütüphane + iki pilotun gerçek fark envanteri.
4. **Rejimden bağımsızlık ölçümü (ay 8):** 4691 kural seti, çekirdek hesap motorunun kaynak koduna dokunulmadan yalnızca bildirimsel kural dosyalarıyla yazılır. *Metrik:* bildirimsel kapsama oranı ≥%90; çekirdek kodda rejime özgü kaçış kancası ≤3 (her biri mevzuat maddesiyle gerekçelendirilir); 5746 tarafında regresyon 0; 4691 tarafında ≥24 gerçek çapa. *Ek metrik (rejimler arası):* iki rejimi bir arada işleten bir kuruluş senaryosunda, aynı kazanç/ücret üzerinden çifte istisna talebi içeren enjekte edilmiş vakaların tamamı (≥20 vaka) tespit edilir ve mevzuat maddesi atfıyla raporlanır.
5. **Cari dönem kontrol hesabı (ay 11):** Pilot kuruluşlarda, kapanan aylar için tahakkuk kesinleşmeden bağımsız kontrol hesabının çalıştırılması. *Metrik:* pilot başına en az 3 cari dönemde kontrol hesabı üretilir; bordro çıktısıyla karşılaştırma raporu tahakkuk tarihinden önce teslim edilir; tespit edilen sapmaların mali müşavir/YMM tarafından değerlendirilme oranı raporlanır. *Test seti:* pilot kuruluşların canlı bordro dönemleri.
6. **Saha doğrulaması (ay 12):** İki sanayi kuruluşunda ücretli, dört kapılı saha pilotunun tamamlanması; kurulumdan ilk rapora bir saat içinde ulaşılması (bilgi işlem desteği olmadan, pilotlarda görev tamamlama oranı ≥%80); en az bir kuruluştan yazılı yenileme/abonelik taahhüdü.

## Hedef Kitle

- ☑ TGB Dışında Bulunan Kurum / Kuruluş *(birincil: 5746 kapsamındaki Ar-Ge ve Tasarım Merkezleri)*
- ☑ TGB İçinde Bulunan Kurum / Kuruluş *(4691 kapsamındaki teknoloji geliştirme bölgesi firmaları — 4691 kural seti proje kapsamında ayrı bir iş paketiyle (İP3) geliştirilmektedir; İstanbul Medeniyet Üniversitesi Teknopark bölge firmaları ürünün ilk kullanıcı adaylarıdır. Bölge firması olup aynı zamanda Ar-Ge Merkezi işleten kuruluşlar için rejim sınırı denetimi de sunulmaktadır.)*
- ☑ Sipariş Üzerine *(geçmiş dönem mutabakat hizmeti)*
- ☑ Kendi Firmamız

## Hedef Lokasyon

- ☑ İl içi — ☑ İl dışı *(Türkiye genelinde Ar-Ge/Tasarım Merkezleri ve teknoloji geliştirme bölgesi firmaları)*

## Projenin Nitelikleri

- ☑ Yeni Bir Ürün veya Hizmet Üretilmesi
- ☑ Verimliliği Artıran Yeni Ürün / Süreç Geliştirmesi
- ☑ Ülke bazında teknolojik olarak yeni ürün üretim süreci
- ☑ Yeni teknolojinin ülke koşullarına uyarlanması

## Ar-Ge Yönü

Proje, rutin yazılım geliştirmenin ötesinde **üç** teknik belirsizlik üzerinde çalışacaktır. Üçünün de düşebilir (yanlışlanabilir) bir ölçütü vardır; ölçütü sağlanamayan soru, proje sonunda başarısız olarak raporlanacaktır.

**AS-1 — Üç eksenli yürürlük tarihli sürümleme ve kapanmış dönemlerin as-of yeniden üretilebilirliği.** Mevzuat değişikliklerinin bir kısmı yalnızca bir oranı veya tutarı değiştirir; bir kısmı ise hesaba giren büyüklüğün *tanımını* değiştirir. 2022'de asgari geçim indiriminin kaldırılması ücret istisnası matrahının tanımını değiştirmiştir (parametre değil, şema kırılması); 7555 sayılı düzenlemenin bağlayıcı ücret tavanı 01.08.2025'te ay ortasında yürürlüğe girerek dönem anahtarının kendisini kırmıştır ve mevcut çekirdek bunu yarıyıl anahtarıyla temsil edememektedir. Buna üçüncü eksen eklenir: aynı döneme ait düzeltme beyannameleri, farklı *bilgi tarihleriyle* birden çok geçerli sürüm yaratır. Parametre, hesap şeması ve bilgi tarihi eksenlerinin birlikte sürümlenmesi ve kapanmış bir dönemin, o günkü bilgi durumuyla yeniden üretilebilmesi, yayımlanmış hazır çözümü bulunmayan bir tasarım problemidir.
*Ölçüt (ay 7):* Yukarıdaki Kazanım 1 ve 2'de tanımlanan metrikler.

**AS-2 — Beyan ile yeniden hesap arasındaki farkların abdüktif kök-neden teşhisi ve ayırt edilemezliğin dürüst raporlanması.** Farkı *bulmak* deterministiktir ve rutin yazılımdır; belirsizlik farkın *nedenine* güvenilir biçimde atanmasındadır. Problem klasik bir tanımlanabilirlik (identifiability) problemidir: yuvarlama, kapsam-personel farkı, gün/kısmi çalışma, üst sınır bağlaması, oran farkı, veri eksiği ve gerçek hata gibi birden çok kök neden matematiksel olarak *aynı* fark görüntüsünü üretebilir; üstelik farklar hesap kalemleri arasında zincirleme yayılır. Karşılaştırmalı çift hesap, hipotez taraması, zincirin topolojik sırayla kök nedene indirgenmesi ve ayırt edilemeyen hipotez kümelerinin kanıtla birlikte "belirsiz" raporlanması üzerine kurulu bir teşhis çerçevesi geliştirilecektir. Çerçevenin tamamen deterministik ve kanıt üretir olması, denetim savunulabilirliğinin ve KVKK kısıtının doğrudan sonucudur.
*Ölçüt (ay 10 laboratuvar, ay 12 saha):* Yukarıdaki Kazanım 3'te tanımlanan metrikler.

**AS-3 — Bir teşvik rejiminin ne kadarı bildirimsel kural olarak ifade edilebilir: hesap motorunun rejimden bağımsızlık sınırının 5746 ↔ 4691 üzerinde ölçülmesi.** Tek rejime göre yazılmış bir hesap motoruna ikinci rejim eklemek, kural katmanının hangi soyutlama düzeyinde kesildiğine bağlı olarak ya birinci rejimin doğrulamasını kırar ya da kod çoğaltmasına döner; bu sınırın nerede olduğu tasarım öncesinde bilinemez, ölçülerek bulunur. Soru "ikinci kural setini yazabilir miyiz" değildir — o rutindir; soru, rejime özgü mantığın ne kadarının koddan çıkarılıp bildirimsel kural dosyalarına taşınabildiğidir. 4691 bu ölçüm için uygun bir sınama alanıdır: ücret gelir vergisi istisnası eğitim derecesinden bağımsız işler, kazanç istisnası matrahı farklı kurulur; yani rejim yalnız parametrede değil mantıkta ayrışır.

Sorunun ikinci ve daha zor katmanı, iki rejimin **aynı kuruluşta bir arada bulunmasıdır.** Bir firma hem Ar-Ge Merkezi işletip hem teknoloji geliştirme bölgesinde şirket bulundurduğunda, kural katmanının yalnız "hangi rejim" değil "hangi kalem hangi rejime ait" sorusunu da çözmesi gerekir: personelin ve ücretin rejimler arasında paylaştırılması, aynı kazanç üzerinden çifte istisna talebinin engellenmesi (5746 md. 4 mükerrer yararlanma yasağı) ve bu ayrımın denetimde belgelenebilmesi. Bu, bağımsız iki kural setinin toplamı değil, aralarındaki **sınır koşullarının** modellenmesidir; kural katmanının soyutlama düzeyi bu koşulları ifade edemiyorsa ya çifte yararlanma sessizce geçer ya da kural mantığı yeniden koda sızar.
*Ölçüt (ay 8):* Yukarıdaki Kazanım 4'te tanımlanan metrikler.

**Ar-Ge iddiası olmayan, geliştirme kalemi olarak beyan edilenler:** Belge içeri alma ve format normalizasyonu; masaüstü ürünleştirme, kurulum sihirbazı ve arayüzler; imzalı çevrimdışı güncelleme mekanizması; belge alan çıkarımında hazır bir küçük dil modelinin şema-zorlamalı çözümleme ve deterministik doğrulama kapısıyla olduğu gibi kullanılması. Bu bileşenler proje için gereklidir ancak teknik belirsizlik içermedikleri için araştırma sorusu olarak öne sürülmemektedir.

## Yenilikçi ve Teknolojik Yön

**1. Hesabın kendisi değil, hesabın yeniden kurulabilirliği ürünleştirilmektedir.** Mevcut çözümler teşvik tutarını üretmeye odaklanır. Bu proje, üretilmiş bir beyanın bağımsız olarak yeniden hesaplanmasını, farkının kök nedenine bağlanmasını ve sonucun mühürlenerek denetimde savunulabilir hâle getirilmesini bir ürün işlevi olarak kurar. Ürünün çıktısı bir tutar değil, **tutarın gerekçesidir**.

**2. Zaman-farkındalıklı kural mimarisi.** Yaygın uygulamada mevzuat parametreleri yazılıma tek sürüm hâlinde gömülür; değişiklik geldiğinde eski değerlerin üzerine yazılır ve geçmiş dönem yeniden üretilemez hâle gelir. Bu projede parametre, hesap şeması ve bilgi tarihi ayrı eksenlerde sürümlenir; her hesap, ilgili dönemde yürürlükte olan kural sürümüne ve kaynağı olan mevzuat maddesine bağlı kalır. Bu, ürünün teknolojik ayrımının çekirdeğidir.

**3. Rejim sınırı denetimi.** İki teşvik rejimini bir arada yürüten kuruluşlarda personel, ücret ve kazancın rejimler arasında paylaştırılması ile mükerrer yararlanma kontrolü, ayrı ayrı hesaplama yapan çözümlerin kapsamadığı bir yetenektir; bu proje söz konusu sınırı denetlenebilir bir kural katmanı olarak modellemektedir.

**4. Yapay zekânın bilinçli olarak sınırlandırılması.** Yaygın eğilim, mali ve hukuki hesaplamalarda üretken yapay zekânın karar üretici konumda kullanılmasıdır. Bu projede yapay zekâ **hesap yapmaz, karar vermez**; yalnızca belge alan çıkarımında öneri üretir ve her önerisi deterministik doğrulama kapısından ve insan onayından geçer. Bu tercih, denetim savunulabilirliğinin ve 6698 sayılı Kanun uyumunun ön koşuludur; ürünün çıktısının denetim karşısında tekrarlanabilir olmasını sağlar.

**5. Kapalı devre ve donanım bağımsız çalışma.** Ürün, internet bağlantısı olmayan ortamlardaki sıradan kişisel bilgisayarlarda, grafik işlemci gerektirmeden çalışacak biçimde tasarlanmıştır. Bordro ve personel verisi kurum dışına hiçbir koşulda çıkmaz; mevzuat güncellemeleri elektronik imzalı çevrimdışı paketlerle taşınır. Bu, veri egemenliği ve kapalı ağ gereksinimi olan kuruluşlar (savunma tedarik zinciri, bilgi güvenliği kısıtlı kurumlar) için ürünü erişilebilir kılan teknolojik tercihtir ve ek donanım yatırımı gerektirmez.

**6. Kullanım kolaylığının teknolojik gereklilik olarak ele alınması.** Hedef kullanıcı bilgi işlem personeli değil, mali işler ve insan kaynakları uzmanıdır. Kurulumdan ilk rapora bir saat içinde ulaşılması ölçülebilir bir kabul kriteri olarak tanımlanmıştır; bu, sunucu kurulumu ve bilgi işlem projesi gerektiren kurumsal yazılım yaklaşımından ayrılan bir tasarım tercihidir.

Bu unsurların ayrı ayrı değil **bir arada** bulunması, kamuya açık ürün materyalleri üzerinden yürütülen taramada (EK-1) rastlanmayan bileşimi oluşturmaktadır.

## Proje Ortaklığı

- ☑ Üniversite işbirliği ile yürütülen proje *(İstanbul Medeniyet Üniversitesi öğretim üyelerinden Teknoloji Transfer Ofisi aracılığıyla yazılım mühendisliği alanında akademik danışmanlık talep edilecektir: zaman-farkındalıklı kural sürümleme ve teşhis çerçevesinin değerlendirilmesi)*
- ☑ Farklı ildeki firmaların işbirliği ile yürütülen proje *(saha pilotu yürütülecek sanayi kuruluşları)*

## Proje Kapsamında Teknoparktan Talep Edilen Hizmetler

- **Danışmanlık Hizmetleri:** MUAFİYET UYGULAMALARI; AR-GE PROJE TEKLİF DOSYASININ HAZIRLANMASI; PATENT; MARKA TESCİL
- **Teknik Hizmetler:** EĞİTİM; İNTERNET SERVİSLERİ

## Proje Kapsamında TTO'dan Talep Edilen Hizmetler

- **AKADEMİSYEN DANIŞMANLIĞI** — Yazılım mühendisliği alanında; zaman-farkındalıklı kural sürümleme ve fark kök-neden teşhis çerçevesinin yöntemsel değerlendirilmesi.
- **PROJE DEĞERLENDİRME** — Ara dönem çıktılarının (ay 7 ve ay 10 ölçüm noktaları) bağımsız gözden geçirilmesi.

## Teknoparkta Etkileşimde Bulunulan/Bulunulabilecek Firmalar

Proje, bölge firmalarıyla üç biçimde etkileşim öngörmektedir:

1. **Kullanıcı ve erken geri bildirim kaynağı olarak:** Bölgede faaliyet gösteren firmalar 4691 kapsamında istisna ve muafiyet hesabı yükümlülüğü taşıdığından, ürünün doğrudan hedef kullanıcısıdır. 4691 kural setinin geliştirildiği İP3 aşamasında, gönüllü bölge firmalarından kullanılabilirlik geri bildirimi ve — gizlilik sözleşmesi çerçevesinde — anonimleştirilmiş örnek hesap senaryoları talep edilmesi planlanmaktadır.
2. **Mali müşavirlik/denetim hizmeti veren bölge firmalarıyla:** Varsa, kural setlerinin teyidi ve raporlama çıktılarının uygulamadaki karşılığının değerlendirilmesi konusunda iş birliği.
3. **Yazılım geliştiren bölge firmalarıyla:** Veri içe aktarım formatları ve bordro sistemleri entegrasyonu konusunda deneyim paylaşımı.

*(Etkileşim kurulacak firma adları, bölge yönetiminin yönlendirmesi ve ilgili firmaların onayı ile başvuru sürecinde netleştirilecektir.)*

## Finansman Kaynakları

- ☑ Öz Sermaye *(birincil)*
- ☑ Kamu Destekleri *(TÜBİTAK-TEYDEB başvurusu değerlendirilmektedir; başvuru yapılması hâlinde 4691 muafiyetleriyle mükerrer destek kurallarına göre kalem ayrıştırması yapılacaktır)*

## Proje Ar-Ge Aşamaları

- ☑ Kavram Geliştirme
- ☑ Teknolojik/Teknik ve Ekonomik Yapılabilirlik Etüdü
- ☑ Bir Yenilik Unsuru İçeren Yazılım Geliştirme
- ☑ Yeni ya da İyileştirilmiş Ürün ya da Süreçler İçin Prototip Geliştirme
- ☑ Patent ve Lisans Çalışmaları

## Bölge Dışı Görevlendirme Süresi ve Gerekçesi

Talep edilen süre: **240 saat.** *Gerekçe:* Kişisel veri kurum dışına çıkarılamadığı için saha pilotları, müşteri sanayi kuruluşlarının kendi tesislerinde kurulum ve doğrulama gerektirmektedir; bordro sistemi veri aktarım testleri de müşteri ortamında yürütülecektir.

## Proje Detayı

**Problem:** 5746 sayılı Kanun kapsamındaki Ar-Ge ve Tasarım Merkezleri, her ay bordroyla iç içe geçen teşvik hesaplamaları (gelir vergisi stopajı teşviki, sigorta primi işveren desteği, damga vergisi istisnası, kurumlar vergisi indirimi) yapmak ve düzenli aralıklarla denetlenmek yükümlülüğündedir; 4691 kapsamındaki teknoloji geliştirme bölgesi firmaları da aynı nitelikte aylık istisna hesapları ve bildirimleriyle yükümlüdür. Hesaplar ağırlıkla elektronik tablo ve dönemsel mali müşavirlik hizmetiyle yürütülmekte; geçmiş bir dönemin, o dönemin kurallarıyla yeniden kurulabilmesini sağlayan bir kayıt tutulmamaktadır. Hatalı veya eksik hesap; teşvik iadesi, belge iptali ve eksik yararlanma riski doğurmaktadır.

**Çözüm mimarisi:** (1) *Deterministik hesap çekirdeği* — her fonksiyonu mevzuat maddesine atıflı, aynı girdiyle her zaman aynı sonucu üreten, kapanan dönemleri değiştirilemez biçimde mühürleyen hesap motoru (firmamızın önceden geliştirdiği, gerçek dönem verisiyle iç doğrulaması tamamlanmış çekirdek üzerine kurulur). (2) *Zaman-farkındalıklı kural katmanı* — parametre, hesap şeması ve bilgi tarihi eksenlerinde sürümlenen kural setleri; 5746 ve 4691 bu katmanın iki uygulaması olup, iki rejimi bir arada işleten kuruluşlar için rejim sınırı denetimi (personel/ücret/kazanç paylaştırması ve mükerrer yararlanma kontrolü) bu katmanda kurulur. (3) *Geçmiş beyan mutabakatı ve mühürlü baz* — kuruluşun geçmiş resmî beyanları (Muhtasar ve Prim Hizmet Beyannamesi, Sosyal Güvenlik Kurumu hizmet listeleri, tahakkuk fişleri) ile bordro verisi sisteme alınır; her dönem kendi kurallarıyla yeniden hesaplanır, kademeli mutabakat kurulur, farklar kök nedenine göre sınıflandırılır ve insan onayıyla kapanan dönemler bütünlük zinciri korunan değişmez kayıtlara dönüştürülür. (4) *Masaüstü ürün ve çevrimdışı güncelleme* — tek paketle kurulan, grafik işlemci gerektirmeyen uygulama; mevzuat güncellemeleri elektronik imzalı dosya paketleriyle taşınır.

**İş paketleri:** Her paketin adam-ayı, ayı, çıkış kriteri ve Ar-Ge/geliştirme etiketi aşağıdadır; adam-ayı tanımlanmamış hiçbir taahhüt yoktur.

| İP | Kapsam | Ay | Adam/Ay | Nitelik | Çıkış kriteri |
|---|---|---|---|---|---|
| İP1 | Çekirdek devralma; yarıyıl → aylık dönem çözünürlüğü; opsiyonel parametre imzası deseniyle "davranış varsayılanlarla birebir korunur" ilkesi; YMM imzalı regresyon protokolü | 1-2 | 3 | Ar-Ge | Parametresiz koşumda 96/96 kuruş farksız, sıfır regresyon *(İP6 pilotlarının ön koşuludur)* |
| İP2 | Üç eksenli yürürlük tarihli kural katmanı; Resmî Gazete referanslı ve YMM madde madde teyitli geçmişe dönük parametre tablosu; as-of yeniden üretim; etki analizi | 1-7 | 6 | Ar-Ge (AS-1) | Gerçek çapa 96 → ≥140; "doğrulanmamış parametreli ay hesaplanamaz ve raporlanamaz" motor seviyesinde sert kural |
| İP3 | 4691 kardeş kural seti — çekirdek koda dokunulmadan, bildirimsel kural dosyalarıyla | 5-8 | 3 | Ar-Ge (AS-3) | Bildirimsel kapsama ≥%90; kaçış kancası ≤3; 5746'da sıfır regresyon; 4691'de ≥24 gerçek çapa |
| İP4 | Retrospektif belge içeri alma *(alt kalem: geliştirme)*; kademeli mutabakat; çapraz tutarlılık kural zinciri; abdüktif kök-neden sınıflandırıcı; karşı-olgusal çift hesap; ≥60 senaryoluk kütüphane; ≥400 vakalık YMM etiketli kalibrasyon seti; insan onaylı mühürlü baz | 4-10 | 7 | Ar-Ge (AS-2) | Kalem bazında ≥%85 doğru sınıflandırma; belirsiz tutar payı ≤%5 |
| İP5 | Masaüstü ürünleştirme; imzalı çevrimdışı güncelleme; denetim savunma dosyası çıktısı; kurulum sihirbazı; dosya tabanlı içe aktarım; hazır küçük modelle şema-zorlamalı belge alan çıkarımı ve deterministik doğrulama kapısı (~1 AA); 12 aylık teşvik projeksiyonu raporu (~0,5 AA) | 7-11 | 4 | **Ar-Ge iddiası değil — geliştirme** | Kurulumdan ilk rapora ≤1 saat; görev tamamlama ≥%80 |
| İP6 | İki ücretli, dört kapılı saha pilotu (veri odası → veri kalite karnesi → retroaktif mutabakat → yönetim sunumu ve baz sertifikası); sertleştirme; v1.0 | 8-12 | 2 | Destek | Pilot kapanış raporları; en az bir yenileme taahhüdü |
| | **Toplam** | **12 ay** | **25** | *(19 Ar-Ge + 6 geliştirme/destek)* | |

**Proje ekibi:** Proje yöneticisi, iki kıdemli yazılım geliştirici, bir arayüz/ürün geliştirici ve bir test-altyapı uzmanı (5 kişi, ortalama 2,1 tam zaman eşdeğeri). Mevzuat doğrulaması YMM'den hizmet alımıyla sağlanacaktır. Firmamız 2013'ten bu yana 5746 süreçleri alanında sanayi kuruluşlarına yazılım geliştirmekte olup projenin çekirdek hesap motoru bu birikimle üretilmiş ve gerçek dönem verisiyle iç doğrulaması tamamlanmıştır — projenin en riskli görünen bileşeni fiilen çalışır durumdadır. Riskli olan kısım motorun kendisi değil, etrafına kurulacak zaman-farkındalıklı kural katmanı ve kök-neden teşhis çerçevesidir.

**Bütçe kırılımı (7.500.000 ₺):**

| Kalem | Tutar (₺) |
|---|---|
| Personel — 25 adam/ay × 230.000 ₺ (brüt + işveren maliyeti + genel gider payı; kırılım ve dayanak: **EK-3**) | 5.750.000 |
| Dış hizmet — YMM (5746 ve 4691 kural setlerinin madde madde teyidi, geçmiş parametre tablosu teyidi, iki pilotta mutabakat denetimi) ve geriye dönük düzeltme pencerelerine ilişkin yazılı hukuk görüşü | 550.000 |
| Donanım — 3 geliştirici iş istasyonu + 2 referans test bilgisayarı | 300.000 |
| Yazılım lisansları, kod imzalama sertifikası ve çevrimdışı güncelleme imza altyapısı, test araçları | 200.000 |
| Patent ön değerlendirmesi ve başvurusu, marka tescili, akademik danışmanlık | 250.000 |
| Genel gider, pilot saha seyahati ve öngörülemeyen | 450.000 |

**Başlıca riskler ve önlemleri:** (1) *Geçmiş dönem parametrelerinin hatalı kurulması* — hiçbir dönem, Resmî Gazete referanslı ve YMM teyitli parametre seti ile yıl bazında kuruş farksız örnek doğrulama tamamlanmadan hesaplanmaz ve raporlanmaz (motor seviyesinde sert kural). (2) *Kök-neden sınıflandırmasında yanlış alarm* — kesinlik ayarı pilot öncesinde ≥60 senaryoluk mevzuat referanslı kütüphaneyle yapılır ve İP4'ün çıkış kriteridir; ayırt edilemeyen kalemler tek nedene zorlanmaz, "belirsiz" raporlanır. (3) *Çekirdek imza genişletmesinin mevcut doğrulamayı bozması* — opsiyonel parametre deseni kullanılır; parametresiz koşumda 96/96 birebir korunur ve bu, pilotların ön koşuludur. (4) *Pilot kuruluşlardan veri temininde gecikme* — veri talepleri firma ve mali müşaviri olmak üzere iki muhataplı protokole bağlanır; dosya tabanlı yedek aktarım yolu mevcuttur. (5) *Yerel dil modeli bileşeninin yetersiz kalması* — bileşen tek bir dar görevde ve deterministik doğrulama kapısı arkasında kullanılır; devre dışı bırakılması ürün değerini etkilemez.

## Proje Çıktılarına Yönelik Bilgiler

**Proje Çıktılarında Kullanılacak Sektör:** İmalat sanayii Ar-Ge/Tasarım Merkezleri (otomotiv, beyaz eşya, seramik, kimya, elektronik dâhil); teknoloji geliştirme bölgesi firmaları; mali müşavirlik ve denetim hizmetleri.

**Patent Çıktısı Var Mı:** Var *(hedeflenmektedir)*. Üç eksenli yürürlük tarihli kural sürümleme ve fark kök-neden teşhis yöntemleri için projenin 9. ayında patentlenebilirlik ön değerlendirmesi yapılacak; uygun bulunması hâlinde Türk Patent ve Marka Kurumu'na başvurulacaktır. "Denetci" markası için tescil başvurusu planlanmaktadır.

**Çevreye Etkileri:** Ürünün grafik işlemci gerektirmeyen, mevcut kişisel bilgisayarlarda çalışan mimarisi, yapay zekâ kullanımının enerji ayak izini bulut tabanlı alternatiflere kıyasla önemli ölçüde düşürür ve ek donanım yatırımı ile elektronik atık oluşturmaz.

**Sürdürülebilirlik:** Ürünün yaşam döngüsü mevzuata bağlıdır: teşvik mevzuatı düzenli olarak değiştiği için imzalı çevrimdışı güncelleme aboneliği hem sürekli gelir hem sürekli geliştirme döngüsü yaratır. Kural katmanı mimarisi, ileride yeni teşvik rejimlerinin bildirimsel kural setleri olarak eklenmesine açıktır; bu genişleme proje kapsamında değil, ticarileşme fazının yol haritasındadır.

**Ekonomik Değeri:** Ar-Ge personeli başına yıllık teşvik tutarı yaklaşık bir milyon TL mertebesindedir; 150 kişilik bir merkezde yıllık teşvik akışı yüz milyon TL düzeyine ulaşır ve bugün büyük ölçüde elektronik tabloda yönetilmektedir. Ürünün ekonomik değeri üç kanaldan ölçülür: geçmiş dönemlerden geri kazanılabilir tutarlar, önlenen kayıp ve denetim riski, uyum için harcanan nitelikli iş gücünün Ar-Ge'nin kendisine kayması. Fiyat, teorik teşvik hacmine değil müşterinin hâlihazırda ödediği mali müşavirlik/danışmanlık harcamasının üzerine eklenen marjinal tutara çıpalanır ve pilotlarda ölçülür; ilk fiyat bandı olarak yıllık toplam sahip olma bedeli ≤75 personelli merkezlerde ~0,3-0,5 M TL, 76-200 personelli merkezlerde ~0,5-0,9 M TL öngörülmektedir. Hata oranı ve geri kazanım büyüklüğüne ilişkin varsayımlar, pilot 1'de ölçülecek hipotez olarak açıkça etiketlenmiştir. Firma açısından iki gelir kalemi öngörülmektedir: yıllık lisans + güncelleme aboneliği ve proje bazlı geçmiş dönem mutabakat hizmeti.

**Alınacak Dış Hizmetler:** Yeminli Mali Müşavirlik hizmeti (5746 ve 4691 kural setlerinin madde madde teyidi, geçmiş parametre tablosunun teyidi, pilot mutabakat denetimi); geriye dönük düzeltme pencerelerine ilişkin yazılı hukuk görüşü.

**Projenin Müşterisi:** Birincil müşteri kitlesi üç durumu kapsar: (a) yalnız 5746 kapsamında Ar-Ge veya Tasarım Merkezi işleten sanayi kuruluşları, (b) yalnız 4691 kapsamında teknoloji geliştirme bölgesinde faaliyet gösteren firmalar, (c) **her ikisini bir arada yürüten kuruluşlar** — bu üçüncü grup, rejim sınırı ve mükerrer yararlanma denetimi ihtiyacı nedeniyle ürünün en yüksek değer ürettiği ve en az ikame edilebilir olduğu segmenttir. İkincil: mali müşavirlik/YMM ofisleri. Projenin İstanbul Medeniyet Üniversitesi Teknopark bünyesinde yürütülmesi, ürünün ilk kullanıcılarına bölge içinden ulaşılmasına ve bölge firmalarına doğrudan fayda üretilmesine imkân verir. İki sanayi kuruluşundan yazılı ihtiyaç görüşü alınmış olup pilot çalışmalar bu kuruluşlarla planlanmaktadır.

**Hedef Pazar, Pazarın Lokal veya Globalliği:** Ulusal. İki rejim ve bunların kesişimi: 5746 kapsamındaki 1.300'ü aşkın Ar-Ge/Tasarım Merkezi ile 4691 kapsamındaki teknoloji geliştirme bölgesi firmaları. Bu iki küme ayrık değildir — bir kuruluş her iki rejimde birden yer alabildiğinden pazar büyüklüğü iki sayının toplamı olarak değil, kesişim dikkate alınarak değerlendirilmektedir. Ürün Türk teşvik mevzuatına özgüdür; yurt dışı genişleme proje hedefi değildir.

## Rekabet Analizi

Ağustos-Eylül 2026'da, kamuya açık ürün web siteleri ve tanıtım materyalleri üzerinden yedi ürün/hizmet kategorisi taranmıştır (ayrıntılı liste ve yöntem: **EK-1**). Yurt içinde 5746 kapsamında hesaplama yapan yerli yazılımlar mevcuttur; bunlardan en az biri 4691 kapsamını da ilan etmektedir. Dolayısıyla projenin iddiası kategori boşluğu değil, **özellik bileşimi**dir: incelenen ürünlerin kamuya açık materyallerinde; geçmiş beyan mutabakatı, yürürlük tarihli kural sürümleme, kapalı devre çalışma ve iki rejimi bir arada yürüten kuruluşlar için rejim sınırı denetimi yeteneklerinin **bir arada** ilan edildiği bir çözüme rastlanmamıştır. Ürünlerin ilan edilmemiş yetenekleri bulunabileceğinden, bu tespit kamuya açık materyalle sınırlıdır ve mutlak üstünlük iddiası içermez. Bordro ve kurumsal kaynak planlama paketlerinin teşvik modülleri ileriye dönük aylık hesabı yapmakta, ancak tek sürümlü kural tablosuyla çalıştıkları için geçmiş bir dönemi kendi kural sürümüyle yeniden kuramamaktadır. Yurt dışındaki Ar-Ge vergi teşviki otomasyon ürünleri kendi ülke mevzuatlarına özgüdür. Projenin rekabet konumu dört dayanağa oturur: gerçek dönem verisiyle doğrulanmış deterministik hesap çekirdeği, zaman-farkındalıklı kural katmanı, iki rejimi bir arada yürüten kuruluşlarda rejim sınırı ve mükerrer yararlanma denetimi, ve verinin kurum dışına çıkmadığı kapalı devre çalışma modeli.

## Fikri Sınai ve Mülkiyet Hakları

| Başvuru/Yayın Numarası | Belge Adı | Koruma Tipi |
|---|---|---|
| *(planlanan)* | "Denetci" marka tescil başvurusu | Marka |
| *(değerlendirilecek)* | Üç eksenli yürürlük tarihli kural sürümleme ve fark kök-neden teşhis yöntemi | Patent (ön değerlendirme ay 9) |

Projede geliştirilen tüm yazılım, veri modelleri ve yöntemlerin fikri hakları firmamıza aittir; proje öncesinde firma bünyesinde geliştirilen hesap çekirdeği başlangıç varlığı olarak beyan edilir.

## Alınan Ar-Ge Destekleri

| Kurum Adı | Destek Tipi | Destek Dönemi |
|---|---|---|
| *(beyan edilecek)* | — | — |

## Projeye Ait Ürünler

| Ürün Adı | Ürün Tipi |
|---|---|
| Denetci Masaüstü — 5746 ve 4691 kural setleriyle **cari dönem bağımsız kontrol hesabı** (her bordro döneminde, tahakkuk kesinleşmeden fark raporu), mevzuat maddesi atıflı raporlama, 12 aylık teşvik projeksiyonu; geçmiş beyan mutabakatı, kök-neden teşhisi, mühürlü baz ve denetim savunma dosyası yetenekleri personel kademesine göre açılır | Yazılım — masaüstü uygulama |
| Mevzuat güncelleme aboneliği — elektronik imzalı çevrimdışı kural paketleriyle dağıtım | Hizmet — abonelik |
| Geçmiş dönem mutabakat hizmeti — 12-24 dönemlik retroaktif yeniden hesap ve YMM eşliğinde kapanış raporu | Hizmet — proje bazlı |

*Sipariş formu iki satırdır: (1) yıllık lisans + güncelleme aboneliği, (2) geçmiş dönem mutabakat hizmeti. Yetenek kademeleri ayrı ürün olarak satılmaz.*

## Proje Ekipman Listesi

| Ekipman | Adet | Amaç |
|---|---|---|
| Geliştirici iş istasyonu | 3 | Yazılım geliştirme |
| Referans test bilgisayarı (asgari sistem: 4 çekirdek, 16 GB bellek, grafik işlemcisiz) | 2 | Ürünün hedef donanımda doğrulanması ve kapalı devre kurulum senaryolarının sınanması (ağdan yalıtılmış ortam sanal makineyle karşılanır) |

## Başvuru Ekleri

| Ek | İçerik |
|---|---|
| **EK-1** | Rekabet analizi — incelenen ürün listesi, tarama yöntemi ve karşılaştırma ölçütleri |
| **EK-2** | Pilot kuruluşlardan alınacak niyet mektupları (iki adet; şablon ve toplama süreci) |
| **EK-3** | Personel birim maliyeti dayanağı — ekip kıdem dağılımı ve maliyet kırılımı |
| **EK-4** | Proje ekibi ve özgeçmişler — roller, efor dağılımı ve nitelik beyanı |
| **EK-5** | Firma tanıtım dosyası, referanslar, mali tablolar ve proje finansman beyanı |

---

### Portala Aktarım Öncesi Düzeltilecek Kayıtlar *(bu bölüm forma aktarılmaz)*

1. "Projenin Sektörü" alanı portalda **"Ambalaj"** görünmektedir → **"Yazılım"** olarak düzeltilmelidir.
2. Kimlik alanlarındaki süre/bütçe/iş gücü değerleri sıfır görünmektedir → 9 ay, 7.500.000 ₺, 19 + 6 = 25 adam/ay olarak girilmelidir *(25 adam/ay, portaldaki mevcut taahhütle örtüşmektedir)*.
3. "Toplam Personel: 2" ve "Kiralanan Alan: 10 m²" kayıtları proje ekibiyle (5 kişi) çelişmektedir → personel kaydı güncellenmeli, alan ihtiyacı gözden geçirilmelidir. Hakem heyetinin ilk bakacağı tutarlılık noktalarındandır.
4. Rekabet analizinde atıf yapılan "incelenen ürün listesi" eki hazırlanmalıdır (ürün adları, inceleme tarihi, kaynak bağlantıları).
