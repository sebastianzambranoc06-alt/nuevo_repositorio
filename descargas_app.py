import gdown
import os

# URL directa de descarga desde Google Drive
url_app = "https://drive.google.com/uc?export=download&id=1sSq89mEv5MyrbQcHEpxvB8EB2uX1tIUu"

# Nombre local del archivo que se descargará
app_local = "app_test.py"

# Verificar si el archivo ya existe
if not os.path.exists(app_local):
    print("📥 Descargando app_test.py desde Google Drive...")
    gdown.download(url_app, app_local, quiet=False)
    print("✅ Descarga completada correctamente.")
else:
    print("✅ app_test.py ya existe, no se descarga nuevamente.")
