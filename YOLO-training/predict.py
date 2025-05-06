from ultralytics import YOLO

# Cargar el modelo
model = YOLO('runs/detect/yolov8_documents5/weights/best.pt')

# Realizar la predicción
results = model.predict('./datasets/documents/test-images/test2.jpg', save=True)