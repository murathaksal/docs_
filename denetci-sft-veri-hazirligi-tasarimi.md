# Denetçi Modeli: Veri Hazırlığı ve SFT Tasarımı

*EK-6 "veri nereden gelir, etiketi kim koyar" sorusunu cevaplar ve forma esas özettir. Bu belge onun mühendislik karşılığıdır: kayıt şeması, örnek bütçesi ve çeşitlilik aritmetiği, bölme ve sızıntı protokolü, istatistiksel güç, veri ölçekleme merdiveni, LoRA tarifi ve etiketleme eforu. Model seçimi EK-7'dedir; bu belge o seçimi veri tarafından besler.*

*Belgenin en önemli iki bulgusu §4 ve §5'tedir ve forma yansıtılması gereken değişiklik önerileri doğurur (§13).*

---

## 1. Bu belge EK-6'nın üstüne ne ekliyor

| EK-6'da var | Burada eklenen |
|---|---|
| Etiketin motordan geldiği ilkesi | Kayıt şeması, istem/tamamlama ayrımı, kayıp maskeleme (§2) |
| G1-G4 görev tanımları | Her görevin token bütçesi, örnek sayısı ve ağırlığı (§2, §3) |
| Kaynak A-D ve hedef hacimler | **Çeşitlilik aritmetiği:** 2.500 örnek 60 senaryodan türetilirse etkin örneklem 60'tır (§3) |
| "Bölme kuruluş ve dönem bazındadır" | **Üç seviyeli sızıntı anahtarı;** senaryo düzeyinde bölme; 60 senaryonun kör teste 9 senaryo bıraktığı bulgusu (§4) |
| Kazanım 1'deki eşikler | **Her eşiğin kaç örnekle kanıtlanabileceği** (§5) |
| "Hangi eşikten sonra ek veri kazanç getirmez" sorusu (AS-1b) | Sorunun cevabını üretecek **veri ölçekleme merdiveni** ve kaynak ablasyonu (§6) |
| "İnce ayar olgun bir araçtır" | Somut LoRA tarifi, iki kademe, eğitim bütçesi (§7) |
| "Eleme kayıtları eğitime döner" | İkinci turun yöntemi: düzeltilmiş SFT mi, tercih öğrenmesi mi (§8) |

## 2. Veri birimi ve kayıt şeması

### 2.1 Tek kayıt biçimi

Her eğitim örneği tek bir JSON satırıdır ve **dört bloktan** oluşur. Bu ayrım, kayıp maskelemenin (loss masking) ön şartıdır: model yalnızca `completion` bloğundan öğrenir, `system` ve `user` bloklarından öğrenmez.

```jsonc
{
  "id": "A-S017-p03-G2-0142",      // kaynak-senaryo-parametre-görev-sıra
  "split_key": {                    // §4'teki sızıntı anahtarı; bölme BUNUNLA yapılır
    "fault_type": "S017",           // kök neden/senaryo tipi
    "org": "SYN-014",               // kuruluş (sentetikte sanal kuruluş)
    "period": "2024-03"             // dönem
  },
  "task": "G2",
  "system": "...",                  // sabit; önek önbelleğine giren blok
  "user": {                         // motor çıktısı, şemalı
    "fark_imzasi": { "kalem": "gv_stopaj_terkin", "yon": "eksik", "tutar_bandi": "10k-50k" },
    "kural_surumu": "5746/2024-03#r7",
    "ihlal_edilen_kurallar": ["K4", "K9"],
    "belge_envanteri": ["muhtasar", "sgk_hizmet_listesi"]
  },
  "completion": { ... },            // ŞEMALI çıktı; kayıp yalnızca burada
  "label_source": "motor_otomatik", // motor_otomatik | insan_kapanis | insa_geregi
  "quality": { "sema_gecerli": true, "dedup_hash": "…", "yakinlik_skoru": 0.31 }
}
```

**Üç kural:**
1. **Tutar yok.** `completion` içinde hiçbir hesaplanmış tutar bulunmaz — yalnızca bant (`10k-50k`), enum kodu, kural kimliği ve kısa Türkçe metin. Bu, modelin "hesap yapmaz" tasarım kuralının veri düzeyindeki karşılığıdır; veri hattında otomatik denetlenir.
2. **Sabit önek.** `system` bloğu ve kural tabanı alıntıları bayt düzeyinde sabittir. Bu yalnızca eğitim hijyeni değil, EK-7 §3'teki **önek önbelleği** kazancının ön şartıdır: eğitimde değişken olan bir önek, çıkarımda önbelleklenemez.
3. **Eğitim biçimi = çıkarım biçimi.** Eğitimdeki sohbet şablonu, ürün çıkarımında kullanılan şablonla **birebir** aynı olmalıdır. Hibrit düşünme destekli modellerde (Qwen3-4B özgün sürüm) düşünmesiz kip, şablona boş bir düşünme bloğu yerleştirir; eğitim verisi bunu içermezse eğitim ve çıkarım biçimi ayrışır ve kazanç kaybolur. **Faz 0'da tokenize edilmiş tek bir örnek elle karşılaştırılarak doğrulanacaktır.**

### 2.2 Görev başına bütçe

| Görev | Girdi ~token | Çıktı ~token | Hedef örnek | Ağırlık | Etiket kaynağı |
|---|---|---|---|---|---|
| **G1** bulgu yorumlama | 1.200-2.500 | 120-250 | ~1.400 | 30% | inşa gereği / insan kapanış |
| **G2** araştırma yönlendirme | 1.400-2.800 | 60-120 | ~1.600 | 35% | **motor otomatik** (belge getirilir, motor koşulur, çözdü/çözmedi) |
| **G3** denetçi sorusu | 1.000-2.000 | 80-180 | ~900 | 20% | YMM oturum notları / senaryo beklenen soruları |
| **G4** belge alan çıkarımı | 800-3.000 | 100-400 | ~700 | 15% | iç-toplam kontrolü / inşa gereği |

G2'nin en büyük paya sahip olması bilinçlidir: **etiketi insan koymaz, motor koyar.** Ölçeklenebilen tek görev budur ve Kazanım 1'in birincil metriği (yönlendirme isabeti ≥%70) ondan gelir.

**Uzunluk kararı:** `max_seq_len = 4096`. Örneklerin ~%95'i buna sığar; sığmayanlarda kural tabanı alıntısı kısaltılır, fark imzası asla kırpılmaz. 8192'ye çıkmak eğitim maliyetini iki katlar ve çıkarımda EK-7 §3'teki bellek/gecikme bütçesini bozar.

## 3. Örnek bütçesi ve çeşitlilik aritmetiği

**EK-6'nın gizli varsayımı:** 60 senaryo × parametrik türetme ≈ 2.000-3.000 örnek. Bu, **senaryo başına 42-50 türetme** demektir.

**Sorun:** Aynı senaryonun tutarı, kişi sayısı ve dönemi değiştirilerek üretilen 42 örnek, birbirinden bağımsız 42 örnek değildir. Çıktı metni büyük ölçüde aynı kalır; model kök nedeni *çıkarmayı* değil, fark imzasından şablonu *eşlemeyi* öğrenir. Bunun adı şablon çöküşüdür (template collapse) ve sentetik veriyle eğitilen küçük modellerin bilinen başarısızlık biçimidir. Laboratuvarda yüksek skor üretir, gerçek pilot verisinde çöker — yani tam olarak AS-1'in ölçtüğü aktarım başarısızlığı.

**Üç karşı önlem:**

1. **Türetme tavanı:** senaryo başına en fazla **12 türetme**. Örnek sayısını korumak için senaryo sayısı artırılır: 2.500 örnek için ~200 senaryo gerekir, ~60 değil.
2. **Çeşitlilik ekseni türetmede değil, kompozisyonda:** türetme yalnızca tutar/dönem/kişi sayısı oynatarak değil; (a) belge envanteri eksikliği, (b) çoklu kök neden birleşimi, (c) rejim (5746/4691) ve rejim sınırı, (d) fark yönü ve büyüklük bandı, (e) "belirsiz" doğru cevabı olan ayırt-edilemez vakalar eksenlerinde yapılır. Bu eksenler **çıktıyı** değiştirir, yalnızca girdiyi değil.
3. **Otomatik yakınlık denetimi:** her yeni örnek, mevcut havuza karşı çıktı metni üzerinde n-gram ve gömü benzerliğiyle ölçülür; **yakınlık skoru > 0,85 olan örnek havuza alınmaz.** Kabul edilen örneklerin skor dağılımı veri kartında raporlanır.

**Yeniden hesaplanmış hacim hedefi:**

| Kaynak | EK-6 hedefi | Bu tasarımın önerisi | Gerekçe |
|---|---|---|---|
| A: senaryo kütüphanesi | ≥60 senaryo → 2.000-3.000 örnek | **≥150 senaryo → ≤1.800 örnek** (tavan 12/senaryo) | Çeşitlilik ve §4'teki kör test bölmesi |
| B: hata enjeksiyonu | ≥400 vaka → 1.500-2.500 örnek | ≥400 vaka, **≥40 farklı hata tipi**, tip başına tavan 15 | Vaka sayısı değil **tip sayısı** çeşitliliği taşır |
| C: pilot kayıtları | pilot başına ≥200 kalem | değişmez; ağırlıklı **test** | Gerçek dağılımın tek kaynağı |
| D: denetçi dili | metin korpusu | G3 için ≥300 atıflı soru örneği | Atıf disiplini ancak örnekle öğrenilir |

Toplam eğitim havuzu ≈ **3.500-4.500 örnek**, etkin çeşitlilik ≈ **150 senaryo + 40 hata tipi + pilot**. Sayı küçülmüş görünür ama bağımsız bilgi miktarı artmıştır.

## 4. Bölme ve sızıntı protokolü

EK-6 "bölme kuruluş ve dönem bazındadır" der. **Bu yeterli değildir.** Sentetik veride kuruluş ve dönem zaten uydurmadır; aynı senaryodan türetilen iki örnek farklı kuruluş ve döneme atanabilir ve bölmenin iki yakasına düşebilir. O zaman kör test, eğitimde görülmüş bir şablonu ölçer.

**Sızıntı anahtarı üç bileşenlidir ve bölme en kaba bileşenden yapılır:**

```
split_key = (fault_type, org, period)
bölme sırası: fault_type → org → period
```

| Seviye | Kural | Neyi engeller |
|---|---|---|
| **L1 — hata tipi / senaryo** | Bir senaryodan türeyen **hiçbir** örnek bölmenin iki yakasında bulunamaz | Şablon ezberinin kör testte ödüllendirilmesi |
| **L2 — kuruluş** | Aynı kuruluşun hiçbir dönemi hem eğitimde hem testte olamaz | Kuruluşa özgü desen ezberi |
| **L3 — dönem** | Aynı kuruluş-dönem çifti tek yakada | Zaman sızıntısı |

**Bölme aritmetiği ve asıl bulgu:**

| Senaryo sayısı | Eğitim | Doğrulama | **Kör test** |
|---|---|---|---|
| 60 (EK-6 hedefi) | 42 | 9 | **9** |
| 150 (öneri) | 105 | 22 | **23** |
| 200 | 140 | 30 | **30** |

**60 senaryoyla kör test setinde 9 senaryo kalır.** Dokuz senaryodan kaç örnek türetilirse türetilsin, istatistiksel olarak bağımsız gözlem sayısı dokuzdur; §5'teki hiçbir eşik bu setle kanıtlanamaz. Kör test seti bu nedenle **Kaynak B (hata tipi düzeyinde ayrılmış) ve Kaynak C (pilot)** üzerine kurulur; Kaynak A yalnızca eğitim ve doğrulamada kullanılır.

**Gizli sızıntı uyarısı:** Kaynak B'nin enjekte edilen hataları, Kaynak A'nın senaryo kütüphanesinden üretiliyorsa iki kaynak bağımsız değildir. Bu durumda `fault_type` her iki kaynakta **ortak anahtar** olarak kullanılmalı, bölme bu ortak anahtar üzerinden yapılmalıdır. Enjeksiyon setinin en az **%30'u**, senaryo kütüphanesinde karşılığı olmayan hata tiplerinden üretilmelidir; aksi hâlde "sentetikten gerçeğe aktarım" ölçümü kendi kendini doğrular.

**Pilot verisinin ayrımı (KVKK ile birlikte):** Her pilot kuruluşun dönemleri önce ikiye ayrılır — kör test dönemleri hiçbir koşulda eğitime girmez, ay 10 ölçümünden sonra bile. Ay 11'deki ikinci tur yalnızca eğitime ayrılmış dönemleri kullanır ve ay 12 ölçümü aynı kör dönemlerle yapılır. Böylece ay 10 ve ay 12 skorları karşılaştırılabilir kalır.

## 5. İstatistiksel güç: hangi eşik kaç örnekle kanıtlanır

Kazanım 1 ve 2 sayısal eşikler taahhüt ediyor. Bir eşiğin "tutturulduğunu" söylemek, ölçülen oranın eşiğin üstünde çıkmasından ibaret değildir; **güven aralığının alt sınırının** eşiğin üstünde olması gerekir. Aşağıdaki sayılar iki terimli oran için hesaplanmıştır.

**a) Oran kesinliği (%95 güven aralığı yarı genişliği):**

| Gerçek oran | n=100 | n=200 | n=400 | n=900 |
|---|---|---|---|---|
| %70 | ±9,0 | ±6,4 | ±4,5 | ±3,0 |
| %80 | ±7,8 | ±5,5 | ±3,9 | ±2,6 |
| %85 | ±7,0 | ±4,9 | ±3,5 | ±2,3 |
| %90 | ±5,9 | ±4,2 | ±2,9 | ±2,0 |

**Okunuşu:** EK-6'daki 200 örneklik kör setle ölçülen %70, aslında **%63,6-%76,4** aralığıdır. "≥%70 hedefi tutturuldu" cümlesi bu setle kurulamaz.

**b) Eşiğin üstünde olduğunu kanıtlamak** (tek yönlü %95 alt sınır > eşik):

| Kör set n | ≥%70 iddiası için gereken gözlenen oran |
|---|---|
| 100 | %78 |
| 200 | %76 |
| 400 | %74 |

**c) Katı eşikler (Kazanım 2):**

| İddia | Gerekli tasarım |
|---|---|
| Atıf doğruluğu **≥%98** | n=150 ve **sıfır hata**; n=300 ile en fazla 2 hata; n=400 ile en fazla 3 hata |
| Desteksiz iddia **≤%1** | n=300 ve sıfır olay (üst sınır %0,89). **Tek bir olay olursa n=300 yetmez** (üst sınır %1,48); n≥400 gerekir |

**d) İyi haber — "ince ayarsız tabana karşı ≥15 puan" ucuzdur.** Bu eşleştirilmiş bir karşılaştırmadır (aynı örnekler, iki model) ve McNemar testiyle ölçülür:

| Uyuşmaz çift oranı | Güç %80 | Güç %90 |
|---|---|---|
| %20 | n≈70 | n≈94 |
| %25 | n≈88 | n≈117 |
| %30 | n≈105 | n≈140 |

**Karar:** Kör test seti **n≥400** olmalıdır; bunun içinde G2 (yönlendirme) kalemleri ≥250, atıf denetimi ≥300 atıf, YMM etiketli G1/G3 örneklemi ≥150 olmalıdır. G2 etiketi motor tarafından üretildiği için 400'e çıkmanın ek insan maliyeti yoktur — **pahalı olan yalnızca YMM etiketli kısımdır ve o bilinçli olarak küçük tutulur.**

## 6. Veri ölçekleme merdiveni (AS-1b'nin cevabı)

AS-1(b) "hangi eşikten sonra ek veri kazanç getirmiyor" sorusunu soruyor. Bu soru ancak **planlı bir merdivenle** cevaplanabilir; eğitim bittikten sonra geriye dönük anlaşılmaz.

**Merdiven:** aynı model, aynı hiperparametre, aynı kör test; yalnızca eğitim havuzu büyür.

| Basamak | Örnek | Not |
|---|---|---|
| E0 | 0 | ince ayarsız taban — **önce ölçülür ve kilitlenir** |
| E1 | 250 | |
| E2 | 500 | |
| E3 | 1.000 | |
| E4 | 2.000 | |
| E5 | 3.500-4.500 | tam havuz |

Her basamak alt küme değil **iç içe** küme olmalıdır (E1 ⊂ E2 ⊂ … ), ve her basamak senaryo düzeyinde katmanlı örneklenmelidir — 250 örnek tek bir senaryo ailesinden gelirse eğri anlamsızdır. Her basamak **iki farklı tohum** (seed) ile eğitilir; aradaki fark, eğrideki gürültü tabanını verir. Bu olmadan "3.000'den sonra kazanç durdu" cümlesi kurulamaz, çünkü fark tohum gürültüsü olabilir.

**Kaynak ablasyonu (aynı düzenekte, tam havuz büyüklüğünde sabit):** A-yalnız, B-yalnız, A+B, A+B+C. Bu dört koşu, Kazanım 1'deki "veri kaynağına göre başarım" taahhüdünün ve EK-6'daki "hangi kaynak eksik" teşhisinin doğrudan karşılığıdır. Sentetikten gerçeğe aktarım, A+B ile A+B+C arasındaki farktır.

**Toplam eğitim koşusu:** 6 basamak × 2 tohum + 4 ablasyon ≈ **16 koşu**, ayrıca iki model boyutu için (1,7B ve 4B) → ~32 koşu. §7'deki bütçeyle bu tamamen karşılanabilir.

## 7. SFT tarifi

### 7.1 Neden LoRA, neden tam ince ayar değil

Üç gerekçe: (1) tam ince ayar 4B modelde kiralık GPU maliyetini ve saklama yükünü büyütür; (2) LoRA'nın **daha az unuttuğu** literatürde gösterilmiştir ve bu projede kritiktir — modelin Türkçe genel dil yeteneği korunmalıdır, yalnızca denetçi davranışı eklenmelidir; (3) LoRA adaptörü ayrı bir dosyadır, **bizim telif hakkımızdadır** ve kapalı tutulabilir; taban model Apache-2.0 olarak ayrı taşınır (EK-7 §6).

### 7.2 Başlangıç hiperparametreleri (Faz 3'te taranacak)

| Parametre | Başlangıç | Not |
|---|---|---|
| `r` (rank) | 32 | 16-64 aralığı taranır; dar görevde 16 çoğu zaman yeter |
| `lora_alpha` | 64 | α = 2r kuralı |
| `lora_dropout` | 0,05-0,1 | küçük veri havuzunda aşırı uyuma karşı |
| Hedef modüller | `q,k,v,o,gate,up,down_proj` | tüm doğrusal katmanlar; yalnız dikkat katmanları dar görevde yetersiz kalır |
| Öğrenme oranı | 1e-4 (LoRA) | rank yükselirse düşürülür; kosinüs çizelge, %3 ısınma |
| Epoch | 2-3 | 3.500-4.500 örnekte 3'ten sonra ezber başlar; erken durdurma doğrulama kaybına bağlanır |
| Etkin yığın | 16-32 örnek | gradyan biriktirmeyle |
| `max_seq_len` | 4096 | §2.2 |
| Kayıp maskeleme | **yalnız `completion`** | istem üzerinde kayıp hesaplanmaz; bu ayar unutulursa model istemi ezberler |
| Paketleme (packing) | açık, **örnek sınırı korunarak** | çapraz-örnek dikkat sızıntısı engellenmeli |

**Değişmez işlem sırası:** LoRA eğit → merge (bf16) → Türkçe imatrix üret → nicemle → GGUF. Asla önce nicemleyip sonra ince ayar yapılmaz (EK-7 §5).

### 7.3 İki kademe tek hattan

EK-7'deki iki kademe (4B kalite / 1,7B etkileşim) **aynı veri havuzu ve aynı tarifle** eğitilir; yalnızca rank (küçük modelde 16) ve epoch sayısı (küçük modelde 3-4) ayarlanır. Böylece iki kademe arasındaki fark modele atfedilebilir, veriye değil.

### 7.4 Eğitim bütçesi

4.500 örnek × ~2.400 token ≈ **11 M token/epoch**. Kiralık GPU'da 3 epoch ≈ **1,5-4 GPU-saat**, yani koşu başına birkaç dolar. 32 koşuluk tam merdiven ve ablasyon programı bile **~50-130 GPU-saat**, kabaca **100-250 USD** bandındadır.

**Bunun anlamı nettir: GPU bütçe kalemi değildir.** Bütçe kalemi §12'deki etiketleme eforudur. Ar-Ge dosyasında maliyet gerekçesi buna göre kurulmalıdır.

## 8. İkinci tur: eleme kayıtlarından öğrenme

EK-6 ve Kazanım 2, sembolik kapıdan elenen bulguların "olumsuz örnek olarak eğitime döndüğünü" söylüyor. Yöntem belirtilmemiş; iki seçenek vardır ve bu proje için tercih nettir.

| Yöntem | Ne yapar | Bu proje için |
|---|---|---|
| **Düzeltilmiş SFT** | Elenen çıktının **düzeltilmiş hâli** eğitime eklenir | **Birincil.** Basit, tekrarlanabilir, kapalı devre hatta oturur. Düzeltme çoğu vakada otomatiktir: kapı "bu kural kimliği yok" der, doğru kimlik kural tabanından bulunur |
| **Tercih öğrenmesi (DPO/KTO)** | (elenen, kabul edilen) çiftiyle tercih eğitimi | **İkincil.** Elenen örnek sayısı birkaç yüzü aştığında ve düzeltilmiş SFT platoya ulaştığında denenir; ek hiperparametre ve ek koşu maliyeti getirir |

**Ölçülecek olan:** Kazanım 2 "eleme oranının turlar boyunca düştüğü" taahhüdünü içeriyor. Bu, tur bazında **aynı kör setle** ölçülür ve raporlanır: tur 1 eleme oranı → tur 2 eleme oranı. Düşüş yoksa bu olumsuz sonuç olarak raporlanır; AS-2'nin düşebilir ölçütü budur.

**Tuzak:** Eleme kayıtları kör test setinden gelemez. Kapı, kör test üzerinde de çalışır ama oradaki elemeler eğitime **asla** dönmez — döndüğü anda kör test kirlenir ve sonraki ölçümler geçersiz olur.

## 9. Şema-zorlamalı çözümleme ile eğitim uyumu

Ürün, çıktıyı dilbilgisi kısıtlı çözümlemeyle (GBNF) şemaya zorluyor. Bunun veri tarafında iki sonucu var:

1. **Eğitim verisi, gramerin ürettiği biçimle birebir aynı olmalıdır** — aynı alan sırası, aynı ayraçlar, aynı enum yazımı. Eğitimde `{"kok_neden": ...}` görüp çıkarımda gramerle farklı sıra dayatmak, modelin öğrendiği dağılımı bozar.
2. **Şema geçerliliği tek başına metrik değildir.** Gramer altında şema geçerliliği zaten ~%100 çıkar. Bu yüzden veri kartında ve ölçümde **"şema-geçerli ama yanlış"** oranı ayrı raporlanır (EK-7 §5'teki zorunlu KPI). Bir denetim ürününde en tehlikeli hata biçimi budur: otomatik doğrulayıcıdan geçmiş görünür.

Eğitim havuzunda bilinçli olarak **"kanıt yetersiz / belirsiz" doğru cevabı olan örnekler** bulunur (hedef: havuzun **%12-15'i**). Bu oran boş bir tercih değil, Kazanım 3'teki "belirsiz tutar payı ≤%5" taahhüdünün dengesidir: model belirsizi hiç öğrenmezse her farkı bir nedene zorlar; fazla öğrenirse her şeye "belirsiz" der. Oran, doğrulama setinde iki yönlü olarak izlenir.

## 10. Kalite kapıları ve veri kartı

Her eğitim koşusundan önce havuz şu kapılardan geçer; biri bile düşerse koşu başlatılmaz:

| Kapı | Ölçüt |
|---|---|
| **V1 — şema** | Örneklerin %100'ü çıktı şemasına uyar; uymayan eğitime alınmaz |
| **V2 — tutar yasağı** | Hiçbir `completion` içinde hesaplanmış tutar yok (otomatik desen denetimi) |
| **V3 — yakınlık** | Yakınlık skoru > 0,85 olan örnek yok; skor dağılımı raporlanır |
| **V4 — sızıntı** | `split_key` üçlüsü bölmenin iki yakasında kesişmiyor (otomatik küme kesişim testi) |
| **V5 — denge** | Kök neden sınıfları ve "belirsiz" sınıfı hedef dağılımda; hiçbir sınıf %25'i aşmıyor, hiçbiri %2'nin altında değil |
| **V6 — atıf geçerliliği** | Eğitim verisindeki **her** kural kimliği ve mevzuat atfı, kural tabanında gerçekten var (eğitim verisi kendi kapısından geçer) |
| **V7 — anonimlik** | Kişisel veri deseni taraması temiz (§11) |

**Veri kartı** her koşuyla birlikte sürümlenir ve arşivlenir: kaynak dağılımı, görev dağılımı, senaryo/hata tipi sayısı, türetme histogramı, yakınlık skor dağılımı, sınıf dengesi, bölme anahtarları, V1-V7 sonuçları, havuz SHA-256'sı. **Ar-Ge iddiasının tekrarlanabilirliği bu karta dayanır**; hakem "bu skor hangi veriyle üretildi" diye sorduğunda cevap tek bir karttır.

## 11. KVKK ve veri yönetişimi

| Konu | Karar |
|---|---|
| Özel nitelikli veri | Bordro; sendika aidatı, engellilik ve sağlık indirimi kalemleri içerir → **KVKK md. 6** kapsamındadır. "Anonimleştirildi" demek yetmez; yöntem ve yeniden kimliklendirme riski analizi dosyaya eklenir |
| Anonimleştirme sırası | **Müşteri tesisinde, eğitim hattına girmeden önce.** Kimlik alanları müşteride kalan anahtarla tokenize edilir; anahtar hiçbir koşulda dışarı çıkmaz |
| Ücret alanları | Eğitim verisinde ham tutar yok, **bant** var (§2.1). Bu hem KVKK hem "model hesap yapmaz" kuralının ortak sonucudur |
| Küçük hücre riski | Tek kişilik Ar-Ge merkezlerinde bant + dönem + kuruluş birleşimi yeniden kimliklendirilebilir; bu tür kayıtlar **kuruluş düzeyinde birleştirilerek** veya çıkarılarak işlenir |
| Bulut GPU | Yalnız sentetik ve anonimleştirilmiş veri. Dosyaya yazılacak ayrım: **"eğitim: kiralık GPU, sentetik/anonim veri — çıkarım: müşteride CPU, kapalı devre"** |
| Kör test verisi | Pilot kör dönemleri hiçbir koşulda buluta çıkmaz; kör ölçüm yerel referans makinede yapılır |

## 12. Efor ve takvim

**Asıl maliyet kalemi budur** (§7.4: GPU değil).

| İş | Birim | Efor |
|---|---|---|
| Senaryo kütüphanesi ≥150 senaryo (mevzuat referanslı yazım) | ~1,5 saat/senaryo | **~28 gün** (mevzuat uzmanı + geliştirici) |
| Hata enjeksiyon hattı ve ≥40 tip | geliştirme | ~15 gün |
| G2 etiketleme | **otomatik** (motor) | ~0 insan eforu |
| YMM etiketli altın set (G1/G3, ~400 kalem) | ~15 dk/kalem | **~100 saat ≈ 12,5 YMM-günü** |
| Kör test seti onayı ve mühürlenmesi | — | ~5 gün |
| Merdiven + ablasyon koşuları ve raporlama | 32 koşu | ~10 gün (çoğu otomatik) |

Bu, İP4'ün (9 adam-ay, ay 4-10) senaryo/enjeksiyon kalemleriyle ve İP5'in (10 adam-ay, ay 6-12) eğitim kalemleriyle örtüşür. **Takvim kritik yolu senaryo kütüphanesidir**, model eğitimi değil: İP5'in ilk ince ayarı ay 8-9'da yapılacaksa ≥150 senaryo **ay 7 sonunda** hazır olmalıdır.

## 13. Riskler ve forma yansıması gereken değişiklikler

| # | Risk | Önlem | Forma etkisi |
|---|---|---|---|
| R1 | **Şablon çöküşü** — 60 senaryodan 2.500 örnek türetilir, laboratuvarda yüksek skor, pilotta çöküş | Türetme tavanı 12, senaryo sayısı ≥150, yakınlık denetimi (§3) | **İP4 çıkış kriteri "≥60 senaryo" → "≥150 senaryo"** olarak güncellenmeli |
| R2 | **Kör test setinin istatistiksel olarak yetersiz olması** — n=200 ile ≥%70 iddiası kurulamaz | Kör set n≥400; G2 kalemleri ≥250; atıf denetimi ≥300 atıf (§5) | Kazanım 1'deki test seti tanımına **asgari örneklem sayısı** eklenmeli |
| R3 | **Kaynak A ile B arasında gizli sızıntı** — enjeksiyon hataları senaryo kütüphanesinden üretilirse aktarım ölçümü kendini doğrular | Ortak `fault_type` anahtarı; enjeksiyonun ≥%30'u kütüphane dışı tipten (§4) | EK-6 §4'e sızıntı anahtarı tanımı eklenmeli |
| R4 | **Oracle yanlılığı** — model motorun kendine has davranışlarını öğrenir, denetçi mantığını değil | G3 etiketleri motordan değil YMM oturumlarından gelir; pilot kör seti nihai hakem | Değişiklik gerekmez; EK-6 zaten bu ayrımı kuruyor |
| R5 | **Eğitim/çıkarım biçim ayrışması** — sohbet şablonu, düşünme bloğu veya gramer sırası farkı kazancı siler | Faz 0'da tokenize edilmiş örnek karşılaştırması; eğitim = çıkarım biçimi kuralı (§2.1, §9) | Değişiklik gerekmez |
| R6 | **Türkçe genel yeteneğin unutulması** — dar SFT sonrası model akıcılığını kaybeder | LoRA (tam ince ayar değil); doğrulama setinde alan-dışı Türkçe kontrol örnekleri | Değişiklik gerekmez |
| R7 | **"Belirsiz" sınıfının dengesizliği** — ya hiç öğrenilmez ya her şeye denir | Havuzda %12-15 hedef oran, iki yönlü izleme (§9) | Değişiklik gerekmez |
| R8 | **Kör testin kirlenmesi** — kapı elemelerinin kör setten eğitime dönmesi | Eleme kayıtları yalnız eğitim/doğrulama bölmesinden (§8) | Değişiklik gerekmez |

---

*Bu belge İP4 ve İP5'in veri tarafındaki uygulama tasarımıdır. §13'teki R1-R3 maddeleri, Proje Bilgi Formu'nda değişiklik önerisi doğurur ve başvuru revizyonundan önce karara bağlanmalıdır.*
