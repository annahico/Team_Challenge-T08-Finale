import requests

# URL del endpoint de predicción
url = "https://team-challenge-t08-finale.onrender.com/predict"

# Parámetros de entrada (puedes cambiarlos para probar distintas flores)
params = {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}

# Hacer la petición GET
response = requests.get(url, params=params, timeout=10)

# Mostrar la respuesta JSON
if response.status_code == 200:
    print("Respuesta de la API:")
    print(response.json())
else:
    print("Error al llamar a la API:", response.status_code)
