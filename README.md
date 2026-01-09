# ♻️ SMART RECYCLE AI

SMART RECYCLE AI, gerçek zamanlı kamera görüntüsünden geri dönüşüm nesnelerini yapay zekâ kullanarak tanıyan akıllı bir sınıflandırma sistemidir. TensorFlow ile eğitilmiş derin öğrenme modeli sayesinde plastik, metal, cam gibi atık türlerini yüksek doğrulukla tespit eder ve sonuçları kullanıcı dostu bir arayüzle ekranda gösterir.

Bu proje, çevre teknolojileri ve yapay zekânın birleşimini hedefleyen eğitim, demonstrasyon ve akıllı sistem uygulamaları için geliştirilmiştir.

## 🚀 Özellikler

- Gerçek zamanlı kamera üzerinden nesne tanıma  
- TensorFlow / Keras tabanlı derin öğrenme modeli  
- %88 güven eşiği ile yanlış tahminleri filtreleme  
- Son 10 tahmine dayalı kararlılık filtresi (tahmin titremesini önler)  
- OpenCV ile hazırlanmış sade ve anlaşılır kullanıcı arayüzü  
- Otomatik dosya yolu algılama (her dizinde sorunsuz çalışır)  
- GPU ve gereksiz TensorFlow loglarının kapatılması ile stabil çalışma  

## 🧠 Kullanılan Teknolojiler

- Python  
- TensorFlow / Keras  
- OpenCV  
- NumPy  
- Pillow (PIL)  

## 📁 Proje Yapısı

SMART-RECYCLE-AI/  
├── keras_model.h5  
├── labels.txt  
├── main.py  
└── README.md  

## ⚙️ Kurulum

Projeyi çalıştırmadan önce gerekli kütüphanelerin yüklenmesi gerekir.

pip install tensorflow opencv-python pillow numpy

## ▶️ Çalıştırma

Aşağıdaki komut ile proje başlatılır:

python main.py

Uygulama çalıştırıldığında kamera otomatik olarak açılır. Geri dönüşüm nesnesini kameraya göstererek sınıflandırma yapılır. Programdan çıkmak için Q tuşuna basılması yeterlidir.

## 🎯 Çalışma Mantığı

Uygulama kameradan alınan görüntüyü yapay zekâ modelinin anlayabileceği formata dönüştürür. Model her kare için sınıflandırma yapar ve güven oranını hesaplar. %88 güven eşiğinin altındaki tahminler gösterilmez. Son 10 tahmin analiz edilerek en sık tekrar eden sonuç ekrana yansıtılır ve böylece kararlı bir çıktı elde edilir.

## 🖼️ Arayüz

Uygulama arayüzünde üst bilgi bandı, tespit edilen nesnenin adı ve güven oranı yer alır. Nesne algılanmadığında bekleme durumu gösterilir. Renkli göstergeler sayesinde sistem durumu kullanıcı tarafından kolayca anlaşılır.

## 📌 Kullanım Alanları

- Akıllı geri dönüşüm kutuları  
- Eğitim ve bitirme projeleri  
- Yapay zekâ ve görüntü işleme uygulamaları  
- Çevre ve sürdürülebilirlik odaklı teknolojiler  

## 📄 Lisans

Bu proje MIT Lisansı ile paylaşılmıştır. Ticari ve kişisel projelerde özgürce kullanılabilir.

## 👤 Geliştirici

Mustafa Öz  
Türkiye 🇹🇷

Projeyi beğendiyseniz GitHub üzerinden yıldız vererek destek olabilirsiniz.
