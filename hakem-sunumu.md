# HAKEM SUNUMU: Denetci.AI

*İstanbul Medeniyet Üniversitesi Teknopark A.Ş. proje değerlendirme sunumu. Kaynak belge: `denetci-proje-bilgi-formu.md`. Akademik kaynakların tam künyesi: `ek-7-akademik-kaynakca.md`. Hakem sorularına hazırlık: `hakem-sunumu-soru-cevap.md`.*

---

## Sunum hakkında

**Hedef süre:** 20 dakika sunum + soru-cevap. 21 ana slayt, ortalama 55 saniye.

**15 dakikaya indirmek gerekirse:** 14 (Ekip), 15 (Bütçe), 18 (Rekabet) ve 19 (Veri yönetimi) slaytları hızlı geçilir; içerikleri yedek slaytlarda ve soru-cevap bankasında hazırdır.

**Dil kuralları:** Her kısaltma ilk kullanımda açılmıştır. Mutlak rekabet üstünlüğü iddiası kurulmamıştır. Her sayısal hedef, ölçüm ayı ve test setiyle birlikte verilmiştir. Literatürden gelen her rakamın künyesi EK-7'dedir.

**Heyet karması:** Yapay zekâ akademisyeni, teknopark yönetimi, sektör temsilcisi. Slaytlar üçünün de anlayacağı dilde yazılmıştır; teknik derinlik konuşma metnindedir.

---
---

# BÖLÜM 1: PROBLEM VE ÇÖZÜM (Slayt 1-4, ~4 dakika)

---

## Slayt 1 — Kapak

> ### Denetci.AI
> ### Denetçi Rolünde Nöro-Sembolik Yerel Yapay Zekâ
>
> **Hesabı motor yapar, bulguyu model inceler, kararı insan verir.**

- ARGELOG A.Ş. | Proje kodu: ARGELOG-002 | Proje yöneticisi: Murat Haksal
- 12 ay | 39 adam-ay (31 Ar-Ge + 8 geliştirme) | 7.000.000 ₺ | 4 kişi
- Kapsam: 5746 sayılı Kanun (Ar-Ge ve Tasarım Merkezleri) ve 4691 sayılı Kanun (Teknoloji Geliştirme Bölgeleri)
- Teknoloji Hazırlık Seviyesi (THS): 5'ten 7'ye
- Dört araştırma sorusu: slaytlarda AS-1'den AS-4'e kısaltılmıştır

**Görsel:** Sade kapak. Altta üç kutulu şerit: MOTOR (hesaplar) → MODEL (inceler) → İNSAN (karar verir).

**Konuşma metni:**
> Teşekkür ederim. Projemizin adı Denetci.AI. Tam adı "Denetçi Rolünde Nöro-Sembolik Yerel Yapay Zekâ"; bu mimarinin teknik adı nöro-sembolik ve terimi hemen açayım. Sembolik taraf, kurallarla kesin hesap yapan bir motordur; aynı girdiye her zaman aynı sonucu verir. Nöral taraf ise öğrenen bir dil modelidir. Projemiz bu ikisini tek sistemde birleştiriyor.
>
> Projeyi tek cümleyle anlatayım: hesabı motor yapar, bulguyu model inceler, kararı insan verir. Motor, bir kuruluşun Ar-Ge ve teknopark teşvik beyanlarını, o dönemde yürürlükte olan mevzuatla bağımsız olarak yeniden hesaplar. Yanına da bulunan farkı bir denetçi gibi inceleyen, kurum içinde çalışan küçük bir yapay zekâ modeli koyuyoruz.
>
> Dört araştırma sorumuz var. Slaytlarda bunları AS-1'den AS-4'e kadar kısaltarak göstereceğim; üçü yapay zekâ bileşenine, biri onun dayandığı kural tabanına ait.

---

## Slayt 2 — Problem: hesap elektronik tabloda, geçmiş dönem yeniden kurulamıyor

- 1.373 Ar-Ge ve 347 Tasarım Merkezi; toplam 1.720 kuruluş (Haziran 2026)
- 113 teknoloji geliştirme bölgesinde 13.452 firma, 134.686 personel (Ağustos 2026)
- Ar-Ge personeli başına yıllık teşvik yaklaşık bir milyon TL mertebesinde
- Elektronik tablo bugünün oranlarıyla üzerine yazılır; eski hesabın kural sürümü kalmaz
- Farkı yorumlayacak uzman kıt ve pahalı; hata en geç, en pahalı anda çıkar

**Görsel:** İki kutu. Solda "Bugün: elektronik tablo + yıllık danışmanlık", sağda "Denetimde: üç yıl önceki rakam nasıl kuruldu?" ve arada kopuk bir zincir halkası.

**Konuşma metni:**
> Türkiye'de 1.720 Ar-Ge ve Tasarım Merkezi, 13.452 teknopark firması var. Bunların her biri her ay bordroyla iç içe geçmiş teşvik hesapları yapıyor: gelir vergisi stopajı teşviki, sigorta primi işveren desteği, damga vergisi istisnası, kurumlar vergisi indirimi. Bir Ar-Ge personeli başına yıllık teşvik yaklaşık bir milyon TL mertebesinde; 150 kişilik bir merkezde yılda yüz milyon TL düzeyinde bir akıştan söz ediyoruz.
>
> Bu akış bugün büyük ölçüde elektronik tabloda yönetiliyor. Elektronik tablonun iki yapısal sorunu var. Birincisi, oranlar değiştiğinde tablo üzerine yazılıyor; üç yıl önceki bir rakamın hangi mevzuat sürümüyle nasıl kurulduğunu gösteren bir kayıt kalmıyor. Denetime girdiğinizde, o rakamı savunacak belgeye sahip değilsiniz.
>
> İkincisi ve bizim için daha önemlisi: bir fark bulunduğunda, o farkın ne anlama geldiğini yorumlamak, doğru soruyu sormak ve hangi belgeye bakılacağını belirlemek tamamen uzman emeğine bağlı. Bu emek kıt, pahalı ve ölçeklenemez. Sonuç olarak hatalar çoğunlukla denetimde, düzeltme maliyetinin en yüksek olduğu anda ortaya çıkıyor.

*Kaynak: T.C. Sanayi ve Teknoloji Bakanlığı istatistikleri. Sürekli denetim literatürü: EK-7 bölüm 9.*

---

## Slayt 3 — Yapay zekâ evet, ama hesaplayıcı koltuğunda değil

- Hukuki sorularda dayanaksız yanıt: ChatGPT-4'te %58, Llama 2'de %88 *(Dahl vd., 2024)*
- Hukuka özel ticari araçlarda bile dayanaksız iddia %17-33 *(Magesh vd., 2025)*
- Dünya genelinde 2.041 mahkeme kararı, dosyaya sunulmuş uydurma atıf tespit etti
- Soruya alakasız tek cümle eklenince başarı %65'e varan oranda düşüyor *(Mirzadeh vd., 2025)*
- Halüsinasyon bir arıza değil, ölçme biçiminin yapısal sonucu *(Kalai vd., 2026, Nature)*

**Görsel:** Dört büyük rakam kartı: %58 / %17-33 / 2.041 / %65. Altta tek satır: "Bu yüzden model hesaplamıyor."

**Konuşma metni:**
> Şimdi projenin en kritik tasarım kararına geleyim: neden yapay zekâyı hesaplayıcı koltuğuna oturtmuyoruz.
>
> Stanford ekibinin 2024'te Journal of Legal Analysis'te yayımladığı ölçüm, gerçek mahkeme kararları hakkında doğrulanabilir sorular sorulduğunda ChatGPT-4'ün yüzde 58, Llama 2'nin yüzde 88 oranında dayanaksız yanıt ürettiğini gösterdi. "Genel model kullanmayız, hukuka özel araç kullanırız" diyebilirsiniz; aynı ekibin 2025'teki ikinci çalışması, hukuk alanının en pahalı ticari erişim destekli araçlarında bile dayanaksız iddia oranının yüzde 17 ile 33 arasında kaldığını ölçtü.
>
> Bu akademik bir kaygı da değil. Bugün itibarıyla dünya genelinde 2.041 mahkeme kararı, dosyaya sunulan belgelerde yapay zekânın uydurduğu atıf bulunduğunu tespit etmiş durumda.
>
> Ve bu davranış giderilebilir bir hata değil. Bu yıl Nature'da yayımlanan çalışma, modellerin halüsinasyon üretmesinin gizemli bir arıza değil istatistiksel bir zorunluluk olduğunu gösteriyor: modeller, tıpkı zor bir sınavda boş bırakmak yerine tahmin yürüten öğrenciler gibi, bilmediklerini itiraf etmek yerine tahmin etmeye ödüllendiriliyorlar.
>
> Bizim alanımızda bir tutarın yüzde 17 ihtimalle uydurma olması kabul edilebilir değil. Bu yüzden yapay zekânın rolünü bilinçli olarak daralttık.

*Tam künyeler ve ölçüm tanımları: EK-7 bölüm 2.*

---

## Slayt 4 — İş bölümü: hesabı motor yapar, bulguyu model inceler, kararı insan verir

- **Motor:** Beyanı, o dönemin kural sürümüyle bağımsız olarak yeniden hesaplar
- **Model:** Farkı denetçi gibi inceler, yorumlar, soru sorar, kanıt belgesi ister
- Model hiçbir aşamada tutar hesaplamaz; bu ayrım kod düzeyinde ve denetim iziyle kanıtlanır
- Her mevzuat atfı kural tabanına karşı doğrulanır; karşılığı olmayan iddia elenir
- Karar insanda: Yeminli Mali Müşavirin (YMM) tasdik yetkisi ve sorumluluğu değişmez

**Görsel:** Döngü şeması. Motor → fark → Model (yorum + soru + belge talebi) → Doğrulama kapısı → İnsan → belge → Motor. Kapının altında elenen bulguların "eğitime geri dön" oku.

**Konuşma metni:**
> İş bölümümüz şu. Motor hesaplar. Bulduğu farkı model inceler: bu fark ne anlama geliyor, hangi kural sürümünün uygulanmamasıyla tutarlı, bir denetçi burada ne sorardı, hangi belgeyi istemeli. Model bu belgeyi işaret eder, belge getirilir, motor yeniden koşar ve döngü kapanır.
>
> Buradaki asimetri projenin can damarı: model bir hata yaparsa sonuç yanlış bir tutar değil, gereksiz bir inceleme adımıdır. Çünkü model hesaba hiç girmiyor; bu ayrım kod düzeyinde kurulu ve denetim iziyle kanıtlanabiliyor.
>
> Literatürde bu yaklaşımın adı var. Gao ve arkadaşlarının program destekli dil modelleri çalışması, modelin problemi doğru parçalasa bile hesap adımında hata yaptığını, hesabı deterministik bir yürütücüye devretmenin bu hatayı ortadan kaldırdığını gösteriyor. Kambhampati ve arkadaşları bunu bir adım ileri götürüp şunu söylüyor: dil modelleri kendilerini doğrulayamaz, ama dış ve model tabanlı doğrulayıcılarla çevrelendiklerinde güçlü fikir üreticisi olurlar. Bizim sembolik doğrulama kapımız tam olarak böyle bir dış doğrulayıcıdır.
>
> Son olarak: karar insanda kalıyor. Ürün beyan üretmiyor, beyanname göndermiyor, tasdik etmiyor.

*Kaynaklar: EK-7 bölüm 1.*

---
---

# BÖLÜM 2: BİLİMSEL ÇEKİRDEK (Slayt 5-10, ~7 dakika)

---

## Slayt 5 — Mimari: üç katman, model hesaba hiç girmez

- **Sembolik katman:** Deterministik hesap çekirdeği, zaman-farkındalıklı kural tabanı, sembolik teşhis
- **Nöral katman:** Denetçi rolünde, 1-4 milyar parametreli, dar kapsamlı yerel model
- **Bağlantı katmanı:** Sembolik doğrulama kapısı; belge gelir, motor koşar, döngü kapanır
- Grafik işlemci gerekmez; internet gerekmez; bordro verisi kurum dışına çıkmaz
- **Başarısızlık eşiği:** 16 GB bellekli, grafik işlemcisiz bilgisayarda bulgu başına ≤30 saniye

**Görsel:** Üç yatay katman, aralarında tek yönlü oklar. Sembolik katmandan nöral katmana "bulgu", nöral katmandan kapıya "yorum + belge talebi"; nöral katmandan hesaba giden ok YOK ve bu boşluk kırmızı kesik çizgiyle işaretli.

**Konuşma metni:**
> Mimarimiz üç katmanlı. Altta sembolik katman: her fonksiyonu mevzuat maddesine atıflı deterministik hesap çekirdeği, parametre ve hesap şeması sürümlenen kural tabanı, ve farkı açıklayabilecek hipotez kümesini eksiksiz üreten sembolik teşhis.
>
> Üstte nöral katman: 1 ila 4 milyar parametre sınıfında, dar kapsamlı, kurum içinde çalışan bir model. Bu boyut bilinçli bir tercih. Modelden istediğimiz iş açık uçlu üretim değil; kapalı bir kök neden kümesinde sınıflandırma, hipotez sıralama ve sonlu bir belge listesinden bir sonraki adımı seçme. Bu tür dar görevlerde küçük modellerin yeterli olduğuna dair kanıt var: Hsieh ve arkadaşlarının çalışmasında 770 milyon parametreli bir model, dar bir görevde 540 milyar parametreli bir modeli geçebiliyor.
>
> Ortada bağlantı katmanı, yani doğrulama kapısı.
>
> Burada bir terimi açayım: slaytlarda "başarısızlık eşiği" göreceksiniz. Her araştırma sorumuza önceden bir eşik yazdık. Eşiği tutturamazsak o soruyu olumsuz sonuçlandı diye raporlarız; sonucu değiştirmeyiz, eşiği de değiştirmeyiz.

*Kaynaklar: EK-7 bölüm 1, 4 ve 5.*

---

## Slayt 6 — Araştırma Sorusu 1 (AS-1): Denetçi rolü küçük bir modele öğretilebilir mi?

- Etiketi insan değil, doğrulanmış deterministik motor koyar; motor referans kaynağıdır (oracle)
- Dört görev: bulgu yorumlama, araştırma yönlendirme, denetçi sorusu üretme, belge alan çıkarımı
- **Yönlendirmede etiket otomatik:** önerilen belge getirilir, motor koşar, fark çözüldü mü?
- Hacim: ≥60 senaryodan ~2.000-3.000 örnek (ay 7); ≥400 vakadan ~1.500-2.500 örnek (ay 8); pilot başına ≥200 gerçek fark kalemi (ay 10-12)
- **Başarısızlık eşiği (ay 10 laboratuvar, ay 12 saha):** yönlendirme isabeti ≥%70; ince ayarsız temel modele karşı ≥15 puan; uzmanın bulgularının ≥%80'i yakalanır; denetçi sorusu nitelenme oranı ≥%70

**Görsel:** Veri hattı şeması: senaryo/enjeksiyon/pilot → MOTOR → fark imzası + kural sürümü → dört görev için girdi-çıktı çifti → şema doğrulaması → eğitim/test bölmesi. G2 kutusunun yanında "etiketi motor koyar" rozeti.

**Konuşma metni:**
> Birinci araştırma sorumuz: bir denetçinin yaptığı ön inceleme işi, küçük ve yerel bir modele öğretilebilir mi?
>
> Buradaki asıl zorluk eğitim verisidir. Bu göreve klasik anlamda etiketli veri üretmek mümkün değil; alan uzmanının binlerce örneği elle etiketlemesi gerekirdi. Bizim yaklaşımımız farklı: doğrulanmış deterministik motoru referans kaynağı olarak kullanıyoruz. Motorun ürettiği fark imzaları, karşı olgusal çift hesap sonuçları ve uygulanan kural sürümü birlikte eğitim çiftleri oluşturuyor.
>
> En güçlü olduğumuz yer araştırma yönlendirme görevi. Orada etiket bir yargı değil, mekanik bir olgu: önerilen belgeyi getir, motoru yeniden koş, fark kapandı mı kapanmadı mı. İnsan yorumuna hiç açık değil. Bunun literatürde emsali var; Toolformer çalışması, bir modelin araç çağırmayı elle etiketlenmiş veri olmadan, otomatik bir yararlılık ölçütüyle öğrenebildiğini gösterdi.
>
> Dürüst olayım: insan üç yerde devrede. Sentetik senaryoların mevzuat referansını yazarken, pilot mutabakat oturumlarında kapanış kararını verirken, ve kör test setini onaylarken. Yani "hiç insan yok" demiyoruz; yönlendirme görevinde etiketi hiç kimse elle koymuyor diyoruz.
>
> Sentetik veri riskini de biliyoruz. Nature'da yayımlanan çalışma, modelin kendi ürettiği veriyle özyinelemeli eğitilmesinin geri dönüşsüz çöküşe yol açtığını gösterdi. Bizde özyineleme yok: veriyi model değil, 96 gerçek dönemde kuruş farksız doğrulanmış motor üretiyor.

*Kaynaklar: EK-7 bölüm 4. Veri üretim yöntemi: EK-6.*

---

## Slayt 7 — Araştırma Sorusu 2 (AS-2): Doğrulama kapısı dayanaksız iddiayı kullanıcıya ulaştırmaz

- Modelin her atfı (madde, kural sürümü, dönem, belge türü) kural tabanına karşı doğrulanır
- Karşılığı olmayan bulgu elenir; eleme kaydı bir sonraki ince ayara olumsuz örnek döner
- Çıktı şema zorlamalı üretilir; model kural tabanı dışına çıkan ifade kuramaz
- Modeller kendi akıl yürütme hatasını düzeltemez; doğrulama dışsal ve sembolik olmalıdır
- **Başarısızlık eşiği (ay 10):** atıf doğruluğu ≥%98; desteksiz iddia ≤%1; kapının haklı bulguyu eleme oranı ayrıca ölçülür ve raporlanır

**Görsel:** Huni şeması. Model bulguları → kapı (iki soru: madde var mı? o dönemde yürürlükte miydi?) → kullanıcıya geçenler / elenenler. Elenenlerden eğitime geri dönen ok.

**Konuşma metni:**
> İkinci araştırma sorusu: küçük bir modelin ürettiği gerekçeler, sembolik bir kural tabanına karşı doğrulanarak kanıta bağlı tutulabilir mi?
>
> Dil modellerinin bilinen zayıflığı akıcı ama dayanaksız iddia üretmeleri. Mevzuat alanında bu, var olmayan bir maddeye atıf ya da o dönemde yürürlükte olmayan bir kurala dayanma biçiminde çıkıyor. Bizde modelin her çıktısı şema zorlamalı üretiliyor ve içindeki her atıf kural tabanına karşı iki soruya tabi tutuluyor: bu madde var mı, ve o dönemde yürürlükte miydi? Karşılığı olmayan bulgu kullanıcıya ulaşmadan eleniyor, eleme kaydı da modelin bir sonraki ince ayar turuna olumsuz örnek olarak dönüyor.
>
> Bunu neden model kendi kendine yapamıyor? Çünkü yapamadığı ölçüldü. Huang ve arkadaşlarının ICLR 2024 çalışması, dil modellerinin dışarıdan geri bildirim almadan akıl yürütme hatalarını düzeltemediğini, hatta kendini düzeltme denemesinin çoğu kez performansı düşürdüğünü gösterdi. Doğrulamanın dışsal olması zorunlu.
>
> Bir noktayı kendim söyleyeyim: kapı doğru bulguları da eleyebilir. Bunu ölçmeyi taahhüt ediyoruz. Ama en kötü sonucu şu: kapı yanlış elerse kullanıcı, bugün olduğu gibi yorumsuz bir farkla kalır. Kapı hiçbir tutarı gizlemiyor; motorun bulduğu fark her koşulda kullanıcıya gidiyor. Elenen şey tutar değil, yorumdur.

*Kaynaklar: EK-7 bölüm 1 ve 3.*

---

## Slayt 8 — Araştırma Sorusu 3 (AS-3): Farkı bulmak kolay, nedenini atamak zor

- Farkı bulmak deterministiktir ve rutin yazılımdır; belirsizlik, nedenin atanmasındadır
- Yuvarlama, kapsam farkı, kısmi çalışma, üst sınır, oran farkı, veri eksiği: **aynı fark görüntüsü**
- Sembolik katman hipotez kümesini eksiksiz ve kanıtlı üretir; nöral katman bağlama göre sıralar
- Ayırt edilemeyen kalem tek nedene zorlanmaz; dürüstçe "belirsiz" raporlanır
- **Başarısızlık eşiği (ay 10/12):** kalem bazında ≥%85 doğru sınıflandırma; doğru neden ilk üç hipotezde ≥%90; belirsiz **tutar** payı ≤%5

**Görsel:** Solda tek bir fark tutarı, sağda ondan çıkan altı olası neden oku. Altta iki metrik kutusu, birinin paydası "kalem", diğerininki "tutar" olarak vurgulanmış.

**Konuşma metni:**
> Üçüncü soru teşhisle ilgili. Farkı bulmak deterministiktir; iki sayıyı çıkarırsınız. Asıl belirsizlik, farkın nedenine güvenilir biçimde atanmasında.
>
> Bu klasik bir tanımlanabilirlik problemidir: yuvarlama, kapsam-personel farkı, kısmi çalışma, üst sınır bağlaması, oran farkı, veri eksiği ve gerçek hata matematiksel olarak aynı fark görüntüsünü üretebilir. Üstelik farklar hesap kalemleri arasında zincirleme yayılır.
>
> Bu problemin yapay zekâda kırk yıllık bir literatürü var. Reiter'ın 1987'deki birinci ilkelerden teşhis kuramı, teşhisi tek bir tahmin değil, çelişkiyi giderebilecek aday kümelerinin tümünün hesaplanması olarak tanımlar. Aynı sayıda de Kleer ve Williams çoklu hata teşhisini kurar ve bir adım daha atar: adayları en çok ayrıştıracak bir sonraki ölçüm hangisidir? Bizim "hangi belgeyi istemeli" görevimiz tam olarak budur.
>
> İş bölümümüz şu: sembolik katman doğruluğu taşır, kümeyi eksiksiz üretir. Nöral katman verimliliği taşır, kümeyi kuruluşun bağlamına göre sıralar.
>
> Bir soruyu ben sorayım: zor vakaların hepsini "belirsiz" etiketleyip yüzde 85'i kolayca tutturamaz mısınız? İki metriği bilerek birbirine kilitledik. Doğruluk kalem bazında ölçülüyor, belirsiz payı ise tutar bazında ve tavanı yüzde 5. Zor vakaları belirsize atmak tutar payını şişirir ve ikinci metriği kırar.

*Kaynaklar: EK-7 bölüm 6.*

---

## Slayt 9 — Araştırma Sorusu 4a (AS-4): Her dönem kendi kuralıyla hesaplanır

- Üç ayrı eksende sürümleme: **oran/parametre**, **hesap şeması**, **bilgi tarihi**
- 2022'de asgari geçim indiriminin kaldırılması matrahın *tanımını* değiştirdi: parametre değil, şema kırılması
- 7555 sayılı düzenlemenin ücret tavanı 01.08.2025'te **ay ortasında** yürürlüğe girdi: dönem anahtarı kırıldı
- Düzeltme beyannameleri, aynı döneme farklı bilgi tarihleriyle birden çok geçerli sürüm yaratır
- **Başarısızlık eşiği (ay 7):** doğrulanmış gerçek beyan çapası 96'dan ≥140'a; parametresiz koşumda sıfır regresyon

**Görsel:** Zaman ekseni üzerinde üç paralel şerit (oran / şema / bilgi tarihi), iki kırmızı dikey çizgi: 2022 AGİ ve 01.08.2025 ay ortası.

**Konuşma metni:**
> Dördüncü soru, modelin dayanacağı kural tabanıyla ilgili. Modelin her atfının doğrulanabilmesi, kural tabanının her dönem için "o gün yürürlükte olan" kuralı kesin olarak bilmesini gerektiriyor.
>
> Mevzuat değişikliklerinin bir kısmı sadece bir oranı değiştirir; bunlar kolaydır. Bir kısmı ise hesaba giren büyüklüğün tanımını değiştirir. İki somut örnek vereyim. 2022'de asgari geçim indiriminin kaldırılması, ücret istisnası matrahının tanımını değiştirdi; bu bir parametre değişikliği değil, şema kırılmasıdır. İkincisi: 7555 sayılı düzenlemenin ücret tavanı 1 Ağustos 2025'te, yani ay ortasında yürürlüğe girdi ve dönem anahtarının kendisini kırdı.
>
> Üçüncü eksen bilgi tarihi. Aynı döneme ait düzeltme beyannameleri, farklı bilgi tarihleriyle birden çok geçerli sürüm yaratır. Kapanmış bir dönemi, o günkü bilgi durumuyla yeniden üretebilmek gerekir.
>
> Bu problemin veritabanı literatüründe adı var: geçerlilik zamanı ve işlem zamanı ayrımı, ve SQL:2011 standardında dilin içine alınmış durumda. Mevzuat metinleri için kurulan zamansal veri modelleri de mevcut. Bizim katkımız bu üç ekseni bir teşvik rejiminin hesap mantığıyla birleştirmek.
>
> Eşiğimiz somut: bugün YMM teyitli 96 gerçek çapamız var, bunu en az 140'a çıkaracağız. Ve motor seviyesinde sert bir kural koyduk: bir ayın oranları doğrulanmadan, o ay için ne hesap ne rapor üretilir. Bu bir uyarı değil, motorun içine gömülü bir engel.

*Kaynaklar: EK-7 bölüm 8. Not: kural tabanı geçmiş dönemleri kapsar; cari yıl parametreleri yürürlük tarihinde YMM teyidiyle eklenir.*

---

## Slayt 10 — Araştırma Sorusu 4b (AS-4): Kuralın ne kadarı kod yazmadan ifade edilebilir?

- Sorumuz: bir teşvik rejiminin ne kadarı koddan çıkarılıp kural dosyasına taşınabilir?
- 4691 uygun bir sınama alanıdır: ücret istisnası eğitim derecesinden bağımsız, kazanç matrahı farklı kurulur
- **Rejim sınırı denetimi:** iki rejimi bir arada yürüten kuruluşta personel, ücret ve kazancın paylaştırılması
- 5746 sayılı Kanun'un 4. maddesi aynı kazançtan çifte yararlanmayı yasaklar; sistem bu sınırı denetler
- **Başarısızlık eşiği (ay 8):** 4691 kurallarının ≥%90'ı kod yazılmadan tanımlanabilmeli; çekirdekte rejime özgü kaçış ≤3; 5746'da sıfır regresyon; ≥20 çifte istisna vakasının tamamı yakalanır

**Görsel:** İki daire (5746 ve 4691) ve kesişimleri. Kesişimin üstünde "5746 md. 4: mükerrer yararlanma yasağı" etiketi.

**Konuşma metni:**
> Aynı sorunun ikinci yarısı: rejime özgü mantığın ne kadarı koddan çıkarılıp bildirimsel kural dosyalarına taşınabilir? Bu sınır tasarım öncesinde bilinemez; ölçülerek bulunur.
>
> 4691 iyi bir sınama alanı, çünkü rejim yalnız parametrede değil mantıkta ayrışıyor: ücret gelir vergisi istisnası eğitim derecesinden bağımsız işler, kazanç istisnası matrahı farklı kurulur.
>
> Asıl zor kısım şu: bu iki rejim ayrı müşteri segmentleri değil. Çok sayıda kuruluşta bir arada bulunuyorlar; aynı firma tesisinde Ar-Ge Merkezi işletirken teknopark bölgesinde de şirket bulunduruyor. 5746 sayılı Kanun'un 4. maddesi aynı kazanç üzerinden 4691 istisnasından ayrıca yararlanılmasını yasaklıyor. Dolayısıyla personelin, ücretin ve kazancın rejimler arasında doğru paylaştırılması ve bu ayrımın denetimde belgelenebilmesi gerekiyor. Biz iki kural setini toplamıyoruz; aralarındaki sınır koşullarını modelliyoruz.
>
> Bu yaklaşımın kökü 1986'ya dayanıyor: Imperial College ekibi İngiliz Vatandaşlık Kanunu'nun tamamını mantık programına çevirerek bir kanunun doğrudan çalıştırılabilir kurala dönüştürülebileceğini gösterdi. Bugün Fransa'da vergi mevzuatı için tasarlanmış Catala gibi diller var. Bizim sorumuz o çalışmaların sormadığı bir soru: bir teşvik rejiminde bu oran pratikte ne çıkıyor?
>
> Son olarak bir soruyu peşinen cevaplayayım. 2028'de yeni bir tebliğ çıkarsa modeli yeniden mi eğiteceğiz? Hayır. Yeni bir tebliğ, yeni bir kural sürümü dosyasıdır. Model parametre, oran ve limit taşımıyor; sadece fark imzasını yorumluyor ve kural tabanına atıf yapıyor.

*Kaynaklar: EK-7 bölüm 7.*

---
---

# BÖLÜM 3: YÖNTEM, PLAN VE ÖLÇME (Slayt 11-16, ~6 dakika)

---

## Slayt 11 — Ölçüm düzeneği: kör karşılaştırma, sızıntısız bölme

- **Beş karşılaştırma kolu:** ince ayarlı model | ince ayarsız aynı model | ince ayarsız model + kural tabanı erişimi | alan dışı genel model | uzman denetçi
- AS-3 için ayrıca sembolik taban çizgisi: nöral sıralamanın kazancı buna karşı ölçülür
- Yönlendirmede etiketi motor koyar; bulgu yorumu ve denetçi sorusunda YMM etiketli kör örneklem
- **Sızıntı ve kalite kontrolü dört adım (EK-6 §4):** kuruluş ve dönem bazlı bölme (aynı kuruluşun aynı dönemi hem eğitimde hem testte bulunamaz); şema geçerliliği denetimi; kök neden sınıflarının ve "belirsiz" sınıfının dengelenmesi; eğitim öncesi anonimleştirme
- Eşikler ve kör test seti **ay 7'de mühürlenir**; ölçümden sonra eşik de payda da değişmez

**Görsel:** Beş kollu karşılaştırma şeması ve altında bir kilit ikonu: "Ay 7: eşikler mühürlenir, TTO ve YMM nezdinde saklanır."

**Konuşma metni:**
> Ölçüm düzeneğimiz projenin en çok emek verdiğimiz kısmı, çünkü bir yapay zekâ iddiası ancak ölçüm düzeneği kadar değerlidir.
>
> Beş karşılaştırma kolumuz var. İnce ayarlı modelimiz; aynı modelin ince ayarsız hâli; kural tabanını bağlam olarak alan erişim destekli kol; alan dışı genel bir model; ve uzman denetçi. Üçüncü kol özellikle önemli, çünkü "neden erişim destekli üretim yetmiyor da ince ayar gerekiyor" sorusunun cevabını tahmine değil ölçüme bağlıyor.
>
> AS-3 için bir kol daha ekliyoruz: hipotezleri önceki dönem sıklığına göre sıralayan kural tabanlı basit bir sezgisel. Nöral katmanın kazancını buna karşı ölçüyoruz. Kazanç yoksa üründe ucuz olanı kullanırız ve bunu olumsuz sonuç olarak raporlarız.
>
> Sızıntıya karşı dört kontrolümüz var ve dördü de EK-6'da yazılı. En güçlü koruma ise metriğin kendisinde: yönlendirme metriği ezberlenemez, çünkü ölçüm bir etiket dizesini eşleştirmek değil, motoru fiilen yeniden koşturmaktır.
>
> Ve en önemli taahhüdümüz: bütün eşikler ve kör test seti ay 7'de mühürlenip Teknoloji Transfer Ofisi ile YMM nezdinde yazılı olarak saklanacak. Ölçümden sonra ne eşiği ne paydayı değiştiririz.

*Not: kör test setinin bir kısmının iki bağımsız YMM tarafından etiketlenmesi ve uyum katsayısının raporlanması önerilir; bu, EK-6 §6'nın genişletilmesini gerektirir. Kaynak dönem kesişim taraması ve tamamen kör tutulan pilot da EK-6'da yoktur. Bkz. sunum sonu, "Karar bekleyen maddeler" A1 ve A7.*

---

## Slayt 12 — Her araştırma sorusu bir eşiğe bağlı, THS 5'ten 7'ye

| Soru | Eşik | Ölçüm ayı |
|---|---|---|
| **AS-1** | Yönlendirme isabeti ≥%70; temel modele karşı ≥15 puan; uzman bulgularının ≥%80'i | 10 ve 12 |
| **AS-2** | Atıf doğruluğu ≥%98; desteksiz iddia ≤%1 | 10 |
| **AS-3** | Kalem bazında ≥%85; ilk üç hipotezde ≥%90; belirsiz tutar ≤%5 | 10 ve 12 |
| **AS-4** | Çapa 96'dan ≥140'a; kural dosyasıyla kapsama ≥%90; kaçış ≤3 | 7 ve 8 |

- **THS 5 bugün:** hesap çekirdeği doğrulandı, denetçi model laboratuvar düzeyinde (THS 3); seviye en olgun bileşene göre değil, bütünleşme durumuna göre verildi
- **THS 7 hedefi:** iki sanayi kuruluşunun kendi ortamında, gerçek veriyle çalışan, uzmanla kör karşılaştırması yapılmış prototip. THS 8 iki pilotla gerçekçi bulunmadı

**Görsel:** Tablo ve yanında THS merdiveni; 5 dolu, 7 hedef, 8 soluk ve "ticarileşme fazı" etiketli.

**Konuşma metni:**
> Bu tablo sunumun omurgası. Dört sorunun her biri düşebilir, yani yanlışlanabilir bir eşiğe bağlı.
>
> Eşiklerin nereden geldiğini soracaksınız. Örnek vereyim: yüzde 70 yönlendirme isabeti literatürden alınmış bir sabit değil, iki referansa göre kondu. Birincisi rastgele taban: sembolik katmanın bir fark için ürettiği hipotez sayısı İP4 senaryo kütüphanesinde ölçülecek; ön gözlemimiz fark başına üç ila beş hipotez, yani rastgele seçim yüzde 20 ile 33 arası. Yüzde 70 bunun yaklaşık iki ila üç buçuk katı. İkincisi işin ekonomisi: bir belge talebinin kalemlerin yaklaşık yüzde 70'inde farkı çözmesi, uzmanın inceleme turunu üçten ikiye indirir. Bu ikinci gerekçe saha deneyimimize dayalı bir varsayımdır ve pilotlarda ölçülecektir.
>
> Teknoloji hazırlık seviyesine gelince. Bugün 5 diyoruz ama bu en olgun bileşenimize göre değil. Hesap çekirdeğimiz doğrulanmış durumda; denetçi model ise henüz laboratuvar düzeyinde, yani seviye 3. Bütünleşik sistem için beyan ettiğimiz seviye, bileşenlerin bütünleşme durumuna göre verildi.
>
> Hedefimiz 7. Kabul kanıtı da açık: iki sanayi kuruluşunun kendi işletme ortamında, gerçek bordro ve beyan verisiyle çalışan, uzman denetçiyle kör karşılaştırması yapılmış prototip; kanıtı pilot kapanış raporları ve baz sertifikası. Seviye 8'i iki pilotla iddia etmeyi gerçekçi bulmadık, ticarileşme fazına bıraktık.

---

## Slayt 13 — Yedi iş paketi, beş ölçüm kapısı

| İP | Kapsam | Ay | Adam/Ay | Nitelik |
|---|---|---|---|---|
| İP1 | Çekirdek devralma, aylık dönem çözünürlüğü | 1-2 | 3 | Ar-Ge |
| İP2 | Üç eksenli kural tabanı, çapa 96→140 | 1-7 | 6 | Ar-Ge (AS-4) |
| İP3 | 4691 kural seti, rejim sınırı | 5-8 | 3 | Ar-Ge (AS-4) |
| İP4 | Sembolik teşhis, ≥60 senaryo, ≥400 vaka | 4-10 | 9 | Ar-Ge (AS-3) |
| İP5 | **Denetçi model:** veri hattı, ince ayar, doğrulama kapısı | 6-12 | 10 | Ar-Ge (AS-1, AS-2) |
| İP6 | Masaüstü ürünleştirme, imzalı güncelleme | 8-12 | 5 | **Ar-Ge değil** |
| İP7 | İki ücretli saha pilotu, dört kapı | 9-12 | 3 | Destek |

- **Kritik yol:** İP2 (ay 7 kural tabanı) → İP5 doğrulama kapısı; İP4 setleri (ay 8) → İP5 ilk ince ayar
- **Ölçüm kapıları:** ay 7 kural tabanı | ay 8 rejim sınırı | ay 10 laboratuvar | ay 11 cari dönem | ay 12 saha
- Hesap çekirdeği proje öncesinde geliştirildi ve **başlangıç varlığı olarak beyan edildi**

**Görsel:** Gantt şeridi; beş ölçüm kapısı dikey çizgi olarak işaretli, kritik yol kalın okla.

**Konuşma metni:**
> Yedi iş paketimiz var ve her birinin adam-ayı, ayı ve çıkış kriteri yazılı. Adam-ayı tanımlanmamış hiçbir taahhüdümüz yok.
>
> Burada açıkça söylemem gereken bir şey var: deterministik hesap çekirdeği proje öncesinde firmamızda geliştirildi ve 96 çapa testiyle iç doğrulaması tamamlandı. Bunu başlangıç varlığı olarak beyan ettik. "O zaman Ar-Ge içeriği daralmıyor mu" diye sorabilirsiniz; tersi oluyor. Çalışan bir motorun üzerine kurduğumuz için Ar-Ge eforumuzun 19 adam-ayını doğrudan yapay zekâ bileşenine ve teşhis altyapısına ayırabiliyoruz. Projenin Ar-Ge iddiası çekirdeğin yazılması değil; aylık dönem ve üç eksenli sürümleme, abdüktif kök-neden teşhisi, modelin motordan üretilen veriyle eğitilmesi, ve sembolik doğrulama kapısıdır.
>
> Altıncı paketi Ar-Ge iddiası olarak öne sürmüyoruz ve bunu forma da böyle yazdık. Masaüstü ürünleştirme, kurulum sihirbazı, imzalı güncelleme; bunlar gerekli ama tek başlarına teknik belirsizlik içermiyor. İnce ayar, nicemleme ve şema zorlamalı çözümleme araçlarının kendisi de olgun araçlardır ve onları da Ar-Ge iddiası olarak sunmuyoruz.
>
> Takvim riskine karşı iki önlemimiz var. Ay 2-3'te, yani İP5 başlamadan önce, kısa bir fizibilite ölçümü yapıyoruz: açık ağırlıklı bir model, sentetik bir bulgu örneklemi, referans bilgisayarda süre ve ham isabet ölçümü. Ay 4'te karar kapısı. İkincisi, kapsam kısma sırası önceden yazılı: gecikme hâlinde önce ikinci ince ayar turu, sonra alan dışı karşılaştırma kolu çıkar. İP1'den İP3'e kadar olan sembolik omurga ve pilot mutabakatı hiçbir koşulda kısılmaz.

---

## Slayt 14 — Ekip: kim, hangi pakette, kaç adam-ay

| Kişi | İP1 | İP2 | İP3 | İP4 | İP5 | İP6 | İP7 | Toplam |
|---|---|---|---|---|---|---|---|---|
| Proje yöneticisi | 1 | 1 | – | 1 | 1 | 1 | 1 | **6** |
| Kıdemli yazılım geliştirici | 2 | 4 | 2 | 2 | – | 2 | – | **12** |
| **Yapay zekâ / DDİ mühendisi** | – | – | – | 3 | 8 | – | 1 | **12** |
| Analiz ve test-altyapı uzmanı | – | 1 | 1 | 3 | 1 | 2 | 1 | **9** |
| **Toplam** | 3 | 6 | 3 | 9 | 10 | 5 | 3 | **39** |

- Kıdemli geliştirici ve yapay zekâ mühendisi 12 ay tam zamanlı; ortalama 3,25 tam zaman eşdeğeri
- Proje personeli, firmanın danışmanlık kolundan **ayrı maliyet merkezinde** çalışır; hizmet kolu personeli bu 39 adam-aya dâhil değildir
- Ekipte bulunmayan mevzuat derinliği, 550.000 ₺'lik YMM dış hizmetiyle kapatılmıştır
- Yapay zekâ tarafında akademik danışmanlık, TTO aracılığıyla alınacaktır

**Görsel:** Efor matrisi tablosu; İP5 sütunu ve yapay zekâ mühendisi satırı vurgulu.

**Konuşma metni:**
> Dört kişilik çekirdek ekip, 39 adam-ay, ortalama 3,25 tam zaman eşdeğeri. Bu tablonun satır toplamları kişi eforlarına, sütun toplamları iş paketi adam-aylarına birebir eşit; çapraz okuyabilirsiniz.
>
> Projenin yapay zekâ ekseni tek bir role bağlı: İP5'in paket yöneticisi olan yapay zekâ ve doğal dil işleme mühendisi. Veri üretim hattı, ince ayar, doğrulama kapısı ve değerlendirme düzeneği bu kişide. Anahtar kişi riskini biliyoruz; İP5'in yordamları belgeleniyor, kıdemli geliştirici ilk aydan itibaren kod tabanına ortak erişimli, ve TTO akademik danışmanı yedek yürütme kapasitesi sağlıyor.
>
> Bir konuyu peşinen açayım, çünkü teknopark yönetiminin doğrudan denetlediği bir konu: proje personeli firmanın danışmanlık kolundan ayrı bir maliyet merkezinde çalışacak. Hizmet kolu personeli bu 39 adam-aya dâhil edilmedi. Bölge içi çalışma süreleri ve 240 saatlik bölge dışı görevlendirme kayıtları 4691 mevzuatına uygun olarak ayrı tutulacak.

---

## Slayt 15 — Bütçe: dokuz satır, her satır bir işe bağlı

| Harcama | Portal kategorisi | Tutar (₺) |
|---|---|---|
| 39 adam/ay × 130.000 ₺ | Personel Giderleri | 5.070.000 |
| YMM hizmeti: kural teyidi, parametre doğrulama, pilot denetimi, uzman etiketleme, hukuk görüşü | Hizmet Alımları | 550.000 |
| Kısa süreli bulut grafik işlemci kirası *(yalnızca sentetik ve anonim veriyle)* | Hizmet Alımları | 200.000 |
| Patent, marka, akademik danışmanlık | Hizmet Alımları | 250.000 |
| Lisans, kod imzalama, değerlendirme araçları | Hizmet Alımları | 200.000 |
| 3 iş istasyonu + 2 referans test bilgisayarı | Makina ve Teçhizat | 300.000 |
| Pilot saha ziyaretleri ve konferans katılımı | Seyahat | 230.000 |
| Test ortamı ve sarf | Sarf | 50.000 |
| Öngörülemeyen giderler | Genel Giderler | 150.000 |
| **Toplam** | | **7.000.000** |

- Bütçenin %72'si personel, %4,3'ü donanım; adam-ay birim maliyeti kırılımı **EK-3**'tedir
- 130.000 ₺ = brüt ücret + işveren maliyeti + genel gider payı

**Görsel:** Tablo; personel satırı vurgulu, altında yatay oranlı çubuk (%72 personel).

**Konuşma metni:**
> Bütçemiz portaldaki harcama kategorileriyle birebir eşleşen dokuz satır. Yüzde 72'si personel; bu bir yazılım Ar-Ge projesi için beklenen orandır. Donanım payı yüzde 4,3, yani bu bir ekipman alma projesi değil.
>
> İki kalemi özellikle açayım. YMM hizmeti 550.000 TL. Bu kalem projenin ölçüm altın standardını üretiyor: 5746 ve 4691 kural setlerinin madde madde teyidi, geçmiş parametre tablosunun Resmî Gazete referanslı doğrulanması, senaryo kütüphanesinin teyidi, iki pilotta mutabakat denetimi, ve kör değerlendirmede uzman etiketleme. Bu kalem olmadan ne kural tabanı doğrulanabilir ne kör karşılaştırma yapılabilir.
>
> İkincisi bulut grafik işlemci kirası, 200.000 TL. Burada haklı bir soru var: madem kapalı devre iddianız var, neden buluta çıkıyorsunuz? Cevabı net: buluta yalnızca eğitim için ve yalnızca sentetik senaryolar ile kimlik ve ücret alanları müşteri tarafında tutulan anahtarla tokenize edilmiş kayıtlar çıkıyor. Ham bordro verisi hiçbir koşulda çıkmıyor. Ürünün çalışması ise tamamen kurum içinde, grafik işlemcisiz.

---

## Slayt 16 — Risk ve karşılığı: başarısızlık hatalı tutar üretmez

| Risk | Erken uyarı | Önlem |
|---|---|---|
| Denetçi model eşiği tutmaz | Ay 4 fizibilite kapısı | AS-1 olumsuz raporlanır; **ürün sembolik katmanla eksiksiz çalışır** |
| Model dayanaksız iddia üretir | Kapıdan eleme oranı | Kapı eler, eleme kaydı eğitime döner; kapı başarımı ayrı ölçülür |
| Sentetikten gerçeğe aktarım zayıf | Ay 10 kör pilot ölçümü | Sentetik-gerçek uçurumu ayrı sayı olarak raporlanır |
| Geçmiş parametreler hatalı kurulur | Çapa regresyonu | Doğrulanmamış oranlı ay hesaplanmaz ve raporlanmaz |
| Pilot verisi gecikir | Veri odası takvimi | İki muhataplı protokol; dosya tabanlı yedek aktarım |
| Anahtar kişi ayrılır | İşe alım takvimi | Belgelenmiş yordamlar; ortak kod erişimi; TTO danışmanı |
| 30 saniye hedefi tutmaz | Ay 3 donanım ölçümü | Bulgu üretimi arka planda toplu işe alınır |

- **AS-4 kapsama hedefi tutmazsa:** doğrulama kapısı 4691 tarafında daraltılmış kapsamla çalışır ve bu kısıt üründe sert kural olur

**Görsel:** Risk tablosu; ilk satırın "Önlem" hücresi vurgulu.

**Konuşma metni:**
> Sunumun en önemli slaydı bu olabilir, çünkü hakem heyetinin haklı olarak soracağı soru şu: yapay zekâ bileşeni hedefe ulaşamazsa 7 milyon TL boşa mı gitmiş olur?
>
> Cevap hayır ve nedeni mimarinin kendisinde. Model hiçbir aşamada hesap yapmıyor. Dolayısıyla başarısızlığı hatalı bir tutar üretmek değil; ön incelemenin insan tarafından yapılmaya devam etmesi demek. Bu durumda AS-1'i olumsuz sonuçlu bir araştırma sorusu olarak, veri kaynağı ve hacim etkisi ölçümleriyle birlikte raporlarız. Bu da bilimsel bir çıktıdır. Ürün ise sembolik katman üzerinden eksiksiz çalışmaya devam eder: geçmiş dönem mutabakatı, kök-neden teşhisi, mühürlü baz, denetim savunma dosyası ve cari dönem kontrolü modele bağlı değil.
>
> Diğer risklerin her birinin erken uyarı göstergesi ve önlemi tabloda. Bir tanesini vurgulayayım: dördüncü araştırma sorusunda kapsama hedefi tutmazsa, doğrulama kapısı 4691 tarafında daraltılmış kapsamla çalışır ve model bulguları yalnızca kapsanan kalemlerde kullanıcıya ulaşır. Bunu üründe sert kural olarak uygularız.

---
---

# BÖLÜM 4: DEĞER, VERİ, TEKNOPARK (Slayt 17-21, ~3 dakika)

---

## Slayt 17 — Değer dört kanaldan gelir, fiyat danışmanlığa çıpalanır

- **Geri kazanım:** geçmiş dönemlerde eksik yararlanılan teşvikler tutar ve kök nedeniyle çıkar
- **Önlenen risk:** teşvik iadesi ve belge iptali, beyandan önce görülür
- **İş gücü kayması:** uyum için harcanan nitelikli emek Ar-Ge'nin kendisine döner
- **Uzman verimliliği:** aynı denetçi aynı sürede çok daha fazla dönem inceler
- Fiyat teorik teşvik hacmine değil, mevcut danışmanlık harcamasının marjinal artışına çıpalanır: ≤75 personelli merkezlerde yıllık 0,3-0,5 mn ₺; 76-200 personelli merkezlerde 0,5-0,9 mn ₺

**Görsel:** Dört kanal ikonu. Sağda "hizmet edilebilir pazar: 2.500-3.500 kuruluş *(saha deneyimine dayalı tahmin)*".

**Konuşma metni:**
> Ekonomik değer dört kanaldan geliyor. Geri kazanım toplantıyı açar, denetim savunulabilirliği sözleşmeyi kapatır. Ama süreklilik sağlayan üçüncü kanal cari dönem kontrolü: ürün her bordro döneminde çalıştığı için hata denetimde değil, oluştuğu ay yakalanıyor. Bu, muhasebe literatüründe otuz yıldır "sürekli denetim" diye adlandırılan yaklaşımın teşvik mevzuatına uygulanması.
>
> Dördüncü kanal denetçi modelin ölçeklenme etkisi: bugün her farkın yorumlanması uzman saati gerektiriyor; model bu ön incelemeyi üstlendiğinde uzman yalnızca karar noktasına çağrılıyor.
>
> Fiyatlama konusunda dürüst olayım: teorik teşvik hacmine çıpa atmıyoruz, çünkü o sayı satın alma kararını açıklamıyor. Müşterinin hâlihazırda ödediği mali müşavirlik harcamasının üzerine eklenen marjinal tutara çıpalıyoruz, ve bu bandı pilotlarda ölçeceğiz.
>
> Pazar tarafında: 1.720 Ar-Ge ve Tasarım Merkezi artı 113 bölgedeki 13.452 firmadan, 30 ve üzeri Ar-Ge personeli olan merkezler ve 10 ve üzeri istisna kapsamlı personel çalıştıran bölge firmaları filtresiyle 2.500-3.500 kuruluşluk bir hizmet edilebilir pazar çıkıyor. Bu bizim saha deneyimimize dayalı bir tahmindir ve varsayım olarak etiketlenmiştir.

---

## Slayt 18 — Rekabet: kategori boşluğu değil, özellik bileşimi

- Ağustos-Eylül 2026'da yedi ürün ve hizmet kategorisi kamuya açık materyalle tarandı (EK-1); bunlar dört rakip sınıfında toplanır. Beşinci sınıf olan genel amaçlı bulut yapay zekâ araçları taramaya değil mimari gerekçeye dayanır
- Yerli 5746/4691 yazılımları ve bordro/ERP modülleri ileriye dönük aylık hesaba odaklı
- Bordro/ERP modülleri tek sürümlü kural tablosuyla çalışır; geçmiş dönem kendi kural sürümüyle kurulamaz
- Yerli 5746/4691 yazılımlarında sürümleme ve geçmiş beyan mutabakatı, kamuya açık materyalde **ilan edilmiş bir yetenek olarak görülmemiştir** (EK-1, Ö1-Ö2)
- YMM hizmeti rakip değil dağıtım ortağı: tasdik yetkisini almıyoruz, tasdik dosyasını belgeli hâle getiriyoruz
- **İddia özellik bileşimidir:** mutabakat + sürümleme + kapalı devre + rejim sınırı + denetçi model. Tespit kamuya açık materyalle sınırlıdır; mutlak üstünlük iddiası içermez

**Görsel:** Dört ölçütlü karşılaştırma tablosu (EK-1'deki Ö1-Ö4), sütunlarda ürün kategorileri.

**Konuşma metni:**
> Rekabet konusunda abartılı bir iddiada bulunmayacağım. Kategori boş değil: yurt içinde 5746 hesaplaması yapan yerli yazılımlar var ve en az biri 4691 kapsamını da ilan ediyor.
>
> İncelediğimiz ürünlerin ağırlıklı konumu ileriye dönük hesaplama. Geçmiş bir dönemin, o dönemin kural sürümüyle yeniden kurulması ve farkın kök nedene bağlanması kamuya açık materyallerde ilan edilen bir yetenek olarak görülmedi. İki rejimi bir arada yürüten kuruluşlar için sınır denetimi de öyle.
>
> Bu tespitin sınırını açıkça söylüyorum: kamuya açık materyalle sınırlıdır. Ürünlerin ilan edilmemiş yetenekleri bulunabilir; mutlak üstünlük iddia etmiyoruz.
>
> YMM ofislerini de rakip olarak görmüyoruz. Ürün YMM'nin yetkisini almıyor, tasdik işini belgeli ve hızlı hâle getiriyor; bu yüzden dağıtım ortağı olarak konumlanıyor.

---

## Slayt 19 — Veri, sorumluluk ve insan gözetimi

- **Veri sorumlusu pilot kuruluş, ARGELOG veri işleyendir;** yazılı veri işleyen sözleşmesiyle yürütülür
- İşleme kuruluşun kendi tesisinde, kapalı devre kurulumda yapılır; ham bordro verisi dışarı çıkmaz
- Buluta yalnızca sentetik ve tokenize edilmiş veri çıkar; her yükleme öncesi kontrol listesiyle belgelenir
- **Sorumluluk:** ürün beyan üretmez, göndermez, tasdik etmez. Çıktı karar destek niteliğindedir; beyanın sorumluluğu mükellefte, tasdikin sorumluluğu YMM'dedir ve lisans sözleşmesinde yazılıdır
- **İnsan gözetimi arayüzde zorunludur:** bir bulgu, dayandığı madde ve kanıt belgesi görüntülenmeden onaylanamaz; dönem mührünü adı kayda geçen kullanıcı atar

**Görsel:** İki bölgeli şema: "Kurum içi (ham veri)" ve "Dışarı (yalnızca sentetik/tokenize)", arada tek yönlü filtre.

**Konuşma metni:**
> Bordro verisi yoğun kişisel veridir; bu yüzden veri yönetimini tasarım düzeyinde kurduk.
>
> Pilot kuruluş veri sorumlusu, biz veri işleyeniz ve bu ilişki yazılı sözleşmeye bağlanıyor. İşleme kuruluşun kendi tesisinde, kapalı devre kurulumda yapılıyor. Proje sonunda pilot verisi sözleşmede tanımlı sürede imha ediliyor ve imha tutanağı pilot kapanış raporunun eki oluyor.
>
> Dağıtılan model ağırlıklarına da hiçbir kuruluşa özgü içerik girmiyor: pilot kayıtları eğitime yalnızca kuruluştan arındırılmış fark imzası, kural sürümü ve kök neden sınıfı üçlüsü olarak giriyor.
>
> Sorumluluk konusuna gelince. Ürün beyan üretmiyor, beyanname göndermiyor, tasdik etmiyor. Çıktısı karar destek niteliğinde. Beyanın sorumluluğu mükellefte, tasdikin sorumluluğu YMM'de, ve bunu lisans sözleşmesine açıkça yazıyoruz.
>
> İnsan gözetimini de temenni olarak değil, arayüz kısıtı olarak kurduk: bir bulgu, dayandığı mevzuat maddesi ve kanıt belgesi görüntülenmeden onaylanamıyor. Bu, AB Yapay Zekâ Tüzüğü'nün 14. maddesinin etkin insan gözetimi tanımıyla ve otomasyon yanlılığı literatürünün önerdiği tasarımla uyumlu.

*Kaynaklar: EK-7 bölüm 10.*

---

## Slayt 20 — Teknopark ve TTO: bağımsız göz, ilk kullanıcılar, bölgeye taahhüt

**Teknoparktan ve TTO'dan talebimiz**
- Akademisyen danışmanlığı: veri üretim hattı, değerlendirme düzeneği ve doğrulama kapısının yöntemsel değerlendirilmesi
- Ay 7 ve ay 10 ölçüm noktalarında bağımsız gözden geçirme
- Muafiyet uygulamaları, patent ve marka tescili danışmanlığı

**Bölgeye taahhüdümüz**
- Bölgede istihdam: 4 kişi, proje sonu hedefi 6
- En az 5 bölge firmasına 4691 kural setinin ön sürümünün kullandırılması ve geri bildirim oturumu
- Bölge firmalarına yönelik 2 seminer; AS-1 ve AS-2 sonuçları için TTO ile ortak bildiri
- Ay 9'da patentlenebilirlik ön değerlendirmesi; 240 saat bölge dışı görev (veri çıkamadığı için pilot tesisinde çalışıyoruz)

**Görsel:** İki sütunlu "talep / taahhüt" tablosu.

**Konuşma metni:**
> Neden teknoparkta? Üç şey aynı anda burada: 4691 kural setinin ilk kullanıcıları, yapay zekâ tarafındaki akademik danışmanlık, ve ölçümlerimizi gözden geçirecek bağımsız göz. Ürünün 4691 kural seti burada, hedef kullanıcının yanında doğrulanacak.
>
> TTO'dan somut olarak istediğimiz şu: yapay zekâ, makine öğrenmesi ve doğal dil işleme alanında akademik danışmanlık. Özellikle üç konuda: eğitim verisi üretim hattının yöntemsel değerlendirmesi, kör karşılaştırma düzeneğinin tasarımı, ve doğrulama kapısının ölçülmesi. Ayrıca ay 7 ve ay 10 ölçüm noktalarında bağımsız gözden geçirme talep ediyoruz; ölçümü yapan taraf olarak bunu kendi lehimize değil, sonucun güvenilirliği için istiyoruz.
>
> Bölgeye taahhüdümüzü de sayısal koydum: dört kişiyle başlıyoruz, proje sonu hedefimiz altı. En az beş bölge firmasına 4691 kural setinin ön sürümünü kullandıracağız ve geri bildirim oturumu yapacağız. İki seminer vereceğiz. Ve uygun bulunması hâlinde AS-1 ile AS-2 sonuçlarını TTO ile ortak bildiri olarak sunmak istiyoruz.

---

## Slayt 21 — Kapanış: geriye ne kalacak

1. **Doğrulanmış zaman-farkındalıklı kural tabanı:** YMM teyitli gerçek çapa 96'dan en az 140'a; 5746 ve 4691 bildirimsel kural setleri
2. **Denetçi rolündeki yerel model ve ölçüm düzeneği:** yönlendirme isabeti en az %70, atıf doğruluğu en az %98, grafik işlemcisiz çalışır
3. **THS 7 prototip ve iki referans vaka:** Tüpraş ve Kale Seramik'te ücretli saha pilotları; **yazılı ihtiyaç görüşleri alındı**, niyet mektuplarının kurumsal imza süreci devam ediyor (şablon ve toplama süreci EK-2'de)
4. **Fikri mülkiyet:** "Denetci.AI" marka başvurusu; iki yöntem için ay 9'da patentlenebilirlik ön değerlendirmesi

> **Araştırma sorusu düşerse bile ürün sembolik katman üzerinden eksiksiz çalışır.**
>
> **Hesabı motor yapar, bulguyu model inceler, kararı insan verir.**

**Görsel:** Dört çıktı kartı; altta kapak slaytındaki üç kutulu şerit tekrar.

**Konuşma metni:**
> Toparlayayım. Proje sonunda geriye dört somut şey kalacak.
>
> Birincisi, 5746 ve 4691 için doğrulanmış, zaman-farkındalıklı bir kural tabanı. Bugün YMM teyitli 96 gerçek çapamız var, en az 140'a çıkacak.
>
> İkincisi, denetçi rolündeki yerel model ve onu ölçen düzenek. Düzenek modelin kendisi kadar önemli, çünkü bu alanda eksik olan şey model değil, ölçüm.
>
> Üçüncüsü, iki sanayi kuruluşunda gerçek veriyle çalışan bir prototip ve iki referans vaka çalışması. Tüpraş ve Kale Seramik'ten yazılı ihtiyaç görüşü aldık; her ikisiyle de ücretli pilot planlıyoruz.
>
> Dördüncüsü fikri mülkiyet: marka tescil başvurusu ve iki yöntem için patentlenebilirlik ön değerlendirmesi.
>
> Ve son cümlem şu: araştırma sorusu düşerse bile ürün çalışır. Çünkü doğruluğu model değil motor taşıyor. Hesabı motor yapar, bulguyu model inceler, kararı insan verir.
>
> Teşekkür ederim, sorularınızı almaktan memnuniyet duyarım.

---
---

# YEDEK SLAYTLAR (soru gelirse)

Soru-cevap sırasında açılmak üzere hazırlanır, ana akışta gösterilmez.

| # | Yedek slayt | Hangi soruya cevap verir |
|---|---|---|
| Y1 | EK-6 veri hattı şeması ve hacim tablosu | "Kaç örnekle eğitiyorsunuz?" |
| Y2 | 96 çapanın yıl × rejim × kalem kapsama matrisi | "Motor da bir yazılım, nasıl güveniyorsunuz?" |
| Y3 | Örneklem büyüklüğü ve istatistiksel test planı | "15 puanlık fark anlamlı mı?" |
| Y4 | Dört kapılı pilot akışı ve yedek pilot planı | "Pilotlar gerçekten olacak mı?" |
| Y5 | EK-1 rekabet karşılaştırma tablosu (Ö1-Ö4) | "Rakipler bunu yapmıyor mu?" |
| Y6 | Gelir merdiveni ve 30/60/90 gün planı | "Ticarileşme nasıl olacak?" |
| Y7 | İki somut mevzuat vakası: 2022 AGİ ve 01.08.2025 ay ortası tavan | "Şema kırılması ne demek?" |
| Y8 | Kapsama-doğruluk eğrisi taslağı | "Belirsiz etiketi metriği şişirmez mi?" |

---
---

# SUNUM ÖNCESİ KARAR BEKLEYEN MADDELER

*Aşağıdaki maddeler sunum metninde yer alıyor ancak başvuru dosyasında henüz karşılığı yok ya da düzeltilmesi gereken bir kayıt var. Sunum günü çelişki üretmemesi için önceden karara bağlanmalıdır.*

## A. Dosyaya eklenmesi gereken taahhütler

| # | Sunumdaki ifade | Durum | Yapılacak |
|---|---|---|---|
| A1 | Slayt 11 dipnotu: kör setin bir kısmının **iki bağımsız YMM** tarafından etiketlenmesi ve uyum katsayısının (Cohen kappa) raporlanması *önerilmektedir*; slaytlarda taahhüt olarak yer almaz | EK-6 §6 tek etiketleyici varsayıyor; 550.000 ₺'lik YMM kalemi buna göre kurulmuş | Taahhüt edilecekse EK-6 §6'ya ikinci etiketleyici eklenir ve YMM kalemi gözden geçirilir; edilmeyecekse slayt 11 dipnotu kaldırılır |
| A2 | **Beş karşılaştırma kolu** (erişim destekli kol ve sembolik taban çizgisi dâhil) | Formda üç kol var: ince ayarlı, ince ayarsız, alan dışı | Formdaki Kazanım 1'e iki kol eklenmeli ya da sunum üç kola indirilmeli |
| A3 | **Ay 2-4 fizibilite ölçümü ve karar kapısı** | Formda yok | İP5 tanımına eklenebilir; eklenmezse sunumda "planlıyoruz" olarak söylenir |
| A4 | **Eşiklerin ay 7'de mühürlenmesi** ve TTO/YMM nezdinde saklanması | Formda yok | TTO'dan talep edilen hizmetlere eklenebilir |
| A5 | **Ezberleme sınaması** ve dağıtılan model ağırlıklarının kuruluştan arındırılması | Formda ve EK-6'da yok | EK-6 §4'e eklenmesi önerilir; pilot kuruluşun hukuk birimi bunu soracaktır |
| A6 | **Bölgeye taahhütler** (6 kişi istihdam, 5 bölge firması, 2 seminer) | Formda yok | Taahhüt edilecekse forma işlenmeli; edilmeyecekse sunumdan çıkarılmalı |
| A7 | **Kaynak dönem kesişim taraması, karıştırılmış etiket kontrol koşumu ve tamamen kör tutulan bir pilot** | EK-6 §4 bu üç kontrolü içermiyor; "tamamen kör pilot" ise EK-6 §5 takvimiyle çelişiyor (ay 11'de her iki pilotun eğitim kısmı kullanılıyor) | Taahhüt edilecekse EK-6 §4 ve §5 buna göre güncellenmeli. Sunumdan çıkarıldı; soru-cevap bankasında S10 da EK-6'ya indirildi |

## B. Düzeltilmesi gereken kayıtlar

| # | Sorun | Yapılacak |
|---|---|---|
| B1 | Portal kaydında "Toplam Personel: 2" yazıyor; ekip 4 kişi | Portalda 4'e çekilmeli. Heyet portal çıktısını ekranla karşılaştırabilir |
| B2 | Portal kaydında "Kiralanan Alan: 10 m²"; 4 kişide kişi başına 2,5 m² düşüyor | Alan ihtiyacı gözden geçirilmeli |
| B3 | Formda kural tabanı kapsamı "2019-2026"; proje 26.10.2026-25.10.2027 arası yürüyor ve ay 11'de cari dönem kontrolü yapılacak | Kapsam "2019'dan cari döneme" olarak düzeltilmeli; aksi hâlde 2027 dönemleri, formun kendi sert kuralı gereği hesaplanamaz |
| B4 | Formda "yedi ürün/hizmet kategorisi tarandı" deniyor ama beş kategori listeleniyor | Sunumda "yedi ürün tarandı, beş sınıfta toplandı" denerek çözüldü; formda da aynı biçimde düzeltilmesi önerilir |
| B5 | Formda Tüpraş "aynı il" olarak işaretli | Pilot sahasının ili teyit edilmeli |
| B6 | Sunumdaki literatür rakamları (%58, %17-33, 2.041, %65) formda geçmiyor | **EK-7 bu boşluğu kapatır.** Başvuru dosyasına ek olarak sunulmalıdır |

## C. Sunum öncesi son kontroller

1. **EK-1'i yeniden tara.** Rakip ürün siteleri Ağustos-Eylül 2026'dan bu yana değişmiş olabilir.
2. **EK-1'deki ölçüt sayısını düzelt.** Tabloda dört ölçüt (Ö1-Ö4) var ama metin iki yerde "üç ölçüt" diyor: Yöntem paragrafı ve Değerlendirme maddesi 1. Yedek slayt Y5 bu tabloyu ekrana getirdiği için heyet çelişkiyi görür.
3. **Niyet mektuplarını topla.** Kurumsal imza süreci 2-4 hafta sürüyor.
4. **EK-3'teki tutarları doldur.** Yer tutucu bırakılmış bir maliyet dayanağı, bütçe sorusunda savunulamaz.
5. **EK-4'teki özgeçmişleri doldur;** özellikle "diğer projelerdeki yük" alanını. Bu alan boşsa 39 adam-ay beyanı sorgulanır.
6. **Yapay zekâ mühendisinin istihdam durumunu netleştir.** Slayt 14'te bu satır boş kalmamalı.
7. **Taban model lisansını kayda geçir.** Ticari kullanıma ve türev ağırlık dağıtımına izin veren bir aile seçilmeli; bu, ürünleştirmenin hukuki ön koşuludur.
