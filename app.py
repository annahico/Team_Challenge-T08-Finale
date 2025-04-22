import pickle

import numpy as np
from flask import Flask, jsonify, request
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Cargar el modelo previamente entrenado
with open("model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/")
def home():
    return jsonify({
        "message": "Bienvenido a la API del modelo de clasificación de flores Iris 🌸",
        "uso": "Envía una petición GET al endpoint /predict con los siguientes parámetros:",
        "parámetros": [
            "sepal_length (float)",
            "sepal_width (float)",
            "petal_length (float)",
            "petal_width (float)"
        ],
        "ejemplo": "/predict?sepal_length=5.1&sepal_width=3.5&petal_length=1.4&petal_width=0.2"
    })


@app.route("/predict", methods=["GET"])
def predict():
    try:
        # Obtener los parámetros de la consulta
        sl = float(request.args.get("sepal_length"))
        sw = float(request.args.get("sepal_width"))
        pl = float(request.args.get("petal_length"))
        pw = float(request.args.get("petal_width"))

        # Crear el array de entrada para el modelo
        features = np.array([[sl, sw, pl, pw]])

        # Realizar la predicción
        prediction = model.predict(features)[0]

        # Devolver la predicción como respuesta JSON
        return jsonify({
            "predicción": int(prediction),
            "clases": {
                "0": "setosa",
                "1": "versicolor",
                "2": "virginica"
            }
        })
    except (ValueError, TypeError) as e:
        return jsonify({"error": str(e)})

@app.route('/retrain', methods=['GET'])
# Enruta la funcion al endpoint /retrain
def retrain(): # Rutarlo al endpoint '/retrain', metodo GET
    iris = load_iris()
    X, y = iris['data'], iris['target']
    model = RandomForestClassifier()
    model.fit(X, y)

<<<<<<< HEAD
        with open("model.pkl", "wb") as f:
            pickle.dump(model, f)
        return f"✅ Modelo entrenado y guardado como model.pkl"
=======
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)
    return f"Modelo entrenado y guardado como model.pkl"
>>>>>>> b57a0416413f872f8b5796b91cb60d1e17f0dcb0

# Endpoint oculto para usar en redespliegue
# @app.route("/extra")
# def extra():
#     return jsonify({
#         "mensaje": "¡Este es el nuevo endpoint activado tras redesplegar! 🚀",
#         "info": "Aquí podríamos agregar nuevas funcionalidades, estadísticas, etc."
#     })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
