# EK-7: Denetçi Rolündeki Dar Kapsamlı Modelin Seçimi

*Proje Bilgi Formu'ndaki AS-1 araştırma sorusunun, Hedeflenen Kazanım 1'in ve İP5 iş paketinin dayanağıdır. "1-4 milyar parametre sınıfında bir model" taahhüdünün hangi somut modellerle karşılanacağını, hangi adayların neden elendiğini ve kararın hangi ölçümle kesinleşeceğini gösterir. Formun risk maddesi (8) uyarınca nihai seçim referans bilgisayarda ölçülerek yapılacaktır; bu ek, ölçüme girecek aday kümesini ve varsayılan başlangıç noktasını belirler.*

*Lisans doğrulama tarihi: 17.09.2026. Aşağıdaki birincil ve yedek adayların lisans metinleri bu tarihte depo içindeki `LICENSE` dosyasından birebir okunmuştur.*

---

## 1. Seçimi belirleyen dört zorunlu ölçüt

Aday kümesi, projenin kendi taahhütlerinden çıkan dört zorunlu ölçütle daraltılmıştır. Bir ölçütü sağlamayan model, diğerleri ne kadar iyi olursa olsun ürün modeli olamaz.

| # | Ölçüt | Kaynağı | Eleme eşiği |
|---|---|---|---|
| **Ö1** | **Türev ağırlığın ticari yeniden dağıtımı serbest olmalı** | Ürün, müşteri tesisine kurulan kapalı devre masaüstü uygulamadır; ince ayarlı ağırlık müşteriye **dağıtılır** | Apache-2.0 / MIT. Koşullu lisanslar (araştırma-amaçlı, kullanıcı arayüzüne marka koyma zorunluluğu, kullanım kısıtlarını müşteri sözleşmesine geçirme yükümlülüğü) elenir |
| **Ö2** | **Kendi ince ayarlı ağırlığımız GGUF'a çevrilebilmeli** | İş akışı: LoRA eğit → merge → nicemle → dağıt. Hazır GGUF indirmek yetmez | `convert_hf_to_gguf.py` mimariyi desteklemeli |
| **Ö3** | **Türkçe mali-hukuki metinde çalışabilmeli** | 5746/4691 mevzuatı, bordro, Muhtasar ve Prim Hizmet Beyannamesi | Resmî dil kapsamında Türkçe bulunmalı veya ölçülmüş Türkçe başarımı olmalı |
| **Ö4** | **1-4 milyar parametre sınıfı, GPU'suz 16 GB makinede çalışmalı** | Kazanım 1, AS-1 ve İP5'te üç yerde aynı taahhüt | Toplam parametre ≤ 4 milyar; Q4 dosyası ≲ 3 GB |

**Lisans belirleme kuralı (dosyaya sabit kural olarak yazılır):** *Lisans, model kartı etiketinden değil, eğitim zincirindeki en kısıtlayıcı taban modelin birincil `LICENSE` metninden belirlenir.* Bu kural boş bir tedbir değildir: tarama sırasında en az üç modelde ikincil kaynakların lisansı yanlış bildirdiği görülmüştür (aşağıda §4).

## 2. Karar: iki kademeli tek aile

Tek bir model yerine, **aynı aileden iki boyut** seçilmiştir. Gerekçe §3'teki hız aritmetiğidir: 4 milyar sınıfı bir model, 4 çekirdekli bir bilgisayarda "bulgu başına ≤30 saniye" hedefini etkileşimli kullanımda güvenle tutamaz; 1-2 milyar sınıfı tutar ama yorumlama kalitesi düşer. İki boyut aynı aileden seçildiği için **tokenizer, istem biçimi, SFT verisi, GBNF grameri ve dönüşüm hattı ortaktır**; tek bir eğitim hattı iki ürün kademesi üretir ve ek Ar-Ge maliyeti doğurmaz.

| Rol | Model | Parametre | Lisans (17.09.2026'da doğrulandı) | Ürün içindeki işlevi |
|---|---|---|---|---|
| **Birincil — kalite kademesi** | `Qwen/Qwen3-4B-Instruct-2507` | 4,0 B | **Apache-2.0** (`LICENSE` dosyası okundu: "Apache License, Version 2.0") | Arka planda toplu çalışan tam bulgu üretimi; kör karşılaştırmada ölçülen asıl model |
| **Birincil — etkileşim kademesi** | `Qwen/Qwen3-1.7B` | 1,7 B | **Apache-2.0** (model kartı; aynı depo ailesi) | Kullanıcı ekranda beklerken çalışan, ≤30 sn bütçesini rahat tutan kademe |
| **Yedek 1 (lisans + Türkçe)** | `microsoft/Phi-4-mini-instruct` | 3,8 B | **MIT** (`LICENSE` dosyası okundu) | Birincil ailede Türkçe yetersiz kalırsa geçilecek model; aynı zamanda Taban B |
| **Yedek 2 (hız)** | `Qwen/Qwen3-4B` (özgün, hibrit düşünme) | 4,0 B | Apache-2.0 | Resmî GGUF deposu ve doğrulanmış dosya boyutu olan sürüm; `enable_thinking=False` ile kullanılır |
| **Karşılaştırma tabanı (Türkçe-yerli)** | `vngrs-ai/Kumru-2B` | 2,4 B | Apache-2.0 *(kart etiketi; depoda ayrı `LICENSE` dosyası yok — yazılı teyit alınacak)* | Türkçe-yerli tokenizer'ın hız kazancını ölçen kontrol kolu |

**Birincil seçimin gerekçesi.** Qwen3-4B-Instruct-2507, dört ölçütü birlikte sağlayan adaydır: (Ö1) koşulsuz Apache-2.0 — isimlendirme zorunluluğu, kullanım politikası eki, gelir/kullanıcı eşiği veya müşteri sözleşmesine hüküm geçirme yükümlülüğü yoktur; (Ö2) standart yoğun Qwen3 mimarisi `convert_hf_to_gguf.py` tarafından uzun süredir desteklenir, yani **kendi** ince ayarlı ağırlığımızı çevirebiliriz; (Ö3) Qwen3 teknik raporunda (arXiv:2505.09388) Türkçe, INCLUDE ve MT-AIME2024 dil listelerinde ve Belebele `tur_Latn` kırılımında yer alır; (Ö4) 4 milyar sınırına oturur, Q4_K_M dosyası ~2,5 GB'dir. Ayrıca **düşünme modu zorunlu değildir** — 30 saniyelik bütçenin en büyük düşmanı zorunlu düşünme çıktısıdır.

**Dürüstlük kaydı (dosyaya bu haliyle yazılmalıdır):** Adayların hiçbirinin Türkçe'ye özgü, tekil, resmî bir başarım skoru yoktur. Birincil adayın Türkçe kanıtı çok dilli agregat düzeyindedir (INCLUDE 44 dil ortalaması; Türkçe alt kırılımı yayımlanmamıştır). Türkçe yeterlilik, §5'teki kendi değerlendirme setimizle kanıtlanacaktır. Seçim, mutlak Türkçe üstünlük iddiasına değil, **"lisansı koşulsuz + dönüşüm zinciri çalışan + düşünmesiz çok dilli kalitesi sınıfının en iyisi"** üçgenine dayanmaktadır.

## 3. Hız gerçekliği: "bulgu başına ≤30 saniye" nerede tutar, nerede tutmaz

Bu bölüm, hakem heyetinin en kolay sorgulayacağı taahhüdü açıkça ele alır.

**Ölçülmüş çapa noktaları (yayımlanmış, gerçek):** 4 vCPU / 16 GiB sınıfı bir sunucuda Qwen2.5-3B Q4_K_M ≈ **8,4 tok/s**; 6 çekirdek Zen3 + DDR4'te Qwen3-4B Q4_K_M ≈ **15 tok/s**; dört çekirdekli ARM tek kart bilgisayarda aynı model ≈ **1,3 tok/s** (bu nedenle ARM tek kart bilgisayar referans donanım olarak **kabul edilmez**).

**Aritmetik.** 4 milyar sınıfı model, 4 çekirdekli referans makinede ~5-9 tok/s bandındadır. 250 tokenlik bir bulgu çıktısı **28-50 saniye** eder; buna ön-doldurma (prefill) süresi de eklenir. Yani hedef, 4 milyarlık modelde **etkileşimli kullanımda tutmaz**. 1,7 milyarlık model ~12-20 tok/s bandındadır ve aynı çıktı **13-21 saniyede** biter.

**Bunun ürün kararına yansıması — beş kaldıraç, bu sırayla:**
1. **İki kademeli paketleme (asıl çözüm):** kullanıcı ekranda beklerken 1,7 B kademesi çalışır; 4 B kademesi, formun risk maddesi (8)'te zaten öngörülen **arka plan toplu işlemi** olarak koşar. Böylece ≤30 sn taahhüdü etkileşimli akışta korunur, kalite arka planda kazanılır.
2. **Çıktıyı kısaltmak (tek en büyük kazanç):** tutarları deterministik motor üretir; model yalnızca kısa Türkçe metin + enum kodları yazar. 450 → 200 token, 4 B'de ~25 saniye kazandırır.
3. **Önek önbelleği (`cache_prompt`):** sabit sistem istemi + kural metni + mevzuat alıntıları önek olarak sabitlenir; bulgu başına yalnızca 400-800 tokenlik fark işlenir.
4. **Düşünme modunu kapatmak:** `enable_thinking=False` sabitlenir.
5. **Nicemleme/iş parçacığı ayarı:** Q4_K_M birincil, Q5_K_M yedek; masaüstü üründe `-t 3` + düşük öncelik önerilir (4 çekirdekte `-t 4` arayüzü dondurur, kazancı ~%5'tir).

**Ölçülmemiş olanı ölçülmüş gibi yazmama kuralı:** yukarıdaki tok/s değerleri, ölçülmüş çapa noktalarından türetilmiş **tahminlerdir**. 4 çekirdek + 16 GB referans makinede hiçbir aday için yayımlanmış birebir `llama-bench` tablosu yoktur. Ar-Ge dosyasına yazılacak nihai sayılar §5 Faz 1'de kendi referans makinemizde üretilecektir.

**Faz 0'da netleştirilecek iki tanım:** (a) "30 saniye" ön-doldurma dâhil mi hariç mi? (b) "300-600 çıktı" **token** mı **kelime** mi? Türkçe'de token/kelime oranı ~2,2-2,8'dir; kelime kastediliyorsa 750-1500 token demektir ve **sınıftaki hiçbir model hedefi tutmaz**. Bu iki tanım, model seçiminden önce kesinleşmelidir.

## 4. Elenen adaylar ve gerekçeleri

Aşağıdaki liste, "neden bu model değil" sorusunun cevabıdır ve seçimin keyfî olmadığını gösterir.

### 4.1 Lisans nedeniyle elenenler
| Model | Eleme gerekçesi |
|---|---|
| `Qwen/Qwen2.5-3B(-Instruct)` | **Qwen Research License** — hak verilişi birebir "for non-commercial purposes only". Ticari yeniden dağıtım yasak. *(Aynı ailenin 1.5B ve 7B'si Apache-2.0'dır; bu, "aile Apache-2.0" genellemesinin neden yapılamayacağının örneğidir.)* |
| `meta-llama/Llama-3.2-3B/1B-Instruct` | Llama Community License: türev ürünün **kullanıcı arayüzünde** "Built with Llama" ibaresi zorunlu; kabul edilebilir kullanım politikası müşteri sözleşmesine geçer. Kapalı devre kurum yazılımında taşınması istenmeyen yük. |
| `google/gemma-3-4b-it` ve `gemma-3-1b-it` | Gemma Terms of Use: kullanım kısıtlamalarını müşteri sözleşmesine **icra edilebilir madde** olarak koyma ve her alıcıya lisans kopyası verme yükümlülüğü; HF'de kapılı erişim. Apache-2.0 alternatif varken gereksiz hukuki yük. |
| `boun-tabi-LMG/TURNA` | Kart metninde üç ayrı yerde: "solely for non-commercial academic research purposes". Mutlak eleyici. |
| `tiiuae/Falcon-H1`, `Falcon3` | **"Apache-2.0 sanılan ama değil" tuzağı:** çok sayıda ikincil kaynak Apache-2.0 der; birincil metin kendi ifadesiyle "in part, based on the Apache License" olan özel bir TII lisansıdır. |
| `LiquidAI/LFM2.5` ailesi | Teknik olarak GPU'suz senaryoya en iyi oturan aile; ancak LFM Open License ticari kullanımı gelir eşiğine bağlar. |

### 4.2 Türkçe kanıtı bulunmadığı için elenenler
`ibm-granite/granite-4.2-3b` (kart, test edilen dilleri isimle sayar; Türkçe listede yoktur), `HuggingFaceTB/SmolLM3-3B` (yalnız 6 Batı Avrupa dili; tokenizer'ı Türkçe'de aşırı parçalanma üretir), `BSC-LT/salamandra-2b`, Gemma 4 E2B *(teknik raporun tam metninde "Turkish" hiç geçmez; `ai.google.dev` sayfasının altındaki "Türkçe" ifadesi sitenin arayüz dil seçicisidir, model dil desteği kanıtı değildir)*. `utter-project/EuroLLM-1.7B` Türkçe'yi isimle destekleyen nadir Apache-2.0 ailedir ancak bağlam uzunluğu 4.096 token ile bu ürün için yetersizdir.

### 4.3 Teknik boru hattı nedeniyle elenenler
| Model | Eleme gerekçesi |
|---|---|
| `Qwen/Qwen3.5-4B` | Lisansı temiz (Apache-2.0) ve kalitesi üstündür; **ancak llama.cpp `convert_hf_to_gguf.py` hibrit tensörleri dönüştüremez** (ggml-org/llama.cpp issue #27019, 13.08.2026'da açılmış, PR #27132 taslak; 17.09.2026 itibarıyla açık). Hazır GGUF çalışır ama **kendi ince ayarlı ağırlığımızı çeviremeyiz** — bu, projenin iş akışının ön şartıdır. **İzleme listesinde tutulur:** dönüştürücü birleşirse Faz 1'de yeniden değerlendirilir. |
| `Qwen/Qwen3-4B-Thinking-2507` | Ailenin en yüksek kalitesi, ancak yalnızca düşünme modunu destekler; 30 saniyelik bütçeyle bağdaşmaz. **Laboratuvarda tavan ölçümü** olarak kullanılır, ürüne girmez. |
| `asafaya/kanarya-2b` | Lisansı nettir (Apache-2.0) ancak mimarisi güncel GGUF dönüştürücüsünde desteklenmemektedir. |

### 4.4 Parametre sınıfı veya doğrulanabilirlik nedeniyle elenenler
Trendyol LLM serisi (4 milyar ve altında üretken model yok; en küçüğü 7 B), YTÜ CE COSMOS `Turkish-Llama-8b` / `Turkish-Gemma-9b`, `Turkcell-LLM-7b` ve benzerleri: hem **1-4 milyar taahhüdünü aşarlar** hem de taban modelleri Llama/Gemma olduğu için **lisans mirası** §4.1'deki kısıtları geri getirir. Gemma 4 E4B (4,5 B etkin / 8 B toplam) parametre taahhüdünü aşar ve ölçülmüş CPU hızı 2-5 tok/s'dir.

## 5. Seçimi kesinleştirecek ölçüm protokolü

Form, "model boyutu ve nicemleme düzeyi referans bilgisayarda ölçülerek seçilir" taahhüdünü içerir. Karar mekanizması budur; §2'deki sıralama yalnızca protokole giren aday kümesini belirler.

**Referans makine tanımı (şartnameye yazılacak):** 4 fiziksel çekirdek x86-64, AVX2 zorunlu; 16 GB RAM, çift kanal; ARM tek kart bilgisayar kabul edilmez. `llama.cpp` sürümü commit hash ile sabitlenir ve arşivlenir.

| Faz | Hafta | İş | Kapı / çıktı |
|---|---|---|---|
| **Faz 0** | 1 | "30 sn" ve "300-600 çıktı" tanımlarının netleştirilmesi; **tokenizer bereketi ölçümü** — tüm adayların tokenizer'ı kendi korpusumuzda (5746 tebliğleri, bordro açıklama alanları, muhtasar alan adları) token/kelime oranı için ölçülür | Yarım günlük iş, en yüksek getirili tek ölçüm: adaylar arası %30'a varan fark, Q4-Q5 seçiminden (~%15) ve gramer ek yükünden (~%12) daha büyüktür |
| **Faz 1** | 2 | Referans makinede `llama-bench -p 2048 -n 512 -t 3` ve `-t 4`; prefill/decode tok/s, Q4 dosya boyutu, `n_ctx=8192` + KV cache Q8_0 ile tepe RAM | **Kapı K1:** gerçekçi istem profilinde (2500 girdi + 250 çıktı, `cache_prompt` açık) uçtan uca ≤30 sn. Geçemeyen aday **etkileşim kademesi** olamaz. Tüm tahminler ölçümle değiştirilir |
| **Faz 2** | 2-5 | **Türkçe mali-hukuki altın standart set** (≥200 bulgu-yorum çifti, YMM/mali müşavir etiketli; "kanıt yetersiz" doğru cevabı olan negatif örnekler dâhil) | Kamuya açık hiçbir Türkçe kıyas seti mali-hukuki alanı veya şema uyumunu ölçmez; bu set projenin özgün Ar-Ge çıktısıdır |
| **Faz 3** | 6-12 | **İnce ayarsız taban skorları önce ölçülür ve kilitlenir**; sonra LoRA/QLoRA SFT (kiralık GPU, yalnız sentetik/anonim veri) | Ar-Ge katma değerinin tek doğrudan kanıtı, ince ayarsız tabana karşı farktır |
| **Faz 4** | 13-14 | LoRA merge → **Türkçe imatrix üret** → `llama-quantize --imatrix`; Q4_K_M ve Q5_K_M karşılaştırması | **Kapı K2:** nicemleme sonrası Faz 2 metriklerinde kabul edilemez düşüş yoksa sürüm dondurulur |

**İşlem sırası değişmez:** ince ayar → merge → nicemleme. Asla önce nicemleyip sonra ince ayar yapılmaz. imatrix kalibrasyonu **kendi Türkçe alan korpusumuzla** yapılır, varsayılan İngilizce metinle değil.

**Faz 2'de dört metrik ayrı ayrı raporlanır** (tek bir "doğruluk" sayısı bu üründe yanıltıcıdır):
1. **Şema geçerliliği** — GBNF ile %100 beklenir, bu yüzden tek başına anlamsızdır.
2. **Cevap doğruluğu** — içerik doğru mu?
3. **Çalıştırılabilir doğruluk** — üretilen kanıt talebi gerçekten farkı çözüyor mu? *(Bu etiketi motor otomatik üretir; bkz. EK-6 G2.)*
4. **"Yanlış ama şema-geçerli" oranı** — **zorunlu KPI.** Bir denetim ürününde en tehlikeli hata modudur; otomatik doğrulayıcıdan geçmiş gibi görünür. Sert şema zorlamasının bu oranı yükseltebildiği literatürde raporlanmıştır.

**Karşılaştırma tabanları (Kazanım 1'deki "ince ayarsız aynı model" ve "alan-dışı genel model" taahhütlerinin karşılığı):**
- **Taban A (zorunlu):** ince ayarsız Qwen3-4B-Instruct-2507, aynı istem, aynı GBNF, aynı nicemleme. Faz 3'e başlamadan **önce** ölçülür ve kilitlenir.
- **Taban B (zorunlu):** alan-dışı genel model — `Phi-4-mini-instruct` (MIT, Türkçe resmî dil listesinde).
- **Taban C (opsiyonel):** `Kumru-2B`, ince ayarlı ve ince ayarsız iki koşuda — Türkçe-yerli tokenizer'ın hız kazancı gerçekte ne kadar?
- **Tavan ölçümü (ürüne girmez):** Qwen3-4B-Thinking-2507 veya daha büyük bir Apache-2.0 model, yalnız laboratuvarda, yalnız sentetik/anonim veriyle. "4 milyarla ulaşılabilecek tavan neresi" sorusunu cevaplar.

## 6. Lisans yükümlülüklerinin ürüne yansıması

Apache-2.0 ve MIT "hiçbir şey yapmana gerek yok" demek değildir. Ürün paketinde yerine getirilecekler:

1. **Kurulum dizininde `LICENSE` ve `NOTICE` dosyaları** + uygulamada "Üçüncü Taraf Bildirimleri" ekranı (Apache-2.0 md. 4/a).
2. **Değişiklik bildirimi** (md. 4/b): tek bir `.gguf` dosyasında bu, GGUF üstveri alanlarıyla yapılır — `general.license`, `general.base_model` ve değişiklik notu alanı doldurulur.
3. **Marka kullanımı:** kökeni tanımlarken "Qwen3 tabanlı" demek serbesttir; ürün adında veya pazarlamada üçüncü taraf markası kullanılmaz.
4. **Sürüm dondurma:** seçilen ağırlığın SHA-256'sı, taban depo commit hash'i ve o tarihteki `LICENSE` metninin arşiv kopyası ürün dosyasında saklanır. Apache-2.0 geri alınamaz; indirilen sürüm için haklar kalıcıdır. **Gelecek sürümler farklı lisansla gelebilir**, bu nedenle her sürüm yükseltmesi ayrı bir lisans incelemesi tetikler.
5. **Sorumluluk ayrımı:** upstream lisansının sorumluluk reddi model sağlayıcısını korur, **bizi korumaz.** Müşteriye karşı çıktı sorumluluğu üründedir; ürün EULA'sındaki sınırlama ile 3568 sayılı Kanun kapsamındaki meslek mensubunun sorumluluğu arasındaki ayrım sözleşmede açıkça kurulur. *(Mimarinin bu riski düşürdüğü unutulmamalıdır: model tutar hesaplamaz, yalnızca bulgu yorumlar; kararı insan verir.)*
6. **KVKK:** bordro, sendika aidatı ve engellilik indirimi gibi **özel nitelikli kişisel veri** kalemleri içerir (KVKK md. 6). SFT korpusu gerçek bordrodan türetilecekse anonimleştirme yöntemi ve yeniden kimliklendirme riski analizi dosyaya eklenir; "anonimleştirildi" demek yeterli değildir. Eğitim kiralık GPU'da yapılacağı için **"eğitim: kiralık GPU, yalnız sentetik/anonim veri — çıkarım: müşteride CPU, kapalı devre"** ayrımı KVKK dosyasında açıkça yazılır.
7. **Değerlendirme setlerinin lisansı** model lisansından ayrıdır: kamuya açık Türkçe kıyas setlerinin çoğu ticari kullanımı kısıtlar; ürün içi kullanımda değil, yalnız laboratuvar ölçümünde kullanılır.

## 7. Doğrulanamayan ve ölçülmesi gereken noktalar

Aşağıdaki maddeler bu çalışmada kesinleştirilememiştir. Ar-Ge dosyasında kesin ifade olarak kullanılmamalı, ölçülmeli veya "doğrulanamadı" notuyla yazılmalıdır.

1. **4 çekirdek + 16 GB referans makinede hiçbir aday için yayımlanmış `llama-bench` tablosu yoktur.** §3'teki tok/s değerleri tahmindir; "bulgu başına ≤30 saniye" taahhüdü kendi makinemizde ölçülmeden dosyaya **ölçülmüş** olarak yazılamaz.
2. Q4_K_M dosya boyutlarından yalnızca Qwen3-4B (2,50 GB), Kumru-2B (1,46 GB) ve Granite 4.2-3b (2,24 GB) birincil kaynaktan doğrulanmıştır; Qwen3-4B-Instruct-2507, Qwen3-1.7B ve Phi-4-mini boyutları indirilerek teyit edilecektir. Qwen3-1.7B resmî GGUF deposunda yalnızca Q8_0 (1,83 GB) bulunmaktadır; Q4_K_M kendi dönüşümümüzle üretilecektir.
3. **Hiçbir adayın Türkçe'ye özgü tekil resmî skoru yoktur.** Eldeki en güçlü vekil ölçümler aile veya agregat düzeyindedir. Bağımsız Türkçe kıyas çalışmalarında 4 milyar altı modellerin skorları düşüktür ve gerçek bir boyut uçurumu vardır: **1-4 milyar sınıfında Türkçe'de bir bedel ödendiği dosyada açıkça yazılmalıdır.** Bu, mimari tercihin neden doğru olduğunun da kanıtıdır — model hesap yapmaz, her atfı sembolik kapı doğrular.
4. Kumru-2B'nin kendi kart iddiası ile bağımsız kıyas sonucu arasındaki çelişki çözülememiştir; bu nedenle ürün modeli değil, **karşılaştırma tabanı** olarak konumlandırılmıştır.
5. Qwen3.5 ailesinin llama.cpp dönüştürücü desteği izlenecektir (issue #27019 / PR #27132). Birleşirse Faz 1'de yeniden değerlendirilir.
6. Kumru-2B deposunda ayrı `LICENSE` dosyası bulunmadığı için, karşılaştırma tabanı olarak dahi kullanılmadan önce VNGRS'den yazılı lisans teyidi alınacaktır.

---

*Bu ek, Proje Bilgi Formu'nun İP5 iş paketine ve risk maddesi (8)'e dayanak teşkil eder. Model seçimi, Faz 1 ve Faz 4 kapılarından geçtikten sonra ölçüm tablosuyla birlikte kesinleşir.*
