import cv2
import numpy as np
import tensorflow as tf
from PIL import Image, ImageOps
import os
import sys
from collections import deque

# ============================================================
# SMART RECYCLE AI — FINAL VERSION (OTOMATIK DOSYA YOLU)
# ============================================================

# Gereksiz loglari ve GPU uyarlarini kapat
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
tf.config.set_visible_devices([], "GPU")

class RecycleAI:
    def __init__(self):
        # 1. DOSYA YOLLARINI AYARLA (Script nerede calisirsa calissin dosyalarini bulur)
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.model_path = os.path.join(self.base_path, "keras_model.h5")
        self.label_path = os.path.join(self.base_path, "labels.txt")

        self.labels = []
        self.model = None
        
        # Kararlilik filtresi (Titremeyi onlemek icin son 10 tahmini tutar)
        self.history = deque(maxlen=10)

        self.setup()

    def setup(self):
        print("--- Sistem Baslatiliyor ---")
        
        # Dosya kontrolu
        if not os.path.exists(self.model_path):
            print(f"HATA: {self.model_path} bulunamadi!")
            sys.exit()
        
        if not os.path.exists(self.label_path):
            print(f"HATA: {self.label_path} bulunamadi!")
            sys.exit()

        # Modeli yukle
        try:
            self.model = tf.keras.models.load_model(
                self.model_path,
                compile=False,
                custom_objects={"DepthwiseConv2D": tf.keras.layers.DepthwiseConv2D}
            )
        except Exception as e:
            print(f"Model yuklenirken hata olustu: {e}")
            sys.exit()

        # Etiketleri yukle
        with open(self.label_path, "r", encoding="utf-8") as f:
            self.labels = [line.strip() for line in f.readlines()]

        print("Sistem hazir | Model ve Etiketler yuklendi.")

    def preprocess(self, frame):
        """Kameradan gelen görüntüyü yapay zekanın anlayacağı formata sokar."""
        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        img = ImageOps.fit(img, (224, 224), Image.Resampling.LANCZOS)
        arr = (np.asarray(img).astype(np.float32) / 127.5) - 1
        return np.expand_dims(arr, axis=0)

    def draw_ui(self, frame, label=None, score=0):
        """Ekrana şık bir arayüz ve tespit bilgilerini çizer."""
        h, w, _ = frame.shape
        
        # Üst bilgi çubuğu (Siyah şerit)
        overlay = frame.copy()
        cv2.rectangle(overlay, (0, 0), (w, 90), (15, 15, 15), -1)
        cv2.addWeighted(overlay, 0.75, frame, 0.25, 0, frame)

        if label:
            color = (0, 255, 0) # Tespit varsa Yeşil
            text = f"TESPIT: {label} (%{int(score*100)})"
        else:
            color = (0, 165, 255) # Beklemede Turuncu
            text = "DURUM: NESNE BEKLENIYOR..."

        cv2.putText(frame, text, (20, 55), cv2.FONT_HERSHEY_DUPLEX, 0.8, color, 2)
        cv2.putText(frame, "Cikis: Q", (w-120, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

    def run(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Kamera acilamadi!")
            sys.exit()

        print("Kamera aktif. Geri donusum nesnelerini gosterin.")

        while True:
            ret, frame = cap.read()
            if not ret: break

            # Görüntüyü aynala (Daha doğal kullanım için)
            frame = cv2.flip(frame, 1)

            # Tahmin yap
            inp = self.preprocess(frame)
            preds = self.model.predict(inp, verbose=0)[0]

            idx = np.argmax(preds)
            score = preds[idx]

            # Etiketteki rakamları temizle (Örn: "0 Plastik" -> "Plastik")
            raw_label = self.labels[idx]
            label = "".join([c for c in raw_label if not c.isdigit()]).strip()

            # Eşik değeri kontrolü (%88 güven oranı)
            if score > 0.88:
                self.history.append(label)
                # En çok tekrar eden tahmini seç (Dalgalanmayı önler)
                final_label = max(set(self.history), key=self.history.count)
                self.draw_ui(frame, final_label, score)
            else:
                self.history.clear()
                self.draw_ui(frame)

            cv2.imshow("SMART RECYCLE AI", frame)

            # Q tuşu ile çıkış
            if cv2.waitKey(1) & 0xFF in [ord("q"), ord("Q")]:
                break

        cap.release()
        cv2.destroyAllWindows()

# ============================================================
if __name__ == "__main__":
    app = RecycleAI()
    app.run()