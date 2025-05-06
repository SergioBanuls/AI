# Proyecto de procesamiento de imágenes y entrenamiento YOLO

Este repositorio contiene dos aplicaciones principales:

## 1. imageScript

Esta aplicación tiene como funcionalidad principal:
- Convertir un formato concreto de metadatos al formato requerido por YOLO.
- Permitir visualizar los metadatos sobre las imágenes correspondientes, para comprobar que la conversión se ha realizado correctamente.
- Re-escalar la imagen de origen a un tamaño más pequeño si es necesario.

Esto facilita la preparación y validación de los datos antes de entrenar modelos de detección de objetos con YOLO.

## 2. YOLO-training

Esta aplicación permite:
- Entrenar modelos de detección de objetos con YOLOv8 usando los datos preparados.
- Probar los modelos entrenados para evaluar su rendimiento.

Incluye scripts y utilidades para gestionar datasets, entrenar modelos y realizar predicciones.

---

Si necesitas más detalles sobre el uso de cada aplicación, consulta la documentación específica en cada carpeta o los scripts principales.
