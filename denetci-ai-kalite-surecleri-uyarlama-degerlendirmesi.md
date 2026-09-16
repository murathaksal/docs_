# Denetci.AI'nın Kalite Süreçleri Denetimine Uyarlanması: Değerlendirme

*Soru: Denetci.AI mimarisi, kalite yönetim sistemi süreçlerinin denetimine uyarlanabilir mi? Bu belge, mimariyi katman katman sökerek hangi parçanın taşındığını, hangisinin taşınmadığını ve hangi koşulda taşınabileceğini değerlendirir. Belge bir karar önerisi ve ölçülebilir bir ön adımla biter.*

*Not: Bu değerlendirme mevcut teknopark başvurusunun kapsamını değiştirmez; `denetci-proje-bilgi-formu.md` aynen geçerlidir. Gerekçesi bölüm 7'dedir.*

---

## 1. Kısa cevap

**Mimari uyarlanabilir, ürün doğrudan uyarlanamaz.**

Denetci.AI'nın değerini taşıyan altı katmandan beşi (kural tabanı sürümleme, sembolik doğrulama kapısı, denetçi rolündeki model, kapalı devre çalışma, mühürlü kayıt) kalite süreçlerine iyi, bazı noktalarda mevzuat denetiminden **daha iyi** oturur. Taşınmayan katman birinci katmandır ve projenin taşıyıcı kolonu odur: **deterministik hesap motoru (oracle)**.

5746 tarafında "doğru cevap" hesaplanabilir bir tutardır; motor onu kuruş farksız üretir ve EK-6'daki tüm eğitim verisi üretim yöntemi bu tek gerçeğe dayanır. Kalite tarafında "doğru cevap" çoğu bulguda bir **uygunluk yargısıdır** ve hesaplanamaz. "Eğitim kaydı, 7.2'nin istediği yetkinlik kanıtı olarak yeterli mi" sorusunun kapalı formu yoktur.

Bu, uyarlamanın önünde bir duvar değil, bir **ölçüm sorusudur**: kalite bulgularının ne kadarlık bir dilimi kayıtlardan deterministik olarak kurulabilir? O dilim yeterince genişse (bölüm 9'daki eşik), mimari taşınır ve ikinci bir Ar-Ge projesi olarak gerçek ve yeni bir araştırma sorusu doğar. Dar kalırsa ürün, yapay zekâ iddiası olmayan bir kontrol listesi aracına iner.

---

## 2. Katman katman aktarılabilirlik

Mevcut mimarinin altı bileşeni (ana belge, "Çözüm mimarisi") karşısında kalite alanındaki karşılıkları:

| # | Denetci.AI bileşeni | Kalitedeki karşılığı | Aktarım |
|---|---|---|---|
| 1 | Deterministik hesap çekirdeği (tutarı yeniden kurar) | Tam karşılığı **yok**; yerine "kayıt tabanlı uygunluk kural motoru" (tarih, kapsama, tamlık, çapraz tutarlılık) | **Kısmi / yeniden inşa** |
| 2 | Zaman-farkındalıklı kural tabanı (parametre, şema, bilgi tarihi) | Standart revizyonu, müşteri özel gereklilikleri (CSR) sürümü, kuruluşun kendi prosedür revizyonu | **Tam, hatta daha güçlü** |
| 3 | Geçmiş beyan mutabakatı ve sembolik teşhis | Geçmiş kayıtların, o tarihte yürürlükte olan prosedür revizyonuna göre yeniden denetimi; mühürlenmiş denetim dosyası | **Tam** |
| 4 | Denetçi rolündeki dar kapsamlı yerel model | Bulgu yorumlama, denetçi sorusu üretme, kanıt talebi, uygunsuzluk ifadesi taslağı | **Tam; görev tanımı bire bir** |
| 5 | Sembolik doğrulama kapısı (atıf doğrulama) | Madde kütüğüne karşı atıf doğrulama + kapsam uygulanabilirliği (ISO 9001 md. 4.3) | **Tam** |
| 6 | Kapalı devre masaüstü, imzalı çevrimdışı güncelleme | Savunma, havacılık, ilaç, tıbbi cihaz ve müşteri gizlilik sözleşmeli otomotiv işlerinde aynı ihtiyaç | **Tam, ama satın alma kaldıracı zayıflar** |

Tablonun okunuşu: **taşınmayan tek satır birincidir ve diğer beşinin hepsi ona bağlıdır.** Model (4) motorun (1) bulgusunu inceler; kapı (5) motorun kural tabanına (2) karşı doğrular; eğitim verisi (EK-6) motorun çıktısından üretilir. Birinci katman zayıflarsa zincirin tamamı zayıflar.

---

## 3. Kritik kırılma noktası: oracle sorunu

EK-6'nın temel ilkesi tek cümledir: *"etiketi insan değil, deterministik motor üretir."* Projenin AS-1 araştırma sorusunun "(a) eğitim verisi nereden gelir?" katmanı bu ilkeyle cevaplanmıştır ve hakem heyetine verilen cevap budur.

Kalite denetimine geçildiğinde bu ilke üç yerden kırılır:

**a) Doğru cevap hesaplanamaz.** Bir uygunsuzluk bulgusu üç parçadan kurulur: gereklilik (hangi madde), kanıt (ne görüldü), uygunsuzluk ifadesi (neden karşılamıyor). Üçüncü parça bir yargıdır. Motor "kalibrasyon süresi 14 ay önce dolmuş" diyebilir; "bu, ürün uygunluğunu etkiledi mi" sorusunu hesaplayamaz.

**b) G2'nin otomatik etiketi kaybolur.** Mevcut projede araştırma yönlendirme görevinin etiketini motor kendiliğinden koyar: önerilen belge getirilir, motor yeniden koşar, fark kapandıysa öneri doğrudur. Kalitede "fark kapandı" sinyali yoktur; belge getirildiğinde kapanma kararını yine insan verir. Bu, EK-6'nın en zarif parçasının, projenin elle etiketleme darboğazını aşan mekanizmasının doğrudan taşınamaması demektir.

**c) Girdi yapılandırılmamıştır.** 5746 tarafında girdi Muhtasar ve Prim Hizmet Beyannamesi, hizmet listesi, tahakkuk fişi; biçimi belli, iç toplamları kendini doğrulayan belgelerdir (EK-6, G4). Kalitede girdi prosedür metni, serbest formatlı form, taranmış kayıt, fotoğraf ve üçüncü parti yazılım ekranıdır. Belge alan çıkarımı (G4) burada yardımcı bir kalem olmaktan çıkıp **baskın mühendislik maliyeti** hâline gelir.

Bu üç kırılma, uyarlamanın "aynı ürüne ikinci kural seti eklemek" (İP3'ün 4691 için yaptığı iş) olmadığını gösterir. 4691, 5746 ile aynı matematiksel türdendir: girdi bordro, çıktı tutar. Kalite farklı türdendir.

---

## 4. Ama tamamen değil: kalitede deterministik çekirdek nerede var

Uyarlamanın yaşayabilir olması, kalite bulgularının hesaplanabilir bir alt kümesinin bulunmasına bağlıdır. Böyle bir alt küme **vardır** ve sanıldığından geniştir. Aşağıdakilerin her biri, kayıtlardan tekrarlanabilir biçimde kurulabilen, yargı içermeyen kontrollerdir:

**Tarih ve geçerlilik kontrolleri**
- **Kalibrasyon geçerliliği (ISO 9001 md. 7.1.5.2):** her ölçüm kaydı için, ölçümün yapıldığı tarihte cihazın kalibrasyonu geçerli miydi? Tamamen deterministik.
- Personel yetkinlik ve eğitim geçerliliği (md. 7.2): görev gereklilik matrisi ile eğitim/sertifika kayıtlarının tarih bazlı eşleşmesi.
- Doküman revizyon geçerliliği (md. 7.5): kayıt, doldurulduğu tarihte yürürlükte olan form revizyonuyla mı doldurulmuş?
- Tedarikçi yeniden değerlendirme periyodu (md. 8.4), DÖF termin aşımı ve etkinlik doğrulama gecikmesi (md. 10.2).

**Kapsama ve tamlık kontrolleri**
- **İç denetim programı kapsaması (md. 9.2.2):** çevrim içinde her süreç, her madde ve (IATF 16949'da) her vardiya denetlenmiş mi? Bu bir küme kapsama hesabıdır, deterministiktir.
- Yönetimin gözden geçirmesi girdi tamlığı (md. 9.3.2): standardın saydığı girdi kalemlerinin tamamı toplantı kaydında var mı?
- IATF 16949'da imalat süreci denetimi ve ürün denetimi frekans kapsaması.

**Çapraz tutarlılık zincirleri (mevcut İP4'ün "çapraz tutarlılık kural zinciri" yeteneğinin bire bir karşılığı)**
- **PFMEA ↔ Kontrol Planı ↔ İş Talimatı ↔ PPAP dörtlüsü:** FMEA'da tanımlı bir kontrol, kontrol planında yer alıyor mu; kontrol planındaki ölçüm sıklığı iş talimatıyla aynı mı; kontrol planındaki karakteristik PPAP ölçüm sonuçlarında var mı? Otomotiv denetimlerinin klasik bulgu kaynağıdır ve tamamen kural bazlıdır.
- Özel karakteristik işaretlerinin resim, FMEA ve kontrol planı arasında tutarlılığı.

**Sayısal ve istatistiksel kontroller (burada gerçek bir hesap motoru vardır)**
- MSA: tekrarlanabilirlik ve yeniden üretilebilirlik yüzdesi ile ayırt edilebilir kategori sayısının yayımlanmış kabul ölçütlerine göre değerlendirilmesi.
- SPC: süreç yeterlilik indekslerinin müşteri eşiğine göre hesabı; kontrol grafiği kural ihlallerinin (seri, trend, sınır aşımı) otomatik taranması.
- Bu iki başlık, kalite tarafındaki **gerçek deterministik motordur** ve 5746 motorundaki "kuruş farksız yeniden hesap" rolünü üstlenebilir.

**En güçlü yapısal benzerlik:** ISO 9001 md. 7.1.5.2, bir ölçüm cihazının amaca uygun olmadığı tespit edildiğinde **önceki ölçüm sonuçlarının geçerliliğinin olumsuz etkilenip etkilenmediğinin belirlenmesini** ister. Bu, tam olarak Denetci.AI'nın geriye dönük mutabakat işlemidir: bir kural sapması bulunur, geçmiş dönemler o sapmanın ışığında yeniden değerlendirilir, etkilenen kapsam tutarıyla (burada: parça adedi, sevkiyat, karantina kapsamı) çıkarılır, mutabık kalınan kısım mühürlenir. Üstelik çıktı burada da **paraya çevrilebilir**: karantina ve geri çağırma kapsamının daraltılması ölçülebilir bir tutardır.

**Değerlendirme:** kalitede hesaplanabilir çekirdek vardır, ancak 5746 motorundan **daha sığ ve daha geniş yüzeylidir**. Tek bir derin hesap yerine çok sayıda küçük kural ailesi söz konusudur. Bu, mühendislik maliyetini kural yazımına kaydırır ve Ar-Ge iddiasının ağırlık merkezini bölüm 8'de anlatıldığı yere taşır.

---

## 5. Kural tabanı: kalitede karşılık daha güçlü

AS-4'ün üç eksenli yürürlük tarihli sürümleme sorusu (parametre, hesap şeması, bilgi tarihi) kalite alanına yalnızca taşınmakla kalmaz, **daha zengin bir sınama alanı bulur**:

| Denetci.AI ekseni | Kalitedeki karşılığı |
|---|---|
| Parametre sürümü | Standart revizyonu ve geçiş dönemi; yaptırım gücündeki yorumların yürürlük tarihleri |
| Hesap şeması sürümü | Yapı değiştiren revizyonlar (örneğin risk temelli düşünceye geçişte madde yapısının değişmesi); yeni FMEA yöntemine geçiş |
| Bilgi tarihi | Kuruluşun kendi prosedür ve form revizyon tarihleri; müşteri özel gerekliliklerinin (CSR) sürüm tarihleri |

Buradaki saha ihtiyacı gerçektir ve bugün karşılanmamaktadır: **denetçiler geçmiş kayıtları çoğu zaman bugünkü prosedüre göre denetler.** 2024 tarihli bir kayda 2026 revizyonunun gerekliliğiyle uygunsuzluk yazılması yaygın bir tartışma konusudur. "O tarihte yürürlükte olan prosedür revizyonuna göre denetle" yeteneği, mevcut projedeki "o dönemin mevzuat sürümüyle yeniden hesapla" yeteneğinin doğrudan karşılığıdır ve aynı özgünlük iddiasını taşır.

**Ancak bir maliyet farkı vardır.** 5746 ve 4691 tek bir ulusal mevzuat ailesidir; kural tabanı bir kez kurulur, herkese aynı gider. Kalitede kural tabanı üç katmanlıdır: standart (ortak), müşteri özel gereklilikleri (**her müşteri için ayrı**) ve kuruluşun kendi dokümantasyonu (**her kuruluş için ayrı**). Bu, tek bir kural paketinin tüm müşterilere dağıtıldığı abonelik modelini kırar ve bakım yükünü müşteri sayısıyla birlikte büyütür. **Uyarlamanın en ciddi ticari riski budur** ve bölüm 6'daki iş modeli sonucunu doğurur.

---

## 6. İş modeli ve pazar

**a) Toplantıyı açan kaldıraç kaybolur.** Mevcut gelir tezinin ilk cümlesi *"geri kazanım toplantıyı açar, denetim savunulabilirliği sözleşmeyi kapatır."* Kalitede hesaplanabilir bir geri kazanım tutarı yoktur; ilk cümle boşalır. Yerine konabilecek en güçlü aday, bölüm 4'ün sonundaki kalibrasyon sapması senaryosudur (etkilenen sevkiyat kapsamının daraltılması) ve ikinci aday müşteri denetimine hazırlık süresidir. İkisi de mevcut kaldıraç kadar keskin değildir.

**b) Rekabet çok daha yoğundur.** 5746/4691 alanı ince bir niştir ve EK-1'deki tarama az sayıda ürün bulmuştur. Kalite yönetim yazılımı alanı ise doymuş bir pazardır; yerli tarafta yaygın kurulu tabanı olan doküman ve DÖF yönetim paketleri, yurt dışı tarafta çok sayıda kurumsal ürün bulunur ve neredeyse tamamı yapay zekâ özellikleri duyurmaktadır. "Kategori boşluğu değil özellik bileşimi" argümanı burada da kurulabilir, ama çok daha dar bir açıklıkta.

**c) Kurulu taban entegrasyon yükü doğurur.** Hedef kuruluşlarda kalite kayıtları çoğunlukla mevcut bir yazılımın içindedir. Ürün ya o sisteme bağlanacak (bu, mevcut projenin en güçlü satış argümanını, yani "bulut onayı, bilgi güvenliği anketi, bilgi işlem projesi gerekmez" avantajını zayıflatır) ya da yapılandırılmamış belge okuyacaktır (bölüm 3c'deki maliyet). Kapalı devre çalışma avantajı yine de savunma, havacılık, ilaç ve müşteri gizliliği ağır basan otomotiv işlerinde geçerliliğini korur.

**d) Bütçe sahibi değişir.** Mevcut üründe alıcı mali işlerdir ve karşılığında vergi/teşvik tutarı vardır. Kalitede alıcı kalite yönetimidir; bütçesi tipik olarak daha küçüktür ve yazılım kalemi çoğunlukla harcanmış durumdadır.

**Sonuç:** kalite uyarlaması, mevcut ürünün ikinci bir müşteri segmenti değil, **ayrı ekonomisi olan ikinci bir üründür.** Aynı satış hattından ve aynı fiyat merdiveninden yürümez.

---

## 7. Mevcut başvuruya eklenmemelidir

Bu, değerlendirmenin en net maddesidir.

1. **Kapsam daraltması bilinçli ve belgelenmiş bir güçtür.** Ana belge kapsamı "bilinçli olarak tek mevzuat ailesiyle" sınırlar; CBAM ayağı aynı disiplinle projeden çıkarılmıştır (README, düzeltme kaydı). Üçüncü bir alan eklemek, hakem heyetine kapsam şişkinliği gerekçesi verir ve daraltma kararının değerini geriye dönük olarak zayıflatır.
2. **Adam-ay bütçesi kaldırmaz.** 31 Ar-Ge adam-ayının 10'u İP5'te, 9'u İP4'tedir. Kalite tarafında kural motoru sıfırdan kurulacaktır; mevcut planın içinden çıkarılacak bir yer yoktur.
3. **THS beyanı bozulur.** Mevcut THS 5 beyanı, sembolik çekirdeğin gerçek veriyle doğrulanmış olmasına dayanır. Kalite tarafında böyle bir çekirdek yoktur; bütünleşik sistem beyanı THS 3-4'e iner.
4. **Zamanlama uygun değildir.** Portal doldurma ve ek toplama süreci açıktır (README, "Başvuru öncesi yapılacaklar"). Bu aşamada kapsam değişikliği, tamamlanmış tutarlılık kontrollerinin (portal v5 kontrol raporu) tekrarını gerektirir.

**Doğru yer: ARGELOG-003, ardıl proje.** Bu yalnızca bir erteleme değil, daha iyi bir kurgudur. Mevcut proje AS-1'i tek bir alanda, oracle'ın **tam** olduğu koşulda sınar. Ardıl proje, aynı yöntemi oracle'ın **kısmi** olduğu bir alanda sınar. İkincisi, birincisinin tekrarı değil, doğal ve özgün devamıdır; mevcut projenin çıktıları (denetçi modeli, doğrulama kapısı, veri üretim hattı, şema-zorlamalı çıktı altyapısı) ikinci projenin başlangıç varlığı olur ve platform tezini kanıtlar.

---

## 8. ARGELOG-003 yapılacaksa: önerilen çerçeve

**Standart seçimi: IATF 16949 (otomotiv) birincil aday.** Gerekçe: kural yoğunluğu en yüksek ve en buyurgan standarttır (bu, bildirimsel kural tabanı için en verimli alan demektir); yürürlük tarihli sürümlemesi hazırdır (kurallar sürümleri ve yaptırım gücündeki yorumlar yürürlük tarihleriyle yayımlanır, AS-4'ün üç ekseni için gerçek bir sınama alanıdır); çapraz doküman tutarlılığı (bölüm 4) deterministiktir; denetim baskısı ve uygunsuzluk maliyeti yüksektir (özel statü ve müşteriye bağlı yaptırımlar); Türkiye'de tedarikçi tabanı geniş ve coğrafi olarak kümelenmiştir.

*Alternatif:* ISO 13485 / tıbbi cihaz. Denetim acısı ve ödeme gücü daha yüksektir, ancak Türkiye pazarı dardır ve ürünün kendisinin yazılım validasyonundan geçmesi gerekir (kalite sisteminde kullanılan yazılımın validasyonu şartı); bu, doğrudan maliyet demektir. İlk sürüm için önerilmez.

**Yeni araştırma sorusunun şekli.** Mevcut AS-1 "oracle var" varsayımıyla kuruludur. Ardıl projenin sorusu tam olarak bunun kalktığı yerdir:

> **AS-1':** Oracle yalnızca bulgu uzayının bir alt kümesini kapsadığında, denetçi rolündeki model nasıl eğitilir? Deterministik alt kümeden öğrenilen denetçi dili (atıf disiplini, soru kalıbı, kanıt talebi biçimi), yorumlayıcı alana ne ölçüde aktarılır?

Bu, literatürde açık ve sınanabilir bir sorudur; düşebilir ölçütü de nettir: deterministik alt kümeyle eğitilmiş modelin, yorumlayıcı bulgularda ince ayarsız temel modele karşı ölçülebilir üstünlük sağlayıp sağlamadığı, kör YMM/baş denetçi değerlendirmesiyle ölçülür. Üstünlük çıkmazsa soru olumsuz sonuçlanır ve bu da geçerli bir Ar-Ge çıktısıdır.

**Doğrulama kapısı (AS-2') burada daha da güçlüdür.** Madde atfı doğrulamasına kalitede bir kontrol daha eklenir: **kapsam uygulanabilirliği.** Kuruluş, ISO 9001 md. 4.3 uyarınca belirli maddeleri kapsam dışı bırakmış olabilir (tipik örnek: tasarım ve geliştirme). Kapsam dışı bir maddeye uygunsuzluk yazan bulgu, kullanıcıya ulaşmadan elenmelidir. Bu, mevcut kapının doğal bir genişlemesidir ve ölçülebilir bir metrik verir.

**Değişmeyen ilke.** "Hesabı motor yapar, bulguyu model inceler, kararı insan verir" ilkesi kalitede yalnızca korunmaz, **zorunludur**: belgelendirme ve iç denetim düzenlemeleri denetçiyi bir kişi olarak tanımlar, denetçi bağımsızlığı ve yetkinliği şarta bağlıdır. Model hiçbir koşulda uygunsuzluk kararı veremez; denetçinin ön inceleme yükünü üstlenir. Bu, mevcut projedeki konumlandırmanın bire bir aynısıdır ve satış argümanı olarak da aynı işi görür.

**Pilot erişimi.** Mevcut pilot muhatapları (yazılı ihtiyaç görüşü alınan iki sanayi kuruluşu) kalite yönetim sistemi işleten kuruluşlardır; erişim avantajı vardır. Ancak muhatap birim değişir (mali işler yerine kalite yönetimi) ve bu, ilişkinin sıfırdan kurulacağı anlamına gelir; ihtiyaç görüşü yeniden alınmalıdır.

---

## 9. Karar önerisi ve ölçülebilir ön adım

**Öneri:** Uyarlama yapılmalıdır, ancak (i) mevcut başvurunun kapsamına girmeden, (ii) ayrı ürün ekonomisiyle, (iii) ve **önce ucuz bir ölçümle** kapısı açılarak.

Uyarlamanın tamamı tek bir ampirik soruya bağlıdır: *kalite bulgularının ne kadarı kayıtlardan deterministik olarak kurulabilir?* Bu soru tartışmayla değil sayımla cevaplanır.

### Ön adım: bulgu kapsama ölçümü

**Yöntem.** İki veya üç kuruluştan, son üç yılın iç denetim ve belgelendirme denetimi bulguları toplanır (hedef: 120-150 bulgu). Her bulgu üç sınıftan birine atanır:

- **A: Deterministik.** Yalnızca kayıtlara, tarihlere ve çapraz tutarlılığa bakılarak, yargı olmadan kurulabilir.
- **B: Kısmi.** Deterministik bir tetikleyicisi vardır, sonuçlandırması yargı ister.
- **C: Yorumlayıcı.** Tamamen denetçi yargısına dayanır.

Sınıflandırma, bir baş denetçi ile birlikte ve kör olarak (iki bağımsız sınıflandırıcı, uyuşmazlık oranı raporlanır) yapılır.

**Maliyet.** Yaklaşık 2 kişi-hafta, artı baş denetçi hizmet alımı. Yazılım geliştirme yoktur.

**Karar kapısı (düşebilir ölçüt).**

| Sonuç | Karar |
|---|---|
| A ≥ %30 **ve** A+B ≥ %60 | Uyarla. Oracle çekirdeği ürünü taşır; AS-1' sınanabilir bir araştırma sorusudur; ARGELOG-003 yazılır. |
| A %20-30 | Dar kapsamla uyarla: yalnızca kalibrasyon geçerliliği, program kapsaması ve çapraz doküman tutarlılığı. Yapay zekâ bileşeni ikinci sürüme bırakılır. |
| A < %20 | **Uyarlama.** Bu durumda ürün bir kontrol listesi aracıdır, Ar-Ge iddiası taşımaz ve doymuş bir pazara özelliksiz girer. |

**İkinci ölçüm (birinciyle birlikte, aynı maliyetle).** Toplanan bulguların kaçı, kuruluşun **mevcut** yazılımlarındaki yapılandırılmış veriden üretilebilirdi? Bu oran, bölüm 3c'deki belge okuma maliyetinin ne kadarının atlanabileceğini gösterir ve entegrasyon mu belge çözümleme mi sorusunu veriyle cevaplar.

### Ölçüm yapılmadan alınabilecek tek karar

Mevcut başvuru değiştirilmez. Kalite uyarlaması, gerekiyorsa teknopark görüşmelerinde **projenin ardıl yol haritası** olarak sözlü biçimde anlatılabilir; bu, platform tezini güçlendirir ve başvuru metnine hiçbir risk eklemez. Ana belgedeki "tek mevzuat ailesi" disiplini, tam da bu tür bir genişlemenin sonraki projeye bırakıldığını gösterdiği için güçlüdür.

---

## 10. Özet tablo

| Soru | Cevap |
|---|---|
| Mimari taşınır mı? | Evet; altı katmanın beşi doğrudan, biri yeniden inşa gerektirir. |
| En büyük risk? | Oracle'ın kısmi olması; EK-6'daki otomatik etiketleme mekanizmasının doğrudan taşınamaması. |
| İkinci risk? | Kural tabanının müşteri ve kuruluş bazında çoğalması (bakım yükü) ve yapılandırılmamış girdi. |
| Mevcut başvuruya eklensin mi? | **Hayır.** Kapsam disiplini, adam-ay ve THS beyanı üç ayrı gerekçe verir. |
| Doğru form? | ARGELOG-003 ardıl projesi; mevcut projenin çıktıları başlangıç varlığı. |
| Hangi standart? | IATF 16949 birincil; ISO 13485 ilk sürüm için önerilmez. |
| Sonraki somut adım? | 120-150 geçmiş bulgu üzerinde kapsama ölçümü (yaklaşık 2 kişi-hafta), bölüm 9'daki karar kapısıyla. |
