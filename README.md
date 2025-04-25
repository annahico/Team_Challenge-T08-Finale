# Proyecto de Clasificación de Flores Iris

Este proyecto consiste en la creación de una API REST que permite realizar predicciones sobre el tipo de flor Iris utilizando un modelo de clasificación entrenado con el conjunto de datos Iris. La API está desarrollada con **Flask** y utiliza un modelo de clasificación basado en **RandomForestClassifier**.

## Colaboradores

- **Anna Hidalgo Costa**
- **José Estévez** @esjoal
- **Pablo García** @pajuanes

## 🚀 Enlaces de despliegue

- **API principal (JSON)**:  
  👉 https://team-challenge-t08-finale.onrender.com/

- **Demo de la Web App (HTML)**:  
  👉 https://team-challenge-t08-finale.onrender.com/web

## 🔍 Endpoints disponibles

| Endpoint   | Método | Descripción                                                                                  |
| ---------- | ------ | -------------------------------------------------------------------------------------------- |
| `/`        | GET    | Página de bienvenida e instrucciones de uso                                                  |
| `/predict` | GET    | Predice la clase de una flor Iris usando parámetros como `sepal_length`, `sepal_width`, etc. |
| `/retrain` | GET    | Reentrena el modelo utilizando el dataset Iris                                               |
| `/web`     | GET    | Interfaz HTML amigable para probar el modelo                                                 |

## 🖼 Vista de la Web App

![Captura de la Web App](https://raw.githubusercontent.com/annahico/Team_Challenge-T08-Finale/master/static/API_Web.png)

## Descripción

La API proporciona dos endpoints principales:

1. **`/`**: Página principal que proporciona información sobre el uso de la API.
2. **`/predict`**: Endpoint para realizar predicciones sobre el tipo de flor Iris. Acepta cuatro parámetros:

   - `sepal_length` (longitud del sépalo)
   - `sepal_width` (anchura del sépalo)
   - `petal_length` (longitud del pétalo)
   - `petal_width` (anchura del pétalo)

   <!-- Ejemplo de uso:
   https://team-challenge-t08-finale.onrender.com/predict?sepal_length=5.1&sepal_width=3.5&petal_length=1.4&petal_width=0.2 -->

3. **`/retrain`**: Endpoint para reentrenar el modelo utilizando el dataset Iris. Este endpoint requiere un parámetro adicional `force=true` para autorizar el reentrenamiento. Solo debe ser usado con precaución.

<!-- Ejemplo de uso:
https://team-challenge-t08-finale.onrender.com/retrain?force=true -->

## Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/annahico/Team_Challenge-T08-Finale.git
cd Team_Challenge-T08-Finale
```

## Ejecución

1. En la terminal primero hay que entrenar el modelo:

```bash
python train_model.py
```

2. Realizar el test:

```bash
python test_request.py
```
