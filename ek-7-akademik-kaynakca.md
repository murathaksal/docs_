# EK-7: Akademik ve Kurumsal Kaynakça

*Proje Bilgi Formu'ndaki dört araştırma sorusunun (AS-1 - AS-4) ve hakem sunumundaki her sayısal iddianın dayanağıdır. Sunumda geçen literatür rakamlarının tamamı bu ekte künyesiyle verilmiştir; hakem heyeti, sunumda duyduğu bir oranı bu ekten tek tek doğrulayabilir.*

## Bu kaynakçanın kuralları

1. **Her künye birincil kaynaktan doğrulanmıştır.** Yayıncı sayfası, konferans bildiri kaydı, kurumsal arşiv veya resmî mevzuat metni üzerinden yazar, yıl, yayın yeri ve sayfa bilgisi teyit edilmiştir.
2. **Doğrulanamayan kaynak listeye alınmamıştır.** Tarama sırasında konuya uygun görünen ancak künyesi birincil kaynaktan teyit edilemeyen çalışmalar, ne kadar ilgili olursa olsun elenmiştir; elenenlerin listesi ve gerekçeleri bölüm 12'dedir.
3. **İkincil kaynakta dolaşan sayılar kullanılmamıştır.** Bloglarda ve haber metinlerinde tekrarlanan iki halüsinasyon oranı, birincil kaynağın tam metninde bulunamadığı için sunumdan çıkarılmıştır (bölüm 12).
4. **Ön baskı ile hakemli yayın ayrılmıştır.** Hakem denetiminden geçmemiş çalışmalar künyesinde açıkça belirtilir.

---

## 1. Nöro-sembolik mimari: hesabın deterministik bir araca devredilmesi

*AS-1 ve AS-2'nin mimari zemini. Bu kaynaklar, dil modelinin hesap ve karar üretmek yerine sembolik bir motorla çevrelenmesinin literatürdeki karşılığını verir.*

**[GarcezLamb2023]** Garcez, A. d'Avila & Lamb, L. C. (2023). Neurosymbolic AI: the 3rd wave. Artificial Intelligence Review, 56(11), 12387-12406.
  https://doi.org/10.1007/s10462-023-10448-w
  *Bulgu:* Yapay zekânın üçüncü dalgası, öğrenen sinir ağları ile kural tabanlı sembolik akıl yürütmeyi tek mimaride birleştirmektir; güven, güvenlik ve açıklanabilirlik ancak bu birleşimle sağlanır.
  *Projede:* Projenin genel mimari tezi (AS-1 + AS-2): sinirsel öğrenme ile sembolik bilgi temsili/mantıksal çıkarımı ilkeli biçimde birleştirmek. Sunumda "nöro-sembolik" teriminin ilk açıklandığı slaytın akademik dayanağı.

**[Booch2021]** Booch, G., Fabiano, F., Horesh, L., Kate, K., Lenchner, J., Linck, N., Loreggia, A., Murgesan, K., Mattei, N., Rossi, F. & Srivastava, B. (2021). Thinking Fast and Slow in AI. Proceedings of the AAAI Conference on Artificial Intelligence, 35(17), 15042-15046.
  https://ojs.aaai.org/index.php/AAAI/article/view/17765
  *Bulgu:* Kahneman'ın hızlı/yavaş düşünme ayrımı yapay zekâya taşındığında sinirsel işleme Sistem-1'e, yavaş ve düşünülmüş sembolik akıl yürütme Sistem-2'ye karşılık gelir; ideal sistem ikisini birlikte çalıştırır.
  *Projede:* AS-1: 'Hesabı motor yapar, bulguyu model inceler' iş bölümünün bilişsel gerekçesi. Sistem-1 (hızlı, örüntüsel = yerel dil modeli) ile Sistem-2 (yavaş, kurala dayalı = deterministik motor) ayrımı.

**[Gao2023PAL]** Gao, L., Madaan, A., Zhou, S., Alon, U., Liu, P., Yang, Y., Callan, J. & Neubig, G. (2023). PAL: Program-aided Language Models. Proceedings of the 40th International Conference on Machine Learning (ICML), PMLR 202, 10764-10799.
  https://proceedings.mlr.press/v202/gao23f.html
  *Bulgu:* Dil modelleri problemi doğru parçalasalar bile hesap adımında mantık ve aritmetik hatası yapar; hesabı bir Python yorumlayıcısına devretmek bu hatayı ortadan kaldırır.
  *Projede:* Çekirdek tez: 'Model ASLA tutar hesaplamaz.' Dil modeli problemi okur ve yapıyı kurar, çözüm/hesap adımı deterministik bir yürütücüye devredilir.

**[Chen2023PoT]** Chen, W., Ma, X., Wang, X. & Cohen, W. W. (2023). Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks. Transactions on Machine Learning Research (TMLR), 2023.
  https://arxiv.org/abs/2211.12588
  *Bulgu:* Akıl yürütmeyi hesaptan ayırıp hesabı dış bir bilgisayara yaptırmak, düşünce zinciri yöntemine göre ortalama %12 doğruluk kazancı sağlar; kazanç finansal soru-cevap veri kümelerinde de ölçülmüştür.
  *Projede:* Çekirdek tez ve AS-2: Akıl yürütme ile hesabın birbirinden AYRILMASI. Ayrıca finansal soru-cevap alanında (FinQA, ConvFinQA, TATQA) ölçülmüş olması, mali mevzuat alanına doğrudan emsal oluşturur.

**[Schick2023]** Schick, T., Dwivedi-Yu, J., Dessi, R., Raileanu, R., Lomeli, M., Hambro, E., Zettlemoyer, L., Cancedda, N. & Scialom, T. (2023). Toolformer: Language Models Can Teach Themselves to Use Tools. Advances in Neural Information Processing Systems 36 (NeurIPS 2023).
  https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html
  *Bulgu:* Bir dil modeli, hangi aracı ne zaman ve hangi girdiyle çağıracağını elle etiketlenmiş veri olmadan, kendi ürettiği denemeleri otomatik bir yararlılık ölçütüyle eleyerek öğrenebilir.
  *Projede:* AS-1: Modelin araç (deterministik motor) çağırmayı ELLE ETİKETLENMİŞ veri olmadan, otomatik bir ölçüte göre filtrelenen kendi üretimiyle öğrenebilmesi. EK-6'daki 'oracle ile otomatik etiketleme' yaklaşımının doğrudan emsali.

**[Kambhampati2024]** Kambhampati, S., Valmeekam, K., Guan, L., Verma, M., Stechly, K., Bhambri, S., Saldyt, L. P. & Murthy, A. B. (2024). Position: LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks. Proceedings of the 41st International Conference on Machine Learning (ICML), PMLR 235, 22895-22907.
  https://proceedings.mlr.press/v235/kambhampati24a.html
  *Bulgu:* Dil modelleri tek başlarına plan yapamaz ve kendilerini doğrulayamaz; ancak dış, model tabanlı doğrulayıcılarla çevrelendiklerinde (LLM-Modulo) güçlü bir fikir üreticisi olurlar.
  *Projede:* AS-2 ve genel mimari: Dil modelinin kendi kendini doğrulayamayacağı, ancak DIŞ MODEL TABANLI DOĞRULAYICILARLA çevrelendiğinde değerli olduğu. Projenin 'motor karar verir, model inceler' kurgusunun birebir akademik karşılığı.

**[Pan2023LogicLM]** Pan, L., Albalak, A., Wang, X. & Wang, W. (2023). Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning. Findings of the Association for Computational Linguistics: EMNLP 2023, 3806-3824.
  https://aclanthology.org/2023.findings-emnlp.248/
  *Bulgu:* Dil modelini doğal dili sembolik biçime çevirmekle sınırlayıp çıkarımı deterministik bir çözücüye bırakmak, modelin tek başına çalışmasına göre %39, düşünce zincirine göre %18 daha doğru sonuç verir.
  *Projede:* AS-2: Modelin doğal dili sembolik biçime çevirmesi, çıkarımın DETERMİNİSTİK sembolik çözücü tarafından yapılması ve çözücünün hata mesajlarıyla modelin düzeltilmesi. Projedeki sembolik doğrulama kapısı + geri besleme döngüsünün emsali.

**[Cobbe2021]** Cobbe, K., Kosaraju, V., Bavarian, M., Chen, M., Jun, H., Kaiser, L., Plappert, M., Tworek, J., Hilton, J., Nakano, R., Hesse, C. & Schulman, J. (2021). Training Verifiers to Solve Math Word Problems. arXiv:2110.14168.
  https://arxiv.org/abs/2110.14168
  *Bulgu:* Üreten modelden ayrı bir doğrulayıcı eğitip üretilen çözümleri elemek, modeli büyütmekten daha etkili ve veriyle daha iyi ölçeklenen bir doğruluk artışı sağlar.
  *Projede:* AS-2: ÜRETİCİ ile DOĞRULAYICININ ayrılması ilkesi. Projedeki 'sembolik doğrulama kapısı' bu ayrımın deterministik/sembolik biçimidir.

**[Huang2024]** Huang, J., Chen, X., Mishra, S., Zheng, H. S., Yu, A. W., Song, X. & Zhou, D. (2024). Large Language Models Cannot Self-Correct Reasoning Yet. International Conference on Learning Representations (ICLR 2024).
  https://arxiv.org/abs/2310.01798
  *Bulgu:* Dil modelleri dışarıdan geri bildirim almadan, yalnızca kendi yeteneğiyle akıl yürütme hatalarını düzeltemez; hatta kendini düzeltme denemesi çoğu kez performansı düşürür.
  *Projede:* AS-2'nin VAROLUŞ GEREKÇESİ: Modelin kendi gerekçesini kendi başına düzeltemeyeceği, dolayısıyla DIŞSAL (sembolik kural tabanına dayalı) bir doğrulama kapısının zorunlu olduğu.


## 2. Dayanaksız iddia (halüsinasyon) ve mevzuat alanında ölçülmüş oranlar

*"Neden yapay zekâyı hesaplayıcı koltuğuna oturtmuyoruz" sorusunun sayısal cevabı. Slayt 3'ün ve AS-2'nin dayanağıdır.*

**[Ji2023]** Ji, Z., Lee, N., Frieske, R., Yu, T., Su, D., Xu, Y., Ishii, E., Bang, Y. J., Madotto, A., & Fung, P. (2023). Survey of Hallucination in Natural Language Generation. ACM Computing Surveys, 55(12), Article 248, 1–38.
  https://doi.org/10.1145/3571730
  *Bulgu:* Alanın standart referansı sayılan bu derleme, halüsinasyonu "sistemin verilen kaynakla tutarsız, ama akıcı ve inandırıcı görünen metin üretmesi" olarak tanımlar ve sorunu özetleme, diyalog, soru-cevap, veriden metin üretme ve çeviri görevleri boyunca ölçme ve azaltma yöntemleriyle birlikte sistematikleştirir.
  *Projede:* Tanım slaytı: "halüsinasyon" teriminin alanda kabul görmüş ilk kapsamlı tanımı ve iç/dış (intrinsic/extrinsic) ayrımı. Sunumda terimi ilk kez açarken atıf verilecek temel kaynak; alanın en çok atıf alan derlemesi olduğu için akademisyen hakeme güven verir.

**[Huang2025]** Huang, L., Yu, W., Ma, W., Zhong, W., Feng, Z., Wang, H., Chen, Q., Peng, W., Feng, X., Qin, B., & Liu, T. (2025). A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions. ACM Transactions on Information Systems, 43(2), 1–55.
  https://doi.org/10.1145/3703155
  *Bulgu:* Bilgi erişim sistemleri alanının başlıca dergisinde yayımlanan bu kapsamlı derleme, dayanaksız iddiayı ikiye ayırıyor; OLGUSAL halüsinasyon (üretilen içeriğin doğrulanabilir gerçeklerle çelişmesi: çelişki ve tamamen uydurma) ve SADAKAT halüsinasyonu (verilen talimat, bağlam ya da kendi iç mantığıyla tutarsızlık); ve erişim destekli modellerin bu sorunla mücadelede hâlâ sınırlı kaldığını ayrı bir bölümde ele alıyor.
  *Projede:* Tanım/taksonomi slaytı (jargonun ilk kullanımda açılması gereği) + AS-2. "Dayanaksız iddia" teriminin akademik çerçevesi ve erişim destekli modellerin sınırlarının hakemli kaynakla gösterilmesi.

**[Kalai2026]** Kalai, A. T., Nachum, O., Vempala, S. S., & Zhang, E. (2026). Evaluating large language models for accuracy incentivizes hallucinations. Nature, 653(8116), 1047–1051. (Ön baskı: "Why Language Models Hallucinate", arXiv:2509.04664, 2025.)
  https://doi.org/10.1038/s41586-026-10549-w
  *Bulgu:* Nature'da yayımlanan bu çalışma, dil modellerinin halüsinasyon üretmesinin gizemli bir arıza değil istatistiksel bir zorunluluk olduğunu gösteriyor: modeller tıpkı zor bir sınavda boş bırakmak yerine tahmin yürüten öğrenciler gibi, emin olmadıklarını itiraf etmek yerine tahmin etmeye ödüllendiriliyorlar; eğitim verisinde tekrar etmeyen tekil bilgiler (ör. belirli bir olayın tarihi) için hata kaçınılmaz.
  *Projede:* ÇEKİRDEK TEZ + AS-2 + "belirsiz tutar payı <=%5" metriği. Halüsinasyonun bir yazılım hatası değil, eğitim ve değerlendirme düzeninin YAPISAL sonucu olduğunu gösterir: modeller emin olmadığında susmak yerine tahmin etmeye ödüllendiriliyor. Denetci.AI'ın "bilmiyorum/belirsiz" diyebilen ve tutarı hiç hesaplamayan tasarımının teorik gerekçesi.

**[Dahl2024]** Dahl, M., Magesh, V., Suzgun, M., & Ho, D. E. (2024). Large Legal Fictions: Profiling Legal Hallucinations in Large Language Models. Journal of Legal Analysis, 16(1), 64–93.
  https://doi.org/10.1093/jla/laae003
  *Bulgu:* Stanford ekibi, rastgele seçilmiş federal mahkeme kararları hakkında doğrulanabilir sorular sorulduğunda büyük dil modellerinin ChatGPT-4'te %58, Llama 2'de %88 oranında dayanaksız (halüsinasyon) yanıt ürettiğini ölçtü; modeller ayrıca kullanıcının yanlış hukuki varsayımını çoğu zaman düzeltmiyor ve ne zaman uydurduğunu kendisi de bilemiyor.
  *Projede:* ÇEKİRDEK TEZ + AS-2. "Neden yapay zekâyı hesaplayıcı değil denetçi konumuna koyduk" slaytının ANA dayanağı. Ayrıca AS-2'nin (sembolik doğrulama kapısı) gerekçesi: model kendi hatasını bilmiyor ve kullanıcının yanlış öncülünü düzeltmiyor; bu yüzden kararı insan verir, iddiayı kural tabanı doğrular.

**[Magesh2025]** Magesh, V., Surani, F., Dahl, M., Suzgun, M., Manning, C. D., & Ho, D. E. (2025). Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools. Journal of Empirical Legal Studies, 22(2), 216–242.
  https://doi.org/10.1111/jels.12413
  *Bulgu:* Hukuk alanının en pahalı ticari erişim destekli (RAG) araçları bile hâlâ %17–33 oranında dayanaksız iddia üretiyor: LexisNexis Lexis+ AI sorguların yalnızca %65'ini, Westlaw AI-Assisted Research %42'sini (makalenin Şekil 4 dökümünde %41), Ask Practical Law AI ise %19'unu doğru yanıtlıyor; makalenin sonuç cümlesi net: "hukuki araştırma için yapay zekâ araçları halüsinasyonları ortadan kaldırmadı".
  *Projede:* AS-2 (sembolik doğrulama kapısı) + "atıf doğruluğu >=%98, desteksiz iddia <=%1" metriklerinin gerekçesi. En kritik kaynak: RAG (erişim destekli üretim) halüsinasyonu AZALTIYOR ama ORTADAN KALDIRMIYOR; bu yüzden Denetci.AI erişimin üstüne ayrıca sembolik kural tabanına karşı doğrulama koyuyor.

**[Charlotin2026]** Charlotin, D. (2026). AI Hallucination Cases Database. https://www.damiencharlotin.com/hallucinations/ (Erişim: 14 Eylül 2026). CC BY 4.0.
  https://www.damiencharlotin.com/hallucinations/
  *Bulgu:* 14 Eylül 2026 itibarıyla dünya genelinde 2.041 mahkeme kararı, dosyaya sunulan belgelerde yapay zekânın UYDURDUĞU içtihat/atıf bulunduğunu tespit etmiş durumda; ve bu vakaların bir kısmı ChatGPT gibi genel araçlardan değil, doğrudan hukuk için üretilmiş Westlaw/CoCounsel (16 vaka) ve LexisNexis (11 vaka) araçlarından kaynaklanıyor.
  *Projede:* AÇILIŞ SLAYDI; "sorun teorik değil, sahada gerçekleşti". Sektör temsilcisi ve teknopark yönetimi üyelerine hitap eden somut kanıt. Ayrıca AS-2'nin gerekçesi: hukuk odaklı ticari araçlar (Westlaw/CoCounsel, LexisNexis) kullanılan dosyalarda da uydurma atıf mahkemeye ulaşmış.

**[Walters2023]** Walters, W. H., & Wilder, E. I. (2023). Fabrication and errors in the bibliographic citations generated by ChatGPT. Scientific Reports, 13(1), 14045.
  https://doi.org/10.1038/s41598-023-41032-5
  *Bulgu:* 42 konuda üretilen 84 metindeki 636 kaynak tek tek aranarak doğrulandığında, GPT-3.5'in verdiği kaynakların %55'inin, GPT-4'ünkilerin ise %18'inin tamamen UYDURMA olduğu; gerçek olan kaynakların da sırasıyla %43 ve %24'ünde esaslı künye hatası bulunduğu ölçüldü.
  *Projede:* AS-2 (her mevzuat atfının sembolik kural tabanına karşı doğrulanması) + "atıf doğruluğu >=%98" ve "desteksiz iddia <=%1" metriklerinin gerekçesi. Uydurma atıf sorununun sayısal kanıtı: bu yüzden karşılığı olmayan her atıf kullanıcıya ulaşmadan eleniyor.

**[Islam2023]** Islam, P., Kannappan, A., Kiela, D., Qian, R., Scherrer, N., & Vidgen, B. (2023). FinanceBench: A New Benchmark for Financial Question Answering. arXiv:2311.11944.
  https://arxiv.org/abs/2311.11944
  *Bulgu:* Halka açık şirketlerin mali tablolarına dayanan 10.231 soruluk ilk mali soru-cevap denek taşında, erişim sistemiyle desteklenmiş GPT-4-Turbo soruların %81'ini ya yanlış yanıtladı ya da hiç yanıtlayamadı; tüm modellerde halüsinasyon dâhil zayıflıklar kurumsal kullanıma engel bulundu.
  *Projede:* Mali alanda dil modeli güvenilirliği; "neden genel amaçlı bir modele mali beyan hesaplatmıyoruz" sorusunun cevabı. Ayrıca AS-2 ve saha pilotlarının (Tüpraş, Kale Seramik) kurumsal kullanılabilirlik eşiği argümanı.

**[Nay2024]** Nay, J. J., Karamardian, D., Lawsky, S. B., Tao, W., Bhat, M., Jain, R., Lee, A. T., Choi, J. H., & Kasai, J. (2024). Large language models as tax attorneys: a case study in legal capabilities emergence. Philosophical Transactions of the Royal Society A, 382(2270), 20230159.
  https://doi.org/10.1098/rsta.2023.0159
  *Bulgu:* Royal Society dergisinde yayımlanan bu vergi hukuku çalışması, doğru mevzuat metni getirildiğinde ve örneklerle yönlendirildiğinde modellerin yüksek isabete ulaşabildiğini ama "en iyi modellerimiz bile, bu soruları neredeyse kusursuz yanıtlaması beklenen profesyonel bir vergi avukatının altında kalıyor" sonucuna varıyor; yani model uzmanın yerine değil, yanına konmalı.
  *Projede:* AS-1 (denetçi rolünün öğretilebilirliği) + AS-3 (araştırma yönlendirme: doğru mevzuat metnini getirmek) + "kararı insan verir" iş bölümü. Vergi hukuku seçiminin kendisi de projenin alan seçimini akademik olarak meşrulaştırıyor: bu alan otomatik doğrulama hattı kurmaya elverişli olduğu için seçilmiş; Denetci.AI'ın EK-6 oracle yaklaşımıyla birebir aynı mantık.

**[Kamble2025]** Kamble, K., Russak, M., Mozolevskyi, D., Ali, M., Russak, M., & AlShikh, W. (2025). Expect the Unexpected: FailSafe Long Context QA for Finance. arXiv:2502.06329.
  https://arxiv.org/abs/2502.06329
  *Bulgu:* Mali alanda 24 modelin bozulmuş belge ve kusurlu soru senaryolarında sınandığı bu denek taşında, en sağlam model olan OpenAI o3-mini test vakalarının %41'inde bilgi UYDURDU; en uyumlu model Palmyra-Fin-128k ise vakaların %17'sinde sağlam yanıt veremedi; yani sağlamlık ile uydurmama arasında doğrudan bir ödünleşim var.
  *Projede:* Mali alanda güvenilirlik + AS-2 + "belirsiz tutar payı <=%5" metriği. Sağlamlık ile uydurmama arasındaki ödünleşimi gösterir: bir model ne kadar "her soruya cevap veren" ise o kadar çok uyduruyor. Denetci.AI'ın "cevap veremediğinde belirsiz işaretle" tasarımının deneysel gerekçesi.

**[Xu2024]** Xu, Z., Jain, S., & Kankanhalli, M. (2024). Hallucination is Inevitable: An Innate Limitation of Large Language Models. arXiv:2401.11817 (v2, 2025).
  https://arxiv.org/abs/2401.11817
  *Bulgu:* Bu çalışma öğrenme kuramı sonuçlarını kullanarak halüsinasyonun büyük dil modellerinden TAMAMEN YOK EDİLEMEYECEĞİNİ biçimsel olarak kanıtlıyor: modeller hesaplanabilir tüm fonksiyonları öğrenemedikleri için, genel amaçlı problem çözücü olarak kullanıldıklarında kaçınılmaz biçimde dayanaksız iddia üretirler.
  *Projede:* MİMARİ KARARIN gerekçesi: halüsinasyon tamamen yok edilemeyeceğine göre, tutar hesabı modelin DIŞINDA deterministik motorda kalmalı ve modelin her iddiası sembolik kapıdan geçmeli. "Daha büyük model alsak olmaz mıydı?" sorusuna verilecek cevabın teorik dayanağı.

**[Mirzadeh2025]** Mirzadeh, I., Alizadeh, K., Shahrokhi, H., Tuzel, O., Bengio, S., & Farajtabar, M. (2025). GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models. International Conference on Learning Representations (ICLR 2025). arXiv:2410.05229.
  https://arxiv.org/abs/2410.05229
  *Bulgu:* Apple araştırmacıları, ilkokul düzeyi matematik sorularında bile modellerin sadece sayılar değiştirildiğinde başarısının düştüğünü, soruya cevabı hiç etkilemeyen tek bir alakalı görünümlü cümle eklendiğinde ise başarının tüm ileri düzey modellerde %65'e varan oranda çöktüğünü gösterdi; yani modeller gerçek mantıksal hesap yapmıyor, eğitim verisindeki adımları taklit ediyor.
  *Projede:* "Model ASLA tutar hesaplamaz" kuralının EN GÜÇLÜ tek dayanağı. Hesabı deterministik motora, incelemeyi modele vermemizin teknik gerekçesi. Sunumda "hesabı motor yapar" cümlesinin hemen altına konmalı.


## 3. Kanıta bağlılık, atıf doğruluğu ve şema zorlamalı çıktı

*Sembolik doğrulama kapısının (AS-2) ölçüm ve uygulama yöntemleri.*

**[Gao2023ALCE]** Gao, T., Yen, H., Yu, J. & Chen, D. (2023). Enabling Large Language Models to Generate Text with Citations. Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP), 6465-6488.
  https://aclanthology.org/2023.emnlp-main.398/
  *Bulgu:* Atıf kalitesi ölçülebilir bir büyüklüktür ve en iyi modeller bile ürettikleri cümlelerin yarısında tam kanıt desteği sağlayamamaktadır.
  *Projede:* AS-2 ve ANA METRİK (atıf doğruluğu >=%98, desteksiz iddia <=%1): Atıf/kanıt kalitesinin ölçülebilir bir büyüklük olduğu ve mevcut modellerde çok zayıf olduğu. Projenin hedef eşiklerinin neden iddialı ve neden sembolik kapı olmadan ulaşılamaz olduğunu gösterir.

**[Gao2023RARR]** Gao, L., Dai, Z., Pasupat, P., Chen, A., Chaganty, A. T., Fan, Y., Zhao, V., Lao, N., Lee, H., Juan, D.-C. & Guu, K. (2023). RARR: Researching and Revising What Language Models Say, Using Language Models. Proceedings of the 61st Annual Meeting of the ACL (Volume 1: Long Papers), 16477-16508.
  https://aclanthology.org/2023.acl-long.910/
  *Bulgu:* Herhangi bir dil modelinin çıktısı, kanıt aranarak sonradan denetlenebilir ve desteksiz içerik özgün metni bozmadan ayıklanabilir.
  *Projede:* AS-2: Üretilen metnin kanıta bağlanması, DESTEKSİZ içeriğin sonradan tespit edilip ayıklanması. Projedeki 'karşılığı olmayan iddia kullanıcıya ulaşmadan elenir' akışının emsali.

**[Geng2023GCD]** Geng, S., Josifoski, M., Peyrard, M. & West, R. (2023). Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning. Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP), 10932-10952.
  https://aclanthology.org/2023.emnlp-main.674/
  *Bulgu:* Çıktıyı biçimsel bir dilbilgisine zorlayarak üretmek, ince ayar gerektirmeden hem geçerli yapıyı garanti eder hem de göreve özel eğitilmiş modelleri geçebilir.
  *Projede:* AS-2: Çıktının biçimsel bir dilbilgisiyle ZORLANARAK üretilmesi; yani modelin yalnızca sembolik kural tabanında karşılığı olan ifadeleri üretebilmesi. 'Karşılığı olmayan iddia kullanıcıya ulaşmadan elenir' ilkesinin teknik dayanağı.

**[Rebedea2023]** Rebedea, T., Dinu, R., Sreedhar, M. N., Parisien, C. & Cohen, J. (2023). NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications with Programmable Rails. Proceedings of the 2023 Conference on EMNLP: System Demonstrations, 431-445.
  https://aclanthology.org/2023.emnlp-demo.40/
  *Bulgu:* Dil modeli uygulamalarında güvenlik ve denetim, modeli yeniden eğiterek değil, modelden bağımsız ve yorumlanabilir programlanabilir kurallarla çalışma zamanında sağlanır.
  *Projede:* AS-2: Korkuluk (guardrail) mimarisi; modelden BAĞIMSIZ, kullanıcı tanımlı ve YORUMLANABİLİR çalışma-zamanı kuralları. Projedeki doğrulama kapısının endüstriyel emsali.


## 4. Dar kapsamlı küçük modeller, damıtma ve referans kaynaklı (oracle) veri üretimi

*AS-1'in ve EK-6'daki veri üretim yönteminin dayanağı. Sentetik veri riskini gösteren kaynaklar da bilinçli olarak listeye dâhil edilmiştir.*

**[Hsieh2023]** Hsieh, C.-Y., Li, C.-L., Yeh, C.-K., Nakhost, H., Fujii, Y., Ratner, A., Krishna, R., Lee, C.-Y. & Pfister, T. (2023). Distilling Step-by-Step! Outperforming Larger Language Models with Less Training Data and Smaller Model Sizes. Findings of the Association for Computational Linguistics: ACL 2023, 8003-8017.
  https://aclanthology.org/2023.findings-acl.507/
  *Bulgu:* Güçlü bir kaynaktan üretilen gerekçelerle eğitilen 770 milyon parametreli küçük bir model, 540 milyar parametreli bir modeli mevcut verinin yalnızca %80'ini kullanarak geçebilmektedir.
  *Projede:* AS-1 ve ANA METRİK (ince ayarsız temel modele karşı >=15 puan): Dar kapsamlı KÜÇÜK bir modelin, güçlü bir kaynaktan üretilen gerekçelerle eğitildiğinde çok daha büyük modelleri geçebileceği. 1-4 milyar parametreli, GPU'suz, yerel model tercihinin akademik dayanağı.

**[Zelikman2022STaR]** Zelikman, E., Wu, Y., Mu, J. & Goodman, N. D. (2022). STaR: Bootstrapping Reasoning With Reasoning. Advances in Neural Information Processing Systems 35 (NeurIPS 2022).
  https://proceedings.neurips.cc/paper_files/paper/2022/hash/639a9a172c044fbb64175b5fad42e9a5-Abstract-Conference.html
  *Bulgu:* Doğru cevabı bilen bir denetleyici kullanılarak modelin kendi ürettiği gerekçeler otomatik elenip eğitim verisine çevrilebilir; böylece elle etiketlenmiş büyük gerekçe kümesine gerek kalmaz.
  *Projede:* AS-1 ve EK-6 (oracle ile otomatik etiketleme): Eğitim verisinin elle etiketlenmesine gerek olmadığı; DOĞRU CEVABI bilen bir denetleyicinin (bizde deterministik motor) modelin kendi ürettiği gerekçeleri otomatik olarak eleyip eğitim verisine dönüştürebileceği.

**[Zelikman2022]** Zelikman, E., Wu, Y., Mu, J., & Goodman, N. D. (2022). STaR: Bootstrapping Reasoning With Reasoning. Advances in Neural Information Processing Systems 35 (NeurIPS 2022).
  https://papers.nips.cc/paper_files/paper/2022/hash/639a9a172c044fbb64175b5fad42e9a5-Abstract-Conference.html
  *Bulgu:* Model kendi gerekçelerini üretir, ancak yalnızca doğru cevaba ulaşan gerekçeler eğitime alınır; doğrulama kapısı sentetik veriyi güvenilir kılar.
  *Projede:* EK-6'nın çekirdek yöntemsel dayanağı: Model üretimi veri, DOĞRULUK KAPISINDAN geçirilerek (yalnızca doğru sonuca ulaşan gerekçeler) eğitime alınır. Denetci.AI'da bu kapı motorun kendisidir.

**[Singh2024]** Singh, A., Co-Reyes, J. D., Agarwal, R., Anand, A., Patil, P., Liu, P. J., Harrison, J., Lee, J., Xu, K., Parisi, A., et al. (2024). Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models. Transactions on Machine Learning Research (TMLR).
  https://arxiv.org/abs/2312.06585
  *Bulgu:* Doğruluğu makine tarafından sınanabilen görevlerde, filtrelenmiş model üretimi veriyle eğitim insan eliyle yazılmış veriyle eğitimi belirgin biçimde geçti.
  *Projede:* EK-6: Doğrulanabilir ikili geri bildirimle (doğru/yanlış) filtrelenmiş makine üretimi verinin, elle etiketlenmiş insan verisini GEÇEBİLDİĞİ bulgusu. Motorun oracle olarak kullanılmasının gerekçesi.

**[Ratner2017]** Ratner, A., Bach, S. H., Ehrenberg, H., Fries, J., Wu, S., & Ré, C. (2017). Snorkel: Rapid Training Data Creation with Weak Supervision. Proceedings of the VLDB Endowment, 11(3), 269-282.
  https://doi.org/10.14778/3157794.3157797
  *Bulgu:* Elle etiket yerine kural yazarak üretilen etiketlerle eğitilen modeller, elle etiketlenmiş büyük kümelerin başarımına ortalama %3,6 farkla yaklaştı.
  *Projede:* EK-6: Elle etiketleme yerine KURAL/PROGRAM ile etiketleme (zayıf denetim). Denetci.AI'da etiketi deterministik motor koyar; bu, yerleşik ve hakemli bir paradigmadır.

**[Ratner2016]** Ratner, A., De Sa, C., Wu, S., Selsam, D., & Ré, C. (2016). Data Programming: Creating Large Training Sets, Quickly. Advances in Neural Information Processing Systems 29 (NIPS 2016), 3567-3575.
  https://proceedings.neurips.cc/paper/2016/hash/6709e8d64a5f47269ed5cea9f625f7ab-Abstract.html
  *Bulgu:* Kural tabanlı etiketleyicilerin gürültülü çıktıları, bir üretici model altında birleştirilerek güvenilir eğitim kümesine dönüştürülebilir; programatik etiketlemenin matematiksel temeli.
  *Projede:* EK-6'nın teorik temeli: Gürültülü/çelişkili kural tabanlı etiketleyicilerin çıktısı istatistiksel olarak birleştirilip gürültüden arındırılabilir.

**[Zhou2023]** Zhou, C., Liu, P., Xu, P., Iyer, S., Sun, J., Mao, Y., Ma, X., Efrat, A., Yu, P., Yu, L., Zhang, S., Ghosh, G., Lewis, M., Zettlemoyer, L., & Levy, O. (2023). LIMA: Less Is More for Alignment. Advances in Neural Information Processing Systems 36 (NeurIPS 2023).
  https://arxiv.org/abs/2305.11206
  *Bulgu:* Yalnızca 1.000 özenle seçilmiş örnekle yapılan denetimli ince ayar, çok daha büyük veriyle eğitilmiş sistemlere yakın hizalama sağladı: kalite hacimden önemli.
  *Projede:* EK-6: Eğitim verisinde KALİTE hacimden önemlidir; az sayıda ama doğrulanmış örnekle görev davranışı öğretilebilir. Hakemin 'veri kümeniz küçük' itirazına doğrudan cevap.

**[Gunasekar2023]** Gunasekar, S., Zhang, Y., Aneja, J., Mendes, C. C. T., Del Giorno, A., Gopi, S., Javaheripi, M., Kauffmann, P., de Rosa, G., Saarikivi, O., Salim, A., Shah, S., Behl, H. S., Wang, X., Bubeck, S., Eldan, R., Kalai, A. T., Lee, Y. T., & Li, Y. (2023). Textbooks Are All You Need. arXiv:2306.11644.
  https://arxiv.org/abs/2306.11644
  *Bulgu:* 1,3 milyar parametreli phi-1, 'ders kitabı kalitesinde' seçilmiş ve sentetik veriyle eğitilerek kod üretiminde kendinden kat kat büyük modelleri geçti.
  *Projede:* EK-6: Dar kapsamlı, yüksek kaliteli (ve kısmen sentetik) veriyle eğitilen çok küçük modelin dar görevde üstün başarımı.

**[Abdin2024]** Abdin, M., Aneja, J., Awadalla, H., Awadallah, A., Bubeck, S., et al. (Microsoft) (2024). Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone. arXiv:2404.14219.
  https://arxiv.org/abs/2404.14219
  *Bulgu:* 3,8 milyar parametreli phi-3-mini, bir telefona sığacak boyutta olmasına karşın MMLU ölçütünde %69 ile çok daha büyük modellerle yarışıyor.
  *Projede:* AS-1: 1-4 milyar parametre bandının 'oyuncak model' olmadığının en bilinen kanıtı; yerel/kapalı devre çalıştırma iddiasının dayanağı.

**[Belcak2025]** Belcak, P., Heinrich, G., Diao, S., Fu, Y., Dong, X., Muralidharan, S., Lin, Y. C., & Molchanov, P. (2025). Small Language Models are the Future of Agentic AI. arXiv:2506.02153 (NVIDIA Research).
  https://arxiv.org/abs/2506.02153
  *Bulgu:* Ajan sistemlerinde modelden istenen işlerin çoğu dar ve tekrarlı olduğu için küçük dil modelleri yeterli, yapısal olarak daha uygun ve çok daha ekonomiktir.
  *Projede:* AS-1'in konumlandırma gerekçesi: Ajan/iş akışı uygulamalarındaki çağrıların çoğu dar ve tekrarlıdır; bu işler için küçük modeller yeterli, daha uygun ve ekonomiktir.

**[Mitra2023]** Mitra, A., Del Corro, L., Mahajan, S., Codas, A., Simoes, C., Agrawal, S., Chen, X., Razdaibiedina, A., Jones, E., Aggarwal, K., Palangi, H., Zheng, G., Rosset, C., Khanpour, H., & Awadallah, A. (2023). Orca 2: Teaching Small Language Models How to Reason. arXiv:2311.11045.
  https://arxiv.org/abs/2311.11045
  *Bulgu:* 7 ve 13 milyar parametreli modeller, göreve uygun akıl yürütme stratejisini gösteren özel sentetik veriyle eğitildiğinde 5-10 kat büyük modellerle eşleşti ya da onları geçti.
  *Projede:* AS-1: Küçük modele bir ROL ve çözüm stratejisi (ne zaman adım adım düşün, ne zaman doğrudan cevapla) özel üretilmiş veriyle öğretilebilir. 'Denetçi rolü öğretilebilir mi' sorusunun literatürdeki en yakın karşılığı.

**[Wang2023]** Wang, Y., Kordi, Y., Mishra, S., Liu, A., Smith, N. A., Khashabi, D., & Hajishirzi, H. (2023). Self-Instruct: Aligning Language Models with Self-Generated Instructions. Proceedings of the 61st Annual Meeting of the ACL (Volume 1: Long Papers), 13484-13508.
  https://doi.org/10.18653/v1/2023.acl-long.754
  *Bulgu:* Elle yazılmış yönerge verisi yerine otomatik üretilen yönerge verisiyle yapılan ince ayar, insan verisine yakın başarım verdi.
  *Projede:* EK-6: Makine üretimi yönerge/görev verisiyle ince ayarın yerleşik ve hakemli bir yöntem olduğunu gösterir; elle etiketlemeden kaçınmanın literatürdeki karşılığı.

**[Gudibande2023]** Gudibande, A., Wallace, E., Snell, C., Geng, X., Liu, H., Abbeel, P., Levine, S., & Song, D. (2023). The False Promise of Imitating Proprietary LLMs. arXiv:2305.15717.
  https://arxiv.org/abs/2305.15717
  *Bulgu:* Büyük modelin çıktısını taklit etmek, taklit verisinde iyi temsil edilmeyen görevlerde gerçek yetenek kazandırmıyor; bu yüzden kapsam dar, veri görev-özgü olmalı.
  *Projede:* AS-1'in kapsam sınırı gerekçesi: Büyük modelin genel yeteneklerini taklit etmek işe yaramaz; kazanç ancak taklit verisinin YOĞUN OLARAK kapsadığı dar görevlerde elde edilir. Denetci.AI'nın 'dar kapsam' tercihinin akademik dayanağı.

**[Shumailov2024]** Shumailov, I., Shumaylov, Z., Zhao, Y., Papernot, N., Anderson, R., & Gal, Y. (2024). AI models collapse when trained on recursively generated data. Nature, 631(8022), 755-759.
  https://doi.org/10.1038/s41586-024-07566-y
  *Bulgu:* Model kendi ürettiği veriyle özyinelemeli eğitilirse dağılımın kuyrukları kaybolur ve model geri dönüşsüz biçimde çöker.
  *Projede:* EK-6 savunması (hakemin 'sentetik veriyle eğitim sağlam mı' sorusuna cevabın ilk yarısı): Veri MODELİN KENDİSİNDEN üretilirse çöküş kaçınılmazdır; bu yüzden Denetci.AI verisi modelden değil, doğrulanmış deterministik motordan üretilir.

**[Gerstgrasser2024]** Gerstgrasser, M., Schaeffer, R., Dey, A., Rafailov, R., Sleight, H., Hughes, J., Korbak, T., Agrawal, R., Pai, D., Gromov, A., Roberts, D. A., Yang, D., Donoho, D. L., & Koyejo, S. (2024). Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data. arXiv:2404.01413.
  https://arxiv.org/abs/2404.01413
  *Bulgu:* Sentetik veri gerçek veriyi ikame etmek yerine biriktirilerek eklendiğinde model çöküşü gözlenmiyor.
  *Projede:* EK-6 savunmasının ikinci yarısı: Sentetik veri gerçek veriyi DEĞİŞTİRMEK yerine ona EKLENİRSE çöküş ortadan kalkar. Denetci.AI'da gerçek YMM teyitli regresyon çapası (96 -> 140 vaka) tam olarak bu rolü oynar.


## 5. Grafik işlemcisiz yerel çıkarım ve verimli ince ayar

*Kapalı devre, GPU'suz çalışma vaadinin teknik dayanağı.*

**[Hu2022]** Hu, E. J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Wang, L., & Chen, W. (2022). LoRA: Low-Rank Adaptation of Large Language Models. International Conference on Learning Representations (ICLR 2022).
  https://arxiv.org/abs/2106.09685
  *Bulgu:* Donmuş ağırlıklara düşük ranklı matrisler eklenerek eğitilebilir parametre sayısı 10.000 kata kadar azaltılıyor, başarım tam ince ayarla eş düzeyde kalıyor.
  *Projede:* AS-1 uygulanabilirlik: 39 adam-ay / 7 M TL bütçeyle eğitim gerçekçi mi? Parametre-verimli ince ayar, eğitilebilir parametre sayısını binlerce kat azaltır.

**[Dettmers2023]** Dettmers, T., Pagnoni, A., Holtzman, A., & Zettlemoyer, L. (2023). QLoRA: Efficient Finetuning of Quantized LLMs. Advances in Neural Information Processing Systems 36 (NeurIPS 2023).
  https://arxiv.org/abs/2305.14314
  *Bulgu:* 4-bit nicemlenmiş model üzerinde adaptör eğitimi, tam hassasiyetli ince ayarın başarımını koruyarak bellek ihtiyacını tek bir makineye indiriyor.
  *Projede:* AS-1 uygulanabilirlik + EK-6: 1-4 milyar parametreli modelin mütevazı donanımda ince ayarı mümkün; nicemlenmiş model üzerinde adaptör eğitimi 16-bit başarımını korur.

**[Frantar2023]** Frantar, E., Ashkboos, S., Hoefler, T., & Alistarh, D. (2023). OPTQ (GPTQ): Accurate Post-Training Quantization for Generative Pre-trained Transformers. 11th International Conference on Learning Representations (ICLR 2023), Kigali, Rwanda.
  https://arxiv.org/abs/2210.17323
  *Bulgu:* Eğitim sonrası nicemleme, model ağırlıklarını 3-4 bite sıkıştırırken kayda değer doğruluk kaybı yaratmıyor; küçük belleğe sığdırmanın standart yolu.
  *Projede:* GPU'suz / 16 GB RAM hedefi: Eğitim sonrası nicemleme ile model ağırlıkları 3-4 bite indirilirken doğruluk kaybı ihmal edilebilir düzeyde kalır.

**[Wei2025]** Wei, J., Cao, S., Cao, T., Ma, L., Wang, L., Zhang, Y., & Yang, M. (2025). T-MAC: CPU Renaissance via Table Lookup for Low-Bit LLM Deployment on Edge. Proceedings of the Twentieth European Conference on Computer Systems (EuroSys '25).
  https://doi.org/10.1145/3689031.3696099
  *Bulgu:* Düşük bitli dil modelleri CPU'da tablo-arama yöntemiyle çalıştırıldığında yaygın çözüme göre 4 kata kadar hızlanıyor; Raspberry Pi 5 gibi zayıf bir cihazda bile saniyede 11 kelime parçası üretiliyor.
  *Projede:* ANA METRİK: 'GPU'suz, 16 GB RAM makinede bulgu başına <=30 sn' hedefinin teknik olarak gerçekçi olduğunun hakemli sistem konferansı kanıtı.

**[Alizadeh2024]** Alizadeh, K., Mirzadeh, I., Belenko, D., Khatamifard, S. K., Cho, M., Del Mundo, C. C., Rastegari, M., & Farajtabar, M. (2024). LLM in a flash: Efficient Large Language Model Inference with Limited Memory. Proceedings of the 62nd Annual Meeting of the ACL (Volume 1: Long Papers), Bangkok, Thailand.
  https://aclanthology.org/2024.acl-long.678/
  *Bulgu:* Model parametreleri diskte tutulup talep üzerine belleğe alınarak, mevcut RAM'in iki katı büyüklükte modeller sınırlı bellekli cihazlarda çalıştırılabiliyor.
  *Projede:* '16 GB RAM, GPU'suz kapalı devre makine' kısıtının aşılabilirliği: Bellek sınırlı cihazlarda büyük modelleri çalıştırma yöntemleri hakemli ana akım literatürde mevcut.


## 6. Kök-neden teşhisi, abdüktif çıkarım ve belirsizliğin raporlanması

*AS-3'ün zemini: aynı fark görüntüsünü birden çok neden üretebilir; ayırt edilemeyen durum "belirsiz" olarak raporlanır.*

**[Reiter1987]** Reiter, R. (1987). A theory of diagnosis from first principles. Artificial Intelligence, 32(1), 57–95.
  https://doi.org/10.1016/0004-3702(87)90062-2
  *Bulgu:* Teşhis, sistemin nasıl davranması gerektiğini anlatan modelle gerçek gözlemler arasındaki çelişkiyi giderebilecek en küçük 'sorunlu bileşen' kümelerinin TÜMÜNÜN hesaplanmasıdır; tek bir tahmin değil, eksiksiz bir aday listesi.
  *Projede:* AS-3; Sembolik katmanın hipotez kümesini EKSİKSİZ üretmesi iddiasının kuramsal temeli. Projenin 'fark görüntüsünü açıklayabilecek tüm kök-neden adaylarını üret' kurgusu, Reiter'in çelişki (conflict) kümelerinden minimal teşhisleri hesaplama prosedürünün birebir karşılığıdır. Ayrıca AS-2'nin 'kural tabanından türeyen gerekçe' fikrini de destekler.

**[deKleerWilliams1987]** de Kleer, J., & Williams, B. C. (1987). Diagnosing multiple faults. Artificial Intelligence, 32(1), 97–130.
  https://doi.org/10.1016/0004-3702(87)90063-4
  *Bulgu:* Aynı anda birden çok şeyin bozuk olabileceğini kabul ederek aday açıklamalar üretir; sonra bilgi kuramını (entropi) kullanarak 'adayları en çok ayrıştıracak bir sonraki ölçüm hangisi?' sorusunu kendisi cevaplar.
  *Projede:* AS-3'ün İKİ ayrı iddiasını birden destekler: (a) aynı belirti tablosunu birden çok eşzamanlı kök neden üretebilir (çoklu hata teşhisi), (b) sistem, adaylar arasında ayrım yapacak BİR SONRAKİ ÖLÇÜMÜ kendisi önerir; bu, projenin 'hangi belgeyi istemeli' araştırma yönlendirme görevinin (>=%70 isabet metriği) doğrudan akademik atasıdır.

**[ConsoleTorasso1991]** Console, L., & Torasso, P. (1991). A spectrum of logical definitions of model-based diagnosis. Computational Intelligence, 7(3), 133–141.
  https://doi.org/10.1111/j.1467-8640.1991.tb00388.x
  *Bulgu:* Teşhis iki ayrı mantıkla kurulabilir: gözlemle ÇELİŞMEMEYİ arayan tutarlılık tabanlı teşhis ile gözlemi fiilen AÇIKLAMAYI şart koşan abdüksiyon tabanlı teşhis; ve bu ikisi aslında tek bir çerçevenin iki ucudur.
  *Projede:* AS-3; Tutarlılık tabanlı (consistency-based) ve abdüksiyon tabanlı (abduction-based) teşhis ayrımının kanonik kaynağı. Denetci.AI'nin motoru 'beyan mevzuatla tutarsız mı?' diye sorar (tutarlılık tabanlı), kök-neden katmanı ise 'bu farkı ne AÇIKLAR?' diye sorar (abdüksiyon tabanlı). Bu makale ikisinin tek çerçevenin iki ucu olduğunu gösterir; projenin iki aşamalı kurgusunu meşrulaştırır.

**[Bylander1991]** Bylander, T., Allemang, D., Tanner, M. C., & Josephson, J. R. (1991). The computational complexity of abduction. Artificial Intelligence, 49(1–3), 25–60.
  https://doi.org/10.1016/0004-3702(91)90005-5
  *Bulgu:* En iyi açıklamayı bulmak (abdüksiyon) genel hâlinde hesaplama açısından zor bir problemdir; bu yüzden tüm adayları tek tek tartmak yerine akıllı bir sıralama katmanı gerekir.
  *Projede:* AS-3; NEDEN nöral bir sıralama katmanına ihtiyaç duyulduğunun gerekçesi. Abdüksiyon genel hâlinde NP-zordur; yani 'en iyi açıklamayı' saf sembolik arama ile makul sürede bulmak garanti değildir. Bu, projenin '16 GB RAM, GPU'suz, bulgu başına <=30 sn' performans hedefiyle doğrudan bağlantılıdır: sembolik katman adayları üretir, öğrenilmiş sıralama katmanı arama uzayını daraltır.

**[Sampath1995]** Sampath, M., Sengupta, R., Lafortune, S., Sinnamohideen, K., & Teneketzis, D. (1995). Diagnosability of discrete-event systems. IEEE Transactions on Automatic Control, 40(9), 1555–1575.
  https://doi.org/10.1109/9.412626
  *Bulgu:* Bir arızanın mevcut gözlemlerden kesin olarak teşhis edilip edilemeyeceği, sistemin yapısına bağlı ve önceden sınanabilir bir özelliktir; bazı nedenler gözlemle ilkesel olarak ayırt EDİLEMEZ.
  *Projede:* AS-3'ün TANIMLANABİLİRLİK (identifiability) problemi. Bu makale 'teşhis edilebilirlik' (diagnosability) kavramını resmîleştirir: bir arızanın eldeki gözlemlerle kesin olarak teşhis edilip edilemeyeceği, sistemin kendi yapısına bağlı ve ÖNCEDEN SINANABİLİR bir özelliktir. Projenin 'bazı fark görüntüleri ilkesel olarak ayırt edilemez, bunu dürüstçe raporlarız' duruşunu akademik olarak sağlamlaştırır ve 'belirsiz tutar payı <=%5' metriğini kurama bağlar.

**[Poole1993]** Poole, D. (1993). Probabilistic Horn abduction and Bayesian networks. Artificial Intelligence, 64(1), 81–129.
  https://doi.org/10.1016/0004-3702(93)90061-F
  *Bulgu:* Kurallar hipotezleri üretir, olasılıklar onları sıralar: mantıksal hipotez üretimi ile olasılıksal derecelendirme tek ve tutarlı bir çerçevede birleştirilebilir.
  *Projede:* AS-3'ün 'sembolik katman üretir, nöral katman SIRALAR' iş bölümünün kuramsal öncülü. Poole, mantıksal (Horn kuralı tabanlı) hipotez üretimi ile olasılıksal derecelendirmenin aynı çatı altında tutarlı biçimde birleştirilebileceğini gösterir; projenin mimarisi bu birleşimin modern, öğrenilmiş sıralayıcılı bir versiyonudur.

**[Heckerman1995]** Heckerman, D., Breese, J. S., & Rommelse, K. (1995). Decision-theoretic troubleshooting. Communications of the ACM, 38(3), 49–57.
  https://doi.org/10.1145/203330.203341
  *Bulgu:* Arıza giderme bir karar problemidir: hangi gözlemin isteneceği, beklenen bilgi kazancı ile o gözlemin maliyeti tartılarak seçilir.
  *Projede:* Projenin ARAŞTIRMA YÖNLENDİRME görevinin (hangi belge istenmeli) maliyet-fayda boyutu. Hangi gözlemin yapılacağı, beklenen bilgi kazancı ile o gözlemin maliyeti tartılarak seçilir. Denetçi bağlamında 'mükellefe hangi belgeyi sormak en az yük ile en çok farkı çözer' sorusunun doğrudan karşılığı; pilotlardaki 'kurulumdan ilk rapora <=1 saat' vaadini de besler.

**[deKleerMackworthReiter1992]** de Kleer, J., Mackworth, A. K., & Reiter, R. (1992). Characterizing diagnoses and systems. Artificial Intelligence, 56(2–3), 197–222.
  https://doi.org/10.1016/0004-3702(92)90027-U
  *Bulgu:* Sadece 'en küçük' açıklamaları saklamak genel olarak yetersizdir; aday kümesini doğru ve eksiksiz temsil etmek için çekirdek teşhis kavramı gerekir.
  *Projede:* AS-3'ün 'hipotez kümesi eksiksiz üretilir' iddiasının İNCE AYARI. Makale, yalnızca minimal (en küçük) teşhisleri saklamanın genel hâlde yetersiz olduğunu gösterir ve 'çekirdek teşhis' (kernel diagnosis) kavramını önerir. Hakem 'eksiksizlik' iddiasını sorgularsa verilecek teknik cevap buradadır: eksiksizlik hangi temsil altında sağlanıyor.

**[Shchekotykhin2012]** Shchekotykhin, K., Friedrich, G., Fleiss, P., & Rodler, P. (2012). Interactive ontology debugging: Two query strategies for efficient fault localization. Journal of Web Semantics, 12–13, 88–103.
  https://doi.org/10.1016/j.websem.2011.12.006
  *Bulgu:* Birden çok aday açıklama kaldığında sistem, kullanıcıya cevabı adayları en çok eleyecek soruyu sorar; böylece doğru teşhise en az soruyla ulaşılır.
  *Projede:* AS-3 + araştırma yönlendirme metriği (>=%70 isabet). Bu çalışma, model tabanlı teşhisi BİLGİ TABANLARINA (kural/ontoloji) taşır; ki Denetci.AI'nin sembolik kural tabanı tam olarak budur, devre değil. Birden çok aday teşhis kaldığında sisteme 'kullanıcıya sorulacak en ayırt edici soruyu seç' yeteneği kazandırır; projenin 'kullanıcıdan kanıt isteyen denetçi' davranışının en yakın yayımlanmış örneğidir.

**[Chow1970]** Chow, C. K. (1970). On optimum recognition error and reject tradeoff. IEEE Transactions on Information Theory, 16(1), 41–46.
  https://doi.org/10.1109/TIT.1970.1054406
  *Bulgu:* Bir sisteme 'kararsızım' deme hakkı tanındığında, hata oranı ile cevaplanan vaka oranı arasında matematiksel olarak en iyi denge kurulabilir.
  *Projede:* 'Belirsiz tutar payı <=%5' metriğinin klasik kuramsal temeli. Reddetme seçeneğinin (reject option) matematiksel kurucu makalesi: hata oranı ile cevaplanan vaka oranı arasındaki en iyi denge analitik olarak tanımlanabilir. Denetim bağlamında 'kararsız kalınan tutarı gizlemek yerine ölçülü biçimde ayırmak' ilkesini 56 yıllık bir zemine oturtur.

**[GeifmanElYaniv2017]** Geifman, Y., & El-Yaniv, R. (2017). Selective classification for deep neural networks. In Advances in Neural Information Processing Systems 30 (NIPS 2017), 4878–4887.
  https://proceedings.neurips.cc/paper_files/paper/2017/hash/4a8423d5e91fda00bb7e46540e2b0cf1-Abstract.html
  *Bulgu:* Sinir ağına istenen risk düzeyi baştan verilip, o riski yüksek olasılıkla garanti edecek şekilde belirsiz vakaları reddetmesi (cevaplamaması) sağlanabilir; çekimserlik ölçülebilir bir güvence aracıdır.
  *Projede:* Projenin 'belirsiz tutar payı <=%5' ve 'desteksiz iddia <=%1' metriklerinin yöntemsel karşılığı. Modelin susma/çekimser kalma hakkı bir zaafiyet değil, İSTENEN RİSK DÜZEYİNİ GARANTİ ETMEK için mühendislik aracıdır. Denetçi rolünde 'emin değilim, şu belgeyi isterim' demek tam olarak budur.

**[Bhagavatula2020]** Bhagavatula, C., Le Bras, R., Malaviya, C., Sakaguchi, K., Holtzman, A., Rashkin, H., Downey, D., Yih, W., & Choi, Y. (2020). Abductive commonsense reasoning. In International Conference on Learning Representations (ICLR 2020).
  https://arxiv.org/abs/1908.05739
  *Bulgu:* Abdüktif akıl yürütme için kurulan ilk büyük dil veri kümesinde en iyi model %68,9'da kalırken insan %91,4 başarı gösterdi; 'en makul açıklamayı seçmek' dil modelleri için hâlâ zor bir iştir.
  *Projede:* AS-3'ün nöral katmanına dair GERÇEKÇİ BEKLENTİ ayarı ve ölçüm geleneği. Abdüktif akıl yürütme için ilk büyük ölçekli dil veri kümesini (ART) ve iki ölçülebilir görevi tanımlar. Bulgusu projenin tasarım tercihini haklı çıkarır: dil modelleri 'en makul açıklamayı seçme'de insanın belirgin şekilde gerisindedir; bu yüzden Denetci.AI'de model TEK BAŞINA karar vermez, sembolik doğrulama kapısından geçer ve kararı insan verir.

**[Ahmed2023]** Ahmed, T., Ghosh, S., Bansal, C., Zimmermann, T., Zhang, X., & Rajmohan, S. (2023). Recommending root-cause and mitigation steps for cloud incidents using large language models. In Proceedings of the 45th International Conference on Software Engineering (ICSE 2023), 1737–1749.
  https://doi.org/10.1109/ICSE48619.2023.00149
  *Bulgu:* Gerçek bulut arıza kayıtlarıyla yapılan büyük ölçekli değerlendirmede dil modelleri kök-neden önerisinde mühendise anlamlı katkı sağladı, ancak tek başına karar verecek düzeyde değildi.
  *Projede:* AS-3'ün nöral katmanının ENDÜSTRİYEL güncelliği: kök-neden önerisinde dil modeli kullanmak kurgusal değil, büyük ölçekli gerçek olay verisiyle sınanmış bir yaklaşımdır. Aynı zamanda projenin 'kararı insan verir' ilkesini destekler; bu çalışmada da modeller yardımcıdır, yerine geçici değil. Hakem heyetindeki sektör temsilcisine güncellik göstermek için yararlı, ana tez slaytı için zorunlu değil.


## 7. Mevzuatın bildirimsel kurala dökülmesi (rules as code)

*AS-4'ün birinci yarısı: bir teşvik rejiminin ne kadarı kod yazılmadan kural dosyasıyla ifade edilebilir?*

**[Sergot1986]** Sergot, M. J., Sadri, F., Kowalski, R. A., Kriwaczek, F., Hammond, P., & Cory, H. T. (1986). The British Nationality Act as a logic program. Communications of the ACM, 29(5), 370-386.
  https://doi.org/10.1145/5689.5920
  *Bulgu:* 1986'da Imperial College ekibi İngiliz Vatandaşlık Kanunu'nun tamamını mantık programına çevirerek bir kanunun doğrudan çalıştırılabilir kurala dönüştürülebileceğini gösterdi; bizim 5746/4691 kural tabanımızın 40 yıllık atası budur.
  *Projede:* AS-4 ve projenin genel tezi: bir kanunun madde madde, bildirimsel (declarative) kurallara dökülüp bilgisayarda çalıştırılabileceğinin klasik kanıtı. "Deterministik motor" fikrinin akademik atası.

**[Kowalski1992]** Kowalski, R. A. (1992). Legislation as Logic Programs. In G. Comyn, N. E. Fuchs & M. J. Ratcliffe (Eds.), Logic Programming in Action (LPSS 1992), Lecture Notes in Computer Science, vol. 636 (pp. 203-230). Springer, Berlin/Heidelberg.
  https://doi.org/10.1007/3-540-55930-2_15
  *Bulgu:* Kowalski, mevzuatın büyük bölümünün mantık programı olarak yazılabileceğini ama her hükmün yazılamayacağını göstererek biçimselleştirmenin nerede durması gerektiğini tartışır.
  *Projede:* AS-4: mevzuatın kural olarak ifade edilebilirliği ve bunun SINIRLARI (istisna, yorum gerektiren açık uçlu kavramlar). Projedeki "kaçış kancası <=3" metriğinin kuramsal zemini.

**[Merigoux2021Catala]** Merigoux, D., Chataing, N. & Protzenko, J. (2021). Catala: A Programming Language for the Law. Proceedings of the ACM on Programming Languages, 5(ICFP), Article 77, 1-29.
  https://doi.org/10.1145/3473582
  *Bulgu:* Vergi mevzuatı gibi hesap tarif eden hukuk metinleri, madde madde izlenebilir ve biçimsel olarak doğrulanmış yürütülebilir koda sistematik biçimde çevrilebilir.
  *Projede:* ÇEKİRDEK TEZİN DETERMİNİSTİK MOTOR AYAĞI ve AS-4'e köprü: Mevzuat metninin sistematik biçimde YÜRÜTÜLEBİLİR ve biçimsel olarak doğrulanmış koda çevrilebileceği; vergi mevzuatı üzerinde uygulanmış olması.

**[Merigoux2021Mlang]** Merigoux, D., Monat, R., & Protzenko, J. (2021). A Modern Compiler for the French Tax Code. Proceedings of the 30th ACM SIGPLAN International Conference on Compiler Construction (CC '21), 71-82. ACM.
  https://doi.org/10.1145/3446804.3446850
  *Bulgu:* Fransız Maliye'sinin gelir vergisi hesabı, 48 dosya ve 92.000 satırlık 'M' adlı özel bir kural dilinde yazılıdır ve her vergi yılı için ayrı bir sürüm olarak yayımlanır; devlet ölçeğinde deterministik hesap motorunun somut örneği.
  *Projede:* AS-4 ve projenin "hesabı motor yapar" iş bölümü: gerçek bir devlet vergi hesaplama motorunun deterministik, dile dökülmüş kurallardan oluştuğunun ve her vergi yılının AYRI BİR SÜRÜM olduğunun kanıtı.

**[Sutherland2013]** Sutherland, H., & Figari, F. (2013). EUROMOD: the European Union tax-benefit microsimulation model. International Journal of Microsimulation, 6(1), 4-26.
  https://doi.org/10.34196/ijm.00075
  *Bulgu:* AB'nin 27 ülkeyi kapsayan EUROMOD vergi-yardım mikrosimülasyon altyapısı, kuralları her politika yılı için ayrı ve modüler biçimde saklar; oran/limit değişince kod yeniden yazılmaz; bizim parametre/şema ayrımımızın yerleşik örneği.
  *Projede:* AS-4'ün ÜÇ EKSENİNDEN İKİSİ: "parametre" ile "hesap şeması" ayrımı. EUROMOD kuralları her politika yılı için ayrı saklar ve parametre değişikliği kod değişikliği gerektirmez.

**[MohunRoberts2020]** Mohun, J., & Roberts, A. (2020). Cracking the code: Rulemaking for humans and machines. OECD Working Papers on Public Governance, No. 42. OECD Publishing, Paris.
  https://doi.org/10.1787/3afe6ba5-en
  *Bulgu:* OECD'nin resmi çalışma raporu, mevzuatın makine tarafından okunabilir sürümünü üretmeyi (Rules as Code) bir kamu yönetimi reformu olarak tanımlar ve kodlanmış kuralların sürümlerinin nasıl yönetileceğini çözülmemiş bir soru olarak işaret eder.
  *Projede:* AS-4: "Rules as Code / mevzuatın koda dökülmesi" alanının uluslararası kurumsal çerçevesi; OpenFisca dahil ülke örnekleri. Ayrıca kodlanmış kuralların SÜRÜM YÖNETİŞİMİNİN açık bir problem olduğunu OECD'nin kendisi söylüyor.

**[Lawsky2017]** Lawsky, S. B. (2017). A Logic for Statutes. Florida Tax Review, 21(1), 60-80.
  https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3088206
  *Bulgu:* Vergi hukuku profesörü Lawsky, vergi kanunlarının "kural ve onu bozan istisna" yapısında olduğunu, bu yüzden düz mantıkla değil varsayılan (default) mantıkla modellenmesi gerektiğini gösterir.
  *Projede:* AS-4 ve AS-2: vergi mevzuatı klasik çıkarım (deduction) değil, SAVUNULABİLİR (defeasible) akıl yürütmedir; kural + istisna + öncelik kuralı yapısındadır. Bizim kural tabanımızın neden öncelikli/istisnalı kurgulanması gerektiğinin hukuki gerekçesi.

**[Forgy1982]** Forgy, C. L. (1982). Rete: A fast algorithm for the many pattern/many object pattern match problem. Artificial Intelligence, 19(1), 17-37.
  https://doi.org/10.1016/0004-3702(82)90020-0
  *Bulgu:* Forgy'nin Rete algoritması, yüzlerce kuralın binlerce veri kalemiyle eşleştirilmesini pratik hale getirmiş ve bugünkü tüm kural motorlarının temelini oluşturmuştur; bizim kural motorumuz da bu aileden.
  *Projede:* AS-4: bildirimsel kural temsilinin çalıştırılabilirliği ve başarımı. "16 GB RAM, GPU'suz makinede bulgu başına <=30 sn" hedefinin motor tarafındaki teknik dayanağı.

**[Athan2013]** Athan, T., Boley, H., Governatori, G., Palmirani, M., Paschke, A., & Wyner, A. (2013). OASIS LegalRuleML. Proceedings of the Fourteenth International Conference on Artificial Intelligence and Law (ICAIL '13), 3-12. ACM.
  https://doi.org/10.1145/2514601.2514603
  *Bulgu:* OASIS LegalRuleML, hukuki kuralları makine okunur biçimde temsil ederken her kuralın hangi mevzuat kaynağından geldiğini, hangi tarihte geçerli olduğunu ve hangi istisnayla bozulabileceğini birlikte kaydeden açık bir standarttır.
  *Projede:* AS-2 ve AS-4: uluslararası bir STANDARDIN kural ile kaynak mevzuat maddesi arasındaki bağı, zamanı ve savunulabilirliği açıkça temsil etmesi. Bizim "sembolik doğrulama kapısı" ve "atıf doğruluğu >=%98" metriğimizin standart karşılığı.

**[Athan2015]** Athan, T., Governatori, G., Palmirani, M., Paschke, A., & Wyner, A. (2015). LegalRuleML: Design Principles and Foundations. In Reasoning Web (Lecture Notes in Computer Science, vol. 9203, pp. 151-188). Springer.
  https://doi.org/10.1007/978-3-319-21768-0_6
  *Bulgu:* LegalRuleML'in tasarım ilkelerini ayrıntılandıran bu çalışma, hukuki kuralda zaman ve istisna bilgisinin nasıl yapılandırıldığını teknik olarak açıklar.
  *Projede:* AS-2/AS-4 derinleştirme: LegalRuleML'in zaman, deontik operatör ve savunulabilirlik tasarım ilkelerinin ayrıntılı anlatımı (teknik ekte kullanılabilir).

**[Governatori2010]** Governatori, G., & Rotolo, A. (2010). Changing legal systems: legal abrogations and annulments in Defeasible Logic. Logic Journal of the IGPL, 18(1), 157-194.
  https://doi.org/10.1093/jigpal/jzp075
  *Bulgu:* Governatori ve Rotolo, hukuki değişimi modellemek için iki ayrı zaman ekseni gerektiğini gösterir: kuralın ne zaman geçerli olduğu ve hukuk sisteminin o bilgiyi ne zaman edindiği; bizim üç eksenli sürümlememizin doğrudan kuramsal dayanağı.
  *Projede:* AS-4'ÜN ÇEKİRDEK KAYNAĞI: hukuk sisteminde İKİ AYRI ZAMAN ÇİZGİSİ olduğunu (kuralın kendi geçerlilik zamanı + sistemin zaman içinde değişmesi) biçimsel olarak modeller; yürürlükten kaldırma ile iptali (geçmişe etkili) ayırır.

**[PrakkenSartor2015]** Prakken, H., & Sartor, G. (2015). Law and logic: A review from an argumentation perspective. Artificial Intelligence, 227, 214-245.
  https://doi.org/10.1016/j.artint.2015.06.005
  *Bulgu:* Prakken ve Sartor'un Artificial Intelligence dergisindeki derlemesi, hukukun mantıkla temsilinde 40 yıllık birikimi; zaman, değişim ve istisna dahil; tek makalede toplar.
  *Projede:* AS-2 ve AS-4: hukuk + mantık alanının otoriter derleme makalesi; deontik kavramlar, hukuki ontolojiler ve ZAMAN/DEĞİŞİM temsilini bir arada ele alır. Heyetteki akademisyene alanın olgunluğunu gösterir.

**[Grimmelmann2022]** Grimmelmann, J. (2022). Programming Languages and Law: A Research Agenda. Proceedings of the 2022 Symposium on Computer Science and Law (CSLAW '22), 155-165. ACM.
  https://doi.org/10.1145/3511265.3550447
  *Bulgu:* Cornell hukuk profesörü Grimmelmann, hukuk metinleri ile programlama dilleri arasındaki paralelliği ve ayrımı bir araştırma gündemi olarak tanımlar; alanın akademik meşruiyetini gösteren güncel referans.
  *Projede:* Sunumun çerçevelemesi: "mevzuatı koda dökmek" saygın ve kurumsallaşmış bir araştırma alanıdır. Hukuk ile programlama dilleri arasındaki benzerlik ve farkları (yorum, istisna, belirsizlik) sistematik olarak listeler.

**[Guintchev2025]** Guintchev, P., Joosten, J. J., Santiago Fernández, S., Sancho Adamson, E., Solé Sánchez, A., & Soria Heredia, M. (2025). Specification languages for computational laws versus basic legal principles. arXiv preprint arXiv:2503.09129.
  https://doi.org/10.48550/arXiv.2503.09129
  *Bulgu:* Barcelona ekibi, mevzuatı biçimsel dile çevirmenin belirsizliği azalttığını ama anlaşılabilirlik ve gerekçelendirme gibi temel hukuk ilkeleriyle gerilim yarattığını gösterir; bizim 'kaçış kancası <=3' sınırımızın neden kaçınılmaz olduğunun kanıtı.
  *Projede:* AS-4'ÜN İKİNCİ YARISI: bir teşvik rejiminin bildirimsel kural olarak İFADE EDİLEBİLİRLİK SINIRI. Biçimsel dillerin doğal dile göre kesinlik kazandırdığını ama uzman olmayanlar için anlaşılmazlık ve gerekçenin kaybı gibi bedeller getirdiğini AB ulaştırma mevzuatı üzerinden gösterir.


## 8. Zamansal sürümleme: geçerlilik zamanı, işlem zamanı ve bilgi tarihi

*AS-4'ün ikinci yarısı: parametre, hesap şeması ve bilgi tarihi eksenlerinde sürümleme; kapanmış bir dönemin o günkü bilgi durumuyla yeniden üretilmesi.*

**[SnodgrassAhn1986]** Snodgrass, R. T., & Ahn, I. (1986). Temporal Databases. IEEE Computer, 19(9), 35-42.
  https://doi.org/10.1109/MC.1986.1663327
  *Bulgu:* Snodgrass ve Ahn, bir verinin 'gerçekte ne zaman doğru olduğu' ile 'sisteme ne zaman girildiği' bilgisinin iki ayrı zaman olduğunu tanımlar; bizim 'bilgi tarihi' eksenimiz tam olarak budur.
  *Projede:* AS-4'ün ÜÇÜNCÜ EKSENİ ("bilgi tarihi"): geçerlilik zamanı (valid time) ile işlem zamanı (transaction time) ayrımını literatüre sokan kurucu makale.

**[Jensen1998]** Jensen, C. S., Dyreson, C. E., Böhlen, M., Clifford, J., Elmasri, R., Gadia, S. K., Grandi, F., et al. (1998). The Consensus Glossary of Temporal Database Concepts - February 1998 Version. In Temporal Databases: Research and Practice, Lecture Notes in Computer Science, vol. 1399 (pp. 367-405). Springer.
  https://doi.org/10.1007/BFb0053710
  *Bulgu:* 26 araştırmacının uzlaştığı bu sözlük, zamansal veri yönetiminin terimlerini (geçerlilik zamanı, işlem zamanı, çift zamanlı kayıt) standart biçimde tanımlar.
  *Projede:* AS-4: "bitemporal", "valid time", "transaction time", "as-of sorgu" terimlerinin uzlaşılmış, atıf yapılabilir tanımları. Sunumda jargonu açarken tanım kaynağı olarak verilebilir.

**[Kulkarni2012]** Kulkarni, K., & Michels, J.-E. (2012). Temporal features in SQL:2011. ACM SIGMOD Record, 41(3), 34-43.
  https://doi.org/10.1145/2380776.2380786
  *Bulgu:* Uluslararası SQL:2011 standardı, geçerlilik zamanı ve sistem sürümü tablolarını doğrudan dilin içine almıştır; yani 'o günkü kuralla yeniden hesapla' yeteneği standartlaşmış bir veritabanı özelliğidir.
  *Projede:* AS-4: üç eksenli sürümlemenin STANDART ve UYGULANABİLİR olduğunun kanıtı; ISO SQL standardı 2011'den beri uygulama zamanı (valid time) ve sistem sürümlü (transaction time) tabloları içerir. "Egzotik bir icat değil, standart" mesajı.

**[Snodgrass1999]** Snodgrass, R. T. (1999). Developing Time-Oriented Database Applications in SQL. Morgan Kaufmann, San Francisco, 504 s. ISBN 1-55860-436-7.
  https://www2.cs.arizona.edu/~rts/tdbbook.pdf
  *Bulgu:* Alanın kurucu ismi Snodgrass'ın kitabı, geçmiş ve güncel veriyi birlikte tutan uygulamaların nasıl tasarlanacağını anlatan standart başvuru kaynağıdır (yazarın sitesinde ücretsiz erişilebilir).
  *Projede:* AS-4 uygulama tarafı: bitemporal tabloların gerçek sistemlerde nasıl kurulacağının standart başvuru kitabı; SQL:2011'in zamansal özelliklerini etkilemiştir.

**[Grandi2003]** Grandi, F., Mandreoli, F., Tiberio, P., & Bergonzini, M. (2003). A temporal data model and management system for normative texts in XML format. Proceedings of the 5th ACM International Workshop on Web Information and Data Management (WIDM '03), 29-36. ACM.
  https://doi.org/10.1145/956699.956706
  *Bulgu:* İtalyan ekibin mevzuat için kurduğu zamansal veri modeli, bir normun yayım, geçerlilik, yürürlük ve kayda giriş zamanlarını ayrı ayrı tutarak 'o tarihte yürürlükte olan metni' yeniden üretebilir; projemizin sürümleme mimarisinin birebir akademik karşılığı.
  *Projede:* AS-4 İÇİN EN İSABETLİ KAYNAK: mevzuat metinleri için DÖRT zaman boyutu (yayım, geçerlilik, yürürlük/etki ve işlem zamanı) tanımlar ve geçmiş bir tarihteki mevzuat sürümünün yeniden kurulmasını sağlar. Bizim üç eksenimizin doğrudan öncülü.

**[Bohlen2018]** Böhlen, M. H., Dignös, A., Gamper, J., & Jensen, C. S. (2018). Temporal Data Management - An Overview. In Business Intelligence and Big Data (eBISS 2017), Lecture Notes in Business Information Processing, vol. 324 (pp. 51-83). Springer.
  https://doi.org/10.1007/978-3-319-96655-7_3
  *Bulgu:* Alanın önde gelen dört ismi tarafından yazılan bu güncel derleme, zamansal veri yönetiminin kavramlarını ve modern veritabanı desteğini özetler.
  *Projede:* AS-4: zamansal veri yönetiminin güncel ve derli toplu özeti; sunumun teknik ekinde "bu alan canlı ve olgun" demek için kullanılabilir.

**[deMartim2025]** de Martim, H. (2025). Modeling the Diachronic Evolution of Legal Norms: An LRMoo-Based, Component-Level, Event-Centric Approach to Legal Knowledge Graphs. arXiv preprint arXiv:2506.07853.
  https://doi.org/10.48550/arXiv.2506.07853
  *Bulgu:* Brezilya Anayasası üzerinde çalışan bu yeni model, her değişiklik olayını ayrı sürüm olarak kaydederek bir hükmün herhangi bir geçmiş tarihteki tam metnini deterministik biçimde yeniden üretir; dil modelinin tek başına yapamadığı şey.
  *Projede:* AS-4: "as-of" yeniden üretilebilirlik. Her değişiklik olayını ayrı bir zamansal sürüm olarak modelleyerek bir mevzuat metninin herhangi bir geçmiş tarihteki halinin BİREBİR yeniden kurulabileceğini gösterir; üretken yapay zekânın bunu tek başına yapamadığını açıkça söyler.


## 9. Sürekli denetim ve denetimde yapay zekâ

*Cari dönem kontrol hesabının (Kazanım 6) ve "denetçi emeğinin desteklenmesi" tezinin muhasebe-denetim literatüründeki karşılığı.*

**[VasarhelyiHalper1991]** Vasarhelyi, M. A., & Halper, F. B. (1991). The Continuous Audit of Online Systems. Auditing: A Journal of Practice & Theory, 10(1), 110–125.
  https://raw.rutgers.edu/MiklosVasarhelyi/Resume%20Articles/CHAPTERS%20IN%20BOOKS/C05.%20the%20continuous%20audit%20of%20online%20systems.pdf
  *Bulgu:* Sürekli denetim kavramını literatüre sokan kurucu çalışma: AT&T'nin faturalama verisinde kurulan CPAS sistemi, denetimi yıl sonunda yapılan geriye dönük bir inceleme olmaktan çıkarıp sistemin kendisi üzerinde sürekli çalışan bir izleme-ve-alarm sürecine dönüştürmüştür.
  *Projede:* "Cari dönem kontrol hesabı" / sürekli denetim slaydı; denetimin yıl sonunu beklemeden, sistem üzerinde sürekli yürütülmesi fikrinin KURUCU çalışması. Denetci.AI'nin "beyan verilmeden önce farkı gör" konumlandırmasının akademik atası.

**[VasarhelyiAllesKogan2004]** Vasarhelyi, M. A., Alles, M. G., & Kogan, A. (2004). Principles of Analytic Monitoring for Continuous Assurance. Journal of Emerging Technologies in Accounting, 1(1), 1–21.
  https://doi.org/10.2308/jeta.2004.1.1.1
  *Bulgu:* Sürekli güvence, iş süreçlerinin otomatikleşmesinden yararlanan bir "analitik izleme" yöntemi olarak tanımlanır: sistem sürekli ölçer ve sapma üretir, denetçi bu sapmaları değerlendirir.
  *Projede:* AS-1 ve sürekli denetim mimarisi; "analitik izleme" (analytic monitoring) katmanının kuramsal çerçevesi; motorun sürekli hesap yapıp sapma ürettiği, insanın karar verdiği iş bölümünün öncülü.

**[AllesKoganVasarhelyi2008]** Alles, M. G., Kogan, A., & Vasarhelyi, M. A. (2008). Putting Continuous Auditing Theory into Practice: Lessons from Two Pilot Implementations. Journal of Information Systems, 22(2), 195–214.
  https://publications.aaahq.org/jis/article-abstract/22/2/195/1452/
  *Bulgu:* Sürekli denetimi iki gerçek kurumda pilot olarak kuran bu çalışma, kavramın kuramdan uygulamaya geçtiğini ve asıl zorluğun algoritmada değil kurumun veri ve süreç gerçekliğiyle temasta olduğunu göstermiştir.
  *Projede:* Saha/pilot slaydı (Tüpraş, Kale Seramik ücretli pilotları); sürekli denetimin kuramdan gerçek kurum ortamına taşınmasının nasıl yapıldığını ve nerede zorlandığını gösteren referans çalışma; "kurulumdan ilk rapora <=1 saat" hedefinin neden kritik olduğunu gerekçelendirir.

**[ChiuLiuVasarhelyi2014]** Chiu, V., Liu, Q., & Vasarhelyi, M. A. (2014). The development and intellectual structure of continuous auditing research. Journal of Accounting Literature, 33(1–2), 37–57.
  https://doi.org/10.1016/j.acclit.2014.08.001
  *Bulgu:* Sürekli denetim alan yazınının kapsamlı taraması, konunun 1990'lardan bu yana büyüyen, sınıflandırılabilir ve olgunlaşmış bir araştırma alanı olduğunu ortaya koyar.
  *Projede:* Sürekli denetim slaydının "bu yeni bir heves değil, 30 yıllık yerleşik bir alan yazın" dayanağı; hakem heyetindeki akademisyene alanın olgunluğunu tek kaynakla gösterir.

**[IIA_GTAG2015]** The Institute of Internal Auditors (2015). Global Technology Audit Guide (GTAG): Continuous Auditing; Coordinating Continuous Auditing and Monitoring to Provide Continuous Assurance (2nd Edition). Altamonte Springs, FL: The IIA.
  https://www.theiia.org/globalassets/documents/content/articles/guidance/gtag/gtag-3-continuous-auditing/gtag-3-continuous-auditing-2nd-edition.pdf
  *Bulgu:* Denetim mesleğinin küresel meslek örgütü IIA'nın resmî rehberi sürekli denetimi "teknoloji destekli, süregiden risk ve kontrol değerlendirmesi" olarak tanımlar ve denetçinin geleneksel geriye dönük yaklaşıma göre çok daha kısa sürede raporlamasını mümkün kılan yöntem olarak konumlandırır.
  *Projede:* Sürekli denetim slaydının MESLEKİ/RESMÎ dayanağı (akademik değil); sektör temsilcisi hakem için: bu, denetim mesleğinin kendi resmî rehberinde tanımlanmış bir uygulamadır, akademik bir merak değil.

**[IssaSunVasarhelyi2016]** Issa, H., Sun, T., & Vasarhelyi, M. A. (2016). Research Ideas for Artificial Intelligence in Auditing: The Formalization of Audit and Workforce Supplementation. Journal of Emerging Technologies in Accounting, 13(2), 1–20.
  https://publications.aaahq.org/jeta/article/13/2/1/9209/
  *Bulgu:* Denetim, emek yoğun olduğu ve farklı karar yapıları barındırdığı için kısmi otomasyona uygundur; yapay zekânın denetimdeki iki ayrı rolü denetimin biçimselleştirilmesi ve denetçi işgücünün desteklenmesidir.
  *Projede:* AS-1 ve "iş bölümü" slaydı; denetimin İKİ ayrı bileşene ayrılması fikrinin doğrudan kaynağı: biçimselleştirilebilir (formalization → deterministik motor) kısım ve insan işgücünün desteklenmesi (workforce supplementation → denetçi rolündeki model). Projenin "Hesabı motor yapar, bulguyu model inceler, kararı insan verir" cümlesinin akademik karşılığı.

**[KokinaDavenport2017]** Kokina, J., & Davenport, T. H. (2017). The Emergence of Artificial Intelligence: How Automation is Changing Auditing. Journal of Emerging Technologies in Accounting, 14(1), 115–122.
  https://publications.aaahq.org/jeta/article-abstract/14/1/115/9198/
  *Bulgu:* Yapay zekânın denetimde ortaya çıkışı ve büyük denetim firmalarındaki somut uygulamaları, otomasyonun denetim sürecini ve denetçinin rolünü halihazırda dönüştürdüğünü göstermektedir.
  *Projede:* Giriş/bağlam slaydı; denetimde yapay zekânın büyük denetim firmalarında zaten uygulanıyor olduğunun kanıtı; Denetci.AI'nin "yeni bir fikir" değil, "Türkiye mevzuatına ve KOBİ ölçeğine inen bir uyarlama" olduğunu konumlandırır.

**[Commerford2022]** Commerford, B. P., Dennis, S. A., Joe, J. R., & Ulla, J. W. (2022). Man Versus Machine: Complex Estimates and Auditor Reliance on Artificial Intelligence. Journal of Accounting Research, 60(1), 171–201.
  https://doi.org/10.1111/1475-679X.12407
  *Bulgu:* Denetçiler, yapay zekâ sisteminden gelen çelişkili bulguları insan uzmandan gelen aynı bulgulara göre daha az ciddiye alıp yönetimin tahminlerine daha küçük düzeltmeler önermektedir; yani yapay zekânın bulgusu kanıta bağlanmadığı sürece uygulamada karşılık bulmaz.
  *Projede:* "Kararı insan verir" ve AS-2 (kanıta bağlılık); DENEYSEL kanıt: denetçiler yapay zekâdan gelen çelişkili bulguya, aynı bulgu insan uzmandan gelseydi vereceklerinden DAHA AZ itibar ediyor ("algoritma çekincesi"). Bu, modelin gerekçesini kanıta ve mevzuat atfına bağlama zorunluluğunun ampirik gerekçesidir: kanıt gösterilmezse denetçi zaten dinlemez.

**[Veeramani2026]** Veeramani, K., Allen Joseph, N., & Pavithran, M. (2026). Neuro-symbolic reasoning engine for tax optimisation. Frontiers in Artificial Intelligence, 9, 1802755.
  https://doi.org/10.3389/frai.2026.1802755
  *Bulgu:* Vergi hesaplamasında nöro-sembolik bir motor %80 isabet elde ederek yalnız-LLM yaklaşımını (%75) ve basit belge getirmeli yaklaşımı (%60) geçmiş; sembolik katmanın geçersiz hesap yollarını engelleyip desteksiz çıktı üretmesini önlediği raporlanmıştır.
  *Projede:* AS-2'nin (sembolik doğrulama kapısı) ve çekirdek tezin EN YAKIN GÜNCEL EMSALİ; vergi mevzuatı alanında nöro-sembolik bir motorun, yalnız-LLM ve basit RAG yaklaşımlarını sayısal olarak geçtiğini gösterir. Denetci.AI'nin "model hesaplamaz, sembolik kural tabanı hesaplar ve modelin her atfını doğrular" tercihinin bağımsız ampirik desteği; ayrıca sembolik katmanın, karşılığı olmayan çıktıyı hiç üretmemesini sağladığını raporlar.


## 10. İnsan gözetimi, otomasyon yanlılığı ve yapay zekâ yönetişimi

*"Kararı insan verir" tercihinin gerekçesi; veri koruma ve denetim izi yükümlülükleri.*

**[ParasuramanRiley1997]** Parasuraman, R., & Riley, V. (1997). Humans and Automation: Use, Misuse, Disuse, Abuse. Human Factors: The Journal of the Human Factors and Ergonomics Society, 39(2), 230–253.
  https://doi.org/10.1518/001872097778543886
  *Bulgu:* İnsan-otomasyon ilişkisinin klasik çerçevesi, otomasyona aşırı güvenmenin de onu büsbütün reddetmenin de tasarım hatasından doğduğunu ve dengeyi kurmanın sistemin tasarımcısına düştüğünü ortaya koyar.
  *Projede:* "Kararı insan verir" slaydının kuramsal omurgası; insan-otomasyon iş bölümünün klasik çerçevesi: otomasyona aşırı güven (misuse) ve otomasyonu büsbütün reddetme (disuse) arasındaki dengeyi tasarımın kurması gerekir. Projenin modeli hesap yapmaktan men etmesi bu çerçevenin "abuse" (uygunsuz otomasyon tasarımı) uyarısına verilmiş bir cevaptır.

**[SkitkaMosierBurdick1999]** Skitka, L. J., Mosier, K. L., & Burdick, M. (1999). Does automation bias decision-making? International Journal of Human-Computer Studies, 51(5), 991–1006.
  https://doi.org/10.1006/ijhc.1999.0252
  *Bulgu:* Otomasyon yanlılığı deneyi, "neredeyse doğru" bir otomatik yardımcının insanın dikkatli inceleme refleksini köreltip performansı yardımcısız duruma göre düşürebildiğini göstermiştir; bu yüzden desteksiz iddia kullanıcıya hiç ulaşmamalıdır.
  *Projede:* AS-2 ve "kararı insan verir"; otomasyon yanlılığının (automation bias) DENEYSEL kanıtı: neredeyse ama tam olarak güvenilir olmayan bir otomatik yardımcıyla çalışanlar, yardımcısız çalışanlardan DAHA KÖTÜ performans gösterdi. Denetci.AI'nin sembolik doğrulama kapısının (desteksiz iddianın kullanıcıya hiç ulaşmaması) neden zorunlu olduğunu gösterir: insan gözetimi tek başına yanlış çıktıyı yakalamaya yetmez.

**[Green2022]** Green, B. (2022). The flaws of policies requiring human oversight of government algorithms. Computer Law & Security Review, 45, 105681.
  https://doi.org/10.1016/j.clsr.2022.105681
  *Bulgu:* İnsan gözetimini zorunlu kılan politikaların taraması, gözetimin tek başına bırakıldığında sahte bir güvenlik hissi ürettiğini ve hatalı algoritmaları meşrulaştırdığını gösterir; bu yüzden gözetim, kendisinden önce gelen teknik bir doğrulama katmanıyla desteklenmelidir.
  *Projede:* "Kararı insan verir" slaydının DÜRÜSTLÜK payandası ve projenin farkını anlatan kaynak; 41 politika belgesi taranmış ve insan gözetimi şartının tek başına sahte bir güvenlik hissi ürettiği gösterilmiştir. Denetci.AI bu eleştiriye cevaptır: insan gözetimini TEK savunma hattı yapmaz; önüne sembolik doğrulama kapısını (AS-2) ve deterministik motoru koyar. Akademisyen hakemde ciddi karşılık bulur.

**[AIAct2024_Art14]** Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act), OJ L, 2024/1689, 12.7.2024; Article 14 (Human oversight).
  https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
  *Bulgu:* AB Yapay Zekâ Tüzüğü'nün 14. maddesi, yüksek riskli yapay zekâ sistemlerinin insan tarafından etkin biçimde gözetilebilir olmasını zorunlu kılar ve gözetimi yapan kişiye sistemin çıktısını reddetme ve geçersiz kılma yetkisi tanınmasını, ayrıca "otomasyon yanlılığına" karşı uyanık tutulmasını şart koşar.
  *Projede:* "Kararı insan verir" slaydının RESMÎ mevzuat dayanağı; md.14 yüksek riskli yapay zekâ sistemlerinin gerçek kişilerce etkin biçimde gözetilebilecek şekilde tasarlanmasını şart koşar. md.14(4)(b) doğrudan "otomasyon yanlılığı" terimini kullanır; md.14(4)(d) gözetimi yapan kişinin sistemin çıktısını REDDETME veya GEÇERSİZ KILMA yetkisini şart koşar. Denetci.AI bu maddeyi tasarımın merkezine koymuştur.

**[AIAct2024_Art12]** Regulation (EU) 2024/1689 (Artificial Intelligence Act), OJ L, 2024/1689, 12.7.2024; Article 12 (Record-keeping).
  https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
  *Bulgu:* Tüzüğün 12. maddesi yüksek riskli yapay zekâ sistemlerinin olayları yaşam döngüsü boyunca otomatik olarak kaydetmesini ve sonuçların doğrulanmasına katılan kişilerin kayda geçirilmesini zorunlu kılar; yani izlenebilirlik bir tercih değil, yasal bir yükümlülüktür.
  *Projede:* Denetim izi / değişmez kayıt slaydı; md.12 yüksek riskli sistemlerin yaşam döngüsü boyunca olayları otomatik kaydetmesini (log) ve izlenebilirliği şart koşar; ayrıca sonuçların doğrulanmasına katılan gerçek kişilerin kimliğinin kaydedilmesini ister. Denetci.AI'nin karma zincirli denetim izi ve "hangi kuralın hangi sürümü, hangi tarihte uygulandı" kaydı (AS-4) bu yükümlülüğün doğrudan karşılığıdır.

**[NIST_AI_RMF_2023]** Tabassi, E. (2023). Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. Gaithersburg, MD: National Institute of Standards and Technology, U.S. Department of Commerce. 26 January 2023.
  https://doi.org/10.6028/NIST.AI.100-1
  *Bulgu:* NIST'in yapay zekâ risk yönetimi çerçevesi, riski tek seferlik bir uyum egzersizi değil sürekli bir faaliyet olarak kurgular ve YÖNET / EŞLE / ÖLÇ / İDARE ET işlevleriyle güvenilir yapay zekânın nasıl ölçüleceğini tanımlar.
  *Projede:* Yapay zekâ yönetişimi slaydı; Denetci.AI'nin risk yönetimi söz dağarcığını uluslararası kabul görmüş bir çerçeveye oturtur. GOVERN / MAP / MEASURE / MANAGE dört işlevi, projenin ölçüm rejimini (atıf doğruluğu >=%98, desteksiz iddia <=%1, regresyon çapası) rastgele seçilmiş sayılar değil, kurumsal bir ölçme-yönetme döngüsü olarak sunmayı sağlar.

**[ISO_IEC_42001_2023]** ISO/IEC 42001:2023, Information technology; Artificial intelligence; Management system. First edition, published 18 December 2023. Geneva: ISO/IEC.
  https://www.iso.org/standard/42001.html
  *Bulgu:* ISO/IEC 42001:2023, yapay zekâ yönetim sistemi (AIMS) kurmak, işletmek ve sürekli iyileştirmek için gereklilikleri tanımlayan ilk uluslararası standarttır ve yapay zekâ yönetişimini belgelendirilebilir hâle getirir.
  *Projede:* Yapay zekâ yönetişimi slaydı; dünyanın ilk yapay zekâ yönetim sistemi standardı; projenin kurumsal müşteriye (Tüpraş, Kale Seramik ölçeğinde) "bu sistemin yönetişimi belgelendirilebilir bir standarda oturuyor" diyebilmesini sağlar. Sektör temsilcisi hakem için en somut dayanak.

**[GDPR2016_Art22]** Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data, and repealing Directive 95/46/EC (General Data Protection Regulation), OJ L 119, 4.5.2016, p. 1–88; Article 22.
  https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng
  *Bulgu:* GDPR'ın 22. maddesi, kişiyi yalnızca otomatik işlemeye dayanan ve kendisini önemli ölçüde etkileyen kararlara karşı korur ve asgari güvence olarak insan müdahalesi elde etme hakkını şart koşar.
  *Projede:* "Kararı insan verir" ve KVKK slaydının AB ayağı; md.22(1) kişinin, hakkında yalnızca otomatik işlemeye dayanan ve kendisini önemli ölçüde etkileyen bir karara tabi tutulmama hakkını tanır; md.22(3) asgari güvence olarak İNSAN MÜDAHALESİ elde etme hakkını şart koşar. Denetci.AI'nin "model asla tutar hesaplamaz, kararı insan verir" tasarımı bu maddenin gereğini baştan karşılar.

**[KVKK6698]** 6698 sayılı Kişisel Verilerin Korunması Kanunu, Kabul Tarihi: 24/3/2016, Resmî Gazete: 7 Nisan 2016, Sayı: 29677; özellikle md. 11/1(g) ve md. 12 (veri güvenliğine ilişkin yükümlülükler).
  https://www.resmigazete.gov.tr/eskiler/2016/04/20160407-8.pdf
  *Bulgu:* KVKK'nın 11/1(g) bendi, kişiye verilerinin yalnızca otomatik sistemlerle analiz edilmesi sonucu aleyhine bir sonuç doğmasına itiraz hakkı tanır; yani Türkiye'de de nihai kararın insanda kalması hukuken güvence altına alınmış bir gerekliliktir.
  *Projede:* "KVKK / veri kurum dışına çıkmaz" slaydının BİRİNCİL dayanağı; md.11/1(g) ilgili kişiye, verilerinin MÜNHASIRAN otomatik sistemlerle analiz edilmesi sonucu aleyhine bir sonuç doğmasına İTİRAZ hakkı tanır. Bu, GDPR md.22'nin Türk hukukundaki karşılığıdır ve Denetci.AI'nin "kararı insan verir" tasarımını Türkiye mevzuatı açısından da zorunlu kılar. Ayrıca md.12 veri güvenliği yükümlülüğü, yerel/kapalı devre (on-premise) çalışmanın gerekçesidir: mükellefin bordro, personel ve proje verisi kurum dışına hiç çıkmaz.

**[HaberStornetta1991]** Haber, S., & Stornetta, W. S. (1991). How to time-stamp a digital document. Journal of Cryptology, 3(2), 99–111.
  https://doi.org/10.1007/BF00196791
  *Bulgu:* Kriptografik zaman damgasının kurucu çalışması, bir belgenin tarihinin ne kullanıcı ne de damga hizmeti tarafından geriye veya ileriye alınamayacak biçimde nasıl güvenceye alınacağını gösterir; denetim izinin değişmezliğinin teknik temeli budur.
  *Projede:* Denetim izinin DEĞİŞMEZLİĞİ slaydı; kriptografik zaman damgası ve karma (hash) zinciri klasiği. Denetci.AI'nin "hangi bulgu, hangi kural sürümüyle, hangi tarihte üretildi" kaydının geriye dönük değiştirilemez olmasının kuramsal temeli; AS-4'ün üç eksenli yürürlük tarihli sürümleme iddiasını teknik olarak destekler.

---

## 11. Kaynakçanın okunma biçimi

Bu ek bir literatür taraması değil, **dayanak kaydıdır.** Her kaynak, sunumda veya Proje Bilgi Formu'nda geçen belirli bir cümleye bağlıdır ve *Projede* satırı o bağı açıkça yazar. Hakem heyetinin kaynakçadan beklediği üç şey karşılanmıştır:

1. **Projenin literatürdeki yeri belli midir?** Bölüm 1 ve 4, projenin ne icat ettiğini ve neyi hazır araç olarak kullandığını ayırır. Proje, ince ayar veya nicemleme gibi olgun tekniklerin uygulanmasını Ar-Ge iddiası olarak öne sürmez; iddia, denetim verisinin doğrulanmış deterministik bir referanstan üretilmesi ve bu dar görevde ölçülebilir kazanç elde edilip edilemeyeceğidir.
2. **Karşı kanıt listeye alınmış mıdır?** Evet. Bölüm 4, projenin yaklaşımını zayıflatabilecek üç çalışmayı bilerek içerir: sentetik veriyle özyinelemeli eğitimin çöküşe yol açtığı bulgusu, taklit modellerinin sınırları ve küçük modellerin yüzeysel örüntü ezberi. Projenin bu bulgulara verdiği cevap sunumda ve soru-cevap bankasında açıkça yer alır.
3. **Boşluk nerededir?** Taramalarımızda, 5746 ve 4691 teşvik mevzuatının denetiminde yapay zekâ kullanımını konu alan, künyesi doğrulanmış Türkçe hakemli bir çalışmaya rastlanmamıştır. Bu, "literatürde hiç yoktur" iddiası değil, yapılan taramanın sonucudur.

---

## 12. Elenen kaynaklar ve gerekçeleri

*Bu bölüm bilerek yayımlanmıştır. Bir kaynakçanın güvenilirliği, içine aldıklarından çok dışarıda bıraktıklarıyla ölçülür. Aşağıdaki kayıtlar konuya uygun görünmelerine rağmen künyesi birincil kaynaktan doğrulanamadığı, ikincil kaynakta yanlış aktarıldığı veya kapsam dışı kaldığı için kullanılmamıştır.*

**Sunumda kullanılmaması gereken iki sayı:**

- 'Dil modelleri mali sorguların %41'inde halüsinasyon üretiyor'; blog ve ikincil kaynaklarda genel bir 'mali sorgu oranı' gibi dolaşan bu ifade YANLIŞ aktarımdır. Gerçek kaynak Kamble2025/FailSafeQA'dır ve rakam, yalnızca o3-mini modelinin bozulmuş bağlam senaryolarındaki test vakalarının %41'inde bilgi uydurmasıdır. Genelleştirilmiş biçimiyle reddedildi; doğru biçimiyle Kamble2025 altında yer alıyor.

- 'Stanford çalışmasında GPT-4 %43 oranında halüsinasyon üretti'; bu rakam çok sayıda haber ve blogda tekrarlanıyor ancak Magesh2025'in YAYIMLANMIŞ JELS sürümünün özetinde ve indirilen tam metninde bulunamadı. Makale GPT-4 için yalnızca 'hukuk araçlarından daha fazla halüsinasyon üretir' diyor. Sayısal biçimiyle reddedildi; sunumda kullanılmamalı.

- 'ChatGPT, PCAOB denetim eksiklik raporlarında ISA 620'yi yanlış tanımladı' örneği; yalnızca ikincil/blog kaynaklarında geçiyor, hakemli bir çalışmaya bağlanamadı; reddedildi.

- 'Confabulated references in the age of AI: contamination of the biomedical scientific literature'; tıp alanında uydurma atıf üzerine ilgi çekici görünen bir makale, ancak yayıncısı (Exploration Publishing) ve künyesi yeterince doğrulanamadığı ve tıp alanı projenin kapsamı dışında kaldığı için kapsam dışı bırakıldı.


**Künyesi doğrulanamadığı veya kapsam dışı kaldığı için elenenler:**

- Willard & Louf, 'Efficient Guided Generation for Large Language Models' (Outlines kütüphanesi); kısıtlı çözümleme temasına uygun olurdu ancak bu turda hakemli yayın künyesi doğrulanmadı; yalnızca arXiv ön baskısı olduğu ve Geng vd. 2023 (EMNLP) aynı iddiayı hakemli olarak karşıladığı için elendi.

- Inan vd., 'Llama Guard'; korkuluk mimarileri temasına uygun olurdu ancak hakemli yayın künyesi bu turda doğrulanmadı; NeMo Guardrails (EMNLP 2023 demo) hakemli olduğu için tercih edildi.

- Bohnet vd., 'Attributed Question Answering'; atıf/kanıt temasında aday idi; künyesi bu turda doğrulanmadığı için ALCE (EMNLP 2023) ve RARR (ACL 2023) tercih edildi.

- AuditBench (Wang vd., 2025); mali tablolara hata enjekte ederek denetim kabiliyetini ölçtüğü öne sürülen çalışma. Yalnızca ikincil bir arXiv makalesinin literatür bölümünde anıldığı için künye (tam yazar, mekân, DOI) ve bulguları birinci elden doğrulanamadı; reddedildi.

- FinSheet-Bench: 'Gemini 2.5 Pro karmaşık mali tablolarda %82,4'ten %48,6'ya düşüyor'; arama özetinde çıkan bu rakamların birincil kaynağına ulaşılamadı, hakemli veya ön baskı künyesi doğrulanamadı; reddedildi.

- Finansal İstikrar Kurulu'nun (FSB, 2025) halüsinasyonu 'model uyumsuzluğu riski' olarak sınıflandırdığı iddiası; birincil FSB belgesi bulunup doğrulanamadı; reddedildi.

- llama.cpp / GGUF (ggml-org): GPU'suz yerel çıkarımın fiili standardı olmasına karşın hakemli veya arXiv'de künyeli bir akademik yayını bulunmadığı için kaynak listesine alınmadı; aynı teknik iddia için hakemli EuroSys 2025 çalışması (Wei2025, T-MAC) kullanıldı; o çalışma zaten llama.cpp'yi karşılaştırma tabanı olarak alıyor.

- Zhang, H. & Huang, J. (2025), 'Challenging GPU Dominance: When CPUs Outperform for On-Device LLM Inference' (arXiv:2505.06461): Varlığı doğrulandı (Texas A&M, 2 yazar) ve 1 milyar parametreli modelde yalnızca-CPU yapılandırmasının GPU'yu geçtiğini raporluyor; ancak iki yazarlı, hakem sürecinden geçmemiş ve çok düşük atıflı bir önbaskı olduğu için hakem heyetine sunulacak listeden çıkarıldı. Aynı iddia Wei2025 (EuroSys 2025) ile çok daha güçlü biçimde karşılanıyor.

- Alpaca (Stanford CRFM) ve benzeri blog/duyuru temelli 'taklit modeli' çalışmaları: Künyeli akademik yayın niteliği taşımadıkları için doğrudan kaynak gösterilmedi; bunların sınırlarını akademik olarak inceleyen Gudibande2023 tercih edildi.

- Josephson, J. R. & Josephson, S. G., 'Abductive Inference: Computation, Philosophy, Technology' (Cambridge University Press, 1994); kitabın gerçek olduğu biliniyor ancak bu oturumda basım/edisyon künyesi bağımsız kaynaktan doğrulanamadığı için listeye alınmadı. Abdüksiyonun yapay zekâdaki yeri için Bylander1991 (aynı ekipten, hakemli dergi makalesi) ikame olarak kullanıldı.

- arXiv:2309.16180 'A More General Theory of Diagnosis from First Principles'; Reiter'in genelleştirmesi olarak ilgi çekici, ancak hakemli bir venue teyidi bulunamadığı (yalnızca preprint) için elendi. Not: bu başlığın daha eski ve hakemli bir JAIR versiyonu olabilir; sunumda kullanılacaksa ayrıca doğrulanmalı.

- arXiv:1711.05508 ve arXiv:1612.04791 (Rodler ve ark., ardışık teşhis için ölçüm/sorgu optimizasyonu); konuya çok uygun, ancak yayımlandıkları hakemli venue bu oturumda kesinleştirilemedi. Aynı temayı kapsayan ve künyesi tam doğrulanan Shchekotykhin2012 (Journal of Web Semantics) tercih edildi.

- Genel 'kök-neden analizi (RCA) derlemesi' niteliğinde bir kaynak arandı ancak Denetci.AI'nin kurgusuna (kural tabanlı, deterministik motor + hipotez sıralama) yeterince yakın, künyesi kesin ve hakemli tek bir derleme bulunamadı; bunun yerine tema, Reiter1987 + deKleerWilliams1987 + Sampath1995 üçlüsüyle doğrudan kurulmuştur.

- El-Yaniv & Wiener, 'On the foundations of noise-free selective classification' (JMLR 2010); gerçek olduğu biliniyor, fakat cilt/sayfa künyesi doğrulanmadan listeye alınmadı; reddetme seçeneği teması için künyesi tam doğrulanan Chow1970 (klasik) ve GeifmanElYaniv2017 (modern) çifti yeterli bulundu.

- OpenFisca için hakemli bir akademik makale: Aranmasına rağmen (Google/akademik arama, International Journal of Microsimulation arşivi) OpenFisca'yı konu alan hakemli bir dergi/konferans makalesi BULUNAMADI. OpenFisca gerçek ve yaygın kullanılan bir açık kaynak altyapıdır, ancak akademik atıf olarak değil yazılım/kurumsal kaynak olarak verilmelidir. Önerilen çözüm: OpenFisca'yı OECD raporu (MohunRoberts2020) içindeki ülke örneği olarak ve/veya doğrudan yazılım atfı (https://openfisca.org) olarak anmak; akademik ağırlığı EUROMOD (Sutherland2013) ve Catala (Merigoux2021Catala) taşısın.

- Palmirani & Brighi, 'Norma-System' ve ilgili Akoma Ntoso çalışmaları: Konu olarak uygun (mevzuat sürüm yönetimi) ancak künyeleri Crossref üzerinden birebir doğrulanamadı ve Grandi2003 ile büyük ölçüde örtüşüyor; gereksiz risk almamak için listeye alınmadı. Sürümleme temasını Grandi2003 + Governatori2010 zaten daha güçlü taşıyor.

- Arama sonuçlarında çıkan 'Time as Structure' (arXiv:2608.15270), 'Deterministic Legal Agents' (arXiv:2510.06002) ve 'Beyond Probabilistic Similarity' (arXiv:2606.09724) gibi çok yeni ön baskılar: Konuları ilgi çekici olsa da hakem denetiminden geçmemiş, atıf birikimi olmayan ve künyeleri bağımsız olarak teyit edilemeyen çalışmalar olduğu için hakem heyetine sunulacak listeye alınmadı.

- iso.org/standard/42001 birincil sayfası HTTP 403 döndürdüğü için ISO/IEC 42001 künyesi ISO'nun kendi sitesinden DOĞRUDAN alınamadı; IEC Webstore (publication 90574) ve ANSI/ANAB üzerinden doğrulandı. Sunumda standart numarası ve tarihi güvenle kullanılabilir, ancak standardın MADDE İÇERİĞİNE atıf yapılacaksa satın alınmış nüsha üzerinden teyit edilmelidir (standart metni ücretlidir, açık erişimde değildir).

- Vasarhelyi & Halper (1991) için AAA'nın birincil dergi sayfası ödeme duvarı arkasındadır; sayfa aralığı (110-125) üç bağımsız ikincil kaynakta tutarlı olduğu için doğrulanmış sayıldı, ancak yayıncı nüshasından birebir teyit edilemedi.

- mevzuat.gov.tr ve resmigazete.gov.tr PDF uç noktaları tekrarlanan denemelerde HTTP 503 döndürdü; KVKK md.11 metni bu nedenle ikincil ama metni birebir aktaran hukuk kaynaklarından doğrulandı. Sunuma konulmadan önce mevzuat.gov.tr erişilebilir olduğunda son bir kez teyit edilmesi önerilir.

- IIA GTAG 'Continuous Auditing' rehberinin Eylül 2025 tarihli YENİ bir baskısı bulunmaktadır; doğrulanan ve künyelenen nüsha 2015 tarihli 2. baskıdır. Sunumda baskı yılı mutlaka belirtilmeli, aksi hâlde güncel olmayan sürüme atıf izlenimi doğar.

- Aranan ancak künyesi doğrulanamadığı için LİSTEYE ALINMAYAN kategori: 5746/4691 teşvik mevzuatının denetiminde yapay zekâ kullanımına dair Türkçe hakemli akademik çalışma. Bu boşluk projenin aleyhine değil LEHİNEDİR ve sunumda 'literatür boşluğu' olarak kullanılabilir; ancak 'hiç yok' iddiası yerine 'taramalarımızda doğrulanmış bir emsale rastlanmadı' denmesi daha güvenlidir.


---

*Kaynak sayısı: 98 doğrulanmış künye, 10 bölüm. Elenen kayıt: 26.*
