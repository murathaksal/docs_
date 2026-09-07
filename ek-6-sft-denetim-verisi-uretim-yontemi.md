# EK-6 — Dar Kapsamlı Denetçi Modelinin Eğitim Verisi: Üretim Yöntemi

*Proje Bilgi Formu'ndaki AS-4 araştırma sorusunun ve İP5 iş paketinin dayanağıdır. Hakem heyetinin "bu model neyle eğitilecek, veri nereden gelecek, etiketi kim koyacak" sorularına cevap verir.*

---

## 1. Temel ilke: etiketi insan değil, deterministik motor üretir

Klasik denetimli ince ayar (SFT) için alan uzmanının binlerce örneği elle etiketlemesi gerekir; bu projede o kaynak yoktur ve olsaydı da ölçeklenmezdi. Projenin yaklaşımı farklıdır: **doğrulanmış deterministik hesap motoru, eğitim verisinin referans kaynağı (oracle) olarak kullanılır.** Motorun her koşumu; girdiyi, uygulanan kural sürümünü, sonucu ve beyanla farkı kesin ve tekrarlanabilir biçimde üretir. Eğitim çiftinin "doğru cevap" tarafı bu çıktıdan türetilir. İnsan yalnızca üç yerde devreye girer: sentetik senaryoların mevzuat referansını yazarken, pilot mutabakat oturumlarında kapanış kararı verirken ve kör test setini onaylarken.

## 2. Modelin öğreneceği görevler (denetçi rolünün parçaları)

| Görev | Girdi | Çıktı (şema zorlamalı) | Doğru cevabın kaynağı |
|---|---|---|---|
| **G1 — Bulgu yorumlama** | Fark imzası (hangi kalemlerde, ne yönde, ne büyüklükte fark; uygulanan kural sürümü; ihlal edilen tutarlılık kuralları) | Aday kök neden sınıfları sıralı listesi + mevzuat maddesi atıflı düz Türkçe açıklama | Sentetik/enjeksiyon vakalarında **inşa gereği bilinir**; pilot vakalarında insan kapanış kararı (S1–S5) |
| **G2 — Araştırma yönlendirme** | G1 girdisi + eldeki belge envanteri (hangi dönem için hangi belgeler mevcut) | "Şu belgeye bak, şu alanı kontrol et" — tek bir somut sonraki adım | **Motor tarafından otomatik doğrulanır:** önerilen belge getirilip motor yeniden koşulduğunda fark çözülüyorsa öneri doğrudur |
| **G3 — Denetçi sorusu üretme** | Bulgu + bağlam | Bir denetçinin bu bulgu karşısında soracağı 1–3 soru | Anonimleştirilmiş YMM mutabakat oturumu kayıtları; mevzuat referanslı senaryo kütüphanesindeki "beklenen sorular" |
| **G4 — Belge alan çıkarımı** | Belge metni (Muhtasar ve Prim Hizmet Beyannamesi, hizmet listesi, tahakkuk fişi) | Yapılandırılmış alanlar | Belgenin kendi özet satırlarıyla iç-toplam kontrolü; sentetik belgelerde inşa gereği bilinir |

G1–G3 birlikte modelin **denetçi rolünü** oluşturur: sonucu inceler, ne anlama geldiğini söyler, hangi kanıtı isteyeceğini belirler ve soru sorar. Hiçbir görevde tutar hesaplamaz.

## 3. Veri kaynakları ve üretim hattı

### Kaynak A — Mevzuat referanslı sentetik senaryo kütüphanesi (İP4 çıktısı, ≥60 senaryo)
Her senaryo gerçek bir tebliğ/genelge maddesine bağlı, bilinen tek bir kök nedenli bozulmadır (örnek: yüksek lisans diploması Mart ayında alınmışken Ocak–Şubat terkin oranının %90 uygulanması; 7555 tavanının ay ortası yürürlüğünün göz ardı edilmesi; 5746 ile 4691 arasında aynı ücret üzerinden çifte istisna). Senaryo, sentetik bir personel × dönem verisine uygulanır → motor koşulur → fark imzası, doğru kök neden, çözen belge ve beklenen denetçi soruları **inşa gereği bilinir**. Her senaryo parametrik olduğundan (tutar, kişi sayısı, dönem, rejim değiştirilebilir) tek senaryodan onlarca eğitim örneği türetilir.

### Kaynak B — Hata enjeksiyonlu kalibrasyon seti (İP4 çıktısı, ≥400 vaka)
Doğrulanmış gerçek dönem verisi (çapa testlerindeki 96 → ≥140 dönem) anonimleştirilir; üzerine tek veya çoklu bilinen bozulmalar enjekte edilir; motor koşulur. Etiket enjekte edilen bozulmadır. Çoklu-neden vakaları, modelin "ayırt edilemez → belirsiz" davranışını öğrenmesi için özellikle üretilir.

### Kaynak C — Pilot mutabakat kayıtları (İP7, gerçek veri)
İki pilot kuruluşun gerçek fark envanteri: her fark için motor çıktısı + YMM eşliğindeki kapanış kararı (kök neden sınıfı, çözen belge, karşı görüş). Bu kaynak **yalnızca anonimleştirildikten sonra** (TC kimlik ve ücret alanları müşteri tarafında tutulan anahtarla tokenize edilerek) ve gizlilik sözleşmesi kapsamında kullanılır. Hacmi küçüktür ama gerçek dağılımı temsil eder; ağırlıklı olarak **test ve kalibrasyon** için ayrılır, eğitime yalnızca kör test setinden ayrılmış kısmı girer.

### Kaynak D — Denetçi dili korpusu (G3 için)
Kamuya açık mevzuat metinleri, tebliğ ve genelgeler; anonimleştirilmiş YMM oturum notları; senaryo kütüphanesindeki "beklenen sorular". Modelin soru üretiminde mevzuat maddesine atıf disiplinini öğrenmesi için her örnek madde referansı taşır.

### Hattın işleyişi
```
senaryo/enjeksiyon/pilot verisi → deterministik motor koşumu → fark imzası + kural sürümü + tutarlılık ihlalleri
     → (G1/G2/G3/G4 için) girdi-çıktı çifti şemaya dökülür → şema doğrulaması → eğitim/test bölmesi
     → G2 çiftleri için ek adım: önerilen belge getirilir, motor yeniden koşulur, "çözdü/çözmedi" etiketi otomatik atanır
```

## 4. Sızıntı ve kalite kontrolleri

- **Bölme kuruluş ve dönem bazındadır:** aynı kuruluşun aynı dönemi hem eğitimde hem testte bulunamaz. Pilotlardan ayrılan kör test seti eğitimde hiçbir biçimde kullanılmaz.
- **Şema geçerliliği:** çıktısı şemaya uymayan örnek eğitime alınmaz; modelin çıktısı da dilbilgisi kısıtlı çözümlemeyle şemaya zorlanır.
- **Dengeleme:** kök neden sınıfları ve "belirsiz" sınıfı dengeli temsil edilir; model tek nedene zorlama eğilimi kazanmasın diye çoklu-neden vakaları bilinçli olarak fazla örneklenir.
- **Anonimleştirme eğitimden önce:** hiçbir kişisel veri ham hâliyle eğitim hattına girmez; bulut grafik işlemci kiralaması yalnızca sentetik ve anonimleştirilmiş veriyle yapılır.

## 5. Hedef hacimler ve zamanlama

| Kaynak | Hedef hacim | Hazır olma |
|---|---|---|
| A — Sentetik senaryo kütüphanesi | ≥60 senaryo × parametrik türetme ≈ 2.000–3.000 örnek | Ay 7 |
| B — Hata enjeksiyonlu set | ≥400 vaka ≈ 1.500–2.500 örnek (çoklu görev) | Ay 8 |
| C — Pilot kayıtları | Pilot başına ≥200 fark kalemi; ağırlıklı test/kalibrasyon | Ay 10–12 |
| D — Denetçi dili korpusu | Mevzuat metinleri + anonim oturum notları | Ay 7–10 |

İlk ince ayar ay 8–9'da A+B ile yapılır; ay 10'da C'nin kör kısmıyla ölçülür; ay 11'de C'nin eğitim kısmıyla ikinci tur yapılır ve ay 12'de yeniden ölçülür. Böylece "gerçek veriyle ne kadar kazanç geliyor" sorusu ayrı olarak raporlanabilir.

## 6. Ölçüm — hakem için en önemli özellik

G2'nin (araştırma yönlendirme) doğruluğu **insan etiketine ihtiyaç duymadan** ölçülür: önerilen belge getirilir, motor yeniden koşulur, fark çözülmüşse öneri doğrudur. Bu, değerlendirmenin öznel olmadığı ve pilot verisi büyüdükçe otomatik olarak genişlediği anlamına gelir. G1 ve G3 için YMM etiketli kör örneklem (dönem başına ≥20 kalem) kullanılır; ince ayarsız temel model aynı setle ölçülerek kazanç raporlanır.

## 7. Modelin sınırı (tekrar)

Model; hesap yapmaz, tutar üretmez, karar vermez. Ürettiği her şey bir bulgu yorumu, bir belge talebi veya bir sorudur. Yanlış bir çıktının en kötü sonucu gereksiz bir inceleme adımıdır. Nihai kök neden ataması ve dönemin mühürlenmesi insan onayıyla yapılır; Yeminli Mali Müşavirin tasdik yetkisi ve sorumluluğu değişmez.
