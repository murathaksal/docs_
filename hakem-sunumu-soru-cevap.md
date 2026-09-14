# HAKEM SORU-CEVAP BANKASI: Denetci.AI

*Teknopark hakem heyetinin soracağı zor sorular ve 30-60 saniyede verilecek cevaplar. Sunum: `hakem-sunumu.md`. Kaynak künyeleri: `ek-7-akademik-kaynakca.md`.*

## Nasıl kullanılır

Her soru dört parça hâlinde verilmiştir:

- **Cevap:** Söylenecek olan. Ezberlenmez, mantığı öğrenilir.
- **Dayanak:** Cevabı taşıyan belge, metrik veya kaynak. Hakem "bu nerede yazıyor" diye sorarsa gösterilecek yer.
- **Tuzak:** Bu soruda yapılması muhtemel savunma hatası. En değerli satır budur.

Üç genel kural:

1. **Zayıf noktayı hakemden önce siz söyleyin.** Kabul edilen bir sınır, savunulan bir sınırdan güçlüdür.
2. **Bilinmeyeni bilinmeyen olarak söyleyin.** "Ölçeceğiz" cevabı, uydurulmuş bir kesinlikten iyidir.
3. **Her sayıyı paydasıyla söyleyin.** Payda belirtilmemiş yüzde, hakem nezdinde ölçüm sayılmaz.

---


## 1. Veri ve eğitim yöntemi

*Hakem heyetindeki yapay zekâ akademisyeninin ilk soracağı yer burasıdır: veri nereden geliyor, etiketi kim koyuyor, sızıntı var mı.*

### S1. Eğitim verinizin neredeyse tamamı sentetik. Nature'da yayımlanan çalışma, modelin kendi ürettiği veriyle özyinelemeli eğitiminin geri dönüşsüz çöküşe yol açtığını gösterdi. Sizin hattınız neden çökmesin?

`KRİTİK` — *Altındaki endişe: Sentetik veriyle eğitim son iki yılın en bilinen tuzağı. Hakem, projenin bu tuzağa düşüp düşmediğini ve literatürü bilip bilmediğinizi test ediyor.*

**Cevap.** Çöküşün mekanizması özyinelemedir: model_n, model_{n-1}'in çıktısıyla eğitilir ve dağılımın kuyrukları kaybolur. Bizim hattımızda veriyi model üretmiyor; 96 gerçek dönemde kuruş farksız doğrulanmış deterministik motor üretiyor. Motorun çıktı dağılımı modele hiç bağlı değil, dolayısıyla özyineleme yok. Tek kapalı halka, doğrulama kapısının eleme kayıtlarının ikinci ince ayar turuna olumsuz örnek olarak dönmesidir; orada da etiketi model değil sembolik kapı koyuyor ve bu tek tur. Ayrıca Gerstgrasser'ın gösterdiği koruma bizde zaten var: gerçek YMM teyitli çapa seti ikame edilmiyor, birikiyor; 96'dan 140'a çıkıyor ve her turda regresyon çapası olarak duruyor.

**Dayanak.** Shumailov2024 (Nature 631:755) özyineleme mekanizması; Gerstgrasser2024 (biriktirme çöküşü engelliyor); İP1 çıkış kriteri 96/96 kuruş farksız; İP2 metriği 96→≥140 gerçek çapa; EK-6 §3 üretim hattı şeması (kaynak = motor, model değil).

**Tuzak.** "Bizimki sentetik değil" demek. Sentetiktir. Savunma, kaynağın model değil doğrulanmış motor olması ve gerçek çapa setinin ikame edilmeyip birikmesidir.


### S2. Motoru "oracle" diye sunuyorsunuz. Motor da bir yazılım ve hata yapabilir; ayrıca motor bir tutarın yanlış olduğunu söyleyebilir ama NEDENİNİ bilemez. Kök neden etiketini gerçekte nereden alıyorsunuz?

`KRİTİK` — *Altındaki endişe: Oracle iddiası projenin veri hattının tamamını taşıyor. Hakem, iddianın aşırı genişletilip genişletilmediğini ve sınırının bilinip bilinmediğini yokluyor.*

**Cevap.** İki ayrı iddiayı ayırmam gerekiyor. Motor yalnızca tek görevde gerçek anlamda oracle: araştırma yönlendirmede. Orada etiket bir yargı değil, mekanik bir olgu; önerilen belgeyi getir, motoru yeniden koş, fark kapandı mı kapanmadı mı. Bu insan yorumuna hiç açık değil. Kök neden tarafında motor oracle DEĞİL: etiket ya inşa gereği bilinir, çünkü bozulmayı biz enjekte ettik, ya da pilotta YMM'nin kapanış kararıdır. Motorun kendi doğruluğu da varsayım değil, ölçülmüş büyüklük: 96 gerçek dönemde kuruş farksız, hedef 140. Motor hatası olsaydı çapa setinde sistematik kırılma olarak görünürdü; üstelik doğrulanmamış parametreli bir ayı motor hesaplamayı motor seviyesinde reddediyor.

**Dayanak.** EK-6 §2 görev tablosu (G2'nin doğru cevap kaynağı motor; G1/G3'ünki inşa gereği bilinen etiket veya insan kapanış kararı); EK-6 §6; İP1 ve İP2 çıkış kriterleri; form risk maddesi (4) "doğrulanmamış parametreli ay hesaplanamaz ve raporlanamaz" sert kuralı.

**Tuzak.** Motoru dört görevin hepsinde oracle gibi sunmak. Oracle iddiası yalnızca G2 için geçerlidir; genişletmek hakemin haklı olarak kıracağı yerdir.


### S11. Hata enjeksiyonlu veride bozulmayı siz üretiyorsunuz. Model denetçi akıl yürütmesini değil, sizin üreticinizin parmak izini öğrenmiş olabilir. Gerçek pilot verisinde bu neden çökmesin?

`KRİTİK` — *Altındaki endişe: Sentetikten gerçeğe aktarım (sim-to-real) bu tür projelerin en sık çöktüğü yer. Hakem, uçurumun ölçülüp ölçülmeyeceğini soruyor.*

**Cevap.** Bu risk gerçek ve literatürde adı var: Mirzadeh'in GSM-Symbolic çalışması, modellerin mantık değil eğitimdeki adım örüntülerini taklit ettiğini, alakasız tek bir cümleyle başarının %65'e varan oranda çöktüğünü gösterdi. Bu yüzden ölçüm düzeneğimiz uçurumu gizlemiyor, onu ölçüyor. Ay 8-9'da sentetik ve enjeksiyon verisiyle ince ayar yapıyoruz; ay 10'da hiç görmediğimiz gerçek pilot fark envanteriyle ölçüyoruz; ay 11'de pilotun eğitim kısmını ekleyip ay 12'de tekrar ölçüyoruz. Yani "gerçek veri ne kadar kazandırıyor" ayrı bir sayı olarak çıkıyor. Sentetikte yüksek, gerçekte düşük çıkarsa bu AS-1'in olumsuz sonucudur ve öyle raporlanır. Ayrıca enjeksiyon üreticisini kasten çeşitlendiriyoruz: çoklu-neden vakaları fazla örnekleniyor ve ayırt edilemez vakalar "belirsiz" olarak öğretiliyor.

**Dayanak.** EK-6 §5 zamanlama tablosu (ay 8-9 A+B, ay 10 C'nin kör kısmı, ay 12 yeniden ölçüm) ve §4 dengeleme kuralı; Mirzadeh2025; form risk maddesi (3) kaynak bazlı başarım ölçümü.

**Tuzak.** Sentetik başarımı tek sayı olarak sunmak. Sentetik-gerçek uçurumu ayrı raporlanmazsa ölçümün hiçbir dış geçerliliği yoktur.


### S10. Sızıntı kontrolünün gerçekten çalıştığını nasıl kanıtlayacaksınız? "Bölme kuruluş ve dönem bazında" demek bir taahhüt, kanıt değil.

`KRİTİK` — *Altındaki endişe: Sentetik+gerçek karışık veri hatlarında sızıntı en sık görülmeyen hatadır. Hakem, çalıştırılabilir bir kontrol listesi istiyor.*

**Cevap.** Haklısınız, bölmeyi söylemek yeterli değil; dört çalıştırılabilir kontrol koyuyoruz. Bir: en az bir pilot kuruluş tamamen kör tutulur, hiçbir dönemi eğitime girmez; sadece dönem değil kuruluş bazında ayrım. İki: eğitim ve test fark imzaları arasında birebir ve yakın kopya taraması yapılır, bulunan kopya sayısı sıfır olarak raporlanır. Üç: etiketleri karıştırılmış kontrol koşumu; etiket rastgeleyken model hâlâ yüksek skor alıyorsa bir artefakttan sızıntı var demektir, bu testi de raporlayacağız. Dört ve en güçlüsü: G2 metriği ezberlenemez, çünkü ölçüm bir etiket dizesini eşleştirmek değil, motoru fiilen yeniden koşturmaktır. Ayrıca sentetik test ile gerçek pilot testi ayrı raporlanıyor; aradaki uçurumun kendisi bir ezber göstergesidir.

**Dayanak.** EK-6 §4 (bölme kuruluş ve dönem bazında; kör test seti eğitimde hiçbir biçimde kullanılmaz); EK-6 §5-6 (ay 10 kör ölçüm, ay 11 ikinci tur, ay 12 yeniden ölçüm); Mirzadeh2025 (yüzeysel örüntü ezberi).

**Tuzak.** "Bölmeyi doğru yaptık" deyip geçmek. Sızıntı iddiası, çalıştırılabilir kontrol ve raporlanan sayı olmadan kanıt sayılmaz.



## 2. Model seçimi ve mimari

*Neden bu boyut, neden ince ayar, neden yerel.*

### S3. 1-4 milyar parametrelik bir model bu iş için neden yeterli olsun? Bu bant genellikle oyuncak kabul edilir; mevzuat gibi yoğun bilgi gerektiren bir alanda neden yetsin?

`KRİTİK` — *Altındaki endişe: Model boyutu seçimi projenin GPU'suz/kapalı devre vaadinin temelidir. Hakem, boyutun ürün kısıtı yüzünden mi seçildiğini yoksa görevin gerçekten bu bantta çözülebilir olup olmadığını sorguluyor.*

**Cevap.** Modelden istediğimiz iş açık uçlu üretim değil. Tutar hesaplamıyor, mevzuat metni ezberlemiyor, serbest metin yazmıyor. Üç şey yapıyor: kapalı bir kök-neden sınıfı kümesinde sınıflandırma, sembolik katmanın ürettiği hipotez kümesini sıralama, ve sonlu bir belge türü listesinden bir sonraki adımı seçme. Çıktısı dilbilgisiyle zorlanıyor ve kullandığı mevzuat kimlikleri kural tabanının kendi kimlik listesinden geliyor, modelin hafızasından değil. Bu bant için kanıt var: 3,8 milyar parametreli phi-3-mini MMLU'da %69; Hsieh'in çalışmasında 770 milyonluk model dar görevde 540 milyarlığı geçti. Tek dayanağımız bu da değil: hedef tutmazsa 7-8 milyar parametreli 4-bit nicemlenmiş model de 16 GB'a sığar ve bunu yedek kol olarak ölçeceğiz.

**Dayanak.** Abdin2024 (phi-3-mini 3,8B, MMLU %69); Hsieh2023 (770M > 540B, dar görev, gerekçeyle damıtma); Gunasekar2023 (phi-1, 1,3B); Belcak2025 (NVIDIA: ajan işlerinin çoğu dar ve tekrarlı); Geng2023 (dilbilgisi kısıtlı çözümleme); Dettmers2023 (4-bit adaptör eğitimi).

**Tuzak.** "Küçük model büyük modelle her işte yarışır" demek. Gudibande2023 tam tersini gösteriyor: kazanç yalnızca verinin yoğun kapsadığı DAR görevde var. İddiayı dar tutun.


### S15. Neden erişim destekli üretim (RAG) yetmiyor da ince ayar gerekiyor? Mevzuat metnini modele verseniz aynı sonucu almaz mısınız?

`KRİTİK` — *Altındaki endişe: Hakem, ince ayarın gerçekten gerekli mi yoksa moda mı olduğunu ve daha ucuz alternatifin elenip elenmediğini test ediyor.*

**Cevap.** İkisi farklı problemi çözüyor ve biz aslında ikisini de kullanıyoruz. Erişim, "metin ne diyor" sorusuna cevap verir; bizim sorumuz o değil. Bizim sorumuz "bu fark imzası ne anlama geliyor ve hangi belge bu farkı kapatır". Bunun cevabı hiçbir belgenin içinde yazmıyor; motorun çıktısının bir fonksiyonu; getirilecek bir pasaj yok. İkincisi, erişim halüsinasyonu azaltıyor ama bitirmiyor: Stanford ekibinin ölçümünde hukuk için özel yapılmış en pahalı ticari erişim araçları bile hâlâ %17 ile %33 arasında desteksiz iddia üretiyor. Bizim kapımız erişim değil doğrulama: her atıf, dönem semantiği olan sürümlü kural tabanına karşı sınanıyor. Üçüncüsü, karşılaştırma kollarımızdan biri zaten kural tabanına erişimi olan ama ince ayarsız model; yani "erişim yeterdi" bizde bir hipotez olarak sınanıyor. Yeterse AS-1'in (b) şıkkını olumsuz raporlarız.

**Dayanak.** Magesh2025 (Lexis+ AI sorguların %65'ini, Westlaw AI-AR %41'ini doğru yanıtlıyor; halüsinasyon ortadan kalkmadı); Huang2025 (erişim destekli modellerin sınırı ayrı bölüm); İP2 çıktısı "kural tabanının model tarafından sorgulanabilir arayüzü"; Kazanım 1 karşılaştırma kolları.

**Tuzak.** "RAG kötüdür" demek. RAG kullanılıyor; fark, doğrulama kapısının erişimin ÜSTÜNE konmasıdır.


### S16. Neden hazır büyük bir modeli API üzerinden kullanmıyorsunuz? Kendi modelinizi eğitmek hem pahalı hem riskli değil mi?

`Önemli` — *Altındaki endişe: Hakem, mimari kararın teknik gerekçeye mi yoksa firma tercihine mi dayandığını yokluyor.*

**Cevap.** Üç gerekçe var, ikisi pazarlık dışı. Birincisi hukuki: pilotlar bordro ve personel verisiyle çalışıyor; KVKK'nın 12. maddesi veri güvenliği yükümlülüğü getiriyor ve müşterinin bordrosu kurum dışına çıkmıyor; bu bir tercih değil, satın alma koşulu. İkincisi denetlenebilirlik: mühürlenmiş bir dönemin üç yıl sonra denetimde birebir yeniden üretilebilmesi gerekiyor; sürümü sessizce değişen bir API bunu imkânsız kılar. AB Yapay Zekâ Tüzüğü'nün 12. maddesi de yaşam döngüsü boyunca kayıt ve izlenebilirlik şart koşuyor. Üçüncüsü teknik: Xu ve arkadaşları halüsinasyonun büyük modellerden tamamen yok edilemeyeceğini biçimsel olarak gösterdi; yani "daha büyüğünü alalım" sorunun çözümü değil. Zaten büyük modeli mimarinin neresine koyarsak koyalım, tutarı yine motor hesaplayacak ve atfı yine kapı doğrulayacaktı.

**Dayanak.** KVKK6698 md.12 (veri güvenliği) ve md.11/1(g) (münhasıran otomatik analize itiraz hakkı); AIAct2024_Art12 (kayıt tutma); Xu2024 (halüsinasyonun kaçınılmazlığı, biçimsel kanıt); form: kapalı devre çalışma, bulut GPU yalnızca sentetik/anonim veriyle (200.000 TL).

**Tuzak.** Maliyeti ana gerekçe yapmak. Ana gerekçe veri egemenliği ve geçmiş dönemin yeniden üretilebilirliğidir; maliyet üçüncü sıradadır.


### S17. Modeli 2019-2026 kural sürümleriyle eğitiyorsunuz. 2028'de yeni bir tebliğ çıktığında model eski dünyayı biliyor olacak. Her mevzuat değişikliğinde yeniden mi eğiteceksiniz?

`Önemli` — *Altındaki endişe: Dağılım kayması, mevzuat gibi sürekli değişen alanlarda ürünün ömrünü belirler. Hakem, modelin kural bilgisini ağırlıklarında mı tuttuğunu anlamak istiyor.*

**Cevap.** Hayır, ve bunun sebebi bilinçli bir tasarım kararı. Modelin görevi kural bilmek değil; kural tabanının verdiği kimliklerle sınıflandırma, sıralama ve belge seçimi yapmak. Atıf sözlüğü çalışma anında kural tabanından geliyor, ağırlıklardan değil; dilbilgisi kısıtı da modelin listede olmayan bir kimlik üretmesini fiziksel olarak engelliyor. Yeni bir tebliğ geldiğinde imzalı çevrimdışı paketle kural tabanı güncelleniyor, model dosyasına dokunulmuyor. Eskime riski sıfır değil elbette: yepyeni bir fark türü ortaya çıkarsa model onu hiç görmemiş olur. Bunun erken uyarısı bizde hazır; doğrulama kapısının eleme oranı kanaryadır; güncelleme sonrası eleme oranı yükselirse yeni bir ince ayar turu gerekiyor demektir. Ayrıca ürün model olmadan da eksiksiz çalışıyor; model eskise bile hesap durmaz.

**Dayanak.** İP2 çıktısı (üç eksenli sürümleme + kural tabanının sorgulanabilir arayüzü + as-of yeniden üretim); Geng2023 (dilbilgisi kısıtı geçerli yapıyı garanti eder); Kazanım 2 (kapıdan elenen bulgu oranı raporlanır); Governatori2010 ve Grandi2003 (mevzuatın zamansal sürümlenmesi); form: imzalı çevrimdışı güncelleme.

**Tuzak.** "Model mevzuatı biliyor" izlenimi vermek. Model mevzuatı bilmez; kural tabanına referans verir; bu ayrım tüm mimarinin dayanağıdır.


### S13. 16 GB bellekli, grafik işlemcisiz bir makinede bulgu başına 30 saniye hedefi gerçekçi mi? Bu sayıyı neye dayandırıyorsunuz?

`Önemli` — *Altındaki endişe: Ürünün kapalı devre vaadi bu sayıya bağlı. Hakem, hedefin ölçümden mi yoksa temenniden mi geldiğini anlamak istiyor.*

**Cevap.** Sayıyı açayım. Bir bulgunun çıktısı serbest metin değil, şemaya zorlanmış yapılandırılmış bir kayıt; alanların çoğu sonlu listelerden seçiliyor, o yüzden üretilen simge sayısı yüzler mertebesinde, binler değil. T-MAC çalışması, düşük bitli modellerin CPU'da tablo-arama yöntemiyle çalıştırıldığında Raspberry Pi 5 gibi zayıf bir cihazda bile saniyede 11 simge ürettiğini hakemli bir sistem konferansında gösterdi; dört çekirdekli bir masaüstünde 4-bit 3 milyar parametreli model bu bandın üzerinde. Üç yüz simge, saniyede 10-20 simge, 15-30 saniye eder. Yani hedef rahat değil, sıkı ama ulaşılabilir. Önemlisi şu: bu sayıyı slaytta değil, ekipman listesindeki iki referans test bilgisayarında ölçüp raporlayacağız. Tutmazsa iki kaldıraç var; daha küçük model ya da daha kısa şema; son çare bulgu üretimini arka planda toplu işe almak; risk listesinde sekizinci madde bu.

**Dayanak.** Wei2025 T-MAC (EuroSys'25; Pi 5'te 11 simge/sn, yaygın çözüme göre 4 kata kadar hızlanma); Frantar2023 GPTQ (3-4 bit, ihmal edilebilir doğruluk kaybı); Alizadeh2024; form ekipman listesi (2 adet referans test bilgisayarı: 4 çekirdek, 16 GB, GPU'suz); form risk maddesi (8).

**Tuzak.** Hızı geliştirici iş istasyonunda veya bulutta ölçüp referans donanıma genellemek. Ölçümün nerede yapılacağını adıyla söyleyin.



## 3. Ölçüm, metrik ve istatistik

*Sunumdaki yedi sayısal eşiğin savunulduğu bölüm. Bu sorulara sayıyla cevap verilemezse eşikler keyfî görünür.*

### S4. Araştırma yönlendirme isabeti için %70 eşiğini nereden aldınız? Bu sayı neden anlamlı, ve daha basit bir sembolik sezgisel bu işi zaten yapamaz mı?

`KRİTİK` — *Altındaki endişe: Hakem iki şeyi birden yokluyor: eşiğin keyfi olup olmadığı, ve nöral katmanın sembolik alternatife karşı gerçekten katkı sağlayıp sağlamadığı (ablasyon kolu var mı).*

**Cevap.** %70 literatürden alınmış bir sabit değil, iki referansa göre konmuş bir eşik. Birincisi rastgele taban: sembolik katman bir fark için ortalama üç ila beş hipotez üretiyor, kümeden rastgele seçim %20-33 eder; %70 bunun iki-üç katı. İkincisi işin ekonomisi: uzmanın bugün her fark için yaptığı ön incelemeyi ikiye bölmek için isabetin yarıdan belirgin yukarıda olması gerekir. Asıl kritik nokta ikinci sorunuz: de Kleer ve Williams'ın 1987'deki entropi tabanlı "bir sonraki ölçümü seç" sezgiseli bu işi sinir ağı olmadan da yapabilir. Onu zorunlu üçüncü karşılaştırma kolu olarak ölçeceğiz. Sembolik sezgisel modele yetişirse AS-3'ün nöral yarısını olumsuz raporlar ve ucuz olanı ürüne koyarız.

**Dayanak.** deKleerWilliams1987 (entropi tabanlı sonraki ölçüm seçimi); Heckerman1995 (beklenen bilgi kazancı / maliyet tartımı); Shchekotykhin2012 (en ayırt edici sorunun seçilmesi); Bhagavatula2020 (abdüktif seçimde en iyi model %68,9, insan %91,4).

**Tuzak.** "%70 sektör standardıdır" demek; böyle bir standart yok. Eşiğin gerekçesi taban oran ve iş ekonomisidir; ve sembolik taban kolunu vaat etmeden geçmeyin.


### S5. "İnce ayarsız temel modele karşı ≥15 puan" diyorsunuz. Bu farkın istatistiksel olarak anlamlı olduğunu hangi örneklem büyüklüğüyle ve hangi testle göstereceksiniz?

`KRİTİK` — *Altındaki endişe: Akademisyen hakem için tek yüzde farkı ölçüm değildir. Güç analizi ve test istatistiği yoksa iddia doğrulanamaz sayılır.*

**Cevap.** Karşılaştırma eşleştirilmiş: aynı kör test setini hem ince ayarlı hem ince ayarsız model çözüyor, o yüzden McNemar testi kullanıyoruz. Kaba hesap: 200 kalemlik eşleştirilmiş sette %25 uyuşmazlık oranı ve 15 puanlık fark varsayımıyla z yaklaşık 4,2 çıkar; 100 kalemde bile z=3'tür. Bizim kör setimiz iki pilotun her birinden en az 200 fark kalemi artı enjeksiyon setinin ayrılan kısmı, yani 300-400 bandında. Yani 15 puanlık bir fark bu örneklemde tesadüfle açıklanamaz. Taahhüdümüz şu: tek bir yüzde değil, farkın güven aralığı ve McNemar p değeri raporlanacak; sonuç sınırda çıkarsa sınırda olduğunu söyleyeceğiz.

**Dayanak.** EK-6 §5 (pilot başına ≥200 fark kalemi); İP4 ≥400 vakalık enjeksiyon seti; Kazanım 1 test seti tanımı (kör fark envanteri + YMM etiketli doğrulama örneklemi + pilot gerçek envanteri).

**Tuzak.** Sadece iki yüzdeyi yan yana koyup geçmek. Güven aralığı ve test istatistiği verilmeyen 15 puan iddiası hakem nezdinde ölçüm sayılmaz.


### S6. %98 atıf doğruluğu ve ≤%1 desteksiz iddia iddialarını tam olarak nasıl ölçeceksiniz? Bu eşikler bu kadar keskin konabilir mi?

`KRİTİK` — *Altındaki endişe: Atıf doğruluğu alanın en sık şişirilen metriği. Hakem, ölçümün otomatik mi insan mı olduğunu ve güven aralığının verilip verilmeyeceğini görmek istiyor.*

**Cevap.** İki katmanlı ölçüyoruz. Birincisi otomatik ve tam sayım: kullanıcıya ulaşan her bulgudaki her atıf, kural tabanına karşı iki soruya tabi; bu madde var mı, ve o dönemde yürürlükte miydi. Bu makine kontrolü örneklem değil, yüzde yüz. İkincisi YMM örneklemi: atfın var olması doğru madde olduğu anlamına gelmez, onu insan teyit ediyor. Sayı tarafında dürüst olayım: ≤%1 demek 400 kalemde sıfır ya da bir hata görmek demektir; 400'de sıfır hata %95 üst güven sınırını yaklaşık %0,75'e indirir, bir hata ise %1,4'e çıkarır. Bu yüzden nokta tahmini değil Clopper-Pearson aralığını raporlayacağız. Eşik keyfi de değil: Walters ve Wilder'ın ölçümünde GPT-4'ün verdiği kaynakların %18'i tamamen uydurmaydı; biz iki mertebe aşağısını hedefliyoruz, çünkü atıf sözlüğü modelin hafızası değil kural tabanı.

**Dayanak.** Kazanım 2 metrikleri ve test seti; Walters2023 (GPT-3.5 %55, GPT-4 %18 tamamen uydurma kaynak); Gao2023ALCE (atıf kalitesi ölçülebilir bir büyüklüktür); Magesh2025 (ticari hukuk RAG araçlarında %17-33 desteksiz iddia).

**Tuzak.** Üst güven sınırını vermeden yüzde söylemek; ve atfın "var olması" ile "doğru madde olması"nı tek metriğe karıştırmak.


### S7. Sembolik doğrulama kapısı doğru bulguları da eleyebilir. Bu yanlış eleme oranını nasıl ölçüyorsunuz, ve kapının kendisi bir bilgi kaybı kaynağı değil mi?

`Önemli` — *Altındaki endişe: Her filtrede yanlış pozitif/yanlış negatif dengesi vardır. Hakem, projenin kapıyı tek yönlü bir kazanç gibi sunup sunmadığını test ediyor.*

**Cevap.** Evet, kapı yanlış eleyebilir ve bunu ölçmeyi taahhüt ediyoruz: her turda elenen yığından katmanlı örneklem alınıp YMM'ye "bu aslında geçerli miydi" diye sorulacak; yanlış eleme oranı ayrı bir sayı olarak raporlanacak. İki şey riski sınırlıyor. Birincisi kapı bir eşikli sınıflandırıcı değil, karar verilebilir bir sorgu: madde var mı, o dönemde yürürlükte miydi. İkincisi ve daha önemlisi kapı hiçbir tutarı gizlemiyor. Motorun bulduğu fark her koşulda kullanıcıya gidiyor; kapı yalnızca modelin o fark üzerine yazdığı yorumu eliyor. Yani yanlış elemenin en kötü sonucu, kullanıcının bugünkü gibi yorumsuz bir farkla kalmasıdır; bilgi kaybı değil, katma değer kaybı.

**Dayanak.** AS-2 zaten bu soruyu araştırma sorusunun (ii) şıkkı olarak tanımlıyor; Kazanım 2 "kapıdan elenen bulgu oranı raporlanır ve ince ayar turları boyunca düşer"; SkitkaMosierBurdick1999 (desteksiz çıktının kullanıcıya hiç ulaşmaması gereği); Cobbe2021 (üretici/doğrulayıcı ayrımı).

**Tuzak.** "Kapı yanlış elemez" demek. Eler. Savunma asimetridir: elenen şey tutar değil, yorumdur.


### S8. Kör karşılaştırmada "bir denetçinin soracağı soru" yargısını YMM veriyor. Tek uzmanın etiketi altın standart sayılabilir mi? Değerlendiriciler arası uyumu ölçüyor musunuz?

`Önemli` — *Altındaki endişe: Öznel etiketle ölçülen metrikler uyum katsayısı olmadan yayımlanamaz. Hakem metodolojik titizliği yokluyor.*

**Cevap.** Haklı bir nokta: "bir denetçinin soracağı soru mu" yargısı özneldir ve tek YMM'nin etiketi ölçüm değildir. Taahhüdümüz: kör setin en az yüzde yirmisi iki bağımsız YMM tarafından etiketlenecek, Cohen kappa raporlanacak, hedef 0,6'nın üzerinde; anlaşmazlıklar üçüncü bir hakemle çözülecek ve kaç vakada üçüncü hakeme gidildiği yazılacak. Kappa düşük çıkarsa bu görev metriğinin güvenilir olmadığını raporlarız; "ölçülemedi" de dürüst bir sonuçtur. Zaten projenin ana metriğini kasten G3 değil G2 seçtik: araştırma yönlendirmede etiketi insan koymuyor, motor koyuyor; orada değerlendiriciler arası uyum sorunu yapısal olarak yok.

**Dayanak.** EK-6 §6 (G2'nin doğruluğu insan etiketine ihtiyaç duymadan ölçülür); bütçede 550.000 TL YMM kalemi uzman etiketlemeyi açıkça kapsıyor; Kazanım 1 kör değerlendirme tanımı (YMM tarafından nitelenme oranı ≥%70).

**Tuzak.** Tek YMM etiketini altın standart diye sunmak. Uyum katsayısı verilmeden öznel metrik rapor edilemez; bunu kendiniz söyleyin ki hakem söylemesin.


### S9. 400 vakalık kalibrasyon seti, sekiz-on kök neden sınıfı ve çoklu-neden vakaları için gerçekten yeterli mi? %85 doğruluk iddiasını bu örneklemle kurabilir misiniz?

`Önemli` — *Altındaki endişe: Hakem, örneklem büyüklüğünün iddia edilen metriğin çözünürlüğüne yetip yetmediğini hesaplamanızı bekliyor.*

**Cevap.** Ölçüm birimi vaka değil kalem; her vaka birden çok fark kalemi üretiyor, yani payda 400'den büyük. Toplu iddia için yeterli: %85 civarında ve n=400'de %95 güven aralığının yarı genişliği yaklaşık 3,5 puan. Yeterli olmadığı yeri de söyleyeyim: sınıf bazında. Sekiz-on kök neden sınıfına bölününce sınıf başına kırk vaka kalır ve aralık ±11 puana çıkar. Bu yüzden sınıf bazlı sayıları iddia olarak değil, aralıklarıyla birlikte betimleyici olarak raporlayacağız. Ayrıca 400 tek kaynak değil: mevzuat referanslı 60 senaryo parametrik olduğu için tek senaryodan onlarca örnek türüyor, ve asıl hüküm gerçek pilot fark envanterinde veriliyor. LIMA'nın gösterdiği gibi bu tür görevlerde belirleyici olan hacim değil, doğrulanmış örnek kalitesidir.

**Dayanak.** İP4 çıkış kriteri ≥400 vaka + ≥60 senaryo; EK-6 §5 hacim tablosu (A: 2.000-3.000 örnek, B: 1.500-2.500 örnek); Kazanım 3 (kalem bazında ≥%85); Zhou2023 LIMA (1.000 seçilmiş örnek).

**Tuzak.** 400 vakayı hem toplu hem sınıf bazlı iddiaya yetermiş gibi sunmak. Sınıf bazlı gücün yetmediğini kendiniz teslim edin.


### S12. %85 kök-neden doğruluğunu, zor vakaların hepsini "belirsiz" etiketleyerek kolayca tutturabilirsiniz. Bunu ne engelliyor?

`KRİTİK` — *Altındaki endişe: Çekimserlik hakkı tanınan her sistemde metrik şişirme kapısı açılır. Hakem, metriklerin birbirine kilitli olup olmadığını sınıyor.*

**Cevap.** Hiçbir tek sayı engellemez; o yüzden iki metrik birbirine kilitli. Doğruluk kalem bazında ölçülüyor, belirsiz payı ise tutar bazında ve tavanı %5. Zor vakaları belirsize atmak tutar payını şişirir ve ikinci metriği kırar. Ama bu bile tam savunma değil; taahhüdümüz tek işletme noktası değil, tam risk-kapsama eğrisini yayımlamak: kaç kalem cevaplandı ve o kapsamda doğruluk ne. Chow'un 1970'teki reddetme seçeneği ve Geifman-El-Yaniv'in seçici sınıflandırma çerçevesi tam olarak bunu ister. Üstelik belirsizliğin bir kısmı yeteneksizlik değil ilkeseldir: Sampath'ın teşhis edilebilirlik kavramı, bazı neden çiftlerinin eldeki gözlemle matematiksel olarak ayrılamaz olduğunu söyler. Hangi imza sınıflarının ilkesel olarak ayrılamaz olduğunu önceden hesaplayıp ayrı raporluyoruz.

**Dayanak.** Kazanım 3 (kalem bazında ≥%85 doğruluk, TUTAR bazında ≤%5 belirsiz, iki farklı payda, kasten); Chow1970 (hata/kapsama dengesi); GeifmanElYaniv2017 (istenen risk düzeyini garanti eden çekimserlik); Sampath1995 (teşhis edilebilirlik önceden sınanabilir bir özelliktir); AS-3 tanımlanabilirlik paragrafı.

**Tuzak.** Belirsiz sınıfını sadece "dürüstlük" diye sunup kapsama oranını ve risk-kapsama eğrisini vermemek.


### S18. Veri kaynağına ve hacme göre başarım eğrisi, iki ince ayar turu, en az üç karşılaştırma kolu, birden çok model boyutu; 200.000 TL bulut GPU bütçesiyle bu ablasyon ızgarası gerçekten koşulabilir mi?

`İkincil` — *Altındaki endişe: Hakem, vaat edilen deney tasarımının bütçeyle tutarlı olup olmadığını, yani vaadin gerçekçi mi yoksa dekoratif mi olduğunu kontrol ediyor.*

**Cevap.** Evet, çünkü tam ince ayar yapmıyoruz. QLoRA ile 4-bit nicemlenmiş 3 milyar parametreli bir model üzerinde adaptör eğitiyoruz; eğitilebilir parametre sayısı binlerce kat düşüyor ve beş bin örneklik bir tur tek bir GPU'da saatler mertebesinde kalıyor. 200.000 TL güncel kiralama fiyatlarıyla birkaç bin GPU-saat eder; bizim ihtiyacımız onlarca koşum, yüzlerce değil. Zaten bu projede pahalı olan taraf GPU değil: 550.000 TL'lik YMM kalemi, yani etiket ve teyit tarafı. Bu doğru dağılım; darboğaz hesap gücü değil, doğrulanmış alan bilgisi.

**Dayanak.** Hu2022 LoRA (eğitilebilir parametrede 10.000 kata kadar azalma, tam ince ayarla eş başarım); Dettmers2023 QLoRA (4-bit üzerinde adaptör eğitimi tek makineye iniyor); bütçe tablosu: 200.000 TL bulut GPU, 550.000 TL YMM hizmeti; İP5 = 10 adam-ay.

**Tuzak.** "Gerekirse daha çok GPU alırız" demek. Bütçe sabit; savunma parametre-verimli eğitimin maliyeti düşürmesidir.



## 4. Ar-Ge niteliği, bilimsel çıktı ve başarısızlık

*"Bu Ar-Ge mi, mühendislik mi" itirazı ve olumsuz sonuç senaryosu.*

### S14. Bu proje aslında hazır bileşenlerin bir araya getirilmesi değil mi? İnce ayar, nicemleme, kısıtlı çözümleme; hepsi olgun araçlar. Ar-Ge iddiası tam olarak nerede?

`KRİTİK` — *Altındaki endişe: Teknopark hakemliğinde en belirleyici soru budur. Hakem, Ar-Ge ile mühendisliğin ayrımının yapılıp yapılmadığını görmek istiyor.*

**Cevap.** Bu itirazın büyük kısmını biz de kabul ediyoruz ve forma yazdık: ince ayar, nicemleme, dilbilgisi kısıtlı çözümleme ve belge içeri alma Ar-Ge iddiası değil, geliştirme kalemidir; 39 adam-ayın 8'i böyle etiketlendi. Ar-Ge iddiası dört yerde ve dördünün de yanlışlanabilir ölçütü var. Bir işin Ar-Ge olup olmadığının testi başarısız olabilir olmasıdır: AS-1 %70'i tutturamazsa, AS-2 kapı doğru bulguları haksız yere elerse, AS-3 nöral sıralama sembolik sezgiseli geçemezse, AS-4 kaçış kancası üçü aşarsa; dördü de olumsuz olarak raporlanır. Ayrıca bu görev için hazır bir denek taşı yok; değerlendirme düzeneğinin kendisi projenin bir çıktısı. OECD'nin kendi çalışma raporu, kodlanmış mevzuat kurallarının sürüm yönetişimini çözülmemiş bir soru olarak işaret ediyor; AS-4 tam olarak orada duruyor.

**Dayanak.** Form "Ar-Ge iddiası olmayan, geliştirme kalemi olarak beyan edilenler" paragrafı ve 31+8 adam-ay ayrımı; dört AS'nin de ölçütlü/düşebilir tanımı; MohunRoberts2020 (OECD: kodlanmış kuralların sürüm yönetişimi açık problem); Kowalski1992 ve Guintchev2025 (biçimselleştirmenin sınırı); Grimmelmann2022.

**Tuzak.** Her şeyi Ar-Ge diye savunmak. Mühendislik kısmını isim isim teslim etmek savunmayı zayıflatmaz, güçlendirir.


### S19. Proje sonunda bilimsel bir çıktı olacak mı? Yayın ve patent taahhütleriniz ne kadar gerçekçi?

`İkincil` — *Altındaki endişe: Teknopark hakemi, projenin bölgeye ve akademiye dönen somut çıktısını arıyor; abartılı patent vaatleri güven kaybettirir.*

**Cevap.** Yayın tarafında somut taahhüt var: Teknoloji Transfer Ofisi aracılığıyla akademik danışmanlık alıyoruz ve AS-1 ile AS-2 sonuçlarının ulusal bir yapay zekâ konferansında ortak bildiri olarak sunulması forma yazıldı. Yayımlanabilir içerik üç başlıkta: deterministik motoru referans kaynağı olarak kullanan veri üretim hattı, sembolik doğrulama kapısının yanlış eleme dengesi, ve bu görev için sıfırdan kurulan değerlendirme düzeneği; çünkü bu alanda hazır bir denek taşı yok. Olumsuz sonuç da yayımlanacak; "küçük model bu görevi öğrenemedi" de bir bulgudur ve alan için değerlidir. Patent tarafında dürüst olayım: dokuzuncu ayda patentlenebilirlik ön değerlendirmesi yaptıracağız, ama yazılım yöntemlerinde teknik etki şartı nedeniyle sonucu garanti edemeyiz. Bu yüzden forma "var" değil "ön değerlendirme yapılacak" yazdık; marka tescili ise kesin.

**Dayanak.** Form "TTO'dan Talep Edilen Hizmetler": AS-1 ve AS-2 sonuçlarının ortak bildiri olarak sunulması; FSMH tablosu (iki yöntem için "değerlendirilecek", ay 9 ön değerlendirme); Ar-Ge Aşamaları "Patent ve Lisans Çalışmaları" işaretli; bütçede 250.000 TL patent vekili + akademik danışmanlık.

**Tuzak.** Patentin alınacağını kesinmiş gibi söylemek. "Ön değerlendirme" ifadesini korumak güveni artırır.


### S20. AS-1 ve AS-2 tutmazsa ne olacak? Projenin yapay zekâ iddiası çökerse 7 milyon TL'nin karşılığı nedir?

`Önemli` — *Altındaki endişe: Hakem heyetinin nihai kaygısı budur: başarısızlık senaryosunda kamuya/bölgeye kalan değer. Aynı zamanda projenin dürüstlük testi.*

**Cevap.** Proje bu ihtimale göre kurgulandı. Yapay zekâ bileşeni 39 adam-ayın 10'u; kalan 29 adam-ay motor, zaman-farkındalıklı kural tabanı, rejim sınırı denetimi ve ürünleştirme; bunlar modelden bağımsız çalışan ve tek başına satılabilir bir ürün üretiyor. AS-1 tutmazsa ürün eksiksiz çalışır, sadece ön incelemeyi insan yapmaya devam eder; hatalı bir tutar üretmez, çünkü model zaten hiçbir aşamada tutara dokunmuyor. AS-1'i olumsuz sonuçlu araştırma sorusu olarak, veri kaynağı ve hacim etkisi ölçümleriyle birlikte raporlarız; "hangi eşikten sonra ek veri kazanç getirmiyor" bulgusu da bir çıktıdır. Asimetri şu: yanlış bir bulgunun maliyeti gereksiz bir inceleme adımı, doğru bir bulgunun kazancı bir uzman saati. Bu asimetri olmasaydı yapay zekâyı denetim ortamına hiç sokmazdık.

**Dayanak.** Form risk maddesi (1) (AS-1 olumsuz raporlanır, ürün sembolik katman üzerinden eksiksiz çalışmayı sürdürür); İP tablosu (İP5 = 10/39 adam-ay, İP1-İP4 ve İP6 modelden bağımsız); AS-1(c) asimetri paragrafı; EK-6 §7 (model hesap yapmaz, tutar üretmez, karar vermez).

**Tuzak.** "Başarısız olmayacağız" demek. Olumsuz sonucun maliyetini adam-ay cinsinden sayısallaştırmak çok daha ikna edicidir.


### S25. Yapay zekâ bileşeni hedefe ulaşamazsa 7 milyon TL boşa mı gitmiş olacak?

`KRİTİK` — *Altındaki endişe: Yönetim, başarısızlık hâlinde bölgeye ve firmaya geriye ne kaldığını, yani batık maliyetin büyüklüğünü ölçüyor.*

**Cevap.** Hayır, ve bunu baştan yazdık. Model hiçbir aşamada tutar hesaplamıyor; başarısızlığı hatalı rakam üretmez, sadece ön incelemenin insanda kalması demektir. O senaryoda elimizde kalan şey satılabilir üründür: 96'dan 140'a çıkmış YMM teyitli regresyon çapası, üç eksenli sürümlenen 5746 ve 4691 kural tabanı, rejim sınırı denetimi, kök-neden teşhisi ve iki pilot referansı. AS-1 olumsuz çıkarsa, veri kaynağı ve hacim ölçümleriyle birlikte olumsuz sonuçlu araştırma sorusu olarak raporlanır; bu da bir çıktıdır.

**Dayanak.** Riskler md.1; İP1-İP4 çıkış kriterlerinin hiçbiri modele bağlı değildir (96/96 kuruş farksız, çapa ≥140, bildirimsel kapsama ≥%90, kalem bazında ≥%85).

**Tuzak.** 'Başarısız olmaz' demek. Düşebilir ölçüt koymanın kendisi projenin Ar-Ge niteliğinin kanıtıdır; bunu savunmak güç değil, avantajdır.


### S29. Hesap çekirdeği zaten var ve başlangıç varlığı beyan edilmiş. O zaman bu projenin Ar-Ge içeriği daralmıyor mu?

`KRİTİK` — *Altındaki endişe: Heyet, 4691 muafiyetinden yararlanacak eforun gerçekten Ar-Ge olup olmadığını denetler; mevcut ürünün bakımını Ar-Ge diye sunan başvurular sık görülür.*

**Cevap.** Evet, bilinçli olarak daralıyor; bu dürüstlüktür. Çalışan hesap çekirdeğini başlangıç varlığı beyan ettik ki onu Ar-Ge eforu olarak saymayalım. Ar-Ge iddiası çekirdeğin üstünde başlıyor: 31 Ar-Ge adam-ayının 19'u yapay zekâ bileşeni ve teşhis altyapısı, 12'si zaman-farkındalıklı kural tabanıdır. Belge içeri alma, masaüstü ürünleştirme, arayüz ve hazır araçların uygulanmasını Ar-Ge saymadık; 8 adam-ay geliştirme olarak ayrı beyan ettik. Çekirdek olmasaydı 12 ayda yapay zekâ katmanına hiç sıra gelmezdi.

**Dayanak.** Ar-Ge Yönü sonu: 'Ar-Ge iddiası olmayan, geliştirme kalemi olarak beyan edilenler' listesi; EK-4: İP4+İP5 = 19 AA, İP1-İP3 = 12 AA, İP6+İP7 = 8 AA.

**Tuzak.** Her şeyi Ar-Ge saymaya çalışmak. Tersine, İP1'in 3 adam-ayı en tartışmalı kalemdir; heyet uygun görürse geliştirmeye taşınabileceğini kendiniz teklif edin; 31/8 yerine 28/11 olur, bütçe değişmez, güvenilirlik artar.



## 5. Bütçe, ekip ve takvim

*Teknopark yönetiminin standart soruları. Cevaplar rakama dayanmalı.*

### S21. 7.000.000 TL'lik bütçeyi neye dayandırıyorsunuz? Bu rakam bir yazılım projesi için yüksek değil mi?

`KRİTİK` — *Altındaki endişe: Heyet, rakamın bir hedefe göre geriye doğru uydurulup uydurulmadığını ve firmanın bu parayı gerçekten koyabilecek durumda olup olmadığını sınıyor.*

**Cevap.** Bütçenin 5,07 milyonu personel, 1,93 milyonu dışarıya çıkan nakittir. Yani %72'si zaten bordromuzdaki dört kişinin 39 adam-aylık eforudur; projeye özgü yeni nakit çıkışı 1,93 milyon TL'dir. Kırılımı: 550 bin YMM, 250 bin patent/marka/akademik danışmanlık, 300 bin donanım, 230 bin pilot saha seyahati, 200 bin bulut GPU, 200 bin lisans ve imza altyapısı, 50 bin sarf, 150 bin öngörülemeyen. Finansman kaynağı öz sermayedir; kamu desteği talep etmiyoruz. Riskteki para bizim paramızdır.

**Dayanak.** Proje Bilgi Formu bütçe tablosu (9 portal satırı): 39 AA × 130.000 = 5.070.000 ₺; dış kalemler toplamı 1.930.000 ₺; Finansman Kaynakları bölümünde yalnız 'Öz Sermaye' işaretli.

**Tuzak.** Bütçeyi hibe alınacakmış gibi savunmak. Gelir planındaki eski '8,7 M TL Teknopark hibesi' ifadesi bu forma ait değildir ve sunumda asla telaffuz edilmemelidir; formda kamu desteği kutusu işaretli değildir.


### S22. 130.000 TL'lik adam-ay birim maliyetinin dayanağı nedir? Bu rakamı nereden buldunuz?

`KRİTİK` — *Altındaki endişe: Teknopark yönetimi, personel giderinin şişirilip şişirilmediğini ve rakamın bordroyla doğrulanabilir olup olmadığını arıyor.*

**Cevap.** 130.000 TL bir fiyat değil, tam yüklü maliyettir: ağırlıklı ortalama brüt ücret + işveren SGK ve işsizlik payı + genel gider payı. İçinde kâr marjı yoktur. Karşılaştırma için: hizmet kolumuzda faturalanan adam-gün maliyeti 20-30 bin TL bandındadır, aylık karşılığı 200 bin TL'nin üzerine çıkar; çünkü orada satış, teklif ve boş kapasite de fiyata biner. Ar-Ge bütçesinde bunların hiçbiri yoktur. Kırılım EK-3'tedir; talep ederseniz isimleri maskelenmiş bordro özeti ve genel gider dağıtım anahtarını sunarız.

**Dayanak.** EK-3 birim maliyet tablosu; 5.070.000 ÷ 12 = 422.500 ₺/ay, 3,25 tam zaman eşdeğeri. Gelir planı §6: hizmet koluna atfedilen tam yüklü gün maliyeti 10-15 bin ₺, efektif faturalanan gün maliyeti 20-30 bin ₺.

**Tuzak.** Hizmet kolunun gün maliyeti bandını '130.000 bu bandın içinde' diye sunmak; o bant fiyat tarafıdır ve aylık karşılığı 130.000'in üstündedir. EK-3'teki çapraz kontrol satırı gerçek bordroyla doldurulmadan sunuma girmemelidir; hücreler hâlâ yer tutucudur.


### S23. 4 kişiyle 12 ayda 39 adam-ay nasıl çıkıyor? Bu insanlar başka iş yapmayacak mı?

`Önemli` — *Altındaki endişe: Heyet, adam-ay beyanının kâğıt üzerinde şişirilip şişirilmediğini ve kişilerin fiilen ayrılabilir olup olmadığını kontrol ediyor.*

**Cevap.** 4 kişi × 12 ay teorik tavanı 48 adam-aydır; biz 39 beyan ediyoruz, yani %81 doluluk. Kırılım: proje yöneticisi 6 adam-ay (yarı zamanlı), kıdemli geliştirici 12 (tam zamanlı), yapay zekâ mühendisi 12 (tam zamanlı), analiz ve test uzmanı 9 (dörtte üç zamanlı). Ortalama 3,25 tam zaman eşdeğeri. Yüzde yüz doluluk beyan etmedik, çünkü izin, eğitim ve idari yük gerçektir. EK-4'te kişi × iş paketi matrisi vardır; satır toplamları kişi eforuna, sütun toplamları iş paketi adam-ayına birebir eşittir.

**Dayanak.** EK-4 efor matrisi; sütun toplamları İP1-İP7: 3+6+3+9+10+5+3 = 39 adam-ay.

**Tuzak.** 'Dört kişi de tam zamanlı' demek. Bu 48 adam-ay eder ve beyanla çelişir; yarı zamanlı proje yöneticisi açıkça söylenmelidir.


### S24. 12 ay bu kapsam için yeterli mi? Yapay zekâ bileşenini 12 ayda bitirebilir misiniz?

`KRİTİK` — *Altındaki endişe: Teknopark yönetimi, 12 ayda bitmeyip uzatma talebiyle geri gelecek bir proje mi alıyorum diye bakıyor.*

**Cevap.** Kritik yol şudur: İP1 ay 1-2, kural tabanı İP2 ay 7'de kapanır, teşhis İP4 ay 10, model İP5 ay 12, pilotlar ay 9-12. En dar yer İP5'tir: 10 adam-ay, 7 ay ve tek bir yapay zekâ mühendisi. Bu yüzden hedefi THS 8 değil THS 7 koyduk; ticari olgunluk proje sonrası ilk 12 aya bırakıldı. Gecikme olursa neyin düşeceğini de yazdık: model tarafı düşer, sembolik katman ayakta kalır ve ürün eksiksiz çalışır. 12 ay ürünü değil, araştırma sorusunun cevabını yetiştirmek için planlanmıştır.

**Dayanak.** İş paketi tablosu (İP5: ay 6-12, 10 AA); THS bölümü: 'iki pilotla proje süresi içinde THS 8 iddia edilmesi gerçekçi bulunmamıştır'.

**Tuzak.** 'Rahat yetişir' demek. Dar yerin İP5 olduğu ve tek mühendise bağlı olduğu kabul edilmeli, karşılığında düşen kapsamın ne olduğu net söylenmelidir.


### S28. Yeminli Mali Müşavirlik için 550.000 TL neyin karşılığı? Bu bir danışmanlık lüksü değil mi?

`Önemli` — *Altındaki endişe: Mali temsilci, dış hizmet kaleminin gerçek bir iş karşılığı mı yoksa bütçeyi doldurmak için mi konduğunu ölçer.*

**Cevap.** Bu bir danışmanlık kalemi değil, ölçüm cihazıdır. 550 bin TL yaklaşık 35-40 uzman-gününe karşılık gelir. Dağılımı: 2019-2026 arası geçmiş parametre tablosunun Resmî Gazete referansıyla madde madde teyidi, 5746 ve 4691 kural setlerinin teyidi, 60 senaryoluk kütüphanenin mevzuat doğrulaması, iki pilotta mutabakat denetimi, geriye dönük düzeltme pencereleri için yazılı hukuk görüşü ve en kritiği: kör değerlendirmede uzman etiketleme. Kazanım 1, 2 ve 3'teki metriklerin hiçbiri YMM etiketi olmadan ölçülemez. Bu satırı çıkarırsanız projenin ölçülebilirliği düşer.

**Dayanak.** Alınacak Dış Hizmetler md.1; Kazanım 1 test seti 'YMM etiketli doğrulama örneklemi'; Kazanım 4 'YMM teyitli gerçek regresyon çapası 96 → ≥140'. Günlük uzman ücreti varsayımdır, sözleşme öncesi teklifle netleşecektir.

**Tuzak.** 'Mevzuat danışmanlığı alacağız' diye geçiştirmek. Asıl argüman YMM'nin ölçüm aracı olmasıdır; bu söylenmezse kalem kesilmeye açık hâle gelir.


### S41. Teknopark adam-ay taahhüdündeki personel aynı zamanda firmanın danışmanlık işlerini de yapacak mı? Personel çakışmasını nasıl önlüyorsunuz?

`KRİTİK` — *Altındaki endişe: Teknopark yönetiminin denetimde en sık karşılaştığı uyuşmazlık budur: bölge muafiyetiyle beyan edilen personelin fiilen bölge dışı ticari işte çalışması.*

**Cevap.** Ayrım yazılı ve denetlenebilirdir. Proje ekibi, firmanın danışmanlık kolundan ayrı bir ekip ve ayrı bir maliyet merkezidir; hizmet kolu personeli bu 39 adam-aya dâhil edilmemiştir. Bölge içi çalışma süreleri ve bölge dışı görevlendirme kayıtları 4691 mevzuatına uygun olarak ayrı tutulacaktır. Tek örtüşme proje yöneticisidir: aynı kişi hizmet kolunu da yönetiyor, bu yüzden projeye 12 değil 6 adam-ay yazdık, yani yarı zamanlı. Bunu gizlemiyoruz, EK-3 ve EK-4'te böyle beyan ettik. Hizmet teslimatı için ayrı bir 3-4 kişilik tavan tanımlı ve proje personeli o tarafa kaydırılmayacak.

**Dayanak.** EK-3 'Proje personelinin ayrıştırılması' bölümü; EK-4 efor matrisinde proje yöneticisi 6 AA (0,5 TZE); gelir planı §9: proje personelinin hizmet teslimatına kaydırılması kırmızı çizgi olarak tanımlı.

**Tuzak.** 'Hepsi sadece bu projede çalışacak' demek. Proje yöneticisinin yarı zamanlı olduğu ve neden öyle olduğu kendiniz söylenmezse, denetimde tutarsızlık olarak çıkar.



## 6. Saha pilotları

*THS 7 iddiasının tamamı iki pilota dayanıyor; en kırılgan nokta burasıdır.*

### S26. İki pilot bir yapay zekâ sisteminin doğrulanması için yeterli mi?

`Önemli` — *Altındaki endişe: Heyet, 'iki müşteri = doğrulama' iddiasının bilimsel olarak zayıf olduğunu bilir ve bunu kabul edip etmeyeceğinizi test eder.*

**Cevap.** İstatistiksel güç iki pilottan gelmiyor, gelemez de. Güç laboratuvar setlerinden geliyor: en az 400 vakalık hata enjeksiyonlu kalibrasyon seti, en az 60 mevzuat referanslı senaryo ve 140 YMM teyitli gerçek dönem çapası. Pilotların işi başkadır: sentetikten gerçeğe aktarım tutuyor mu ve ürün müşterinin kendi ortamında çalışıyor mu. İki pilot bunun için yeterlidir, genelleme iddiası için değildir; ve genelleme iddia etmiyoruz. Tabanı genişletmek için mevcut danışmanlık portföyümüzden anonimleştirilmiş dönemler ve bölge firmalarından 4691 senaryoları ekliyoruz.

**Dayanak.** Kazanım 3 test seti tanımı (≥400 vaka + ≥60 senaryo + iki pilotun gerçek fark envanteri); EK-6 §4: bölme kuruluş ve dönem bazındadır, pilot kör test seti eğitime girmez.

**Tuzak.** İki pilotu istatistiksel kanıt gibi sunmak. Pilot dış geçerlilik ve operasyonel hazırlık kanıtıdır; güç setlerden gelir.


### S27. Pilotlar gerçekten ücretli olacak mı? Niyet mektupları bağlayıcı mı?

`KRİTİK` — *Altındaki endişe: Sektör temsilcisi, büyük sanayi kuruluşlarının satın alma süreçlerini bilir ve 'ismi yazmışsınız ama imza var mı' diye bakar.*

**Cevap.** Dürüst cevap: niyet mektubu bağlayıcı değildir, bağlayıcı olduğunu da iddia etmiyoruz; metninde 'bağlayıcı satın alma taahhüdü niteliğinde değildir' cümlesi açıkça yer alır. Elimizde yazılı ihtiyaç beyanı var, imzalı satın alma emri yok. Kurumsal zincir gerçekte 6-12 hafta sürüyor: gizlilik sözleşmesi, bilgi güvenliği anketi, tedarikçi kaydı, satın alma, hukuk. Bu yüzden tedarikçi kayıt sürecini şimdiden başlattık ve yedek olarak tedarikçi kaydı hâlihazırda mevcut olan 10-15 hesaplık sözleşmeli müşteri listemizden iki aday tutuyoruz. Bir pilot düşerse proje durmaz, ismi değişir.

**Dayanak.** EK-2 niyet mektubu şablonu, hukuki nitelik notu; gelir planı Kanal 2: 'Yazılı sinyal ≠ bütçe onayı', yeni logoda 8-12 hafta; Kanal 1: tedarikçi kaydı zaten olan 10-15 isimli hesap.

**Tuzak.** 'Tüpraş ve Kale ile anlaştık' izlenimi vermek. İmza yoksa doğru ifade: 'yazılı ihtiyaç görüşü alındı, niyet mektubu imza sürecinde.' Yanlış beyan, başvurunun tamamının güvenilirliğini götürür.



## 7. Hukuk, veri koruma ve sorumluluk

*Bordro verisi yoğun kişisel veridir; bu bölüm hazırlıksız yakalanılmaması gereken yerdir.*

### S32. Yapay zekânın bulgusuna göre yanlış beyan verilirse sorumlu kim olacak?

`KRİTİK` — *Altındaki endişe: Mali temsilcinin en somut korkusu budur: hatalı beyanın idari ve cezai sonucu kimde kalıyor.*

**Cevap.** Üç katmanlı cevap. Mimari katman: model asla tutar hesaplamaz, bu kod düzeyinde ayrım ve denetim iziyle kanıtlanır; 'yapay zekâ yanlış hesapladı' senaryosu tanım gereği oluşamaz. Hukuk katmanı: beyan ve tasdik her zaman meslek mensubundadır; her raporda 'YMM teyidine tabidir' şerhi ve mevzuat sürüm damgası vardır; sözleşmede sorumluluk tavanı yıllık hizmet bedeliyle sınırlıdır ve mesleki sorumluluk sigortası araştırılmaktadır. Şeffaflık katmanı: yazılı bulgunun sonraki denetimde firma aleyhine kullanılabileceği ve bilinen hatanın düzeltilmemesinin kasıt doğurabileceği, müşteriye sözleşme öncesinde yazılı olarak bildirilir.

**Dayanak.** Kazanım 2: 'modelin hiçbir çıktısının tutar hesabına girmediği kod düzeyinde ayrım ve denetim iziyle kanıtlanır'; gelir planı §8 sorumluluk yönetimi ve aleyhe delil protokolü.

**Tuzak.** 'Sorumluluk müşteride' deyip geçmek. Asıl güçlü cevap modelin hesap yapmadığının teknik olarak kanıtlanabilir olmasıdır; bunu söylemezseniz cevap savunmacı görünür.


### S33. Bordro verisi kişisel veridir. Hangi hukuki dayanakla işleyeceksiniz, KVKK riskini nasıl yönetiyorsunuz?

`KRİTİK` — *Altındaki endişe: 1.700 merkezlik dar bir pazarda tek bir veri sızıntısı firmayı bitirir; heyet bu riskin farkında olup olmadığınızı ölçer.*

**Cevap.** İki ayrı kip var, karıştırılmamalı. Yazılım kipinde veri müşterinin kendi bilgisayarından hiç çıkmaz; biz kişisel veriye dokunmayız, veri işleyen dahi olmayız. Hizmet kipinde, yani geçmiş dönem mutabakatında, veri sorumlusu müşteri biz veri işleyeniz; tek satır veri almadan önce veri işleme sözleşmesi, maskeli kimlik numarası, veri minimizasyonu ve yurt içi barındırma şarttır. Özel nitelikli iz taşıyabilecek alanları; sendika kesintisi, engellilik indirimi; teşvik hesabı için gerekmedikçe hiç almıyoruz. Ayrıca KVKK 11/1-g kişiye, münhasıran otomatik analizle aleyhine sonuç doğmasına itiraz hakkı verir; 'kararı insan verir' tasarımı bu maddenin gereğidir.

**Dayanak.** Proje Özeti (kapalı devre, KVKK tasarım düzeyinde); gelir planı §8 KVKK maddesi; 6698 sayılı Kanun md.11/1-g ve md.12; AB muadili GDPR md.22 ve Yapay Zekâ Tüzüğü md.14 aynı yönde insan müdahalesi şart koşar.

**Tuzak.** İki kipi ayırmadan 'veri dışarı çıkmaz' demek. Hizmet kipinde veri fiilen işlenir; bunu saklamak sonradan tutarsızlık yaratır.


### S34. Bulut grafik işlemci kiralayacaksınız. O zaman veri kurum dışına çıkıyor, 'kapalı devre' iddianız çelişmiyor mu?

`KRİTİK` — *Altındaki endişe: Ürünün tek ayırt edici vaadi verinin dışarı çıkmamasıdır; bu kalem o vaadin tek görünür çelişkisidir.*

**Cevap.** 200 bin TL'lik kalem yalnızca ince ayar eğitimleri içindir ve yalnızca sentetik veriyle kullanılır. Eğitim verisinin ana gövdesi zaten gerçek kişi içermez: 60 parametrik senaryodan türetilen örnekler ve hata enjeksiyonlu vakalar. Pilot verisi bulutta hiç koşulmaz; yerelde kalır ve ağırlıklı olarak eğitime değil kör teste ayrılır. Teknik gerçek şudur: 1-4 milyar parametreli bir modelde düşük ranklı adaptör eğitimi kart-saatler mertebesinde bir iştir. Heyet tercih ederse bu satırı tamamen kaldırıp yerine tek bir yerel eğitim kartı alabiliriz; bütçe yaklaşık nötr kalır, dışarı hiç veri çıkmaz.

**Dayanak.** Bütçe satırı: 'yalnızca sentetik ve anonimleştirilmiş veriyle'; EK-6 §4: 'anonimleştirme eğitimden önce, bulut kiralaması yalnızca sentetik ve anonimleştirilmiş veriyle'; LoRA/QLoRA yöntemleri eğitilebilir parametre sayısını binlerce kat azaltır (Hu 2022; Dettmers 2023).

**Tuzak.** 'Anonimleştiriyoruz, sorun yok' demek. Anahtarla tokenleştirilmiş bordro verisi KVKK anlamında hâlâ takma adlı kişisel veridir; bu yüzden doğru savunma 'pilot verisi buluta hiç gitmez' olmalıdır.



## 8. Pazar, fiyat, rekabet ve ticarileşme

*Sektör temsilcisinin alanı.*

### S30. Teşvik mevzuatı yarın değişirse ya da rejim kaldırılırsa ürünün ömrü ne olur?

`Önemli` — *Altındaki endişe: Sektör temsilcisi, tek bir mevzuat maddesine bağlı ürünün ticari ömrünü sorgular.*

**Cevap.** Mevzuat değişikliği bu üründe risk değil, iş modelidir. Parametre, hesap şeması ve bilgi tarihi ayrı sürümlendiği için değişiklik kod değil kural dosyası demektir; imzalı çevrimdışı güncelleme aboneliğinin gerekçesi tam olarak budur. Gerçek risk rejimin tümüyle kaldırılmasıdır. Orada bile iki payanda var: geriye dönük mutabakat talebi zamanaşımı penceresi boyunca sürer, ve kural tabanı mimarisi başka bir teşvik rejimini bildirimsel kural seti olarak almaya açıktır. Ama dürüst olayım: yeni rejim eklemek proje kapsamında değil, proje sonrası yol haritasındadır.

**Dayanak.** Sürdürülebilirlik bölümü; Kazanım 5: 4691 kural seti çekirdek koda dokunulmadan yazılır, bildirimsel kapsama ≥%90, kaçış kancası ≤3; bu, yeni rejim ekleme maliyetinin ölçülmüş hâlidir.

**Tuzak.** 'Mevzuat hiç değişmez' ya da 'her rejimi kolayca ekleriz' demek. İkisi de yanlıştır; ölçülmüş kaçış kancası sayısı bu sorunun dürüst cevabıdır.


### S31. Yeminli mali müşavirler bu ürünü kendi işlerine rakip görmez mi? Onlar olmadan bu ürün satılabilir mi?

`Önemli` — *Altındaki endişe: Mali temsilci hem meslek mevzuatına uyumu hem de kanalın gerçekten çalışıp çalışmayacağını sorgular.*

**Cevap.** Ürün beyanname düzenlemiyor, bildirge vermiyor, tasdik etmiyor; bunlar 3568 ile meslek mensubunun tekelindedir ve orada kalır. Ürettiğimiz şey YMM'nin tasdik dosyasını güçlendiren delil paketidir. Satışta müşterinin kendi YMM'sini ilk toplantıya davet ediyoruz; baypas edilirse iş ölür, içeri alınırsa onaylayıcı olur. Kanal modelinde para akışı da tersinedir: YMM bize araç lisansı öder, biz YMM'ye komisyon ödemeyiz; komisyon meslek mensubunu disiplin riskine sokar. Dürüst risk şudur: elle mutabakat saatinden kazanan YMM direnç gösterebilir. Bunu henüz test etmedik; kanalı yazılı TÜRMOB uyum görüşü gelmeden açmıyoruz.

**Dayanak.** Gelir planı §8 (3568 sınırı, YMM'ye komisyon yasağı) ve §7 Kanal 6 (ay 6+, hukuk görüşü şartlı); Ticarileşme stratejisi md.3.

**Tuzak.** YMM'yi 'ikame edeceğiz' ya da 'komisyon vereceğiz' demek. Birincisi 3568 ihlali görüntüsü, ikincisi meslek mensubu için disiplin riskidir.


### S35. Pazar büyüklüğü tahminleriniz neye dayanıyor? 2.500-3.500 kuruluş rakamının kaynağı nedir?

`Önemli` — *Altındaki endişe: Heyet, pazar rakamının kaynaklı mı yoksa uydurma mı olduğunu ayırt etmek ister; zayıf noktayı kendiniz söylemek burada puan kazandırır.*

**Cevap.** İki rakamın kaynağı Bakanlıktır: Haziran 2026 itibarıyla 1.373 Ar-Ge ve 347 Tasarım Merkezi, toplam 1.720; Ağustos 2026 itibarıyla 113 bölgede 13.452 firma. Bunlar yayımlanmış sayılardır. Hizmet edilebilir pazar dediğimiz 2.500-3.500 kuruluş ise bizim saha tahminimizdir, yayımlanmış bir kaynağı yoktur ve formda da öyle etiketlenmiştir; sunumun en zayıf sayısı budur. Eşiği şöyle koyduk: bağımsız kontrolü ekonomik kılan ölçek, 30 ve üzeri Ar-Ge personeli ya da bölgede 10 ve üzeri istisna kapsamlı personeldir. Pilot 1'den sonra bu eşiği gerçek dönüşüm verisiyle yeniden hesaplayacağız.

**Dayanak.** Hedef Pazar bölümü ve kaynak dipnotları (sanayi.gov.tr, Haziran ve Ağustos 2026); SAM tahmini formda 'firmamızın saha deneyimine dayalı tahmin' olarak işaretlidir.

**Tuzak.** 1.720 ile 13.452'yi toplayıp 15 bin küsur kuruluşluk pazar iddia etmek. İki küme ayrık değildir; çok sayıda firma her iki rejimde birden yer alır.


### S36. 3-5 yılda 60-100 kuruluş ve 30-50 milyon TL yinelenen gelir hedefi gerçekçi mi?

`KRİTİK` — *Altındaki endişe: Sektör temsilcisi abartılı büyüme vaadini hemen yakalar; hangi sayının taahhüt hangisinin öngörü olduğunu ayırmanızı bekler.*

**Cevap.** Dürüst ayrım yapayım: hesap verdiğim sayı 3-5 yıl değil, 12-24 aydaki 10-14 kuruluştur; 60-100 rakamı formda da hipotez olarak etiketli bir öngörüdür. Tutması için yılda 20-25 yeni müşteri gerekir, bu da bugün sahip olmadığımız bir satış örgütü demektir. Tek gerçekçi yolu YMM ve SMMM kanalıdır: tek bir ofis 20 müvekkiliyle çarpan yaratır. 12 aylık planımız ise ölçülebilir: taban senaryoda 2,2-2,8 milyon TL faturalanan, beklenen senaryoda 4,5-5,5 milyon ve ay-12'de 250-350 bin TL aylık yinelenen gelir. Beni bu sayılardan sorgulayın.

**Dayanak.** Ekonomik Değeri bölümü ('hipotez olarak etiketlenmiştir'); gelir planı §6 üç senaryolu 12 aylık nakit projeksiyonu.

**Tuzak.** Uzun vadeli sayıyı savunmaya çalışmak. Kısa vadeli, ölçülebilir sayıya çekilmek daha güçlüdür ve heyeti ikna eder.


### S37. Logo, Mikro veya Netsis yarın aynı özelliği bordro modülüne eklerse ne olacak?

`Önemli` — *Altındaki endişe: Sektör temsilcisi, büyük bir oyuncunun özelliği kopyalamasıyla küçük firmanın silinip silinmeyeceğini sorgular.*

**Cevap.** Üç yapısal engel var. Birincisi denetim ilkesi: hesabı üreten sistem kendi hesabının bağımsız kontrolü olamaz; bordro kendi çıktısını doğrulayamaz. İkincisi mimari: bu paketler kural tablosunu tek sürüm tutar ve değişiklikte üzerine yazar; 96 ayı kendi kural sürümüyle yeniden kurmak bir özellik değil, mimari değişikliğidir. Üçüncüsü sorumluluk: bir sağlayıcı müşterisine 'geçmiş beyanınız yanlıştı' demenin riskini almak istemez. Dürüst senaryo: eklerlerse cari dönem basit hesap segmentini kaybederiz; geçmiş dönem mutabakatı, kapalı devre çalışma ve denetim savunma dosyası elimizde kalır. Büyük bir paketin bunu istemesi ise bizim için satın alma veya kural motoru tedarikçiliği demektir.

**Dayanak.** EK-1 madde 5 ve Rekabet Analizi md.2: ERP teşvik modülleri tek sürümlü kural tablosuyla çalışır ve hesabı üreten sistem olduklarından bağımsız kontrol sunmazlar.

**Tuzak.** 'Bizi yakalayamazlar' demek. Kaybedilecek segmenti açıkça söylemek, kalan savunulabilir alanı inandırıcı kılar.


### S42. Yıllık 0,3-0,9 milyon TL'lik bir yazılım bedeli Türkiye şartlarında yüksek değil mi? Müşteri bunu neden ödesin?

`Önemli` — *Altındaki endişe: Mali temsilci, fiyatın müşteri bütçesinde gerçekten yer bulup bulmayacağını ve hangi bütçe kaleminden çıkacağını sorgular.*

**Cevap.** Fiyatı teorik teşvik hacmine değil, müşterinin bugün zaten ödediği mali müşavirlik ve danışmanlık harcamasına çıpalıyoruz: giriş fiyatı o harcamanın yüzde 50-80'i. Ölçek olarak: 150 kişilik bir merkezde kurumlar vergisi indirimi hariç operasyonel teşvik akışı yılda yaklaşık 86 milyon TL'dir; 0,5-0,9 milyon TL'lik yıllık bedel bu akışın binde 6 ile yüzde 1'i arasına denk gelir. Savunma cümlesi şudur: binde birlik tek bir hata bile aboneliği öder. Ama bu bant bir varsayımdır, sahada test edilmemiştir; pilotlarda ölçülecek ve gerekirse revize edilecektir.

**Dayanak.** Ekonomik Değeri bölümü fiyat bandı; gelir planı §2: 150 kişide operasyonel teşvik ~86 M TL/yıl, fiyat tavanı kuralı (nicel değerin %15-25'i, danışman harcamasının %50-80'i).

**Tuzak.** Kurumlar vergisi indirimini de içeren şişkin toplam teşvik rakamını (150 kişide 154 M TL) açılış çıpası yapmak. Zararda veya düşük kârlı firmada o tutar nakit değildir; mali işler direktörü bunu ilk beş dakikada yakalar ve kalan bütün rakamları iskonto eder.


### S43. Zaten YMM tasdiki yaptırıyoruz. İkinci bir kontrol katmanına neden ihtiyacımız olsun?

`Önemli` — *Altındaki endişe: Sektör temsilcisi, halihazırda para ödediği bir hizmetin üstüne ikinci bir maliyet bindirmenin gerekçesini arar.*

**Cevap.** YMM tasdiki dönemseldir ve örneklemeye dayanır; bir yılın tamamını kalem kalem yeniden kurmaz. Ürün her bordro döneminde, tahakkuk kesinleşmeden, yüzde yüz kapsamla çalışır. Yani rakip değil, zamanlama farkıdır: YMM yıl sonunda örneklemle bakar, biz her ay tamamına bakarız ve bulduğumuzu YMM'ye delil dosyası olarak veririz. Denetim literatüründe bunun adı sürekli denetimdir; 1990'lardan beri çalışılan yerleşik bir alandır ve iç denetçilerin küresel meslek örgütü IIA'nın resmî rehberinde tanımlıdır. Yeni olan sürekli denetim fikri değil, onu Türkiye'de 5746 ve 4691 ölçeğine indirmektir.

**Dayanak.** Kazanım 6 (cari dönem kontrol hesabı, pilot başına ≥3 dönem, tahakkuk tarihinden önce teslim); Vasarhelyi ve Halper 1991 (sürekli denetimin kurucu çalışması); IIA GTAG 2015 sürekli denetim rehberi.

**Tuzak.** Müşterinin mevcut YMM'sini yanlışlayan ya da iç ekibini suçlayan bir dil kullanmak. Doğru çerçeve 'hatanızı buluruz' değil, 'zorunlu denetiminize birlikte hazırlanalım'dır.



## 9. Teknopark ve bölgeye katkı

*Teknopark hakem heyetlerinin doğrudan puanladığı kalem.*

### S38. Bu proje neden teknoparkta yürütülmeli? Kendi ofisinizde de yapamaz mıydınız?

`KRİTİK` — *Altındaki endişe: Teknopark yönetimi, muafiyetten yararlanmak için gelen 'posta kutusu' başvurularını ayıklamak ister.*

**Cevap.** Dört somut sebep. Bir: 4691 kural seti gerçek 4691 mükellefi olmadan yazılamaz ve doğrulanamaz; bölgenin kendisi sınama alanımızdır; İP3'te en az 24 gerçek çapa ve gönüllü bölge firmalarından senaryo istiyoruz. İki: AS-1 ve AS-2 gerçek araştırma sorularıdır; değerlendirme düzeneğinin bağımsız gözden geçirilmesi için TTO üzerinden akademik danışmanlık istiyoruz, bu niteliği bünyemizde tutmuyoruz. Üç: 4691 istisnaları bu 39 adam-aylık programı öz sermayeyle finanse edilebilir kılıyor. Dört: iki rejimi bir arada yürüten kuruluşlar en değerli segmentimizdir; bölgeye girdiğimizde firmamız o segmentin ilk örneği olur, yani kendi ürünümüzün sıfırıncı müşterisiyiz.

**Dayanak.** İP3 çıkış kriteri (4691'de ≥24 gerçek çapa); Hedef Kitle bölümü: bölge firmaları 4691 kural setinin ilk kullanıcı adaylarıdır; TTO'dan talep edilen hizmetler bölümü.

**Tuzak.** Yalnızca vergi avantajını söylemek. Asıl argüman bölgenin ürünün test alanı olmasıdır; muafiyet dördüncü sırada gelmelidir.


### S39. Projenin bölgeye somut katkısı ne olacak?

`Önemli` — *Altındaki endişe: Yönetim, bölge kaynağının karşılığında bölgeye dönen somut değeri ölçer; özellikle bölge dışı görevlendirme talebi buna bağlı değerlendirilir.*

**Cevap.** Ölçülebilir olanları sayayım: bölgede 4 nitelikli istihdam ve 12 ayda THS 5'ten 7'ye çıkan bir teknoloji; bölge firmalarının doğrudan kullanabileceği bir 4691 uyum aracı ve pilot öncesi erken erişim; iki patent ön değerlendirmesi ve bir marka tescili; uygun görülürse AS-1 ve AS-2 sonuçlarının Medeniyet Üniversitesi öğretim üyesiyle ulusal bir konferansta ortak bildiri olması. Abartmayacağım: 12 ay içinde 4 kişinin üzerine istihdam artışı taahhüt etmiyorum, ayrıca 240 saat bölge dışı görevlendirme istiyorum ve gerekçesi kişisel verinin tesis dışına çıkarılamamasıdır.

**Dayanak.** Proje Çıktıları (patent ön değerlendirmesi ay 9, marka tescili); TTO'dan talep edilen hizmetler (ortak bildiri); Bölge Dışı Görevlendirme: 240 saat.

**Tuzak.** Gerçekleştiremeyeceğiniz istihdam sayıları vermek. 240 saatlik bölge dışı talebi gizlemeden, gerekçesiyle birlikte kendiniz söyleyin.


### S40. İhracat hedefinizin olmaması değerlendirmede dezavantaj oluşturmuyor mu?

`İkincil` — *Altındaki endişe: Değerlendirme kriterlerinde ihracat potansiyeli genelde ayrı bir puan kalemidir; heyet boşluğu fark eder ve gerekçesini duymak ister.*

**Cevap.** Evet, bazı değerlendirme setlerinde puan kaybettirir; bunu bilerek seçtik. Sebep şu: dışa satılabilir olan kural dosyaları değil, yöntemdir. 'Deterministik motoru eğitim verisi referansı olarak kullanmak' ve 'sembolik doğrulama kapısı' rejimden bağımsızdır. Her ülkede aynı problem var: Fransız gelir vergisi hesabı 92 bin satırlık özel bir kural dilinde yazılıdır, AB'nin EUROMOD altyapısı kuralları her politika yılı için ayrı tutar. Yani mimari ihraç edilebilir, tablolar edilemez. Ama 12 aylık plana koymadığım bir ihracat vaadi yazmam; taahhüt etmediğim şeyi savunamam.

**Dayanak.** Hedef Pazar bölümü: 'Ürün Türk mevzuatına özgü olduğundan ihracat hedefi yoktur'; Merigoux ve ark. 2021 (Fransız vergi kodu, 92.000 satır 'M' kural dili); Sutherland ve Figari 2013 (EUROMOD, 27 ülke, yıl bazlı kural sürümleri).

**Tuzak.** Puan almak için sahte bir ihracat hedefi eklemek. Yöntemin taşınabilirliğini anlatmak dürüst ve daha güçlü bir cevaptır.



---

## Cevabı dosyada henüz karşılığı olmayan sorular

Aşağıdaki cevaplar, başvuru dosyasının şu ankı hâlini aşan taahhütler içeriyor. Sunum öncesinde ya dosyaya işlenmeli ya da cevaptan çıkarılmalıdır; ayrıntı için `hakem-sunumu.md` sonundaki "Karar bekleyen maddeler" bölümüne bakınız.

| Soru | Dosyayı aşan taahhüt |
|---|---|
| S8 | İki bağımsız YMM etiketlemesi ve Cohen kappa raporlanması (EK-6 §6 tek etiketleyici varsayıyor) |
| S15, S4 | Erişim destekli (RAG) karşılaştırma kolu ve sembolik taban çizgisi (formda üç kol tanımlı) |
| S24 | Ay 2-4 fizibilite ölçümü ve karar kapısı |
| S5, S6, S9 | McNemar testi, Clopper-Pearson aralığı, güç analizi (formda istatistiksel test planı yok) |
| S10 | Karıştırılmış etiket kontrol koşumu ve kaynak dönem kesişim taraması |
| S39 | Bölgeye sayısal taahhütler (6 kişi istihdam, 5 bölge firması, 2 seminer) |

*Bu tablo bir eksiklik listesi değil, bir hizalama listesidir. Sunumda söylenen her taahhüdün dosyada karşılığı olmalıdır; hakem heyeti ikisini yan yana okur.*
