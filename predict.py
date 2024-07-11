import sys
import joblib

# Cargar el modelo y el vectorizador
model = joblib.load('spam_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Obtener el texto de entrada
input_text = [sys.argv[1]]

# Transformar el texto de entrada
input_vectorized = vectorizer.transform(input_text)

# Realizar la predicción
prediction = model.predict(input_vectorized)

# Imprimir el resultado
print(prediction[0])
