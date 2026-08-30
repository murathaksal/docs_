# ARGUS Hızlı Gelir ve Katma Değer Planı

*Mevcut doğrulanmış hesap çekirdeği + danışmanlık kapasitesiyle, 10 aylık proje bitişini beklemeden gelir üretme planı. Dört mercekli analiz (hizmet-önce gelir, müşteri ekonomisi, fiyatlama/paketleme, kanal) + alıcı-CFO gözüyle adversarial eleştiri + sentez sürecinin çıktısıdır; değer rakamları gerçek hesap motoru koşularak üretilmiştir. Tüm fiyatlar varsayımdır ve sahada test edilecektir.*

---

## 1. Katma Değer Tezi

Müşteri ARGUS'tan "hata avı" değil, bordrosunun yaklaşık yarısı büyüklüğünde bir nakit akışının — Ar-Ge personeli başına yılda ~0,9-1,1 M TL teşvikin (motorla hesaplanmış; profil varsayımlı) — kuruş düzeyinde doğruluğunu ve 2 yılda bir zorunlu denetimde savunulabilirliğini satın alır. Değer üç kanalda TL'ye çevrilir ve her raporda müşterinin KENDİ verisiyle gösterilir: (1) önlenen koşan kayıp — %1-3 hata bandı varsayımıyla 150 kişilik merkezde yılda 0,9-2,6 M TL (KV hariç operasyonel bazda; iki yönlü ölçülür, fazla yararlanma riski de raporlanır); (2) tahsil edilebilir geriye dönük düzeltme — GV/DV'de VUK 5 yıl, SGK'da ~6 aylık pencere (YMM/hukuk teyidine tabi), 150 kişide tek seferlik ~0,5-1,5 M TL; (3) yaptırım riskinin beklenen maliyetinin düşürülmesi — 3 ay durdurma 150 kişide ~21 M TL operasyonel kayıp demek, yıllık %5-10 gerçekleşme varsayımıyla 1,1-2,2 M TL/yıl beklenen maliyet. Toplam nicel yıllık değer 150 kişilik merkezde ~2-5 M TL; ARGUS'un yıllık bedeli (abonelik + hizmetler, ~0,4-0,9 M TL) bu değerin %15-25'i bandında kalır ve "binde birlik tek hata bile aboneliği öder" cümlesiyle savunulur. Ayırt edici üretim aracı bugün çalışan deterministik motordur (Bakanlığın yayımladığı Nisan 2026 verisiyle iç doğrulama — 96/96 çapa testi, yeşil koşum sağlandıktan sonra kullanılacak ifade budur); satılan şey ise motor + insan gözüyle üretilmiş, mevzuat sürümü damgalı, müşterinin YMM'sinin tasdik dosyasını güçlendiren rapor ve sürekli gölge hesaptır — beyan/tasdik daima meslek mensubunda kalır.

## 2. Değer Hesabı (Müşteri Başına TL)

HESAP TABANI (gerçek motorla — hesap çekirdeği — hesap.py — koşulmuş simülasyon; ekonomi merceğinden devralındı): 2026/I parametreleri: brüt asgari ücret 33.030 TL, GV dilimleri 190K/400K/1,5M, DV binde 7,59, SGK aylık tavan 297.270 TL (web kaynaklarıyla teyitli). Bilinen tek sapma: %40 GV dilim eşiği kodda 5,3 M, bazı kaynaklarda 5,0 M TL — profildeki maaşlarda etkisiz, YMM teyidine gidecek. VARSAYIMLAR (açıkça işaretli): tüm personel 4/a ve imalat (%5'lik 5510 indirimi); eğitim karışımı %5 doktora / %25 YL / %70 diğer; fiili ortalama brüt 50 kişide 146,5K, 150 kişide 160,5K, 400 kişide 176,5K TL; yıl boyu 2026/I parametreleri sabit (2026/II artışı tutarları yukarı iter — muhafazakâr yön). SONUÇ — YILLIK YÖNETİLEN TEŞVİK: 50 kişi: toplam ~46 M TL, KV HARİÇ OPERASYONEL ~26 M TL (SGK ~12 M + GV/DV ~14 M); 150 kişi: toplam ~154 M, operasyonel ~86 M; 400 kişi: toplam ~455 M, operasyonel ~258 M. SATIŞTA ANA ÇIPA OPERASYONEL TUTARDIR: KV indirimi (~toplamın %43'ü) zararda/düşük kârlı firmada nakit değildir; CFO bunu ilk beş dakikada yakalar, şişkin açılış rakamı kalan her rakamı iskonto ettirir. KATMA DEĞER (KV hariç operasyonel bazda, yıllık): (a) Önlenen koşan kayıp [%1-3 hata bandı — ampirik değil, hesap çekirdeği doğrulama çalışmalarında fiilen görülen hata sınıflarıyla (dilim hesabı, 'Emekli' yazımının sessiz 4/a'ya düşmesi, emekliye işsizlik primi, destek personeli ceil/int çelişkisi) desteklenen uzman tahmini; Pilot 1'de ölçülüp kalibre edilecek; hatalar İKİ YÖNLÜdür — fazla yararlanma çıkarsa bu tahsilat değil geri ödeme riskidir ve öyle raporlanır]: 50 kişi 0,26-0,78 M; 150 kişi 0,86-2,6 M; 400 kişi 2,6-7,7 M TL. (b) Tek seferlik retrospektif [GV/DV son 12 ay + SGK ~6 ay penceresi; SGK penceresinin (5510 Ek m.17) geriye dönük teşvik taleplerine uygulanması SGK pratiğinde tartışmalı — yazılı YMM/hukuk görüşü gelmeden satış vaadi yapılmaz]: 50 kişi ~0,15-0,45 M; 150 kişi ~0,5-1,5 M; 400 kişi ~1,5-4,5 M TL. (c) Denetim riski beklenen maliyeti [3 ay durdurma = operasyonel yıllığın 1/4'ü; yıllık gerçekleşme olasılığı %5-10 varsayım]: 50 kişi 0,3-0,65 M; 150 kişi 1,1-2,2 M; 400 kişi 3,2-6,5 M TL/yıl. (d) Kısmi danışman ikamesi [pazar tahmini]: 0,3-0,6 / 0,6-1,2 / 1,2-2,4 M TL/yıl. TOPLAM NİCEL YILLIK DEĞER: 50 kişi ~1-2,5 M; 150 kişi ~3-7 M; 400 kişi ~8-20 M TL. FİYAT TAVANI KURALI: müşteri teorik değere değil mevcut alternatife (YMM/danışman harcaması) çıpalar; giriş fiyatı danışman harcamasının %50-80'i, nicel değerin %15-25'i bandında tutulur — 50 kişi ~0,3-0,5 M/yıl, 150 kişi ~0,5-0,9 M/yıl, 400 kişi ~0,9-1,8 M/yıl toplam ARGUS harcaması savunulabilir.

## 3. Gelir Merdiveni

### Basamak 1 — Kama ürün (hafta 2-6)
- **Ürün:** 7555 Tavan Hızlı Analizi: Ağu-2025'ten bugüne kişi×ay bazında tavan bağlama analizi + yanlış terkin tutarı + VUK düzeltme yol haritası (kod hazır: baglayici_ucret_tavani + compliance DK7). Yalnızca mevcut sözleşmeli danışmanlık müşterilerine ve sinyalli 2 firmaya — tedarikçi onboarding'i olmayan yerde satılmaz
- **Fiyat:** 100-150 bin TL sabit (varsayım; efektif maliyet 20-30 bin TL/faturalanan adam-gün ile 3-5 AG işte ince marj — amacı marj değil veri erişimi ve pilot hakkı); 30 gün içinde pilota dönüşürse %100 mahsup
- **Ne zaman:** Mevcut sözleşmeli müşteride ilk fatura hafta 3-6; yeni logoda 8-12 hafta (NDA+KVKK+tedarikçi kaydı gerçeği). Teslim taahhüdü: EKSİKSİZ veri tesliminden itibaren 5 iş günü — sözleşmeye böyle yazılır
- **Ön koşul:** test_anchor.py↔fixture senkronu (1 gün; test 'brut_ucret', model 'arge_brut_ucret' okuyor — teyit edildi) + yeşil 96/96 koşum çıktısı; 2 sayfalık rapor şablonu; KVKK veri alım paketi (DPA, maskeli TCKN, veri minimizasyonu)

### Basamak 2 — Ana giriş ürünü (hafta 4-10)
- **Ürün:** Denetim Hazırlık Taraması: compliance 12 kural + bordro tutarlılık 11 kural + PDKS/TZE raporu; çıktı 'denetçi gözüyle bulgu listesi + hazırlık yol haritası'. Çerçeve 'hatanızı buluruz' DEĞİL 'zorunlu denetiminize hazırlanalım' — mali işler müdürünü kahraman yapan dil; temiz çıktı da satılabilir üründür (denetim güvence raporu)
- **Fiyat:** 125-250 bin TL kademeli (varsayım; hedef müşterinin tek imza onay eşiğinin altında kalmak — eşik müşteri bazında doğrulanır). 5-10 adam-gün efor
- **Ne zaman:** Satış 2-4 hafta (ılık liste), teslim 1-2 hafta; ilk fatura hafta 6-10. Aciliyet çıpası tartışmasız olanlar: 2 yılda bir denetim takvimi + VUK düzeltme zamanaşımının yıl sonu kapanışı (SGK 6-ay penceresi hukuk görüşü gelene dek ana argüman YAPILMAZ)
- **Ön koşul:** Rapor şablonunun compliance.py/bordro_kontrol.py çıktısına bağlanması (~1 hafta); denetim takvimi sorusuyla hedefleme; müşterinin YMM'sinin ilk toplantıya davet edilmesi (itiraz eritici)

### Basamak 3 — Ana değer ürünü (ay 2-4)
- **Ürün:** Retrospektif Mutabakat Pilotu (Concierge, kapılı 6-8 hafta): geçmiş beyan yükleme → motorla mutabakat → üç kanallı değer raporu (tahsil edilebilir TL [YMM teyidine tabi] / önlenen koşan kayıp / denetim savunulabilirliği). Kapsam kapıları sözleşmede: son 12 ay SGK + son 24 ay GV/DV örneklemi, tek tüzel kişilik, personel tavanı, 2 veri teslim turu; aşımı değişiklik talebi
- **Fiyat:** Kademeli sabit: 600 bin (≤75 kişi) / 800 bin (76-200) / 1 M TL (200+) (varsayım); milestone faturalama %25 imza / %35 ara rapor / %40 teslim. BAŞARI PRİMİ YOK (3568 riski — bkz. yasal sınırlar); fiyat itirazında ikinci kart prim değil kapsam daraltmadır
- **Ne zaman:** Sinyalli 2 firmada imza ay 2-3 (yazılı sinyal ≠ bütçe onayı; NDA→bilgi güvenliği→satın alma→hukuk zinciri 6-12 hafta), ilk milestone faturası imzada; teslim +6-8 hafta. İlk pilot gerçekte 1,5-2× efor koşar (60-80 AG) — bilinçli müşteri edinme yatırımı olarak muhasebeleştirilir
- **Ön koşul:** Tarama/flaş ile ön-tanı yapılmış olması (kapanış oranını yükseltir); kapılı sözleşme + sorumluluk tavanı maddesi; fazla-yararlanma-bulgusu protokolünün sözleşmede yazılı olması; danışmanlık kolundan ayrılmış 2-3 kişi (Teknopark 25 AA havuzundan DEĞİL)

### Basamak 4 — Tekrarlayan gelir (ay 3-6)
- **Ürün:** Gölge Hesap + Sürekli Uyum aboneliği: her bordro dönemi motor paralel koşar, tahakkuk kapanmadan fark + compliance raporu; mevzuat değişikliği bildirimi. İleriye dönük tek 'suçsuz' ürün — kimseyi mahcup etmez, mevcut YMM'yi tamamlar; 10 ay sonra ARGUS SaaS'ına birebir devrolan hazır ARR
- **Fiyat:** Kurulum 75-150 bin TL + aylık kademeli: ≤75 kişi 30-40 bin / 76-200 kişi 50-70 bin / 200+ teklifle (90-150 bin çıpası) (varsayım; danışman harcamasının %50-80'i ve aylık teşvik hacminin ~binde 0,5-1'i bandı); yıllık peşine -%10-15. Pilot bedelinin EN FAZLA %50'si ilk yıl aboneliğe mahsup (dönüşüm varsayımı kanıt gelene dek %30-40)
- **Ne zaman:** İlk abonelik ay 3-4 (tarama müşterisinden), pilot dönüşümleri ay 4-6; land-and-expand — yıl 2'de modül/kapsam genişlemesiyle fiyat merdiveni
- **Ön koşul:** En az 1 tamamlanmış tek seferlik hizmet referansı; bordro şablon eşlemesi (bordro_sablon.py mevcut, kurulum 3-5 AG); aylık veri teslim SLA'sı

### Basamak 5 — Premium (ay 5-9)
- **Ürün:** (a) 5 Yıl VUK Retrospektifi (GV/DV odaklı tam pencere taraması — BAZ Hattı'nın ilk üretim vakası, Teknopark iş paketleriyle çift amaçlı); (b) On-prem/kapalı ağ kurulumu (savunma/büyük sanayi — bulut baştan elenen segment)
- **Fiyat:** 5-yıl retro: 1,5-3 M TL proje (60-90 AG); on-prem: abonelik listesinin 1,5-2 katı/yıl + 250-400 bin TL kurulum (varsayım)
- **Ne zaman:** Satış ay 5-7, teslim ay 7-10; ancak 2-3 tamamlanmış referanstan sonra
- **Ön koşul:** BAZ Hattı kısmi teslimi (proje kapsamında zaten yapılıyor); on-prem paketleme/kurulum betikleri; anonim vaka çalışması

### Basamak 6 — Ölçek kanalı (ay 6-12)
- **Ürün:** YMM/SMMM araç lisansı — para akışı TERSİNE: YMM müvekkiline kendi hizmetini satar, ARGUS'u alt yüklenici/yazılım lisansı olarak öder (meslek mensubuna komisyon ödeme modeli mevzuat riski nedeniyle YOK)
- **Fiyat:** 20-40 bin TL/ay/ofis veya kullanım bazlı lisans (varsayım; pazarda test edilecek)
- **Ne zaman:** İlk 90 günün GELİR PLANINDA DEĞİL; ay 6+ — kanal kurmak 6-12 ay sürer
- **Ön koşul:** Yazılı hukuk görüşü (TÜRMOB mevzuatı uyumu); 2-3 isimli/anonim referans vaka; ortak markalı rapor şablonu

## 4. Paketler ve Fiyat Modelleri

### 7555 Tavan Hızlı Analizi
**Fiyat modeli:** 100-150 bin TL tek seferlik sabit; 30 gün içinde pilota dönüşürse %100 mahsup (kapı aralayıcı — marj değil veri erişimi hedefi)

Ağu-2025→bugün bordro dökümünün motora yüklenmesi; kişi×ay tavan bağlama tablosu, yanlış terkin edilen GV+DV tutarı, VUK düzeltme yol haritası; 2 sayfalık yönetici raporu + ek tablo. Eksiksiz veriden itibaren 5 iş günü teslim. 'Tahsil edilebilir' ifadeleri YMM teyidi şerhiyle

### Denetim Hazırlık Taraması
**Fiyat modeli:** 125-250 bin TL tek seferlik sabit (personel kademesine göre); tek imza onay eşiği altı hedeflenir

23 otomatik kural (compliance 12 + bordro tutarlılık 11) + PDKS/TZE raporu + insan gözü yorumu; bulgu listesi 'mevzuat karmaşıklığından kaynaklanan sektörel sapmalar' dilinde, yaptırım senaryoları FUD'suz; hazırlık yol haritası; temiz çıkarsa imzalı denetim güvence raporu. Mevzuat sürümü damgalı

### Retrospektif Mutabakat Pilotu (Concierge)
**Fiyat modeli:** Kademeli sabit 600 bin / 800 bin / 1 M TL (≤75 / 76-200 / 200+ kişi); milestone %25 imza + %35 ara rapor + %40 teslim; başarı primi yok; kapsam kapıları ve sorumluluk tavanı sözleşmede

6-8 hafta kapılı süreç: veri alımı (maskeli, minimize) → motorla dönem dönem yeniden hesap → fark mutabakatı → üç kanallı değer raporu + düzeltme yol haritası (beyan adımları müşterinin YMM/SMMM'sine devredilir, ARGUS hesap+delil dosyası üretir). 4. haftada ara bulgu sunumu. İki yönlü bulgu taahhüdü: eksik de fazla da raporlanır, yayılım kararı müşterinin

### Gölge Hesap + Sürekli Uyum Aboneliği
**Fiyat modeli:** Kurulum 75-150 bin TL + aylık 30-40 / 50-70 / 90-150 bin TL kademeli; yıllık peşine -%10-15; pilot bedelinin ≤%50'si ilk yıl mahsup

Her bordro döneminde bağımsız paralel hesap; tahakkuk kapanmadan fark raporu + compliance uyarıları + mevzuat değişikliği bildirimi; çeyreklik yönetici özeti. Proje çıktıları (bitemporal mevzuat, kök-neden) geldikçe aynı aboneliğe değer eklenir — yeni SKU gerekmez; ARGUS SaaS'ına kesintisiz devir

### Kurucu Müşteri Programı (ilk 5 logo)
**Fiyat modeli:** İndirim, referans taahhütlerinin sözleşmeye yazılması karşılığı; ömür boyu değil 24 ay sınırlı (fiyat tabanını kalıcı çökertmemek için)

24 ay fiyat sabitleme + %15-20 indirim; karşılığında: referans görüşmesi yapma taahhüdü + 1 tanıştırma + anonim/bant rakamlı vaka çalışması izni (isimli vaka yayını zorunlu tutulmaz — kabul oranı düşük). Sinyalli 2 firma 1 ve 2 numaralı adaylar

### Premium: 5 Yıl VUK Retrospektifi / On-Prem
**Fiyat modeli:** 5-yıl retro 1,5-3 M TL proje bazlı; on-prem abonelik ×1,5-2/yıl + 250-400 bin TL kurulum

VUK penceresinin tamamının taranması (GV/DV) — BAZ Hattı'nın ilk üretim vakası; veya kapalı ağ kurulumu + yıllık bakım (savunma sanayii segmenti). Ancak referanslar oluştuktan sonra satışa açılır

## 5. 30 / 60 / 90 Gün Planı

### İlk 30 gün
- GÜN 1-2: hesap çekirdeği deposundaki tests/test_anchor.py alan adı senkronunu düzelt ('brut_ucret' → 'arge_brut_ucret'; satır 42 ve 161 dahil), 96/96 çapa setini yeşile çevir, koşum çıktısını arşivle; tüm materyalde ifadeyi 'Bakanlığın yayımladığı Nisan 2026 verisiyle iç doğrulama' olarak sabitle (Bakanlık onayı/akreditasyonu izlenimi = yanıltıcı ticari uygulama riski)
- GÜN 1-5: Hukuk paketi startı — KVKK veri işleme sözleşmesi (DPA) + NDA + sorumluluk tavanı maddeli hizmet sözleşmesi şablonları; üç yazılı görüş talebi: (a) başarı primi/nispi ücret 3568 analizi, (b) SGK ~6 ay geriye pencere (5510 Ek m.17) uygulanabilirliği, (c) YMM işbirliği/lisans modelinin TÜRMOB mevzuatına uyumu; mesleki sorumluluk sigortası araştırması
- GÜN 3-8: Ürünleştirme — Denetim Hazırlık Taraması tek sayfalık teklif + rapor şablonu (compliance.py/bordro_kontrol.py çıktısından); 7555 Hızlı Analiz 2 sayfalık rapor şablonu; fiyat listesi ve milestone'lu pilot sözleşme taslağı (kapsam kapıları + fazla-yararlanma protokolü + 'YMM teyidine tabidir' şerhi yazılı)
- GÜN 5-10: Veri alım runbook'u — maskeli TCKN/veri minimizasyonu şablonu, excel_import ile kendi seed verisinde uçtan uca prova, 'eksiksiz veri tesliminden itibaren 5 iş günü' SLA dili; anonim demo tenant (anonimleştirme standardı belgeli)
- GÜN 5-12: Hedefleme — mevcut sözleşmeli danışmanlık müşterilerinden 10-15 hesaplık isimli liste (tedarikçi onboarding'i atlanan tek kanal) + sinyalli 2 firma; her hesaba sahip ata; denetim takvimi bilgisi topla
- GÜN 10-20: Sinyalli 2 firmayla toplantı — gündem 'denetim hazırlığı + tahsil edilmemiş hak', müşterinin YMM'si toplantıya davetli; 30 gün hedefi imza DEĞİL: veri paylaşım izni + tarama satışı + pilot niyet mektubu; Kale'de tedarikçi kaydı/bilgi güvenliği anketi sürecini hemen başlat (en uzun kalem)
- GÜN 10-30: Mevcut sözleşmeli müşterilerde 1-2 tarama/flaş satışı ve ilk teslim — İLK FATURA hedefi hafta 3-6 (yalnız bu kanalda gerçekçi)
- GÜN 20-30: Kapasite planı yazılı — hizmet tarafı tavanı 3-4 kişi; Teknopark 25 AA taahhüdündeki isimler hizmet teslimatına atanmaz (hibe denetiminde personel çakışması riski); 90 gün ölçüm panosu: görüşme→teklif→fatura dönüşümleri

### 31–60 gün
- Pilot #1 sözleşmesini imzala (tercihen sinyalli firmalardan tek-imza süreci hızlı olan; Kale bekliyorsa paralel orta ölçekli merkezle başla) — %25 milestone faturası imzada; ilk pilot için iç bütçe 60-80 AG (yatırım olarak kabul edildi), sözleşme kapsamı 40 AG'lik kapılarla korunur
- 2-3 Denetim Hazırlık Taraması teslimi; her teslimde sonraki basamak teklifi ('şu 3 alanda derin bakmaya değer' → pilot; 'her ay böyle takip edelim' → gölge hesap)
- İlk gölge hesap aboneliği kurulumu (tarama müşterisinden; kurulum 3-5 AG, bordro_sablon.py eşlemesi)
- Pilot #1 4. hafta ARA BULGU sunumu — iki yönlü dil ('net etkiyi ölçüyoruz'), rakamlar YMM teyidi şerhiyle; müşterinin YMM'sine delil dosyası formatını göster, düzeltme adımlarını ona devret
- Hukuk görüşleri geldiyse: SGK 6-ay penceresi olumluysa aciliyet mesajına ekle ('her ay bir ay siliniyor'); olumsuz/belirsizse VUK yıl sonu zamanaşımı + denetim takvimi çıpasında kal; prim görüşü ne olursa olsun ilk 12 ay sabit fiyat modelinde kal
- Ilık listeyi işle: 10-15 hesabın tamamına dokunulmuş, 3-5 aktif fırsat, gerçekçi dönüşüm varsayımı görüşme→ücretli iş %10-15 (soğuk kanal ve webinar bu çeyreğin gelir planında YOK — huni beslemesi olarak ay 4'e hazırlık)
- Teslim şablonlarını standartlaştır: tarama eforunu 5-7 AG'ye, flaş kontrolü 3 AG'ye indir; junior devri başlat
- 60. gün ölçümü: kümülatif fatura 0,3-0,7 M TL bandında mı, pilot milestone takviminde mi; sapma varsa önce kanal/konumlandırma gözden geçirilir, fiyat düşürülmez

### 61–90 gün
- Pilot #1 final raporu ve sunumu — üç kanallı değer tablosu (tahsil edilebilir [YMM teyitli] / önlenen koşan kayıp / denetim savunulabilirliği); AYNI toplantıda gölge hesap dönüşüm teklifi: pilot bedelinin ≤%50'si ilk yıl aboneliğe mahsup, tercihen yıllık peşin -%10-15
- Gerçek hata oranını ölç ve yayınlama disiplinine bağla: %1-3 bandı Pilot #1 verisiyle kalibre edilir; pazarlama TL vaatleri bundan sonra bant değil vaka bazlı verilir; bulgu az çıktıysa değer anlatısı denetim güvencesine döner (temiz rapor da üründür)
- Anonim/bant rakamlı vaka çalışması yaz ('150 kişilik merkezde X-Y TL bandı'); kurucu müşteri taahhüdündeki referans görüşmesi ve 1 tanıştırmayı fiilen iste
- Pilot #2 imzası (ikinci sinyalli firma veya tarama müşterilerinden yükseltme); eşzamanlı pilot sayısı azami 2 — kapasite tavanı korunur
- 2-3 gölge hesap abonesine ulaş; abonelik onboarding runbook'unu standartlaştır (2-3 AG/müşteri)
- Kale grup yayılımını 90-180 gün penceresine planla (ayrı tüzel kişilikler = ayrı satın alma süreçleri; 90 günde ek pilot beklenmez); savunma/kapalı ağ talebi çıktıysa on-prem teklif hazırlığı
- Pilot verilerini BAZ Hattı iş paketine girdi yap (gerçek geçmiş-beyan örnekleri + kök-neden vakaları) — hizmet eforu Teknopark çıktılarını müşteri parasıyla besler; hibe raporlamasında personel ayrımı belgeli kalır
- 90. gün karar toplantısı: gerçekleşen dönüşüm oranlarıyla fiyat bantlarını revize et; darboğaz teslim kapasitesi mi satış mı kararlaştır (danışman alımı vs kapıyı daraltma); 2. çeyrek hedefi: 2 pilot + 5-6 abone + tarama hattı. 90 gün BAZ HEDEFİ: 2-4 fatura, 0,5-1,2 M TL faturalanan, 0,3-0,8 M TL tahsilat; 1,5-2,5 M ancak iki sinyalli firmanın da hızlı dönmesi halinde (iyimser etiket)

## 6. 12 Aylık Nakit Projeksiyonu (Üç Senaryo)

ORTAK VARSAYIMLAR (tümü açık): Hizmet koluna atfedilen maliyet ~450-700 bin TL/ay = 2,5-3,5 FTE × tam yüklü 10-15 bin TL/adam-gün (Argelog bordrosuyla kalibre edilmeli); faturalanabilir doluluk %50-65 → efektif maliyet 20-30 bin TL/faturalanan AG (satış, teklif, veri kovalama faturalanamaz). Tahsilat faturadan 30-60 gün sonra (kurumsal vade). Ürün ekibinin (4-6 FTE) maliyeti bu projeksiyona DAHİL DEĞİL — Teknopark hibesi (~8,7 M TL/10 ay) ve özkaynakla taşınır; hizmet kolu başabaşı 'hizmete atfedilen maliyet' bazında tanımlıdır. KDV hariç. Kurlar/parametreler 2026 sabit. --- MUHAFAZAKÂR (yalnız mevcut ilişkiler döner; sinyalli 2 firmadan 1'i, geç): Ay 1-3: 1-2 tarama + 1 flaş (~0,3-0,4 M) + pilot #1 imza ay 3 (%25 ≈ 0,15-0,2 M). Ay 4-6: pilot #1 kalan milestone'lar (~0,45-0,6 M) + 1 tarama + 1 abonelik başlar. Ay 7-12: 2-3 abonelik (ort. 40-60 bin/ay) + 2-3 tarama; 2. pilot YOK. YIL FATURALANAN ≈ 2,2-2,8 M TL; ay-12 MRR ~100-160 bin; hizmet kolu kümülatif BAŞABAŞ YOK — yıl ~0,5-1,5 M açıkla kapanır, bilinçli pazar giriş yatırımı olarak hibe/özkaynak taşır. Ay 6 karar kapısı: dönüşüm yoksa fiyat değil konumlandırma/kanal revize edilir. --- BEKLENEN (sinyalli 2 firma + portföyden istikrarlı akış): Ay 1-3: 2-3 tarama/flaş (~0,5 M) + pilot #1 imza (%25). Ay 4-6: pilot #1 teslim (~0,6 M) + pilot #2 imza + 2 abonelik (kurulum + aylık) ≈ 1,3-1,6 M. Ay 7-9: pilot #2 teslim + 2 tarama + 4-5 abone koşuyor ≈ 1,4-1,6 M. Ay 10-12: pilot #3 imza/başlangıç + 6-7 abone + 1 yıllık peşin ≈ 1,4-1,8 M. YIL FATURALANAN ≈ 4,5-5,5 M TL; ay-12 MRR ~250-350 bin; hizmet kolu AYLIK başabaşı ay 8-10, KÜMÜLATİF başabaş ay 11-12. --- İYİMSER (iki sinyal de erken kapanır + grup/referans yayılımı çalışır): 4-5 pilot, 8-10 tarama, 8-10 abone (2-3 yıllık peşin), ay 8-12'de 1 premium 5-yıl retro (1,5-2 M). YIL FATURALANAN ≈ 8-10 M TL; ay-12 MRR ~450-600 bin; kümülatif başabaş ay 7-9. --- DUYARLILIK: En kritik iki değişken (1) pilot #1'in imza tarihi (her ay gecikme tüm zinciri kaydırır — bu yüzden ilk faturalar pilotu beklemeyen tarama hattından), (2) pilot→abonelik dönüşümü (%30-40 varsayıldı; %50 mahsup nedeniyle dönüşen müşterinin ilk yıl net abonelik geliri düşük görünür — MRR bu netleştirmeyle hesaplandı). Başarı primi hiçbir senaryoda gelir kalemi değildir; SGK penceresi gelirleri (gain-share yerine YMM'ye devredilen süreç) projeksiyona alınmamıştır — olursa üstüne gelir.

## 7. Kanal Planı

SIRALAMA İLKESİ: Satın alma/KVKK darboğazını atlayan kanal önce; her kanal aynı merdivene (tarama → pilot → abonelik) akar; ilk 90 günün geliri yalnız 1-2. kanaldan planlanır. KANAL 1 — MEVCUT SÖZLEŞMELİ DANIŞMANLIK MÜŞTERİLERİ (ilk faturaların tek gerçekçi kaynağı): 10-15 isimli hesap; tedarikçi kaydı/NDA zaten var, ilk fatura 3-6 hafta. Mesaj 'denetim hazırlığı + 7555 güncel sorusu'. Gerçekçi dönüşüm: görüşme→ücretli iş %10-15 (sıcak ilişkide dahi; %30-40 varsayımı eleştirilerde çürütüldü). KANAL 2 — SİNYALLİ 2 FİRMA: Yazılı sinyal ≠ bütçe onayı; hedef 30 günde veri paylaşım izni + niyet mektubu, imza ay 2-3. Kale = referans HEDEFİ, nakit planı ona kurulmaz (en büyük grupta en yavaş satın alma); paralel olarak tek-imzacılı orta ölçekli 2-3 merkez yürütülür. Satışta müşterinin MEVCUT YMM'si ilk toplantıya davet edilir ve rapor 'YMM'nizin tasdik dosyasını güçlendiren delil paketi' olarak konumlanır — YMM baypas edilirse deal ölür, içeri alınırsa onaylayıcı olur. 'Kendi hatanı satın alma' direncine karşı çerçeve daima ileriye dönük koruma/denetim güvencesi; 'ne bulursak önce size, yayılım sizin kararınız' taahhüdü yazılı. KANAL 3 — ILIK LİSTE GENİŞLETME (ay 2-4): Referans görüşmeleri + danışmanlık kolunun ilişki ağından 15-25 hesap; soğuk kanal 90 gün planında YOK (soğuk B2B kapanış %2-5 — huni matematiği taşımaz). KANAL 4 — İÇERİK/WEBINAR (ay 4+, gelir beklentisiz huni besleme): 'Ar-Ge merkezi denetiminde en sık bulgular' teknik webinarı, SAHA İstanbul/teknopark yönetimleriyle (üye sayıları doğrulanmalı); CTA = tarama. KANAL 5 — KALE GRUP YAYILIMI (ay 4-6+): Pilot başarılıysa referans görüşmesi + 1 tanıştırma taahhüdü işletilir; ayrı tüzel kişilik = ayrı süreç, 90-180 gün pencere. KANAL 6 — YMM/SMMM ARAÇ LİSANSI (ay 6+, hukuk görüşü şartlı): Para akışı tersine (YMM öder, komisyon YOK — meslek mensubuna komisyon TÜRMOB mevzuatına takılır); ancak 2-3 referans vakadan sonra. ÖLÇÜM: kanal başına görüşme→teklif→fatura dönüşümü 90. günde raporlanır; kapasite bekçisi: satışa fiilen 1-1,5 FTE, teslimata 2-3 kişi — 30-40 nitelikli görüşme hedefi bu kapasiteyle taşınamaz, hedef 12-18 görüşmedir.

## 8. Yasal ve Etik Sınırlar

- 3568 SINIRI (yetki): Vergi beyannamesi/bildirge düzenleme, düzeltme ve tasdik SMMM/YMM tekelindedir. ARGUS çıktısı sözleşme ve rapor kapağında 'yazılım destekli hesaplama ve veri analizi hizmeti' olarak tanımlanır; beyan/bildirge/idare nezdinde temsil adımları her zaman müşterinin meslek mensubunda kalır; her raporda 'mali sonuçlar YMM/SMMM teyidine tabidir' şerhi + mevzuat sürüm damgası (ör. 2026.04.01). 'Mutabakat/doğrulama/uyum' kelimeleri tasdik izlenimi vermeyecek şekilde kullanılır
- BAŞARI PRİMİ YASAĞI (kendi kırmızı çizgimiz + mevzuat riski): Tahsilata/bulguya endeksli ücret, 3568 kapsamındaki nispi ücret yasağına dolanma görüntüsü verir, 'yetkisiz ve sonuç-endeksli mali danışmanlık' iddiasına ve bulgu şişirme çıkar çatışmasına açıktır. İlk 12 ay yalnız sabit/kademeli sabit fiyat; prim ancak olumlu YAZILI hukuk görüşü + tavan + yalnız fiilen tahsil edilmiş tutar şartlarıyla, o zaman bile varsayılan teklif olarak asla
- YMM'YE KOMİSYON YASAĞI: Meslek mensubuna iş yönlendirme komisyonu ödemek onu disiplin riskine sokar ve kanal hukuken sakat doğar; işbirliği modeli ters akışlıdır (YMM, ARGUS'u araç/alt yüklenici olarak ücretlendirir) ve TÜRMOB uyumu için hukuk görüşü ön şarttır
- KVKK (varoluşsal risk): Bordro verisi kişisel veri; sendika kesintisi/engellilik indirimi izleri ÖZEL NİTELİKLİ olabilir. Tek satır veri alınmadan önce: veri işleyen sıfatıyla DPA, veri minimizasyonu (maskeli TCKN, yalnız teşvik hesabına gerekli alanlar), işverenin çalışan aydınlatmasının bu aktarımı kapsadığının teyidi, yurtiçi barındırma, saklama/imha politikası; demo/anonim veri için belgeli anonimleştirme standardı. 1.705 merkezlik dar pazarda tek sızıntı = şirketin sonu
- PAZARLAMA İDDİASI: '96/96 Bakanlık doğrulaması' ifadesi Bakanlık onayı/akreditasyonu izlenimi verirse yanıltıcı ticari uygulamadır; doğru ifade 'Bakanlığın yayımladığı Nisan 2026 verisiyle iç doğrulama'. Bu iddia, test_anchor.py senkronu yapılıp yeşil koşum çıktısı alınmadan hiçbir materyale girmez
- SORUMLULUK YÖNETİMİ: Sözleşmede sorumluluk tavanı (ör. yıllık hizmet bedeliyle sınırlı), 'nihai karar meslek mensubu ve mükellefindir' kaydı; mesleki sorumluluk sigortası araştırılıp mümkünse yaptırılır; hatalı hesap sonucu müşteri zararı senaryosu için süreç tanımı
- ALEYHE DELİL / FAZLA YARARLANMA PROTOKOLÜ: Yazılı bulgu raporu sonraki denetimde firma aleyhine kullanılabilir ve öğrenilen hatanın düzeltilmemesi kasıt doğurabilir — müşteri sözleşme ÖNCESİ yazılı bilgilendirilir; fazla yararlanma bulgusu çıkarsa izlenecek adımlar (kim, ne zaman, nasıl düzeltir/bildirir), raporun mülkiyeti, gizliliği ve saklama süresi sözleşmede önden tanımlanır; ARGUS 'bildirilmeyen usulsüzlüğün bilen tanığı' konumuna düşürülmez
- SGK 6 AY PENCERESİ (5510 Ek m.17): Geriye dönük teşvik taleplerine uygulanması SGK pratiğinde tartışmalıdır; yazılı YMM/hukuk görüşü gelmeden satış argümanı ve rapor taahhüdü yapılmaz — o zamana dek aciliyet tartışmasız çıpalara (2 yılda bir denetim takvimi, VUK zamanaşımının yıl sonu kapanışı) bağlanır; %40 GV dilim eşiği farkı (kod 5,3 M / kaynaklar 5,0 M) da YMM teyidine gider

## 9. Kırmızı Çizgiler (Hızlı Para Uğruna Yapılmayacaklar)

- Başarı primi / gain-share satmak veya sözlü pazarlıkta telaffuz etmek — yazılı hukuk görüşü olmadan asla; görüş olumluysa bile ilk 12 ay sabit fiyat
- Yeşil test koşumu alınmadan ve 'iç doğrulama' ifadesine çevrilmeden '96/96 Bakanlık doğrulaması' iddiasıyla satışa çıkmak (tek müşteri due-diligence'ı güveni bitirir — test_anchor.py düzeltmesi ilk satıştan önce)
- DPA'sız, maskesiz, minimize edilmemiş bordro verisi almak; anonimleştirme standardı belgelenmemiş 'demo' veri kullanmak
- Korku pazarlaması: '3 ay durdurma / belge iptali' senaryolarıyla FUD satışı; 'X TL bulacağız' garantisi; tek yönlü bulgu vaadi (hatalar iki yönlüdür — fazla yararlanma da çıkabilir ve öyle raporlanır)
- Müşterinin mevcut YMM'sini baypas etmek veya yanlışlamak; iç ekibi (mali işler/İK) suçlayan rapor dili — şampiyonu mahcup eden satış kendini öldürür
- Fiyat tabanını çökertmek: pilotu <400-500 bin TL'ye satmak, %100 mahsup vermek, girişte kalıcı 'ömür boyu' indirimler; ilk pazarlıkta gün×günlük maliyet savunmasına düşmek (fiyat daima değere çıpalanır)
- Teknopark 25 AA taahhüdündeki personeli hizmet teslimatına kaydırmak (hibe denetiminde personel çakışması + 8,7 M TL proje riski); hizmet tarafı 3-4 kişi tavanını aşmak
- Nakit planını iki sinyalli firmaya (özellikle Kale'nin satın alma hızına) rehin etmek; tek müşteriye özel geliştirme taahhütleri vermek
- Kapsam kaymasını sineye çekmek: 40 AG kapılarını aşan işi değişiklik talebi olmadan yürütmek (ilk pilot hariç — o bilinçli ve bütçelenmiş yatırımdır)
- Teyitsiz hukuki yorumu (SGK 6 ay penceresi) ana satış tetiği yapmak; 'tahsil ederiz' iması taşıyan pazarlama dili

## 10. İlk İki Hafta — Hemen Başlanacak Aksiyonlar

1. test_anchor.py'yi model şemasıyla senkronla ('brut_ucret'→'arge_brut_ucret'; hesap çekirdeği deposundaki tests/test_anchor.py satır 42, 161 — teyit edildi), 96/96 çapa setini yeşile çevir, koşum çıktısını satış dosyasına arşivle (1-2 gün, ilk satıştan önce ŞART)
2. Hukuk paketini başlat: KVKK DPA + NDA + sorumluluk tavanlı sözleşme şablonları; üç yazılı görüş talebi gönder (başarı primi/3568, SGK 6-ay penceresi, YMM işbirliği modeli); mesleki sorumluluk sigortası fiyat araştırması
3. İki ürünü paketle: Denetim Hazırlık Taraması (tek sayfa teklif + compliance/bordro_kontrol çıktısından rapor şablonu) ve 7555 Tavan Hızlı Analizi (2 sayfalık rapor şablonu); fiyat listesi + milestone'lu (%25/35/40) kapsam kapılı pilot sözleşme taslağı
4. Veri alım runbook'u: maskeli TCKN/veri minimizasyonu şablonu, excel_import ile seed veride uçtan uca prova, 'eksiksiz veriden itibaren 5 iş günü' SLA dili, belgeli anonimleştirme standardıyla demo tenant
5. Hedef listesi: mevcut sözleşmeli danışmanlık müşterilerinden 10-15 isimli hesap + sinyalli 2 firma; hesap sahipliği ve denetim takvimi bilgisi; satışa fiilen 1-1,5 FTE ataması
6. Sinyalli 2 firmayla toplantı talebi (gündem: 'denetim hazırlığı + 7555 güncel durumu'; müşterinin YMM'si davetli); Kale'de tedarikçi kaydı/bilgi güvenliği anketi sürecini HEMEN başlat — en uzun kalem bu
7. Mevcut sözleşmeli 3-5 müşteriye tarama/flaş teklifi çıkar — ilk fatura hedefi hafta 3-6, yalnız bu kanaldan
8. Kapasite ve ölçüm altyapısı: hizmet tarafı 3-4 kişi tavanı + Teknopark 25 AA personel ayrımı yazılı; görüşme→teklif→fatura dönüşüm panosu (90. gün kalibrasyonunun veri kaynağı)

---

*İlgili dosyalar: `argus-baz-hatti-tasarimi.md` (pilot süreci ve BAZ Hattı), `argus-teknopark-basvuru-formu.md` (proje planı), `arge-proje-fikirleri.md` (market-fit analizleri).*
---

## 11. Masaüstü Pivot Uyarlaması (CPU-yalnız / kapalı devre kararı sonrası)

Ürünün kapalı devre kişisel bilgisayarda CPU-yalnız çalışan masaüstü uygulamaya dönüşmesi, bu plandaki hizmet merdivenini DEĞİŞTİRMEZ (basamak 1-3 hizmet ürünleri aynen geçerli) — değiştirdiği şey tekrarlayan gelirin teslim biçimi ve pazarın genişliğidir:

- **Abonelik SKU'ları lisansa dönüşür:** "Gölge Hesap aboneliği" artık **ARGUS Masaüstü yıllık lisansı + imzalı offline mevzuat güncelleme aboneliği** olarak teslim edilir (sunucu/bulut maliyeti yok → marj yükselir; kapalı devre müşteride bile abonelik gerekçesi nettir: mevzuat paketi güncel kalmazsa ürün eskir). Fiyat çıpaları korunur: ≤75 kişi 30-40 bin / 76-200 kişi 50-70 bin / 200+ 90-150 bin TL/ay bandı; Pro ve Kurum sürümleri kademeli üstüne gelir.
- **Satış sürtünmesi düşer:** "Her bilgisayarda çalışır, bir saatte ilk rapor" — BT projesi onayı, bulut izni ve sunucu tedariki satın alma zincirinden çıkar; tek imza eşiğinin altındaki masaüstü lisansla giriş kolaylaşır, hizmet ürünleri (tarama/pilot) üstüne satılır.
- **Yeni segment — SMMM/YMM araç lisansı öne çekilebilir:** Sunucu gerektirmeyen biçim, ay 6+ olarak planlanan YMM kanalını teknik olarak erkene alabilir; hukuk görüşü ön koşulu değişmez. Çok müvekkilli masaüstü lisans (20-40 bin TL/ay/ofis çıpası) doğrudan bu biçimle test edilir.
- **Savunma kapalı ağ segmenti premium pakete eklenir:** On-prem sunucu yerine "kapalı ağ masaüstü dağıtım + toplu offline güncelleme" paketi — kurulum kalemi düşer, lisans çarpanı (×1,5-2) korunur.
- **Huni ürünü opsiyonu (kırmızı çizgilere tabi):** Sınırlı "7555 tavan hızlı kontrol" masaüstü demosu (tek dönem, örnek veriyle) satış görüşmesinde canlı gösterim aracı olarak kullanılabilir; ücretsiz sürüm dağıtımı ancak KVKK/DPA çerçevesi ve destek yükü değerlendirilerek ayrıca kararlaştırılır — bu planda gelir kalemi değildir.
