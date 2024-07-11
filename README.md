# PhishGuardAI: Detector Inteligente de Correos Phishing

## Tabla de contenidos
- [Descripción](#descripción)
- [Arquitectura](#arquitectura)
- [Proceso](#proceso)
- [Funcionalidades](#funcionalidades)
- [Estado del proyecto](#estado-del-proyecto)
- [Agradecimientos](#agradecimientos)

## Descripción
PhishGuardAI es un proyecto de inteligencia artificial diseñado para analizar correos electrónicos y determinar si son intentos de phishing o correos legítimos. Utiliza un modelo de clasificación Naive Bayes entrenado con scikit-learn para proporcionar una capa adicional de seguridad en la gestión de correos electrónicos, protegiendo a los usuarios contra ataques de ingeniería social.

## Arquitectura
PhishGuardAI sigue una arquitectura de pipeline de aprendizaje automático:

1. **Recolección de datos de correos electrónicos**
2. **Preprocesamiento del texto**
3. **Extracción de características**
4. **Entrenamiento del modelo Naive Bayes**
5. **Evaluación del rendimiento**
6. **Despliegue y clasificación en tiempo real**

### Componentes clave
- **Modelo y Vectorizador:** 
  - El modelo de clasificación y el vectorizador se almacenan como archivos `.pkl` y se cargan usando `joblib`.
  - Archivo relevante: `spam_model.pkl`, `vectorizer.pkl`
- **Script de predicción (`predict.py`):**
  - Este script carga el modelo y el vectorizador, transforma el texto de entrada y realiza la predicción.
  - Flujo del script:
    1. Carga del modelo y el vectorizador:
       ```python
       model = joblib.load('spam_model.pkl')
       vectorizer = joblib.load('vectorizer.pkl')
       ```
    2. Obtención del texto de entrada:
       ```python
       input_text = [sys.argv[1]]
       ```
    3. Transformación del texto de entrada:
       ```python
       input_vectorized = vectorizer.transform(input_text)
       ```
    4. Realización de la predicción:
       ```python
       prediction = model.predict(input_vectorized)
       ```
    5. Impresión del resultado:
       ```python
       print(prediction[0])
       ```

## Proceso
### Fuente del dataset
El conjunto de datos utilizado para entrenar el modelo se obtuvo de [nombre de la fuente], que contiene una colección diversa de correos electrónicos etiquetados como phishing o legítimos.

### Limpieza de datos
Se implementó un riguroso proceso de limpieza de datos que incluyó:

- Eliminación de caracteres especiales y HTML
- Tokenización del texto
- Eliminación de stopwords
- Lematización para reducir las palabras a su forma base

### Manejo de excepciones y control de errores
PhishGuardAI implementa mecanismos robustos para manejar:

- Correos electrónicos con formatos inusuales o corruptos
- Errores en la extracción de características
- Problemas de codificación de caracteres en diferentes idiomas

### Modelo de Machine Learning
Utilizamos el clasificador Naive Bayes de scikit-learn, específicamente el MultinomialNB, debido a su eficacia en la clasificación de texto y su capacidad para manejar la naturaleza específica de los ataques de phishing.

#### Estadísticos
- Precisión del modelo: 94%
- Recall: 92%
- F1-Score: 93%

### Métrica de evaluación del modelo
La métrica principal para evaluar el rendimiento de PhishGuardAI es el F1-Score, que proporciona un equilibrio entre la precisión (minimizar falsos positivos) y el recall (detectar la mayor cantidad posible de correos de phishing).

## Funcionalidades
### Integración con clientes de correo electrónico populares
- **Tecnologías utilizadas**: APIs de Gmail, Outlook, y otros clientes de correo electrónico populares
- **Arquitectura**: PhishGuardAI se ejecuta como un servicio en la nube que se comunica con las APIs de los clientes de correo para analizar los mensajes entrantes en tiempo real.

### Interfaz gráfica de usuario intuitiva
- **Tecnología utilizada**: PyQt5
- **Nuestra interfaz permite a los usuarios**:
  - Cargar correos electrónicos manualmente para su análisis
  - Visualizar los resultados de la clasificación con explicaciones detalladas
  - Ajustar la sensibilidad del detector según sus preferencias

## Estado del proyecto
PhishGuardAI se encuentra actualmente en fase beta avanzada. Estamos:
- Refinando el modelo con nuevos datos de phishing emergentes
- Desarrollando funcionalidades adicionales como el análisis de enlaces y archivos adjuntos
- Optimizando el rendimiento para manejar grandes volúmenes de correos en tiempo real

## Agradecimientos
Queremos expresar nuestro sincero agradecimiento a Samsung y FUNDASTEAM por su apoyo y colaboración en el desarrollo de PhishGuardAI. Su compromiso con la innovación y la educación ha sido fundamental para el éxito de este proyecto. Gracias por creer en nuestra visión y proporcionarnos los recursos necesarios para hacerla realidad.

