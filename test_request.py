import requests

# URL del endpoint
url = "https://team-challenge-t08-finale.onrender.com/predict"

# Parámetros de entrada (ajusta según los valores de tu nuevo dataset)
params = {
    "sepal_length": 6.1,
    "sepal_width": 2.9,
    "petal_length": 4.7,
    "petal_width": 1.4
}

# Realizar la petición GET
response = requests.get(url, params=params, timeout=10)

# Mostrar la respuesta JSON
if response.status_code == 200:
    print("Respuesta de la API:")
    print(response.json())
else:
    print("Error al llamar a la API:", response.status_code)
