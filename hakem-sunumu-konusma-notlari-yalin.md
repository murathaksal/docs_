# KONUŞMA NOTLARI — YALIN SÜRÜM: Denetci.AI hakem sunumu

*Ayrıntılı sürümün sade dille yazılmış karşılığı. Slaytlar, süreler ve sıralama aynıdır; değişen yalnızca anlatım. Terimler yerine gündelik karşılıkları kullanılır, her teknik kavram bir örnekle açılır, akademik atıflar konuşmadan çıkarılıp "Sorarlarsa" satırına konur. Slaytlar: `hakem-sunumu.html`. Ayrıntılı sürüm: `hakem-sunumu-konusma-notlari.md`. Zor sorular: `hakem-sunumu-soru-cevap.md`.*

---

## Hangi sürümü kullanmalı

| Durum | Sürüm |
|---|---|
| Heyette alan dışından üye var; mevzuat veya yapay zekâ uzmanı olmayan hakem bulunuyor | **Bu sürüm** |
| Heyet dar uzman; atıf ve ölçüm ayrıntısı bekleniyor | Ayrıntılı sürüm |
| Emin değilseniz | **Bu sürümle konuşun,** ayrıntıyı "Sorarlarsa" satırlarından verin |

İki sürüm birbirinin yerine geçer: süreler, çıpa cümleler ve geçişler birebir aynıdır. Ortada bir sürümden diğerine geçebilirsiniz.

---

## Kullanım

| Parça | Ne işe yarar |
|---|---|
| **Süre** | Slayt için ayrılan saniye ve kümülatif dakika |
| **Şemada göster** | Ekranda neyi işaret edeceğiniz |
| **Söyle** | Konuşma metni. Kısa cümleler; ezberlemeyin, mantığı kalsın |
| **Örnek** | O slaytın tek somut hikâyesi. Soyut kaldığınızı hissederseniz buraya dönün |
| **Çıpa cümle** | Heyette kalması gereken tek cümle |
| **Geçiş** | Sonraki slayta bağlayan cümle |
| **Sorarlarsa** | Konuşmada söylemediğiniz dayanak: rakam, kaynak, ek ayrıntı |

**Toplam hedef: 15 dakika 10 saniye.** Soru-cevap için en az 10 dakika bırakın.

---

## Terimlerin sade karşılığı

Formda ve slaytlarda teknik terim geçiyor. Siz sade karşılığını kullanın; hakem terimi kullanırsa siz de o terime geçin. İkisini bir kez yan yana söyleyin, sonra sadesinde kalın.

| Slayttaki / formdaki terim | Konuşurken söyleyeceğiniz |
|---|---|
| Nöro-sembolik mimari | Hesap makinesi ile okuyup yazan bir asistanın birlikte çalışması |
| Deterministik hesap çekirdeği | Kuralları harfiyen uygulayan hesap motoru; aynı girdiye hep aynı sonucu verir |
| Zaman-farkındalıklı kural tabanı | Her ayın kendi kuralını hatırlayan kural defteri |
| Sembolik doğrulama kapısı | Modelin söylediğini kural defterine karşı kontrol eden kapı |
| Abdüktif kök-neden teşhisi | Farkın sebebini bulma; doktorun teşhis koyması gibi |
| Denetçi rolündeki dar kapsamlı model | Yalnızca bu işi yapan, küçük, kurum içinde çalışan yapay zekâ |
| Şema zorlamalı çıktı | Modelin serbest metin değil, boş bir formu doldurarak cevap vermesi |
| Kör test seti | Önceden mühürlenmiş, eğitimde hiç kullanılmayan sınav soruları |
| Teknoloji hazırlık seviyesi (THS) | Olgunluk basamağı: 5 laboratuvarda çalışıyor, 7 sahada çalışıyor demek |

---

## Sunum öncesi beş dakika

1. **Destede slayt 1'de olduğunuzdan emin olun** (klavye: `Home`). "Tüm slaytlar" ızgarası açıksa `G` ile kapatın.
2. **Bu notlar destede yoktur;** ayrı bir belgedir. Yansıtılan ekranda yalnızca slaytlar görünür.
3. **Şu üç sayıyı tekrarlayın:** 1.720 merkez · 39 adam-ay · 7.000.000 ₺.
4. **Şu tek örneği tekrarlayın:** yüksek lisans diploması Mart'ta alınmış, oran Ocak'tan uygulanmış, 8.500 lira fark. Bu örnek sunumun dört yerinde işinize yarayacak.
5. **Ekler elinizde olsun:** EK-1 rekabet tablosu, EK-4 efor matrisi, EK-6 veri hattı, EK-7 kaynakça.
6. **Son cümleyi bir kez içinizden söyleyin:** "Hesabı motor yapar, bulguyu model inceler, kararı insan verir."

---
---

# SLAYT SLAYT

---

## Slayt 1 — Kapak

**Süre:** 70 sn · toplam 1:10
**Şemada göster:** Önce zaman eğrisi (2013 kuruluş → 2026 Nisan'da doğrulanmış motor → 2027 Ekim'de saha prototipi), sonra referans kuruluş şeridi.

**Söyle:**

> Teşekkür ederim. Önce kısaca kendimizi tanıtayım. ARGELOG 2013'ten beri sanayi kuruluşlarına Ar-Ge ve teşvik süreçleri için yazılım yapıyor ve danışmanlık veriyor. Ekranda gördüğünüz kuruluşlar müşterilerimiz.
>
> Bu on üç yılda bir hesap motoru geliştirdik. Bu motor, 5746 ve 4691 teşviklerini kurallarına göre hesaplıyor. Nisan ayında doksan altı gerçek dönemde test ettik; hepsinde kuruşu kuruşuna doğru çıktı.
>
> Bugün sizden istediğimiz şey şu: bu çalışan motorun üzerine bir yapay zekâ katmanı kurmak.
>
> Projenin adı Denetci.AI. Tek cümlesi şu: hesabı motor yapar, bulguyu model inceler, kararı insan verir.

**Örnek:** Bu slaytta ayrı bir örnek gerekmiyor; zaman eğrisinin kendisi hikâyeyi anlatıyor. Eğriyi parmağınızla soldan sağa takip edin.

**Çıpa cümle:** Hesabı motor yapar, bulguyu model inceler, kararı insan verir.

**Geçiş:** "Önce çözdüğümüz problemi göstereyim."

**Sorarlarsa:** Motorun teknik adı deterministik hesap çekirdeği; proje başlangıç varlığı olarak beyan edildi (form, İş Paketleri bölümü). Doksan altı test "çapa testi" adıyla geçiyor. Mimarinin adı nöro-sembolik.

---

## Slayt 2 — Kapanmış dönem, kendi kural sürümüyle yeniden üretilemiyor

**Süre:** 75 sn · toplam 2:25
**Şemada göster:** Üstteki tek kutuyu ve ondan dört yıla inen okları; sonra kutunun sağındaki kendine dönen oku; sonra alttaki dört sürümlü şeridi.

**Söyle:**

> Türkiye'de 1.720 Ar-Ge merkezi ve 13.452 bölge firması var. Hepsi her ay bordroyla iç içe geçmiş teşvik hesapları yapıyor. Bu hesaplar çoğunlukla elektronik tabloda tutuluyor.
>
> Elektronik tablonun bir sorunu var: tek bir kural sürümü taşır. Oran değiştiğinde eskisinin üzerine yazarsınız. Geçmiş yılın oranı dosyada kalmaz.
>
> Üstteki şerit bugünü gösteriyor: tek kutu, dört yıla hizmet ediyor. Alttaki şerit bizim yaptığımızı gösteriyor: her yıl kendi mühürlü kural sürümüne bağlı kalıyor.
>
> Ama asıl ağır kısım bu değil. Bir fark bulunduğunda onu yorumlayacak, doğru soruyu soracak ve hangi belgenin isteneceğini bilecek uzman lazım. O uzman az, pahalı ve her firmaya yetmiyor.

**Örnek:** 2023 yılının teşvik hesabını bugün yeniden yaparsanız, bugünün oranlarıyla yaparsınız. O yılın oranını hatırlayan bir defteriniz yoksa, denetimde "bu rakam nasıl çıktı" sorusuna belgeyle cevap veremezsiniz.

**Çıpa cümle:** Asıl darboğaz hesap değil, farkı yorumlayacak uzman emeği.

**Geçiş:** "Burada akla hemen yapay zekâ geliyor. Ama hangi işi yapacak?"

**Sorarlarsa:** Ar-Ge personeli başına yıllık teşvik yaklaşık bir milyon TL; 150 kişilik bir merkezde yılda yüz milyon TL düzeyinde akış. Sayılar Sanayi ve Teknoloji Bakanlığı istatistiklerinden; künyeler EK-7'de.

**Geride kalırsanız:** Pazar sayılarını atlayın, doğrudan örneğe geçin.

---

## Slayt 3 — Mevzuat alanında dil modeli hesap ve karar üretemez

**Süre:** 75 sn · toplam 3:40
**Şemada göster:** Sırayla en uzun çubuğu (%88), sonra %58'i, sonra %17–33 bandını; en son alttaki kısa koyu çubuğu.

**Söyle:**

> Bu, projenin en önemli tasarım kararı. Sorulması gereken soru şu: yapay zekâ bu işte hesabı yapabilir mi?
>
> Cevap hayır, ve bu bir tahmin değil, ölçülmüş bir sonuç. Stanford ekibi gerçek mahkeme kararları hakkında doğrulanabilir sorular sordu. Yaygın kullanılan modeller, sorulara verdikleri cevapların yüzde 58 ile yüzde 88'inde dayanaksız bilgi üretti. Yani uydurdu.
>
> "Genel model değil, hukuka özel araç kullanırız" diyebilirsiniz. Aynı ekip onları da ölçtü: en pahalı ticari araçlarda bile oran yüzde 17 ile 33 arasında kaldı.
>
> Bu giderilebilir bir arıza değil. Modeller boş bırakmak yerine tahmin etmeye eğitiliyor. Sınavda bilmediği soruyu boş bırakmayan öğrenci gibi.
>
> Teşvik hesabında bir tutarın yüzde on yedi ihtimalle uydurma olması kabul edilebilir değil. Bu yüzden yapay zekânın işini bilinçli olarak daralttık.

**Örnek:** Bir modele "bu personelin gelir vergisi terkin oranı kaç" diye sorarsanız size bir oran söyler. O oran doğru da olabilir, uydurma da. Hangisi olduğunu anlamanın bir yolu yok. Oysa kural defterine bakan bir motor size hem oranı hem de dayandığı maddeyi verir.

**Çıpa cümle:** Yapay zekâyı hesaplayıcı koltuğuna oturtmuyoruz, çünkü o koltuk ölçülerek savunulamaz hâle geldi.

**Geçiş:** "Peki hangi koltuğa oturtuyoruz?"

**Sorarlarsa:** Ölçümler Dahl ve arkadaşları 2024 (Journal of Legal Analysis) ile Magesh ve arkadaşları 2025 (Journal of Empirical Legal Studies). "Boş bırakmayan öğrenci" benzetmesinin dayanağı Kalai ve arkadaşları 2026 (Nature). Künyeler EK-7 bölüm 2'de. **Hafızadan ek rakam vermeyin.**

---

## Slayt 4 — İş bölümü: motor hesaplar, model inceler, insan karar verir

**Süre:** 90 sn · toplam 5:10
**Şemada göster:** Soldan sağa dört kutuyu sırayla; sonra alttaki geri dönüş okunu; **en son ve en uzun süre çarpı işaretli kesik çizgiyi.**

**Söyle:**

> İş bölümümüz dört adımda.
>
> Bir: motor hesaplar ve farkı bulur. İki: model o farka bakar ve şunu söyler — bu fark ne anlama geliyor olabilir, hangi belgeye bakmak gerekir, bir denetçi burada ne sorardı. Üç: kapı, modelin söylediği her mevzuat maddesini kural defterine karşı kontrol eder. Dört: kararı insan verir. Belge gelince motor yeniden koşar ve döngü kapanır.
>
> Şemadaki çarpı işaretli kesik çizgi bu sunumun en önemli ayrıntısı. Modelden tutara giden bir yol yok. Model hiçbir rakam üretmiyor, hiçbir rakama dokunmuyor.
>
> Bunun sonucu şu: model yanılırsa ortaya yanlış bir tutar çıkmaz. Gereksiz bir belge istemiş oluruz, o kadar.
>
> Kararı insan veriyor. Ürün beyanname göndermiyor, tasdik etmiyor.

**Örnek:** Bunu somutlaştırayım. Bir mühendis yüksek lisansını Mart ayında bitirmiş. Ama terkin oranı Ocak ayından itibaren yüksek lisans oranıyla uygulanmış. Motor farkı buluyor: iki ay için 8.500 lira fazla yararlanma. Model şunu söylüyor: "Bu, diploma tarihinin yanlış girilmesinden kaynaklanıyor olabilir; mezuniyet belgesine bakın." Belge geliyor, motor yeniden koşuyor, fark kapanıyor. Kararı mali müşavir veriyor. Model bu süreçte tek bir rakam üretmedi.

**Çıpa cümle:** Modelden tutara giden bir yol yok; bu yüzden modelin yanılması hatalı tutar üretmez.

**Geçiş:** "Şimdi dört araştırma sorusuna geçiyorum. Dördünün de düşebilir bir ölçütü var."

**Sorarlarsa:** Bu yaklaşımın literatürdeki adı program destekli dil modelleri; hesabın deterministik bir yürütücüye devredilmesi. Kambhampati ve arkadaşları modelin kendini doğrulayamadığını, dış doğrulayıcıyla çevrelendiğinde güçlü olduğunu gösteriyor. EK-7 bölüm 1 ve 3.

**Bu slaytta acele etmeyin.** Heyet buradan ikna olursa geri kalanı teknik ayrıntıdır.

---

## Slayt 5 — AS-1 · Denetçi rolü dar kapsamlı bir modele öğretilebilir mi?

**Süre:** 90 sn · toplam 6:40
**Şemada göster:** Soldaki üç kaynağı; sonra MOTOR kutusunu; **sonra alttaki geri dönüş okunu.**

**Söyle:**

> Birinci sorumuz: bir denetçinin yaptığı ön inceleme işi, küçük ve kurum içinde çalışan bir modele öğretilebilir mi?
>
> Buradaki zorluk eğitim verisi. Modeli eğitmek için binlerce soru-cevap çifti lazım. Normalde bu cevapları bir uzmanın elle yazması gerekir. Bizde o kaynak yok, olsa da yetişmez.
>
> Çözümümüz şu: cevapları uzman değil, doğrulanmış motor üretiyor. Motor zaten her koşumda girdiyi, uygulanan kuralı ve sonucu kesin olarak veriyor. Eğitim verisinin "doğru cevap" tarafı buradan çıkıyor.
>
> En sağlam olduğumuz yer alttaki geri dönüş oku. "Hangi belgeye bakmalı" görevinde doğruluk bir yorum değil, mekanik bir olgu: önerilen belgeyi getir, motoru yeniden koş, fark kapandı mı kapanmadı mı. Cevap evet ya da hayır.
>
> Dürüst olayım: insan üç yerde devrede. Senaryoların mevzuat referansını yazarken, pilot oturumlarda kapanış kararını verirken, ve sınav sorularını onaylarken.

**Örnek:** Bir öğrenciye soru çözdürüp cevabını cevap anahtarından işaretlemek gibi. Cevap anahtarını biz yazmıyoruz; doksan altı gerçek dönemde kuruşu kuruşuna doğrulanmış motor yazıyor.

**Çıpa cümle:** Etiketi model değil, doğrulanmış motor koyuyor.

**Geçiş:** "İkinci soru, modelin söylediklerinin nasıl kanıta bağlandığı."

**Sorarlarsa:** Veri üretim yöntemi EK-6'da; örnek veri seti `ornek-sft-veriseti/` dizininde çalışır hâlde. Modelin araç çağırmayı elle etiketsiz öğrenebildiğine emsal: Toolformer. Kendi ürettiği veriyle eğitilen modelin çöktüğü bulgusu Nature'da; bizde özyineleme yok, veriyi model değil motor üretiyor.

**Geride kalırsanız:** "İnsan üç yerde devrede" cümlesini atlamayın; dürüstlük sinyali odur.

---

## Slayt 6 — AS-2 · Gerekçeler kural tabanına karşı kanıta bağlanabilir mi?

**Süre:** 75 sn · toplam 7:55
**Şemada göster:** Ortadaki kapı kutusunun içindeki iki soruyu; sonra yukarı çıkan "kullanıcıya" okunu ve aşağı inen "elenen" okunu; sonra en alttaki geri dönüş okunu.

**Söyle:**

> İkinci soru: modelin söylediği gerekçeler kanıta bağlanabilir mi?
>
> Model serbest metin yazmıyor. Boş bir form dolduruyor ve o formda her gerekçe bir mevzuat maddesine bağlanmak zorunda.
>
> Kapı iki soru soruyor: bu madde gerçekten var mı, ve o ayda yürürlükte miydi? İkisinden birine hayır cevabı gelirse cümle kullanıcıya hiç ulaşmıyor.
>
> Neden model bunu kendi kendine yapamıyor? Çünkü yapamadığı ölçüldü: dil modelleri dışarıdan geri bildirim almadan kendi hatalarını düzeltemiyor, denedikleri zaman çoğu kez daha kötü oluyor. Kontrolün dışarıdan yapılması şart.
>
> Bir zayıflığı kendim söyleyeyim: kapı doğru bulguları da eleyebilir. Bunu ölçmeyi taahhüt ediyoruz. Ama en kötü sonuç şu: kullanıcı bugün zaten olduğu gibi yorumsuz bir farkla kalır. Kapı hiçbir tutarı gizlemiyor; elediği şey yorum.

**Örnek:** Model "5746 sayılı Kanun'un 3. maddesine göre terkin oranı yanlış uygulanmış" diyor. Kapı bakıyor: 3. madde var mı? Var. O ayda yürürlükte miydi? Evet. Cümle geçiyor. Model uydurulmuş bir madde numarası verseydi, o cümle kullanıcıya hiç gitmeyecekti.

**Çıpa cümle:** Kapı hiçbir tutarı gizlemez; elediği şey yalnızca modelin yorumudur.

**Geçiş:** "Üçüncü soru teşhisle ilgili ve projenin en zor kısmı."

**Sorarlarsa:** Modelin kendini düzeltemediği bulgusu Huang ve arkadaşları, ICLR 2024. Formdaki terim: sembolik doğrulama kapısı, şema zorlamalı çıktı. Elenen cümleler bir sonraki eğitim turuna olumsuz örnek olarak dönüyor.

---

## Slayt 7 — AS-3 · Farkın sebebini bulma

**Süre:** 75 sn · toplam 9:10
**Şemada göster:** Soldaki tek tutarı; sonra yelpazeyi açan yedi oku; sonra sağdaki daralma zincirini.

**Söyle:**

> Farkı bulmak kolay: iki sayıyı çıkarırsınız. Zor olan, farkın sebebini doğru söylemek.
>
> Şemadaki yelpaze problemi anlatıyor. Tek bir fark tutarını yedi ayrı sebep açıklayabilir: yuvarlama, kapsam farkı, kısmi çalışma, üst sınır, oran farkı, eksik belge, gerçek hata. Hepsi aynı rakamı üretebilir.
>
> İş bölümü şöyle: sembolik taraf, yani kural defteri, olası sebeplerin hiçbirini atlamadan hepsini listeliyor. Yapay zekâ tarafı ise onları en olasıdan en az olasıya sıralıyor ve hangi belgenin ayırt edici olduğunu söylüyor.
>
> Bir soruyu ben sorayım: zor vakaların hepsine "belirsiz" deyip yüzde 85'i kolayca tutturamaz mısınız? Bunu engellemek için iki ölçüyü birbirine kilitledik. Doğruluk kalem sayısıyla, belirsiz payı ise tutarla ölçülüyor ve tavanı yüzde beş.

**Örnek:** Doktorun teşhis koyması gibi. Ateş tek başına yedi hastalıkta da görülür. İyi doktor tek hastalık söyleyip geçmez; olasılıkları sıralar ve "şu tahlili yaptıralım" der. Bizim modelin işi de bu: sebebi sıralamak ve hangi belgenin ayırt edeceğini söylemek. Ayırt edemiyorsa "belirsiz" demek zorunda; tahmin yürütmesi yasak.

**Çıpa cümle:** Kural defteri sebepleri eksiksiz üretir, yapay zekâ onları sıralar; ayırt edilemeyen kalem tek sebebe zorlanmaz.

**Geçiş:** "Dördüncü soru, bu modelin dayanacağı kural defteri."

**Sorarlarsa:** Formdaki terim abdüktif kök-neden teşhisi. Kırk yıllık literatürü var: Reiter 1987 teşhisi tek tahmin değil aday kümesi olarak tanımlar; de Kleer ve Williams "adayları en çok ayrıştıracak sonraki ölçüm hangisi" sorusunu sorar. Bizim "hangi belgeyi istemeli" görevimiz tam olarak budur. EK-7 bölüm 6.

**Kendi sorunuzu sormayı atlamayın.** Heyet o soruyu zaten soracak; siz sorarsanız cevap savunma değil tasarım olur.

---

## Slayt 8 — AS-4 · Her ayın kendi kuralını hatırlayan defter

**Süre:** 90 sn · toplam 10:40
**Şemada göster:** Üç şeridi yukarıdan aşağıya; ortadaki şeritte iki işaretli olayı; sonra dikey kesik çizgiyi.

**Söyle:**

> Modelin her cümlesinin kontrol edilebilmesi için kural defterinin her ay için o gün geçerli olan kuralı kesin bilmesi gerekiyor. Dördüncü sorumuz bu defteri kurmakla ilgili.
>
> Üç tür değişiklik var, üç şerit onları gösteriyor.
>
> Üstteki kolay: oran değişir. Defterde sayıyı değiştirirsiniz, olur biter.
>
> Ortadaki zor. Bazen değişen oran değil, hesabın neyin üzerinden yapılacağı. İki örnek vereyim. 2022'de asgari geçim indirimi kaldırıldı; hesaba giren matrahın tanımı değişti. 2025'te ücret tavanı ayın ortasında, 1 Ağustos'ta yürürlüğe girdi; o ay ikiye bölündü. Bunlar sayı değişikliği değil, hesabın şeklinin değişmesi.
>
> Alttaki de zor. Aynı döneme sonradan düzeltme beyannamesi verilir. Artık o dönemin birden fazla geçerli hâli olur ve hangisine göre konuştuğunuzu söylemeniz gerekir.
>
> Son olarak sık gelen bir soruyu peşinen cevaplayayım: 2028'de yeni bir tebliğ çıkarsa modeli yeniden mi eğiteceğiz? Hayır. Model hiçbir oran ve limit taşımıyor. Yeni tebliğ, yeni bir kural dosyası demek.

**Örnek:** Ortadaki şeridi somutlaştırayım. Diyelim bir personelin ücreti tavanın üstünde. 1 Ağustos 2025'ten önce hesap bir türlü, sonra başka türlü yapılıyor. O ay için tek bir kural yok, ayın içinde kural değişiyor. Defter bunu ay ay değil gün gün tutmak zorunda.

**Çıpa cümle:** Model oran ve limit taşımaz; mevzuat değişince kural dosyası değişir, model değil.

**Geçiş:** "Şimdi bunları nasıl ölçeceğimize geçiyorum."

**Sorarlarsa:** Formdaki terimler: parametre değişikliği, girdi semantiği değişikliği, bilgi zamanı ekseni, as-of yeniden üretim. Tavan düzenlemesi 7555 sayılı. İki rejim bir aradaysa 5746'nın 4. maddesi aynı kazançtan çifte yararlanmayı yasaklar; bu sınırı da denetliyoruz. 4691 iyi bir sınama alanı, çünkü orada teşvik eğitim derecesine bağlı değil.

**Geride kalırsanız:** Alttaki şeridi tek cümleye indirin; iki mevzuat örneğini atlamayın.

---

## Slayt 9 — Ölçüm düzeneği ve başarısızlık eşikleri

**Süre:** 75 sn · toplam 11:55
**Şemada göster:** Sol kutudan çıkan beş oku; **özellikle üçüncü kolu.** Sonra eşik tablosunu ve en alttaki ön kayıt şeridini.

**Söyle:**

> Bir yapay zekâ iddiası, ancak onu ölçen düzenek kadar değerlidir. En çok emeği buraya verdik.
>
> Aynı sınavı beş farklı kurulumda koşuyoruz. Üçüncüsü önemli: kural defterini modele doğrudan veriyoruz ve soruyoruz — bu kadarı yetiyor mu, yoksa modeli gerçekten eğitmek gerekiyor mu? Böylece bu sorunun cevabı tahmin değil ölçüm oluyor.
>
> Tablodaki dört eşiğin her biri düşebilir. Eşiği tutturamazsak bunu saklamayız, olumsuz sonuç olarak raporlarız.
>
> Bir eşiğin nereden geldiğini göstereyim: "hangi belgeye bakmalı" sorusunda hedefimiz yüzde 70 isabet. Bu sayıyı literatürden almadık. Kural defteri bir fark için ortalama üç ila beş sebep üretiyor; yani rastgele seçseniz yüzde 20-33 tutturursunuz. Yüzde 70, bunun iki ila üç buçuk katı.
>
> En önemli taahhüdümüz en alttaki şerit: bütün eşikler ve sınav soruları yedinci ayda mühürlenip Teknoloji Transfer Ofisi ile mali müşavir nezdinde yazılı olarak saklanacak.

**Örnek:** Sınav sorularını sınavdan önce mühürleyip notere bırakmak gibi. Ölçüm yapıldıktan sonra ne soruyu ne geçme notunu değiştirebiliriz.

**Çıpa cümle:** Eşikleri ay 7'de mühürleyip TTO'ya teslim ediyoruz; ölçümden sonra eşik de payda da değişmez.

**Geçiş:** "Bu ölçümleri hangi takvimde ve hangi kaynakla yapacağız?"

**Sorarlarsa:** Üçüncü kolun teknik adı erişim destekli üretim. AS-3 için ayrıca basit bir kural tabanlı taban çizgisi koşuyoruz; yapay zekâ ona yetişemezse ucuz olanı ürüne koyar ve bunu olumsuz sonuç olarak yazarız. Dört eşiğin tamamı formun araştırma soruları bölümünde.

---

## Slayt 10 — İş paketleri, ölçüm kapıları ve kaynak dağılımı

**Süre:** 75 sn · toplam 13:10
**Şemada göster:** Koyu şeridi; sonra dikey kesik kapı çizgilerini; sonra tabloda personel satırını ve %72'yi.

**Söyle:**

> Yedi iş paketimiz var. Her birinin kaç adam-ay olduğu, hangi aylarda yapılacağı ve neyi bitirmiş sayılacağı yazılı. Adam-ayı tanımlanmamış tek bir taahhüdümüz yok.
>
> Koyu şerit projenin yapay zekâ ekseni: 10 adam-ay, altıncı aydan on ikinci aya.
>
> Açıkça söylemem gereken bir şey var. Hesap motoru proje başlamadan önce firmamızda geliştirildi. Bunu başlangıç varlığı olarak beyan ettik, saklamıyoruz. "O zaman Ar-Ge içeriği azalmıyor mu" diye sorabilirsiniz. Tersi oluyor: çalışan bir motorun üzerine kurduğumuz için Ar-Ge eforunun on dokuz adam-ayını doğrudan yapay zekâya ayırabiliyoruz.
>
> Dört kişilik ekip, 39 adam-ay. Bütçenin yüzde 72'si personel, donanım payı yüzde dört. Bu bir ekipman alma projesi değil.

**Örnek:** Mali müşavirlik kalemi neden var, onu somutlaştırayım: kural defterindeki her maddeyi madde madde teyit ettiriyoruz, pilot mutabakatlarını denetletiyoruz ve kör sınavda doğru cevapları uzmana işaretletiyoruz. Yani ölçümün "doğru cevap" tarafını bağımsız bir uzman yazıyor.

**Çıpa cümle:** Çalışan bir motorun üzerine kurduğumuz için Ar-Ge eforunun 19 adam-ayı doğrudan yapay zekâya ayrılabiliyor.

**Geçiş:** "Şimdi en önemli soruya geliyorum: ya tutmazsa?"

**Sorarlarsa:** Kritik yol, kural defteri kapısının yedinci ayda ve senaryo setlerinin sekizinci ayda kapanmasından geçiyor. Efor dağılımı EK-4'te, personel maliyeti dayanağı EK-3'te.

**Geride kalırsanız:** Bütçe cümlesini kısaltın, "başlangıç varlığı" paragrafını atlamayın. Heyet bunu formdan öğrenirse saklandığı izlenimi doğar.

---

## Slayt 11 — Başarısızlık senaryosu ve risk asimetrisi

**Süre:** 60 sn · toplam 14:10
**Şemada göster:** Üstteki hattı soldan sağa; sonra alttaki hattaki kalın dikey engeli.

**Söyle:**

> Heyetin haklı olarak soracağı soru şu: yapay zekâ tutmazsa yedi milyon lira boşa mı gitti?
>
> Cevap hayır. Nedeni şemada.
>
> Üstteki hat: model yanılırsa ortaya yanlış bir tutar çıkmaz, gereksiz bir inceleme adımı çıkar.
>
> Alttaki hat: motorun kuralı doğrulanmamışsa sert bir kural devreye giriyor ve o ay için ne hesap ne rapor üretiliyor. Bu bir uyarı mesajı değil, motorun içine gömülü bir engel.
>
> Yapay zekâ hedefine ulaşamazsa bunu olumsuz sonuçlu bir araştırma sorusu olarak raporlarız; bu da bilimsel bir çıktıdır. Ürün ise çalışmaya devam eder: geçmiş dönem mutabakatı, mühürlü kural defteri ve denetim savunma dosyası modele bağlı değil.

**Örnek:** Somut karşılığı şu: model "mezuniyet belgesine bakın" der, bakarsınız, ilgisi çıkmaz. Kaybınız bir belge isteme adımı. Buna karşılık motor yanlış hesaplasaydı, yanlış bir beyan riski doğardı. İşte bu yüzden hesabı modele vermiyoruz.

**Çıpa cümle:** Doğruluğu model değil motor taşıdığı için, araştırma sorusu düşse bile ürün çalışır.

**Geçiş:** "Toparlıyorum."

**Sorarlarsa:** Sert kuralın formdaki karşılığı: Resmî Gazete referansıyla doğrulanmamış parametreli ay hesaplanmaz.

---

## Slayt 12 — Proje çıktıları ve teknopark katkısı

**Süre:** 60 sn · toplam 15:10
**Şemada göster:** Dört çıktı satırını sırayla; sonra en alttaki alıntı bloğunu.

**Söyle:**

> Proje sonunda geriye dört somut şey kalacak.
>
> Birincisi, 5746 ve 4691 için doğrulanmış bir kural defteri; bugünkü doksan altı doğrulanmış dönem en az yüz kırka çıkacak. İkincisi, kurum içinde çalışan denetçi modeli ve onu ölçen düzenek. Üçüncüsü, iki sanayi kuruluşunda gerçek veriyle çalışan bir prototip. Dördüncüsü fikri mülkiyet.
>
> İkincisini vurgulamak istiyorum: ölçüm düzeneği modelin kendisi kadar önemli. Çünkü bu alanda eksik olan şey model değil, ölçüm.
>
> Neden teknoparkta? Üç şey aynı anda burada: 4691 kurallarının ilk kullanıcıları, yapay zekâ tarafındaki akademik danışmanlık, ve ölçümlerimizi gözden geçirecek bağımsız göz. Bağımsız gözden geçirmeyi kendi lehimize değil, sonucun güvenilirliği için istiyoruz.
>
> Son cümlem: araştırma sorusu düşerse bile ürün çalışır, çünkü doğruluğu model değil motor taşıyor. Hesabı motor yapar, bulguyu model inceler, kararı insan verir.
>
> Teşekkür ederim, sorularınızı almaktan memnuniyet duyarım.

**Çıpa cümle:** Bu alanda eksik olan şey model değil, ölçüm.

**Sorarlarsa:** Teknoparka taahhütlerimiz: 4 kişiyle başlayıp 6'ya çıkmak, beş bölge firmasına 4691 ön sürümü, iki seminer, TTO ile ortak bildiri.

**Son saniye:** Cümleyi bitirdikten sonra susun. Doldurma cümlesi kurmayın; ilk soruyu bekleyin.

---
---

# SORU-CEVAP İÇİN

## İlk otuz saniyede yapılacaklar

1. **Soruyu tekrar edin.** Hem düşünme süresi kazanırsınız hem yanlış anlaşılmayı önlersiniz.
2. **Hangi slayta ait olduğunu söyleyin** ve o slayta dönün. Şemaya bakarak cevap vermek sözle cevap vermekten güçlüdür.
3. **Cevabınız bir sayı içeriyorsa neyin içinde olduğunu da söyleyin.** "Yüzde 70" değil, "üç ila beş aday arasından yüzde 70".

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
3. **Dosyayı aşmayın.** Sunumda söylediğiniz her taahhüdün başvuru dosyasında karşılığı olmalı.

## Terim gelirse ne diyeceksiniz

Hakem teknik terimi kullanırsa paniğe gerek yok; terim sizin de terimeniz. Bir kez karşılığını söyleyin, sonra devam edin.

| Hakem şunu sorarsa | Siz şöyle başlayın |
|---|---|
| "Abdüktif çıkarım nasıl işliyor?" | "Farkın sebebini bulma kısmı. Kural defteri bütün olası sebepleri üretiyor, model onları sıralıyor…" |
| "Bitemporal modeli nasıl kurdunuz?" | "İki tarih birden tutuyoruz: kuralın geçerli olduğu ay, ve o bilgiyi öğrendiğimiz tarih…" |
| "Şema zorlaması ne demek?" | "Model serbest metin yazmıyor, boş bir form dolduruyor…" |
| "Erişim destekli üretim yeterli olmaz mı?" | "Bunu ölçüyoruz; beş kolun üçüncüsü tam olarak bu…" |
| "Halüsinasyon oranınız kaç?" | "Kendi eşiğimiz desteksiz iddia için yüzde bir; ölçtüğümüz kör test setinde raporlayacağız…" |
