# Üretim ve denetim raporu

*`uret.py` ve `dogrula.py` tarafından üretilmiştir. Kayıt sayısı: 168.*

## Denetimler

| Denetim | Sonuç | Kapsam |
|---|---|---|
| D1 şema geçerliliği | **GEÇTİ** | 168 kayıt zarf + görev şemasına karşı doğrulandı |
| D2 sızıntı (kuruluş×dönem) | **GEÇTİ** | 40 kuruluş×dönem çifti tek bölmede; kör test kuruluşları eğitimden tamamen ayrık |
| D3 tutar yasağı | **GEÇTİ** | G1/G2/G3 çıktılarının hiçbirinde tutar iddiası yok |
| D4 mevzuat atfı | **GEÇTİ** | G1 hipotezlerinin ve G3 sorularının tamamı mevzuat maddesine bağlı |
| D5 belirsizlik disiplini | **GEÇTİ** | belirsiz ve veri eksiği kalemleri kanıt talebiyle birlikte raporlanıyor |
| D6 anonimlik | **GEÇTİ** | kişi alanları yalnız tokenize biçimde; 11 haneli kimlik deseni yok |
| D7 etiket kaynağı | **GEÇTİ** | G2 etiketleri motor tarafından, diğerleri inşa gereği atanmış |
| D8 mesaj tutarlılığı | **GEÇTİ** | her kaydın asistan mesajı, yapılandırılmış çıktının birebir karşılığı |
| D9 G4 belgeye dayalılık | **GEÇTİ** | G4 alanlarının tamamı belge metninde birebir bulunuyor; özet satırı okunuyor |
| D10 pilot verisi eğitim dışı | **GEÇTİ** | 3 kaynak C kaydı eğitim dışında ve yer tutucu olarak işaretli |

## Dağılımlar

| Kesit | Dağılım |
|---|---|
| Görev | G1 58, G2 55, G3 43, G4 12 |
| Kaynak | A 141, B 24, C 3 |
| Bölme | egitim 118, kalibrasyon 22, kor-test 28 |
| G1 kök neden sınıfı | S1 4, S2 5, S3 9, S4a 11, S4b 6, S4c 40, S5 12 |

'Belirsiz' (S5) adaylarının payı: **%13.8**. AS-2 hedefi, tutar payı olarak ≤%5'tir; buradaki oran kayıt sayısı üzerinden hesaplanır ve tutar ağırlıklı ölçüm gerçek pilot verisiyle yapılır.
