# HAKEM SUNUMU: Denetci.AI

*İstanbul Medeniyet Üniversitesi Teknopark A.Ş. proje değerlendirme sunumu. Kaynak belge: `denetci-proje-bilgi-formu.md`. Akademik künyeler: `ek-7-akademik-kaynakca.md`. Hakem sorularına hazırlık: `hakem-sunumu-soru-cevap.md`.*

---

## Sunum hakkında

**12 slayt, hedef süre 12-15 dakika + soru-cevap.** Onunda gerçek bir şema vardır; şemalar süsleme değil, sözle anlatılması uzun süren mekanizmaları gösterir.

**Slayt metni bilerek azdır.** Her slaytta bir iddia, bir şema ve en fazla iki satır bulunur. Ayrıntının tamamı konuşma metnindedir. Hakem heyeti slaytı okurken konuşmacıyı dinleyemez; ikisinden birini seçer.

**Dört araştırma sorusu dört slayttadır** (5-8) ve her birinin altında aynı yerde duran bir *başarısızlık eşiği* şeridi vardır: eşik tutmazsa soru olumsuz sonuçlandı diye raporlanır, eşik değiştirilmez.

**Kesilen içerik silinmedi.** Önceki 21 slaytlık sürümdeki ekip matrisi, bütçe kırılımı, rekabet analizi, veri yönetimi ve teknopark katkısı ya bu 12 slayda sıkıştırıldı ya da aşağıdaki yedek slayt listesine taşındı. Soru gelirse açılır.

---


## Slayt 1 — Denetci.AI

*01 · İstanbul Medeniyet Üniversitesi Teknopark · Proje değerlendirme*

- **FirmaARGELOG A.Ş.:** 
- **Proje koduARGELOG-002:** 
- **Süre12 ay:** 
- **İş gücü39 adam-ay · 4 kişi:** 
- **Bütçe7.000.000 ₺:** 
- **Kapsam5746 · 4691:** 
- **HazırlıkTHS 5 → 7:** 

**Konuşma metni:**
> Projemizin adı Denetci.AI. Mimarinin teknik adı nöro-sembolik: sembolik taraf kurallarla kesin hesap yapan bir motor, nöral taraf öğrenen bir dil modeli. İkisini tek sistemde birleştiriyoruz.
>
> Tek cümle: hesabı motor yapar, bulguyu model inceler, kararı insan verir. Motor, Ar-Ge ve teknopark teşvik beyanlarını o dönemde yürürlükte olan mevzuatla bağımsız yeniden hesaplar. Yanına, bulunan farkı bir denetçi gibi inceleyen, kurum içinde çalışan küçük bir model koyuyoruz.
>
> Dört araştırma sorumuz var; slaytlarda AS-1'den AS-4'e kısaltacağım. Üçü yapay zekâ bileşenine, biri onun dayandığı kural tabanına ait.


---

## Slayt 2 — Geçmiş dönem, kendi kural sürümüyle yeniden kurulamıyor

*02 · Problem*

**Şema.** Elektronik tabloda tek kural sürümü tüm dönemleri besler ve değişiklikte üzerine yazılır; Denetci.AI'da her dönem kendi mühürlü kural sürümüne bağlıdır.

*Şema altı:* Elektronik tablo tek sürüm tutar ve değişiklikte üzerine yazar; bu yüzden kapanmış bir dönem denetimde yeniden üretilemez. Ürünün sembolik katmanı her döneme kendi kural sürümünü bağlar.

- 1.720 Ar-Ge ve Tasarım Merkezi, 113 bölgede 13.452 firma; personel başına yıllık ~1 mn ₺ teşvik
- Farkı yorumlayacak, sorgulayacak ve kanıt isteyecek uzman emeği kıt ve pahalı

*T.C. Sanayi ve Teknoloji Bakanlığı istatistikleri, Haziran ve Ağustos 2026.*

**Konuşma metni:**
> Türkiye'de 1.720 Ar-Ge ve Tasarım Merkezi, 13.452 teknopark firması var. Her biri her ay bordroyla iç içe geçmiş teşvik hesapları yapıyor. Bir Ar-Ge personeli başına yıllık teşvik yaklaşık bir milyon TL; 150 kişilik bir merkezde yılda yüz milyon TL düzeyinde bir akış.
>
> Üstteki şema sorunun birinci yarısı. Elektronik tablo tek sürüm tutuyor; oran değişince üzerine yazıyor. Üç yıl önceki bir rakamın hangi mevzuat sürümüyle kurulduğunu gösteren kayıt kalmıyor. Denetime girdiğinizde o rakamı savunacak belgeniz yok. Alttaki şerit bizim yaptığımız şey: her dönem kendi kural sürümüne bağlı kalıyor.
>
> Sorunun ikinci yarısı daha önemli. Bir fark bulunduğunda onu yorumlamak, doğru soruyu sormak ve hangi belgeye bakılacağını belirlemek tamamen uzman emeğine bağlı. Bu emek kıt, pahalı ve ölçeklenemez.


---

## Slayt 3 — Yapay zekâ evet, hesaplayıcı koltuğunda değil

*03 · Tasarım kararı*

**Şema.** Ölçülmüş dayanaksız yanıt oranları: Llama 2 %88, ChatGPT-4 %58, hukuka özel ticari araçlar %17 ile 33 arası, projenin hedef eşiği yüzde 1 veya altı.

*Şema altı:* Hukuk alanında ölçülmüş oranlar. Erişim destekli ticari araçlar oranı düşürüyor ancak ortadan kaldırmıyor; alt şerit projenin kendine koyduğu eşiktir.

- Halüsinasyon giderilebilir bir arıza değil; ölçme biçiminin yapısal sonucu
- Bir tutarın yüzde on yedi ihtimalle uydurma olması denetim ortamında kabul edilemez
- Karar: modelin rolü daraltıldı. Hesap yapmaz, karar vermez

*Dahl vd. 2024, Journal of Legal Analysis; Magesh vd. 2025, Journal of Empirical Legal Studies; Kalai vd. 2026, Nature. Künyeler EK‑7.*

**Konuşma metni:**
> Projenin en kritik tasarım kararı bu. Stanford ekibinin 2024 ölçümü, gerçek mahkeme kararları hakkında doğrulanabilir sorular sorulduğunda ChatGPT-4'ün yüzde 58, Llama 2'nin yüzde 88 oranında dayanaksız yanıt ürettiğini gösterdi.
>
> "Hukuka özel araç kullanırız" diyebilirsiniz. Aynı ekibin 2025 çalışması, alanın en pahalı ticari erişim destekli araçlarında bile oranın yüzde 17 ile 33 arasında kaldığını ölçtü. Ve bu giderilebilir bir hata değil: bu yıl Nature'da yayımlanan çalışma, halüsinasyonun istatistiksel bir zorunluluk olduğunu gösteriyor.
>
> Bizim alanımızda bir tutarın yüzde on yedi ihtimalle uydurma olması kabul edilemez. Bu yüzden yapay zekânın rolünü bilinçli olarak daralttık. En alttaki şerit bizim eşiğimiz; nasıl tutturacağımızı yedinci slaytta anlatacağım.


---

## Slayt 4 — Hesabı motor yapar, kararı insan verir

*04 · İş bölümü*

**Şema.** Motor farkı üretir, model bulguyu inceler, doğrulama kapısı atıfları denetler, insan karar verir ve getirilen belgeyle motor yeniden koşar. Modelden tutara giden bir yol yoktur.

*Şema altı:* Çarpı işaretli kesik çizgi projenin taşıyıcı tercihidir: modelden tutara giden bir yol yoktur. Bu nedenle modelin yanılması hatalı bir tutar değil, gereksiz bir inceleme adımı üretir.

- Ayrım kod düzeyinde kurulu ve denetim iziyle kanıtlanabilir
- YMM'nin tasdik yetkisi ve sorumluluğu değişmez; ürün beyan üretmez, göndermez, tasdik etmez

**Konuşma metni:**
> İş bölümümüz şu. Motor hesaplar. Bulduğu farkı model inceler: bu fark ne anlama geliyor, hangi kural sürümünün uygulanmamasıyla tutarlı, bir denetçi burada ne sorardı, hangi belgeyi istemeli. Kapı modelin her atfını kural tabanına karşı doğrular. İnsan karar verir. Getirilen belgeyle motor yeniden koşar ve döngü kapanır.
>
> Şemadaki çarpı işaretli kesik çizgi bu sunumun en önemli detayı: modelden tutara giden bir yol yok. Model bir hata yaparsa sonuç yanlış bir tutar değil, gereksiz bir inceleme adımıdır.
>
> Literatürde bu yaklaşımın adı var. Program destekli dil modelleri çalışması, modelin problemi doğru parçalasa bile hesap adımında hata yaptığını, hesabı deterministik bir yürütücüye devretmenin bu hatayı ortadan kaldırdığını gösteriyor. Kambhampati ve arkadaşları da dil modellerinin kendilerini doğrulayamadığını, ancak dış doğrulayıcılarla çevrelendiklerinde değerli olduklarını söylüyor. Kapımız tam olarak böyle bir dış doğrulayıcı.


---

## Slayt 5 — Denetçi rolü, motorun kendi çıktısıyla öğretilebilir mi?

*05 · Araştırma Sorusu 1*

**Şema.** Senaryo, enjeksiyon ve pilot verisi motordan geçer, fark imzası ve kural sürümü üretir, buradan eğitim çiftleri çıkar; araştırma yönlendirme görevinde etiketi motorun yeniden koşumu otomatik olarak koyar.

*Şema altı:* Etiketin kaynağı model değil, 96 gerçek dönemde kuruş farksız doğrulanmış motordur. Özyineleme olmadığı için sentetik veriyle eğitimin bilinen çöküş mekanizması bu hatta oluşmaz.

- Hacim: ≥60 senaryodan ~2.000-3.000, ≥400 vakadan ~1.500-2.500 örnek; pilot başına ≥200 gerçek fark kalemi

> **Başarısızlık eşiği · ay 10 ve 12Yönlendirme isabeti ≥ %70  |  ince ayarsız temel modele karşı ≥ 15 puan**
> Uzmanın bulgularının ≥ %80'i yakalanır  |  soru nitelenme oranı ≥ %70

**Konuşma metni:**
> Birinci araştırma sorusu: bir denetçinin ön inceleme işi küçük ve yerel bir modele öğretilebilir mi? Asıl zorluk eğitim verisi. Bu göreve klasik anlamda etiketli veri üretmek mümkün değil; uzmanın binlerce örneği elle etiketlemesi gerekirdi.
>
> Yaklaşımımız şemada. Doğrulanmış motoru referans kaynağı olarak kullanıyoruz. En güçlü olduğumuz yer alttaki geri dönüş oku: araştırma yönlendirme görevinde etiket bir yargı değil, mekanik bir olgu. Önerilen belgeyi getir, motoru yeniden koş, fark kapandı mı kapanmadı mı.
>
> Sentetik veri riskini biliyoruz. Nature'daki çalışma, modelin kendi ürettiği veriyle özyinelemeli eğitilmesinin geri dönüşsüz çöküşe yol açtığını gösterdi. Bizde özyineleme yok: veriyi model değil, doksan altı gerçek dönemde kuruş farksız doğrulanmış motor üretiyor.


---

## Slayt 6 — Dayanaksız iddia kullanıcıya hiç ulaşmaz

*06 · Araştırma Sorusu 2*

**Şema.** Model bulguları doğrulama kapısında iki soruya tabi tutulur; geçenler kullanıcıya gider, elenenler ince ayara olumsuz örnek olarak döner.

*Şema altı:* Kapı hiçbir tutarı gizlemez: motorun bulduğu fark her koşulda kullanıcıya gider. Elenen şey tutar değil, modelin o fark üzerine yazdığı yorumdur.

- Dil modelleri kendi akıl yürütme hatasını düzeltemez; doğrulama dışsal ve sembolik olmalı. Kapının haklı bulguyu eleme oranı da ayrıca ölçülür

> **Başarısızlık eşiği · ay 10Atıf doğruluğu ≥ %98  |  desteksiz iddia ≤ %1**
> 

**Konuşma metni:**
> İkinci soru: küçük bir modelin ürettiği gerekçeler sembolik bir kural tabanına karşı doğrulanarak kanıta bağlı tutulabilir mi?
>
> Modelin her çıktısı şema zorlamalı üretiliyor ve içindeki her atıf kapıda iki soruya tabi tutuluyor: bu madde var mı, ve o dönemde yürürlükte miydi. Karşılığı olmayan bulgu kullanıcıya ulaşmadan eleniyor; eleme kaydı da bir sonraki ince ayar turuna olumsuz örnek olarak dönüyor. Alttaki kesik ok bu.
>
> Neden model bunu kendi kendine yapamıyor? Çünkü yapamadığı ölçüldü. Huang ve arkadaşlarının ICLR 2024 çalışması, dil modellerinin dışarıdan geri bildirim almadan akıl yürütme hatalarını düzeltemediğini, hatta denemenin çoğu kez performansı düşürdüğünü gösterdi. Bir noktayı kendim söyleyeyim: kapı doğru bulguları da eleyebilir ve bunu ölçmeyi taahhüt ediyoruz. En kötü sonucu, kullanıcının bugünkü gibi yorumsuz bir farkla kalmasıdır.


---

## Slayt 7 — Farkı bulmak kolay, nedenini atamak zor

*07 · Araştırma Sorusu 3*

**Şema.** Tek bir fark tutarı yedi ayrı kök nedenle açıklanabilir; sembolik katman bu kümeyi eksiksiz üretir, nöral katman sıralar ve kanıt belgesi ister, ayırt edilemeyen kalem belirsiz olarak raporlanır.

*Şema altı:* Klasik bir tanımlanabilirlik problemi: yedi neden matematiksel olarak aynı fark görüntüsünü üretir. Sembolik katman doğruluğu, nöral katman verimliliği taşır. Ayırt edilemeyen kalem tek nedene zorlanmaz.

- İki metrik farklı paydadadır ve bilerek kilitlidir: zor vakaları belirsize atmak tutar payını şişirir

> **Başarısızlık eşiği · ay 10 ve 12Kalem bazında ≥ %85  |  ilk üç hipotezde ≥ %90  |  belirsiz tutar payı ≤ %5**
> 

**Konuşma metni:**
> Üçüncü soru teşhisle ilgili. Farkı bulmak deterministiktir; iki sayıyı çıkarırsınız. Asıl belirsizlik farkın nedenine güvenilir biçimde atanmasında.
>
> Şemadaki yelpaze problemi anlatıyor: tek bir fark tutarını yedi ayrı kök neden matematiksel olarak açıklayabilir. Bu klasik bir tanımlanabilirlik problemidir ve yapay zekâda kırk yıllık bir literatürü var. Reiter'ın birinci ilkelerden teşhis kuramı, teşhisi tek bir tahmin değil aday kümelerinin tümünün hesaplanması olarak tanımlar. de Kleer ve Williams bir adım daha atar: adayları en çok ayrıştıracak bir sonraki ölçüm hangisidir? Bizim "hangi belgeyi istemeli" görevimiz tam olarak budur.
>
> Bir soruyu ben sorayım: zor vakaların hepsini belirsiz etiketleyip yüzde 85'i kolayca tutturamaz mısınız? İki metriği bilerek birbirine kilitledik. Doğruluk kalem bazında, belirsiz payı tutar bazında ölçülüyor ve tavanı yüzde beş.


---

## Slayt 8 — Her dönem kendi kuralıyla, üç ayrı eksende

*08 · Araştırma Sorusu 4*

**Şema.** Parametre, hesap şeması ve bilgi tarihi eksenleri ayrı ayrı sürümlenir; as-of kesiti üç eksenden o tarihte geçerli olan sürümü seçer.

*Şema altı:* Üç eksen birbirinden bağımsız sürümlenir. Kapanmış bir dönemi yeniden üretmek, üç eksenin kesişiminden o tarihte geçerli olan sürümü seçebilmektir; bu alanda hazır bir çözümü bulunmayan bir bilgi temsili problemidir.

- Sorunun ikinci yarısı: rejime özgü mantığın ne kadarı kural dosyasına taşınabilir? 4691 sınama alanıdır ve iki rejim bir aradaysa aralarındaki sınır da denetlenmelidir

> **Başarısızlık eşiği · ay 7 ve 8YMM teyitli gerçek çapa 96 → ≥ 140  |  oranı doğrulanmamış ay için ne hesap ne rapor üretilir**
> 4691 kurallarının ≥ %90'ı kod yazılmadan tanımlanmalı  |  kaçış ≤ 3

**Konuşma metni:**
> Dördüncü soru, modelin dayanacağı kural tabanıyla ilgili. Modelin her atfının doğrulanabilmesi, kural tabanının her dönem için o gün yürürlükte olan kuralı kesin olarak bilmesini gerektiriyor.
>
> Şemadaki üç şerit üç ekseni gösteriyor. Üstteki kolay: oran değişiklikleri. Ortadaki zor, çünkü hesaba giren büyüklüğün tanımını değiştiriyor. İki somut örnek: 2022'de asgari geçim indiriminin kaldırılması ücret istisnası matrahının tanımını değiştirdi; 7555 sayılı düzenlemenin ücret tavanı 1 Ağustos 2025'te ay ortasında yürürlüğe girip dönem anahtarının kendisini kırdı. Alttaki eksen bilgi tarihi: düzeltme beyannameleri aynı döneme birden çok geçerli sürüm yaratır.
>
> Dikey kesik çizgi as-of kesiti. Bu problemin veritabanı literatüründe adı var ve SQL 2011 standardında dilin içine alınmış durumda; bizim katkımız üç ekseni bir teşvik rejiminin hesap mantığıyla birleştirmek. Son olarak: yeni bir tebliğ çıkarsa modeli yeniden eğitmiyoruz. Model oran ve limit taşımıyor, yeni tebliğ yeni bir kural dosyasıdır.


---

## Slayt 9 — Beş karşılaştırma kolu, mühürlü eşik

*09 · Ölçüm düzeneği*

**Şema.** Aynı kör test seti beş kolda koşulur: ince ayarlı model, ince ayarsız model, erişim destekli kol, alan dışı genel model ve uzman denetçi.

*Şema altı:* Üçüncü kol, "neden erişim destekli üretim yetmiyor da ince ayar gerekiyor" sorusunun cevabını tahmine değil ölçüme bağlar. AS-3 için ayrıca kural tabanlı bir sembolik taban çizgisi koşulur.

| Soru | Eşik | Ay |
|---|---|---|
| AS-1 | Yönlendirme ≥ %70; temel modele karşı ≥ 15 puan; uzman bulgularının ≥ %80'i | 10, 12 |
| AS-2 | Atıf doğruluğu ≥ %98; desteksiz iddia ≤ %1 | 10 |
| AS-3 | Kalem bazında ≥ %85; ilk üçte ≥ %90; belirsiz tutar ≤ %5 | 10, 12 |
| AS-4 | Çapa 96 → ≥ 140; kural dosyasıyla kapsama ≥ %90; kaçış ≤ 3 | 7, 8 |

> **Ön kayıtEşikler ve kör test seti ay 7'de mühürlenip TTO ve YMM nezdinde saklanır.**
> Ölçümden sonra ne eşik ne payda değişir. Sızıntı kontrolü EK‑6 §4'te yazılıdır.

**Konuşma metni:**
> Bir yapay zekâ iddiası ancak ölçüm düzeneği kadar değerlidir; bu yüzden en çok emeği buraya verdik. Aynı kör test seti beş kolda koşuluyor. Üçüncü kol özellikle önemli: kural tabanını bağlam olarak alan erişim destekli kol. Böylece "neden ince ayar gerekiyor" sorusunun cevabı tahmin değil ölçüm oluyor.
>
> Tablodaki dört eşiğin her biri düşebilir, yani yanlışlanabilir. Bir örnek vereyim: yüzde 70 yönlendirme isabeti literatürden alınmış bir sabit değil. Rastgele taban yüzde 20 ile 33 arası; yüzde 70 bunun iki ila üç buçuk katı. İkinci gerekçe işin ekonomisi ve bunu varsayım olarak etiketliyoruz, pilotlarda ölçeceğiz.
>
> En önemli taahhüdümüz alttaki şerit: bütün eşikler ve kör test seti yedinci ayda mühürlenip Teknoloji Transfer Ofisi ile YMM nezdinde yazılı olarak saklanacak. Ölçümden sonra ne eşiği ne paydayı değiştiririz.


---

## Slayt 10 — Yedi iş paketi, beş ölçüm kapısı

*10 · İş planı*

**Şema.** On iki aylık takvimde yedi iş paketi ve ay 7, 8, 10, 11, 12'deki ölçüm kapıları.

*Şema altı:* Koyu şerit İP5'tir: projenin yapay zekâ ekseni, 10 adam-ay. Kritik yol İP2'nin ay 7 kural tabanı kapısından ve İP4'ün ay 8 senaryo setlerinden geçer. Sağdaki sayılar adam-aydır; toplam 39.

| Ekip · 4 kişi | Adam-ay | Bütçe · 7.000.000 ₺ | Pay |
|---|---|---|---|
| Proje yöneticisi | 6 | Proje personeli · 39 × 130.000 ₺ | %72 |
| Kıdemli geliştirici | 12 | YMM hizmeti · kural teyidi, uzman etiketleme | %8 |
| Yapay zekâ mühendisi | 12 | Donanım · 3 iş istasyonu, 2 referans makine | %4 |
| Analiz ve test uzmanı | 9 | Patent, marka, akademik danışmanlık | %4 |
| Toplam · 3,25 TZE | 39 | Seyahat, bulut GPU, lisans, sarf, öngörülemeyen | %12 |

- 31 adam-ay Ar-Ge, 8 adam-ay geliştirme; hesap çekirdeği proje öncesinde geliştirildi ve başlangıç varlığı olarak beyan edildi

**Konuşma metni:**
> Yedi iş paketi, her birinin adam-ayı, ayı ve çıkış kriteri yazılı. Koyu şerit İP5, yani projenin yapay zekâ ekseni: 10 adam-ay, ay 6'dan 12'ye. Kritik yol İP2'nin yedinci aydaki kural tabanı kapısından ve İP4'ün sekizinci aydaki senaryo setlerinden geçiyor.
>
> Açıkça söylemem gereken bir şey var: deterministik hesap çekirdeği proje öncesinde firmamızda geliştirildi ve doksan altı çapa testiyle iç doğrulaması tamamlandı. Bunu başlangıç varlığı olarak beyan ettik. "O zaman Ar-Ge içeriği daralmıyor mu" diye sorabilirsiniz; tersi oluyor. Çalışan bir motorun üzerine kurduğumuz için Ar-Ge eforunun on dokuz adam-ayını doğrudan yapay zekâ bileşenine ayırabiliyoruz.
>
> Bütçenin yüzde 72'si personel; donanım payı yüzde dört. Bu bir ekipman alma projesi değil. YMM kalemi projenin ölçüm altın standardını üretiyor: kural setlerinin madde teyidi, parametre tablosunun doğrulanması, pilot mutabakat denetimi ve kör değerlendirmede uzman etiketleme.


---

## Slayt 11 — Başarısızlık hatalı tutar üretmez

*11 · Risk*

**Şema.** Model yanıldığında sonuç yalnızca gereksiz bir inceleme adımıdır ve tutar değişmez; motorun parametresi doğrulanmamışsa sert kural hesabı ve raporu tamamen durdurur.

*Şema altı:* Asimetri tasarım tercihidir. Nöral katmanın hatası ilerler ama zarar vermez; sembolik katmanın teyitsizliği hiç ilerlemez. Doğruluğu model değil motor taşıdığı için ürün, araştırma sorusu düşse bile çalışır.

- AS-1 tutmazsa olumsuz sonuçlu araştırma sorusu olarak raporlanır; ürün sembolik katmanla eksiksiz çalışır

**Konuşma metni:**
> Hakem heyetinin haklı olarak soracağı soru şu: yapay zekâ bileşeni hedefe ulaşamazsa yedi milyon TL boşa mı gitmiş olur?
>
> Cevap hayır ve nedeni şemada. Üstteki hat: model yanılırsa sonuç yanlış bir tutar değil, gereksiz bir inceleme adımıdır; tutar değişmez. Alttaki hat: motorun parametresi doğrulanmamışsa sert kural devreye girer ve o ay için ne hesap ne rapor üretilir. Bu bir uyarı değil, motorun içine gömülü bir engel.
>
> AS-1 tutmazsa bunu olumsuz sonuçlu bir araştırma sorusu olarak, veri kaynağı ve hacim etkisi ölçümleriyle birlikte raporlarız; bu da bilimsel bir çıktıdır. Ürün ise sembolik katman üzerinden eksiksiz çalışmaya devam eder: geçmiş dönem mutabakatı, kök-neden teşhisi, mühürlü baz, denetim savunma dosyası ve cari dönem kontrolü modele bağlı değil.


---

## Slayt 12 — Geriye ne kalacak

*12 · Kapanış*

| # | Çıktı | Kanıtı |
|---|---|---|
| 1 | Doğrulanmış zaman-farkındalıklı kural tabanı | YMM teyitli gerçek çapa 96 → en az 140; 5746 ve 4691 kural setleri |
| 2 | Denetçi model ve ölçüm düzeneği | Yönlendirme ≥ %70, atıf ≥ %98, grafik işlemcisiz çalışır |
| 3 | THS 7 prototip, iki referans vaka | Tüpraş ve Kale Seramik'te ücretli pilot; yazılı ihtiyaç görüşleri alındı |
| 4 | Fikri mülkiyet | Marka başvurusu; ay 9'da patentlenebilirlik ön değerlendirmesi |

- TTO'dan talebimiz: yapay zekâ tarafında akademisyen danışmanlığı; ay 7 ve ay 10'da bağımsız gözden geçirme
- Bölgeye taahhüdümüz: 4 kişiyle başlayıp 6; beş bölge firmasına 4691 ön sürümü; iki seminer; ortak bildiri

**Konuşma metni:**
> Toparlayayım. Proje sonunda geriye dört somut şey kalacak. Doğrulanmış, zaman-farkındalıklı bir kural tabanı; denetçi rolündeki yerel model ve onu ölçen düzenek; iki sanayi kuruluşunda gerçek veriyle çalışan bir prototip; ve fikri mülkiyet.
>
> İkincisini vurgulamak istiyorum: ölçüm düzeneği modelin kendisi kadar önemli, çünkü bu alanda eksik olan şey model değil, ölçüm.
>
> Neden teknoparkta? Üç şey aynı anda burada: 4691 kural setinin ilk kullanıcıları, yapay zekâ tarafındaki akademik danışmanlık, ve ölçümlerimizi gözden geçirecek bağımsız göz. Ölçümü yapan taraf olarak bağımsız gözden geçirmeyi kendi lehimize değil, sonucun güvenilirliği için istiyoruz.
>
> Son cümlem şu: araştırma sorusu düşerse bile ürün çalışır, çünkü doğruluğu model değil motor taşıyor. Hesabı motor yapar, bulguyu model inceler, kararı insan verir. Teşekkür ederim.


---


# YEDEK SLAYTLAR

*Soru-cevapta açılmak üzere hazırlanır; ana akışta gösterilmez. Kaynakları ana belge ve eklerdir.*

| # | Yedek slayt | Hangi soruya cevap verir |
|---|---|---|
| Y1 | EK-4 kişi × iş paketi efor matrisi (satır 6/12/12/9, sütun 3/6/3/9/10/5/3) | "Bu işi kim yapacak, yapabilecek mi?" |
| Y2 | Bütçenin dokuz satırı, portal harcama kategorileriyle | "7 milyon TL neye gidiyor?" |
| Y3 | EK-1 rekabet karşılaştırma tablosu (Ö1-Ö4) | "Rakipler bunu yapmıyor mu?" |
| Y4 | Veri yönetimi: veri sorumlusu/işleyen, KVKK dayanağı, imha | "Bordro verisini hangi dayanakla işliyorsunuz?" |
| Y5 | Sorumluluk ve insan gözetimi: lisans sözleşmesi, arayüz kısıtı | "Yanlış beyan verilirse sorumlu kim?" |
| Y6 | Ekonomik değerin dört kanalı ve fiyat bandı | "Müşteri bunu neden ödesin?" |
| Y7 | Risk tablosu: yedi risk, erken uyarı ve önlem | "Ya gecikirse, ya pilot düşerse?" |
| Y8 | EK-6 veri hattı ve hacim tablosu | "Kaç örnekle eğitiyorsunuz?" |
| Y9 | 96 çapanın yıl × rejim × kalem kapsama matrisi | "Motor da bir yazılım, nasıl güveniyorsunuz?" |
| Y10 | Örneklem büyüklüğü ve istatistiksel test planı | "15 puanlık fark anlamlı mı?" |
| Y11 | Dört kapılı pilot akışı ve yedek pilot planı | "Pilotlar gerçekten olacak mı?" |
| Y12 | THS bileşen tablosu ve THS 7 kabul kanıtı | "Neden 5'ten 7'ye?" |

---


# SUNUM ÖNCESİ KARAR BEKLEYEN MADDELER

*Aşağıdaki maddeler sunum metninde yer alıyor ancak başvuru dosyasında henüz karşılığı yok ya da düzeltilmesi gereken bir kayıt var. Sunum günü çelişki üretmemesi için önceden karara bağlanmalıdır.*

## A. Dosyaya eklenmesi gereken taahhütler

| # | Sunumdaki ifade | Durum | Yapılacak |
|---|---|---|---|
| A1 | Kör setin bir kısmının **iki bağımsız YMM** tarafından etiketlenmesi ve uyum katsayısının (Cohen kappa) raporlanması. 12 slaytlık sürümde taahhüt olarak yer almaz; soru-cevap bankasında S8'de geçer | EK-6 §6 tek etiketleyici varsayıyor; 550.000 ₺'lik YMM kalemi buna göre kurulmuş | Taahhüt edilecekse EK-6 §6'ya ikinci etiketleyici eklenir ve YMM kalemi gözden geçirilir; edilmeyecekse S8 cevabından çıkarılır |
| A2 | **Beş karşılaştırma kolu** (erişim destekli kol ve sembolik taban çizgisi dâhil); slayt 9'da şema olarak gösteriliyor | Formda üç kol var: ince ayarlı, ince ayarsız, alan dışı | Formdaki Kazanım 1'e iki kol eklenmeli ya da slayt 9 üç kola indirilmeli |
| A3 | **Ay 2-4 fizibilite ölçümü ve karar kapısı** | Formda yok | İP5 tanımına eklenebilir; eklenmezse sunumda "planlıyoruz" olarak söylenir |
| A4 | **Eşiklerin ay 7'de mühürlenmesi** ve TTO/YMM nezdinde saklanması | Formda yok | TTO'dan talep edilen hizmetlere eklenebilir |
| A5 | **Ezberleme sınaması** ve dağıtılan model ağırlıklarının kuruluştan arındırılması | Formda ve EK-6'da yok | EK-6 §4'e eklenmesi önerilir; pilot kuruluşun hukuk birimi bunu soracaktır |
| A6 | **Bölgeye taahhütler** (6 kişi istihdam, 5 bölge firması, 2 seminer) | Formda yok | Taahhüt edilecekse forma işlenmeli; edilmeyecekse sunumdan çıkarılmalı |
| A7 | **Kaynak dönem kesişim taraması, karıştırılmış etiket kontrol koşumu ve tamamen kör tutulan bir pilot** | EK-6 §4 bu üç kontrolü içermiyor; "tamamen kör pilot" ise EK-6 §5 takvimiyle çelişiyor (ay 11'de her iki pilotun eğitim kısmı kullanılıyor) | Taahhüt edilecekse EK-6 §4 ve §5 buna göre güncellenmeli. Sunumdan çıkarıldı; slayt 9 doğrudan EK-6 §4'e atıf yapar, soru-cevap bankasında S10 da EK-6'ya indirildi |

## B. Düzeltilmesi gereken kayıtlar

| # | Sorun | Yapılacak |
|---|---|---|
| B1 | Portal kaydında "Toplam Personel: 2" yazıyor; ekip 4 kişi | Portalda 4'e çekilmeli. Heyet portal çıktısını ekranla karşılaştırabilir |
| B2 | Portal kaydında "Kiralanan Alan: 10 m²"; 4 kişide kişi başına 2,5 m² düşüyor | Alan ihtiyacı gözden geçirilmeli |
| B3 | Formda kural tabanı kapsamı "2019-2026"; proje 26.10.2026-25.10.2027 arası yürüyor ve ay 11'de cari dönem kontrolü yapılacak | Kapsam "2019'dan cari döneme" olarak düzeltilmeli; aksi hâlde 2027 dönemleri, formun kendi sert kuralı gereği hesaplanamaz |
| B4 | Formda "yedi ürün/hizmet kategorisi tarandı" deniyor ama beş kategori listeleniyor; EK-1'in yedi satırı bunlardan yalnızca dördüne karşılık geliyor | Formda "yedi ürün tarandı, dört rakip sınıfında toplandı; beşinci sınıf (genel amaçlı bulut araçları) taramaya değil mimari gerekçeye dayanır" biçiminde düzeltilmeli |
| B5 | Formda Tüpraş "aynı il" olarak işaretli | Pilot sahasının ili teyit edilmeli |
| B6 | Slayt 3'teki literatür rakamları (%58, %88, %17-33) formda geçmiyor | **EK-7 bu boşluğu kapatır.** Başvuru dosyasına ek olarak sunulmalıdır |

## C. Sunum öncesi son kontroller

1. **EK-1'i yeniden tara.** Rakip ürün siteleri Ağustos-Eylül 2026'dan bu yana değişmiş olabilir.
2. **EK-1'deki ölçüt sayısını düzelt.** Tabloda dört ölçüt (Ö1-Ö4) var ama metin iki yerde "üç ölçüt" diyor: Yöntem paragrafı ve Değerlendirme maddesi 1. Yedek slayt Y3 bu tabloyu ekrana getirdiği için heyet çelişkiyi görür.
3. **Niyet mektuplarını topla.** Kurumsal imza süreci 2-4 hafta sürüyor.
4. **EK-3'teki tutarları doldur.** Yer tutucu bırakılmış bir maliyet dayanağı, bütçe sorusunda savunulamaz.
5. **EK-4'teki özgeçmişleri doldur;** özellikle "diğer projelerdeki yük" alanını. Bu alan boşsa 39 adam-ay beyanı sorgulanır.
6. **Yapay zekâ mühendisinin istihdam durumunu netleştir.** Yedek slayt Y1'de ve İP5 anlatısında bu satır boş kalmamalı.
7. **Taban model lisansını kayda geçir.** Ticari kullanıma ve türev ağırlık dağıtımına izin veren bir aile seçilmeli; bu, ürünleştirmenin hukuki ön koşuludur.
