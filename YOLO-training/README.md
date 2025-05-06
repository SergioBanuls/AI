# YOLO-training

Esta aplicación está diseñada para entrenar y probar modelos de detección de objetos usando YOLOv8.

## Funcionalidades principales
- Entrenamiento de modelos YOLOv8 con tus propios datos.
- Prueba y evaluación de modelos entrenados.
- Scripts para gestionar datasets y predicciones.

## Requisitos
- Python 3.8 o superior
- ultralytics (para YOLOv8)
- numpy
- matplotlib
- (Opcional) opencv-python

## Instalación

1. Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

Si no tienes un requirements.txt, puedes instalar las dependencias básicas con:

```bash
pip install ultralytics numpy matplotlib opencv-python
```

## Estructura de Directorios

```
.
├── datasets/           # Datasets para entrenamiento y validación
├── scripts/            # Scripts de entrenamiento y predicción
├── predict.py          # Script para realizar predicciones
├── train.py            # Script para entrenar el modelo
└── documents.yaml      # Configuración de datasets y clases
```

## Uso

### Entrenamiento

1. Prepara tus datos siguiendo la estructura de YOLO (imágenes y etiquetas en carpetas separadas).
2. Configura el archivo `documents.yaml` con las rutas y clases.
3. Ejecuta el entrenamiento:

```bash
python train.py --data documents.yaml --epochs 100 --img 640
```

### Predicción

1. Una vez entrenado el modelo, ejecuta:

```bash
python predict.py --weights runs/train/exp/weights/best.pt --source path/to/images
```

### Notas adicionales
- Consulta los scripts y comentarios para opciones avanzadas.
- Puedes modificar los hiperparámetros y la configuración según tus necesidades.
- Se recomienda usar una GPU para entrenamientos largos.

---

Si tienes dudas sobre el formato de datos o el flujo de trabajo, revisa el README principal del proyecto o los scripts incluidos.
