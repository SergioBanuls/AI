import os
from ultralytics import YOLO
import yaml

# Obtener la ruta absoluta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Configurar el archivo YAML con rutas absolutas
data = {
    'path': 'datasets/documents',
    'train': 'datasets/documents/images/train',
    'val': 'datasets/documents/images/val',
    'nc': 2,
    'names': ['face', 'document']
}

# Guardar la configuración en el archivo YAML
with open('documents.yaml', 'w') as f:
    yaml.dump(data, f, default_flow_style=False)

# Cargar el modelo
model = YOLO('yolov8n.pt')

# Entrenar el modelo
results = model.train(
    data='documents.yaml',
    epochs=50,
    imgsz=640,
    batch=16,
    name='yolov8_documents'
) 