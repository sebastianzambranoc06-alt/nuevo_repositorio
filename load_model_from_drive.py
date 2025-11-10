import gdown
import os

# URL de descarga directa del modelo principal
url_model = "https://drive.google.com/uc?export=download&id=1kU22VwvsU7aK99gYOFesEFk-0-PVkP30"

# Carpeta donde guardarás el modelo
os.makedirs("models", exist_ok=True)

# Ruta local del modelo
model_path = "models/model.keras"

# Descargar si no existe
if not os.path.exists(model_path):
    print("📥 Descargando modelo desde Google Drive...")
    gdown.download(url_model, model_path, quiet=False)
else:
    print("✅ El modelo ya está disponible localmente.")

print("🎯 Descarga completada.")
