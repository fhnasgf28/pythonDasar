import numpy as np
from sklearn.ensemble import IsolationForest

# Data aktivitas (misalnya jumlah pesan per hari)
data = np.array([[10], [12], [9], [11], [50], [8], [10], [9], [13], [100]])

# Model deteksi anomali
model = IsolationForest(contamination=0.2, random_state=42)
model.fit(data)

# Prediksi: -1 = anomali, 1 = normal
predictions = model.predict(data)

for i, (val, pred) in enumerate(zip(data, predictions)):
    status = "Anomali" if pred == -1 else "Normal"
    print(f"Hari {i+1}: {val[0]} pesan → {status}")
