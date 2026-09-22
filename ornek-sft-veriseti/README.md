# Örnek SFT veri seti

*EK-6'daki üretim yönteminin çalışan örneğidir. Hakem heyetinin "bu model neyle eğitilecek, veri nereden gelecek, etiketi kim koyacak" sorusuna, anlatı yerine koşturulabilir bir veri setiyle cevap verir.*

Bu dizin bir **desen**dir, eğitim için hazır bir veri seti değildir. 168 kayıt taşır; hedef hacim EK-6 §5'te 4.000–6.000 örnektir. Gösterdiği şey hacim değil, **biçim ve disiplin**: etiketin nereden geldiği, şemanın neyi yasakladığı, bölmenin nasıl kurulduğu ve hangi denetimlerin geçmeden bir kaydın eğitime giremeyeceği.

```
python3 uret.py        # senaryo kütüphanesinden veriyi üretir   (veri/*.jsonl)
python3 dogrula.py     # on denetimi koşar, raporu yazar         (rapor/uretim-raporu.md)
```

`uret.py` verilen tohumla **bit-özdeş** çıktı üretir; `dogrula.py` bir denetim kalırsa sıfırdan farklı kodla döner, yani sürekli tümleştirmeye doğrudan takılır.

---

## 1. Temel ilke: etiketi insan değil motor üretir

Her kaydın `etiket_kaynagi` alanı, "doğru cevap" tarafının nereden geldiğini söyler:

| Değer | Anlamı | Hangi görevde |
|---|---|---|
| `insa-geregi` | Bozulma bilerek enjekte edildiği için kök neden zaten bilinir | G1, G3 |
| `motor-dogrulamali` | Önerilen belge getirilip motor yeniden koşulmuş, fark çözülmüş | G2 |
| `belge-ic-toplam` | Belgenin kendi özet satırıyla iç toplam kontrolü | G4 |
| `insan-kapanis` | Yeminli mali müşavir eşliğindeki mutabakat oturumu kararı | yalnız kaynak C |

İnsan etiketi yalnızca kaynak C'de görülür ve bu örnekte C henüz **yer tutucudur** (§5).

## 2. Modelin sınırı, şemaya yazılmıştır

Model hesap yapmaz, tutar üretmez, karar vermez. Bu bir temenni değil, üç yerde birden zorlanan bir kısıttır:

1. **Şema**, G1/G2/G3 çıktılarında tutar alanı tanımlamaz (`sema/*.schema.json`).
2. **`dogrula.py` D3**, bu çıktıların serbest metin alanlarında para deseni arar ve bulursa kaydı reddeder. Mevzuat atıfları denetim dışıdır: atıf, iddia değildir.
3. **Sistem istemi** her kayıtta aynı cümleyi taşır: *"tutar HESAPLAMAZSIN, yeni rakam ÜRETMEZSİN, kapanış kararı VERMEZSİN."*

## 3. Dört görev

| Görev | Girdi | Çıktı | Şema |
|---|---|---|---|
| **G1** Bulgu yorumlama | Fark imzası, uygulanan kural sürümü, ihlal edilen tutarlılık kuralları, belge envanteri | En çok üç kök neden adayı; her biri S1–S5 sınıfı, hipotez kodu ve **mevzuat atfı** taşır | `sema/g1.schema.json` |
| **G2** Araştırma yönlendirme | G1 girdisi + önceki yorum | Tek somut adım: hangi belge, hangi alan, hangi dönem | `sema/g2.schema.json` |
| **G3** Denetçi sorusu | Bulgu + bağlam | 1–3 soru, her biri atıflı ve amacı etiketli | `sema/g3.schema.json` |
| **G4** Belge alan çıkarımı | Belge metni | Yapılandırılmış alanlar + iç toplam kontrolü | `sema/g4.schema.json` |

Her kayıt hem **yapılandırılmış** (`girdi` / `cikti`) hem **sohbet** biçiminde (`mesajlar`) tutulur. İkincisi birincisinden türer; `dogrula.py` D8 ikisinin ayrışmadığını denetler. Eğitim çerçeveniz hangisini istiyorsa onu okur.

## 4. Kaynaklar

| Kaynak | Bu örnekte | Gerçek hedef (EK-6 §5) |
|---|---|---|
| **A** Mevzuat referanslı sentetik senaryo kütüphanesi | 14 senaryo × parametrik türetme = 141 kayıt | ≥60 senaryo ≈ 2.000–3.000 örnek, ay 7 |
| **B** Hata enjeksiyonlu kalibrasyon seti | 12 çoklu-neden vakası = 24 kayıt | ≥400 vaka ≈ 1.500–2.500 örnek, ay 8 |
| **C** Pilot mutabakat kayıtları | 3 **yer tutucu** | Pilot başına ≥200 fark kalemi, ay 10–12 |

`senaryolar/senaryo-kutuphanesi.json` her senaryoyu bir mevzuat maddesine ve bir tutarlılık kuralına (K1–K14) bağlar; parametre uzayı sayesinde tek senaryodan onlarca örnek türer. Yedi fark sınıfının tamamı (S1, S2, S3, S4a, S4b, S4c, S5) temsil edilir.

## 5. Kaynak C yer tutucudur

`veri/kaynak-c-yer-tutucu.jsonl` **gerçek pilot kaydı değildir.** Pilot verisi ay 10–12'de, gizlilik sözleşmesi ve anonimleştirme sonrasında oluşacaktır. Bu üç satır yalnızca kaynak C'nin kayıt biçimini ve insan kapanış kararının nereye yazıldığını gösterir; her biri `girdi.yer_tutucu: true` taşır ve `dogrula.py` D10 bunların eğitim bölmesine girmediğini denetler.

## 6. Bölme ve sızıntı

Bölme **kuruluş ve dönem** bazındadır. Kör test kuruluşları (`KUR-SENT-06`, `KUR-ENJ-04`) ve pilot kuruluşları eğitimde hiçbir biçimde görünmez.

| Bölme | Kayıt | Kullanım |
|---|---|---|
| `egitim` | 118 | İnce ayar |
| `kalibrasyon` | 22 | Eşik ve sınıf dengesi ayarı |
| `kor-test` | 28 | Ölçüm; ay 7'de mühürlenip TTO ve YMM nezdinde saklanır |

D2 denetimi, aynı kuruluş×dönem çiftinin iki bölmede birden bulunmadığını doğrular.

## 7. Denetimler

`dogrula.py`, EK-6 §4'teki kalite kontrollerini çalıştırılabilir hâle getirir. Bir denetim kalırsa veri seti eğitime uygun değildir.

| Denetim | Neyi güvence altına alır |
|---|---|
| **D1** şema geçerliliği | Zarf ve görev şemasına uymayan kayıt eğitime alınmaz |
| **D2** sızıntı | Aynı kuruluşun aynı dönemi iki bölmede olamaz; kör test kuruluşu eğitimde görünemez |
| **D3** tutar yasağı | G1/G2/G3 çıktılarının hiçbir metin alanı tutar iddiası taşıyamaz |
| **D4** mevzuat atfı | Atıfsız hipotez ve atıfsız soru kabul edilmez |
| **D5** belirsizlik disiplini | Ayırt edilemeyen kalem S5 adayı ve belirsizlik notu taşır; S3 kanıt talebiyle birlikte gelir |
| **D6** anonimlik | Kişi alanları yalnız tokenize; 11 haneli kimlik deseni hiçbir kayıtta bulunamaz |
| **D7** etiket kaynağı | Sentetik kaynakta insan etiketi olamaz; G2 etiketi motorla doğrulanmış olmalıdır |
| **D8** mesaj tutarlılığı | Sohbet render'ı yapılandırılmış çıktıdan ayrışamaz |
| **D9** G4 belgeye dayalılık | Çıkarılan her alan belge metninde birebir bulunmalıdır |
| **D10** pilot verisi eğitim dışı | Kaynak C eğitim bölmesine giremez |

D3, D9 ve D10 bu veri seti geliştirilirken gerçek hata yakaladı: bir sürümde G4 etiketleri belgeyle ilgisiz üretilmişti, D9 onu yakaladı.

## 8. MOTOR bir taklittir

`uret.py` içindeki `motor()`, doğrulanmış deterministik hesap çekirdeğinin yerine duran küçük bir **taklittir (stub)**: aynı arayüzü verir, aynı fark imzasını üretir, ama yalnızca bu on dört senaryonun aritmetiğini bilir. Gerçek hatta yerine çekirdek konur; kayıtların biçimi ve etiket kaynağı değişmez. Taklit olduğu için buradaki tutarlar **örnektir, mevzuat hesabı değildir.**

## 9. Bu örneğin kapsamadıkları

- **Hacim.** 168 kayıt, hedefin yaklaşık yüzde üçüdür.
- **Sınıf dengesi.** S4c payı yüksektir (kök neden adaylarının yaklaşık yarısı); gerçek kütüphanede sınıflar dengelenir ve çoklu-neden vakaları bilinçli olarak fazla örneklenir.
- **Gerçek dağılım.** Fark büyüklükleri ve kalem dağılımı sentetiktir; gerçek dağılımı yalnız kaynak C temsil eder.
- **Kaynak D.** Denetçi dili korpusu (mevzuat metinleri, anonim oturum notları) bu örnekte yoktur; G3 örnekleri senaryo kütüphanesindeki "beklenen sorular"dan türer.
- **Dilbilgisi kısıtlı çözümleme.** Modelin çıktısının koşum anında şemaya zorlanması burada değil, çıkarım tarafındadır.

## 10. Dizin

```
ornek-sft-veriseti/
├── README.md                       bu dosya
├── uret.py                         üretim hattı (motor taklidi + parametrik türetme)
├── dogrula.py                      on denetim + rapor
├── sema/
│   ├── kayit.schema.json           ortak zarf
│   └── g1..g4.schema.json          görev çıktı şemaları
├── senaryolar/
│   └── senaryo-kutuphanesi.json    14 senaryo, mevzuat ve K-kuralı bağlantılı
├── veri/
│   ├── egitim.jsonl                118 kayıt
│   ├── kalibrasyon.jsonl           22 kayıt
│   ├── kor-test.jsonl              28 kayıt
│   └── kaynak-c-yer-tutucu.jsonl   3 kayıt · GERÇEK PİLOT KAYDI DEĞİLDİR
└── rapor/
    └── uretim-raporu.md            dogrula.py çıktısı
```
