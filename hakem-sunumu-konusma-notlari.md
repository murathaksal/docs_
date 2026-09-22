# KONUŞMA NOTLARI: Denetci.AI hakem sunumu

*Sunum günü elde tutulacak teslim metni. Bu notlar sunum destesinin içinde değildir; deste yalnızca slaytları gösterir. Slaytlar: `hakem-sunumu.html`. Zor sorular: `hakem-sunumu-soru-cevap.md`.*

---

## Kullanım

Her slayt dört parça hâlinde verilmiştir:

| Parça | Ne işe yarar |
|---|---|
| **Süre** | Slayt için ayrılan saniye ve kümülatif dakika. Geride kalırsanız nereden kısacağınız yazılıdır |
| **Şemada göster** | Ekrandaki hangi öğeyi işaret edeceğiniz. Şema varken ona bakmadan konuşmayın |
| **Söyle** | Konuşma metni. Ezberlemeyin; yüksek sesle iki kez okuyun, mantığı kalsın |
| **Çıpa cümle** | O slayttan heyette kalması gereken tek cümle. Başka her şey düşse bu düşmemeli |
| **Geçiş** | Sonraki slayta bağlayan cümle. Bu cümleler sunumun omurgasıdır |

**Toplam hedef: 15 dakika 10 saniye.** Soru-cevap için en az 10 dakika bırakın.

**Dil kaydı.** Slayt başlıkları, Proje Bilgi Formu'ndaki araştırma sorusu adlarıyla eşitlenmiştir; hakem elindeki formla ekrandaki başlığı doğrudan eşleştirebilir. Konuşurken de formun terimlerini kullanın: nöro-sembolik mimari, deterministik hesap çekirdeği, zaman-farkındalıklı kural tabanı, sembolik doğrulama kapısı, abdüktif kök-neden teşhisi, denetçi rolündeki dar kapsamlı model. Aynı kavram için ikinci bir isim uydurmayın; heyet bunu tutarsızlık olarak okur.

---

## Sunum öncesi beş dakika

1. **Destede slayt 1'de olduğunuzdan emin olun** (klavye: `Home`). "Tüm slaytlar" ızgarası açıksa `G` ile kapatın.
2. **Bu notlar destede yoktur;** ayrı bir belgedir. Yansıtılan ekranda yalnızca slaytlar görünür, notları ikinci ekranda veya basılı olarak tutun.
3. **Şu üç sayıyı tekrarlayın:** 1.720 merkez · 39 adam-ay · 7.000.000 ₺. Bunlar en sık sorulanlar.
4. **Ekler elinizde olsun:** EK-1 rekabet tablosu, EK-4 efor matrisi, EK-6 veri hattı, EK-7 kaynakça. Heyet dayanak isterse sayfayı açın, anlatmayın.
5. **Son cümleyi bir kez içinizden söyleyin:** "Hesabı motor yapar, bulguyu model inceler, kararı insan verir."

---
---

# SLAYT SLAYT

---

## Slayt 1 — Kapak

**Süre:** 70 sn · toplam 1:10
**Şemada göster:** Önce zaman eğrisi (2013 kuruluş → 2026 Nisan'da doğrulanmış çekirdek → 2027 Ekim'de THS 7), sonra referans kuruluş şeridi. Künye satırında özellikle 12 ay, 39 adam-ay, 7 milyon TL.

**Söyle:**

> Teşekkür ederim. Kısaca kendimizi tanıtayım: ARGELOG, 2013'ten bu yana sanayi kuruluşlarına Ar-Ge, teknoloji ve inovasyon yönetimi yazılımları geliştiriyor ve danışmanlık veriyor. Ekranda gördüğünüz kuruluşlar bugünkü referanslarımız. Bu projenin başlangıç varlığı olan deterministik teşvik hesap motoru bu on üç yıllık saha birikimiyle üretildi; Nisan 2026'da 96 çapa testinin tamamını kuruş farksız geçerek iç doğrulamasını tamamladı. Bugün sizden istediğimiz, o çalışan motorun üzerine yapay zekâ bileşenini kurmak.
>
> Projemizin adı Denetci.AI. Mimarinin teknik adı nöro-sembolik; terimi hemen açayım. Sembolik taraf, kurallarla kesin hesap yapan bir motordur: aynı girdiye her zaman aynı sonucu verir. Nöral taraf ise öğrenen bir dil modelidir. Biz bu ikisini tek sistemde birleştiriyoruz.
>
> Projeyi tek cümleyle anlatayım: hesabı motor yapar, bulguyu model inceler, kararı insan verir.
>
> Dört araştırma sorumuz var; slaytlarda AS-1'den AS-4'e kısaltacağım. Üçü yapay zekâ bileşenine, biri onun dayandığı kural tabanına ait.

**Çıpa cümle:** Hesabı motor yapar, bulguyu model inceler, kararı insan verir.

**Geçiş:** "Önce çözdüğümüz problemi göstereyim."

---

## Slayt 2 — Kapanmış dönem, kendi kural sürümüyle yeniden üretilemiyor

**Süre:** 75 sn · toplam 2:25
**Şemada göster:** Üstteki tek kutuyu ve ondan dört döneme inen okları; sonra kutunun sağındaki kendine dönen oku ("üzerine yazılır"); sonra alttaki dört sürümlü şeridi.

**Söyle:**

> Türkiye'de 1.720 Ar-Ge ve Tasarım Merkezi, 113 bölgede 13.452 firma var. Her biri her ay bordroyla iç içe geçmiş teşvik hesapları yapıyor. Bir Ar-Ge personeli başına yıllık teşvik yaklaşık bir milyon TL mertebesinde; 150 kişilik bir merkezde yılda yüz milyon TL düzeyinde bir akıştan söz ediyoruz.
>
> Üstteki şerit bugünü gösteriyor. Elektronik tablo tek kural sürümü taşıyor ve oran değiştiğinde üzerine yazıyor. Üç yıl önceki bir rakamın hangi mevzuat sürümüyle kurulduğunu gösteren kayıt kalmıyor. Denetime girdiğinizde o rakamı savunacak belgeniz yok.
>
> Alttaki şerit bizim yaptığımız şey: her dönem kendi mühürlü kural sürümüne bağlı kalıyor.
>
> Ama sorunun asıl ağır yarısı bu değil. Bir fark bulunduğunda onu yorumlamak, doğru soruyu sormak ve hangi belgeye bakılacağını belirlemek tamamen uzman emeğine bağlı. Bu emek kıt, pahalı ve ölçeklenemez.

**Çıpa cümle:** Asıl darboğaz hesap değil, farkı yorumlayacak uzman emeği.

**Geçiş:** "Burada akla hemen yapay zekâ geliyor. Ama hangi konumda?"

**Geride kalırsanız:** Pazar sayılarını atlayın, doğrudan şemaya geçin.

---

## Slayt 3 — Mevzuat alanında dil modeli hesap ve karar üretemez

**Süre:** 75 sn · toplam 3:40
**Şemada göster:** Sırayla en uzun çubuğu (%88), sonra %58'i, sonra %17-33 bandını; en son alttaki kısa koyu çubuğu (kendi eşiğimiz).

**Söyle:**

> Bu, projenin en kritik tasarım kararı.
>
> Stanford ekibinin 2024'te Journal of Legal Analysis'te yayımladığı ölçüm, gerçek mahkeme kararları hakkında doğrulanabilir sorular sorulduğunda ChatGPT-4'ün yüzde 58, Llama 2'nin yüzde 88 oranında dayanaksız yanıt ürettiğini gösterdi.
>
> "Genel model kullanmayız, hukuka özel araç kullanırız" diyebilirsiniz. Aynı ekibin 2025 çalışması, alanın en pahalı ticari erişim destekli araçlarında bile bu oranın yüzde 17 ile 33 arasında kaldığını ölçtü.
>
> Ve bu giderilebilir bir hata değil. Bu yıl Nature'da yayımlanan çalışma, halüsinasyonun gizemli bir arıza değil istatistiksel bir zorunluluk olduğunu gösteriyor: modeller, zor bir sınavda boş bırakmak yerine tahmin yürüten öğrenciler gibi, bilmediklerini itiraf etmek yerine tahmin etmeye ödüllendiriliyorlar.
>
> Bizim alanımızda bir tutarın yüzde on yedi ihtimalle uydurma olması kabul edilebilir değil. En alttaki koyu çubuk bizim kendimize koyduğumuz eşik. Bu yüzden yapay zekânın rolünü bilinçli olarak daralttık.

**Çıpa cümle:** Yapay zekâyı hesaplayıcı koltuğuna oturtmuyoruz, çünkü o koltuk ölçülerek savunulamaz hâle geldi.

**Geçiş:** "Peki nereye oturtuyoruz?"

**Dikkat:** Bu slaytta rakam sorulursa kaynak EK-7 bölüm 2'dedir. Hafızadan ek rakam vermeyin.

---

## Slayt 4 — İş bölümü: motor hesaplar, model inceler, insan karar verir

**Süre:** 90 sn · toplam 5:10
**Şemada göster:** Soldan sağa dört kutuyu sırayla; sonra alttaki uzun geri dönüş okunu; **en son ve en uzun süre çarpı işaretli kesik çizgiyi.**

**Söyle:**

> İş bölümümüz şu. Motor hesaplar. Bulduğu farkı model inceler: bu fark ne anlama geliyor, hangi kural sürümünün uygulanmamasıyla tutarlı, bir denetçi burada ne sorardı, hangi belgeyi istemeli. Kapı, modelin her atfını kural tabanına karşı doğrular. İnsan karar verir. Getirilen belgeyle motor yeniden koşar ve döngü kapanır.
>
> Şemadaki çarpı işaretli kesik çizgi bu sunumun en önemli detayı. Modelden tutara giden bir yol yok. Model bir hata yaparsa sonuç yanlış bir tutar değil, gereksiz bir inceleme adımıdır.
>
> Literatürde bu yaklaşımın adı var. Program destekli dil modelleri çalışması, modelin problemi doğru parçalasa bile hesap adımında hata yaptığını, hesabı deterministik bir yürütücüye devretmenin bu hatayı ortadan kaldırdığını gösteriyor. Kambhampati ve arkadaşları da dil modellerinin kendilerini doğrulayamadığını, ancak dış doğrulayıcılarla çevrelendiklerinde güçlü bir fikir üreticisi olduklarını söylüyor. Bizim kapımız tam olarak böyle bir dış doğrulayıcı.
>
> Karar ise insanda kalıyor. Ürün beyan üretmiyor, beyanname göndermiyor, tasdik etmiyor.

**Çıpa cümle:** Modelden tutara giden bir yol yok; bu yüzden modelin yanılması hatalı tutar üretmez.

**Geçiş:** "Şimdi dört araştırma sorusuna geçiyorum. Dördünün de düşebilir bir ölçütü var."

**Bu slaytta acele etmeyin.** Heyet buradan ikna olursa geri kalanı teknik ayrıntıdır.

---

## Slayt 5 — AS-1 · Denetçi rolü dar kapsamlı bir modele öğretilebilir mi?

**Süre:** 90 sn · toplam 6:40
**Şemada göster:** Soldaki üç kaynağı; sonra MOTOR kutusunu; **sonra alttaki geri dönüş okunu** ("belge getir, motor koş, çözdü mü").

**Söyle:**

> Birinci araştırma sorumuz: bir denetçinin yaptığı ön inceleme işi, küçük ve yerel bir modele öğretilebilir mi?
>
> Buradaki asıl zorluk eğitim verisi. Bu göreve klasik anlamda etiketli veri üretmek mümkün değil; alan uzmanının binlerce örneği elle etiketlemesi gerekirdi.
>
> Bizim yaklaşımımız şemada. Doğrulanmış deterministik motoru referans kaynağı olarak kullanıyoruz. En güçlü olduğumuz yer alttaki geri dönüş oku: araştırma yönlendirme görevinde etiket bir yargı değil, mekanik bir olgu. Önerilen belgeyi getir, motoru yeniden koş, fark kapandı mı kapanmadı mı. Bunun literatürde emsali var; Toolformer çalışması, bir modelin araç çağırmayı elle etiketlenmiş veri olmadan öğrenebildiğini gösterdi.
>
> Dürüst olayım: insan üç yerde devrede. Sentetik senaryoların mevzuat referansını yazarken, pilot mutabakat oturumlarında kapanış kararını verirken, ve kör test setini onaylarken. Yani "hiç insan yok" demiyoruz; yönlendirme görevinde etiketi hiç kimse elle koymuyor diyoruz.
>
> Sentetik veri riskini de biliyoruz. Nature'daki çalışma, modelin kendi ürettiği veriyle özyinelemeli eğitilmesinin geri dönüşsüz çöküşe yol açtığını gösterdi. Bizde özyineleme yok: veriyi model değil, doksan altı gerçek dönemde kuruş farksız doğrulanmış motor üretiyor.

**Çıpa cümle:** Etiketi model değil, doğrulanmış motor koyuyor; bu yüzden özyineleme ve model çöküşü yok.

**Geçiş:** "İkinci soru, modelin söylediklerinin nasıl kanıta bağlandığı."

**Geride kalırsanız:** Toolformer atfını atlayın; "insan üç yerde devrede" cümlesini atlamayın, dürüstlük sinyali odur.

---

## Slayt 6 — AS-2 · Gerekçeler kural tabanına karşı kanıta bağlanabilir mi?

**Süre:** 75 sn · toplam 7:55
**Şemada göster:** Ortadaki kapı kutusunun içindeki iki soruyu; sonra yukarı çıkan "kullanıcıya" okunu ve aşağı inen "elenen" okunu; sonra en alttaki geri dönüş okunu.

**Söyle:**

> İkinci araştırma sorusu: küçük bir modelin ürettiği gerekçeler, sembolik bir kural tabanına karşı doğrulanarak kanıta bağlı tutulabilir mi?
>
> Modelin her çıktısı şema zorlamalı üretiliyor ve içindeki her atıf kapıda iki soruya tabi tutuluyor: bu madde var mı, ve o dönemde yürürlükte miydi. Karşılığı olmayan bulgu kullanıcıya ulaşmadan eleniyor. Eleme kaydı da bir sonraki ince ayar turuna olumsuz örnek olarak dönüyor; alttaki kesik ok bu.
>
> Neden model bunu kendi kendine yapamıyor? Çünkü yapamadığı ölçüldü. Huang ve arkadaşlarının ICLR 2024 çalışması, dil modellerinin dışarıdan geri bildirim almadan akıl yürütme hatalarını düzeltemediğini, hatta denemenin çoğu kez performansı düşürdüğünü gösterdi. Doğrulamanın dışsal olması zorunlu.
>
> Bir noktayı kendim söyleyeyim: kapı doğru bulguları da eleyebilir ve bunu ölçmeyi taahhüt ediyoruz. Ama en kötü sonucu şu: kullanıcı bugün olduğu gibi yorumsuz bir farkla kalır. Kapı hiçbir tutarı gizlemiyor; elenen şey tutar değil, yorumdur.

**Çıpa cümle:** Kapı hiçbir tutarı gizlemez; elediği şey yalnızca modelin yorumudur.

**Geçiş:** "Üçüncü soru teşhisle ilgili ve projenin en zor kısmı."

---

## Slayt 7 — AS-3 · Abdüktif kök-neden teşhisi

**Süre:** 75 sn · toplam 9:10
**Şemada göster:** Soldaki tek tutarı; sonra yelpazeyi açan yedi oku; sonra sağdaki daralma zincirini (sırala → kanıt iste → tek neden veya belirsiz).

**Söyle:**

> Farkı bulmak deterministiktir; iki sayıyı çıkarırsınız. Asıl belirsizlik, farkın nedenine güvenilir biçimde atanmasında.
>
> Şemadaki yelpaze problemi anlatıyor: tek bir fark tutarını yedi ayrı kök neden matematiksel olarak açıklayabilir. Yuvarlama, kapsam-personel farkı, kısmi çalışma, üst sınır bağlaması, oran farkı, veri eksiği ve gerçek hata. Bu klasik bir tanımlanabilirlik problemidir.
>
> Yapay zekâda kırk yıllık bir literatürü var. Reiter'ın 1987'deki birinci ilkelerden teşhis kuramı, teşhisi tek bir tahmin değil, aday kümelerinin tümünün hesaplanması olarak tanımlar. Aynı sayıda de Kleer ve Williams bir adım daha atar: adayları en çok ayrıştıracak bir sonraki ölçüm hangisidir? Bizim "hangi belgeyi istemeli" görevimiz tam olarak budur.
>
> İş bölümü şu: sembolik katman doğruluğu taşır ve kümeyi eksiksiz üretir, nöral katman verimliliği taşır ve kümeyi sıralar.
>
> Bir soruyu ben sorayım: zor vakaların hepsini belirsiz etiketleyip yüzde 85'i kolayca tutturamaz mısınız? İki metriği bilerek birbirine kilitledik. Doğruluk kalem bazında, belirsiz payı tutar bazında ölçülüyor ve tavanı yüzde beş.

**Çıpa cümle:** Sembolik katman doğruluğu taşır, nöral katman verimliliği; ayırt edilemeyen kalem tek nedene zorlanmaz.

**Geçiş:** "Dördüncü soru, bu modelin dayanacağı kural tabanı."

**Kendi sorunuzu sormayı atlamayın.** Heyet o soruyu zaten soracak; siz sorarsanız cevap savunma değil tasarım olur.

---

## Slayt 8 — AS-4 · Üç eksenli sürümleme ve ifade edilebilirlik sınırı

**Süre:** 90 sn · toplam 10:40
**Şemada göster:** Üç şeridi yukarıdan aşağıya; ortadaki şeritte iki işaretli olayı; sonra dikey kesik çizgiyi (as-of kesiti).

**Söyle:**

> Modelin her atfının doğrulanabilmesi, kural tabanının her dönem için o gün yürürlükte olan kuralı kesin olarak bilmesini gerektiriyor.
>
> Şemadaki üç şerit üç ekseni gösteriyor. Üstteki kolay: oran değişiklikleri. Ortadaki zor, çünkü hesaba giren büyüklüğün tanımını değiştiriyor. İki somut örnek vereyim. 2022'de asgari geçim indiriminin kaldırılması, ücret istisnası matrahının tanımını değiştirdi; bu bir parametre değişikliği değil, şema kırılmasıdır. İkincisi, 7555 sayılı düzenlemenin ücret tavanı 1 Ağustos 2025'te, yani ay ortasında yürürlüğe girdi ve dönem anahtarının kendisini kırdı.
>
> Alttaki eksen bilgi tarihi: aynı döneme ait düzeltme beyannameleri farklı bilgi tarihleriyle birden çok geçerli sürüm yaratır. Dikey kesik çizgi as-of kesiti; kapanmış bir dönemi o günkü bilgi durumuyla yeniden üretmek demek.
>
> Sorunun ikinci yarısı: rejime özgü mantığın ne kadarı koddan çıkarılıp kural dosyasına taşınabilir? Bu sınır tasarım öncesinde bilinemez, ölçülerek bulunur. 4691 iyi bir sınama alanı, çünkü rejim yalnız parametrede değil mantıkta da ayrışıyor. İki rejim aynı kuruluşta bir aradaysa aralarındaki sınırı da denetlemek gerekiyor; 5746'nın 4. maddesi aynı kazançtan çifte yararlanmayı yasaklıyor.
>
> Son olarak, sık gelen bir soruyu peşinen cevaplayayım: 2028'de yeni bir tebliğ çıkarsa modeli yeniden mi eğiteceğiz? Hayır. Model oran ve limit taşımıyor; yeni bir tebliğ yeni bir kural dosyasıdır.

**Çıpa cümle:** Model oran ve limit taşımaz; mevzuat değişince kural dosyası değişir, model değil.

**Geçiş:** "Şimdi bunları nasıl ölçeceğimize geçiyorum."

**Geride kalırsanız:** İkinci yarıyı (kural dosyası sınırı) tek cümleye indirin, iki mevzuat örneğini atlamayın.

---

## Slayt 9 — Ölçüm düzeneği ve başarısızlık eşikleri

**Süre:** 75 sn · toplam 11:55
**Şemada göster:** Sol kutudan çıkan beş oku; **özellikle üçüncü kolu** (erişim destekli). Sağdaki gri notlar her kolun neyi ölçtüğünü söyler. Sonra eşik tablosunu ve en alttaki ön kayıt şeridini.

**Söyle:**

> Bir yapay zekâ iddiası ancak ölçüm düzeneği kadar değerlidir; bu yüzden en çok emeği buraya verdik.
>
> Aynı kör test seti beş kolda koşuluyor. Üçüncü kol özellikle önemli: kural tabanını bağlam olarak alan erişim destekli kol. Böylece "neden erişim destekli üretim yetmiyor da ince ayar gerekiyor" sorusunun cevabı tahmin değil ölçüm oluyor. AS-3 için ayrıca kural tabanlı basit bir sembolik taban çizgisi koşuyoruz; nöral katman ona yetişemezse ucuz olanı ürüne koyar ve bunu olumsuz sonuç olarak raporlarız.
>
> Tablodaki dört eşiğin her biri yanlışlanabilir. Bir örnek: yüzde 70 yönlendirme isabeti literatürden alınmış bir sabit değil. Sembolik katman bir fark için ortalama üç ila beş hipotez üretiyor, yani rastgele seçim yüzde 20 ile 33 arası; yüzde 70 bunun iki ila üç buçuk katı.
>
> En önemli taahhüdümüz en alttaki şerit: bütün eşikler ve kör test seti yedinci ayda mühürlenip Teknoloji Transfer Ofisi ile YMM nezdinde yazılı olarak saklanacak. Ölçümden sonra ne eşiği ne paydayı değiştiririz.

**Çıpa cümle:** Eşikleri ay 7'de mühürleyip TTO'ya teslim ediyoruz; ölçümden sonra eşik de payda da değişmez.

**Geçiş:** "Bu ölçümleri hangi takvimde ve hangi kaynakla yapacağız?"

---

## Slayt 10 — İş paketleri, ölçüm kapıları ve kaynak dağılımı

**Süre:** 75 sn · toplam 13:10
**Şemada göster:** Koyu şeridi (İP5); sonra dikey kesik kapı çizgilerini ve alttaki kapı numaralarını; sonra tabloda personel satırını ve %72'yi.

**Söyle:**

> Yedi iş paketimiz var; her birinin adam-ayı, ayı ve çıkış kriteri yazılı. Adam-ayı tanımlanmamış hiçbir taahhüdümüz yok.
>
> Koyu şerit İP5, yani projenin yapay zekâ ekseni: 10 adam-ay, altıncı aydan on ikinciye. Kritik yol İP2'nin yedinci aydaki kural tabanı kapısından ve İP4'ün sekizinci aydaki senaryo setlerinden geçiyor.
>
> Açıkça söylemem gereken bir şey var: deterministik hesap çekirdeği proje öncesinde firmamızda geliştirildi ve doksan altı çapa testiyle iç doğrulaması tamamlandı. Bunu başlangıç varlığı olarak beyan ettik. "O zaman Ar-Ge içeriği daralmıyor mu" diye sorabilirsiniz; tersi oluyor. Çalışan bir motorun üzerine kurduğumuz için Ar-Ge eforunun on dokuz adam-ayını doğrudan yapay zekâ bileşenine ayırabiliyoruz.
>
> Dört kişilik ekip, 39 adam-ay, ortalama 3,25 tam zaman eşdeğeri. Bütçenin yüzde 72'si personel, donanım payı yüzde dört; bu bir ekipman alma projesi değil. YMM kalemi ise projenin ölçüm altın standardını üretiyor: kural setlerinin madde teyidi, parametre tablosunun doğrulanması, pilot mutabakat denetimi ve kör değerlendirmede uzman etiketleme.

**Çıpa cümle:** Çalışan bir motorun üzerine kurduğumuz için Ar-Ge eforunun 19 adam-ayı doğrudan yapay zekâya ayrılabiliyor.

**Geçiş:** "Şimdi en önemli soruya geliyorum: ya tutmazsa?"

**Geride kalırsanız:** Bütçe cümlesini kısaltın, "başlangıç varlığı" paragrafını atlamayın. Heyet bunu formdan öğrenirse saklandığı izlenimi doğar.

---

## Slayt 11 — Başarısızlık senaryosu ve risk asimetrisi

**Süre:** 60 sn · toplam 14:10
**Şemada göster:** Üstteki hattı soldan sağa; sonra alttaki hattaki kalın dikey engeli.

**Söyle:**

> Hakem heyetinin haklı olarak soracağı soru şu: yapay zekâ bileşeni hedefe ulaşamazsa yedi milyon TL boşa mı gitmiş olur?
>
> Cevap hayır ve nedeni şemada. Üstteki hat: model yanılırsa sonuç yanlış bir tutar değil, gereksiz bir inceleme adımıdır; tutar değişmez. Alttaki hat: motorun parametresi doğrulanmamışsa sert kural devreye giriyor ve o ay için ne hesap ne rapor üretiliyor. Bu bir uyarı değil, motorun içine gömülü bir engel.
>
> AS-1 tutmazsa bunu olumsuz sonuçlu bir araştırma sorusu olarak, veri kaynağı ve hacim etkisi ölçümleriyle birlikte raporlarız; bu da bilimsel bir çıktıdır. Ürün ise sembolik katman üzerinden eksiksiz çalışmaya devam eder: geçmiş dönem mutabakatı, kök-neden teşhisi, mühürlü baz, denetim savunma dosyası ve cari dönem kontrolü modele bağlı değil.

**Çıpa cümle:** Doğruluğu model değil motor taşıdığı için, araştırma sorusu düşse bile ürün çalışır.

**Geçiş:** "Toparlıyorum."

---

## Slayt 12 — Proje çıktıları ve teknopark katkısı

**Süre:** 60 sn · toplam 15:10
**Şemada göster:** Dört çıktı satırını sırayla; sonra en alttaki alıntı bloğunu.

**Söyle:**

> Proje sonunda geriye dört somut şey kalacak. Birincisi, 5746 ve 4691 için doğrulanmış, zaman-farkındalıklı bir kural tabanı; bugünkü doksan altı çapamız en az yüz kırka çıkacak. İkincisi, denetçi rolündeki yerel model ve onu ölçen düzenek. Üçüncüsü, iki sanayi kuruluşunda gerçek veriyle çalışan bir prototip. Dördüncüsü fikri mülkiyet.
>
> İkincisini vurgulamak istiyorum: ölçüm düzeneği modelin kendisi kadar önemli, çünkü bu alanda eksik olan şey model değil, ölçüm.
>
> Neden teknoparkta? Üç şey aynı anda burada: 4691 kural setinin ilk kullanıcıları, yapay zekâ tarafındaki akademik danışmanlık, ve ölçümlerimizi gözden geçirecek bağımsız göz. Bağımsız gözden geçirmeyi kendi lehimize değil, sonucun güvenilirliği için istiyoruz.
>
> Son cümlem şu: araştırma sorusu düşerse bile ürün çalışır, çünkü doğruluğu model değil motor taşıyor. Hesabı motor yapar, bulguyu model inceler, kararı insan verir.
>
> Teşekkür ederim, sorularınızı almaktan memnuniyet duyarım.

**Çıpa cümle:** Bu alanda eksik olan şey model değil, ölçüm.

**Son saniye:** Cümleyi bitirdikten sonra susun. Doldurma cümlesi kurmayın; ilk soruyu bekleyin.

---
---

# SORU-CEVAP İÇİN

## İlk otuz saniyede yapılacaklar

1. **Soruyu tekrar edin.** Hem düşünme süresi kazanırsınız hem yanlış anlaşılmayı önlersiniz.
2. **Hangi slayta ait olduğunu söyleyin** ve o slayta dönün. Şemaya bakarak cevap vermek sözle cevap vermekten güçlüdür.
3. **Cevabınız bir sayı içeriyorsa paydasını da söyleyin.** Payda belirtilmemiş yüzde, hakem nezdinde ölçüm sayılmaz.

## En olası altı soru ve hangi yedek slayda dönüleceği

| Soru | Yedek slayt | Tam cevap |
|---|---|---|
| Sentetik veriyle eğitim sağlam mı? | Y8 · EK-6 veri hattı | S1 |
| Motor da bir yazılım, nasıl güveniyorsunuz? | Y9 · çapa kapsama matrisi | S2 |
| 15 puanlık fark istatistiksel olarak anlamlı mı? | Y10 · örneklem ve test planı | S5 |
| Bu Ar-Ge mi, mühendislik mi? | — | S14 |
| Pilotlar gerçekten ücretli olacak mı? | Y11 · dört kapılı pilot akışı | S27 |
| Yanlış beyan verilirse sorumlu kim? | Y5 · sorumluluk ve insan gözetimi | S32 |

*Numaralar `hakem-sunumu-soru-cevap.md` dosyasındaki soru numaralarıdır; 43 sorunun tamamı orada.*

## Üç savunma kuralı

1. **Zayıf noktayı hakemden önce siz söyleyin.** Kabul edilen bir sınır, savunulan bir sınırdan güçlüdür.
2. **Bilinmeyeni bilinmeyen olarak söyleyin.** "Ölçeceğiz" cevabı, uydurulmuş bir kesinlikten iyidir.
3. **Dosyayı aşmayın.** Sunumda söylediğiniz her taahhüdün başvuru dosyasında karşılığı olmalı. Karşılığı olmayanların listesi `hakem-sunumu.md` sonundaki A tablosundadır; sunum gününden önce o listeyi kapatın.
