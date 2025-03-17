#!/usr/bin/env python
import sys
print("Rutas de búsqueda (sys.path):")
for path in sys.path:
    print(" -", path)

import pandas as pd
import matplotlib.pyplot as plt
import re
import string
import os

# Importa la clase desde el paquete instalado
from sentiment_analysis_spanish.sentiment_analysis import SentimentAnalysisSpanish

# Función para limpiar el tweet
def limpiar_tweet(tweet):
    # Convertir a minúsculas
    tweet = tweet.lower()
    # Eliminar URLs
    tweet = re.sub(r'http\S+|www.\S+', '', tweet)
    # Eliminar menciones (@usuario)
    tweet = re.sub(r'@\w+', '', tweet)
    # Eliminar el símbolo de hashtag (se conserva la palabra)
    tweet = re.sub(r'#', '', tweet)
    # Conservar signos de exclamación e interrogación y eliminar el resto de la puntuación
    allowed_punctuation = "!?"  # Conservamos estos signos para mantener énfasis
    punctuation_to_remove = ''.join(ch for ch in string.punctuation if ch not in allowed_punctuation)
    tweet = tweet.translate(str.maketrans('', '', punctuation_to_remove))
    # Eliminar números
    tweet = re.sub(r'\d+', '', tweet)
    # Eliminar espacios en exceso
    tweet = tweet.strip()
    return tweet

# Crear carpeta para guardar imágenes de salida
output_dir = 'outputs'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 1. Cargar el dataset de tweets (asegúrate de que 'data/tweets.csv' exista)
df = pd.read_csv('data/tweets.csv')
print("Primeros registros del dataset original:")
print(df.head())

# 2. Limpiar los tweets y crear una nueva columna
df['tweet_limpio'] = df['tweet'].apply(limpiar_tweet)
print("\nPrimeros registros después de la limpieza:")
print(df[['tweet', 'tweet_limpio']].head())

# 3. Inicializar el analizador de sentimientos para español
analyzer = SentimentAnalysisSpanish()

# Función para obtener el puntaje de sentimiento (valor entre 0 y 1)
def obtener_sentimiento_es(texto):
    score = analyzer.sentiment(texto)
    return score

# 4. Aplicar el análisis de sentimiento sobre los tweets limpios
df['sentimiento'] = df['tweet_limpio'].apply(obtener_sentimiento_es)

# 5. Clasificar el sentimiento basado en el puntaje (umbral: ajustable)
def clasificar_sentimiento(score):
    if score > 0.55:
        return 'positivo'
    elif score < 0.45:
        return 'negativo'
    else:
        return 'neutro'

df['etiqueta_sentimiento'] = df['sentimiento'].apply(clasificar_sentimiento)
print("\nEjemplo de tweets con puntaje y clasificación:")
print(df[['tweet', 'tweet_limpio', 'sentimiento', 'etiqueta_sentimiento']].head(10))

# 6. Visualización: Distribución de puntajes de sentimiento
plt.figure(figsize=(10, 6))
plt.hist(df['sentimiento'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribución de Puntajes de Sentimiento (sentiment_analysis_spanish)')
plt.xlabel('Puntaje de Sentimiento')
plt.ylabel('Frecuencia')
plt.savefig(os.path.join(output_dir, 'sentimiento_histograma_spanish.png'))
plt.show()

# 7. Visualización: Distribución de etiquetas de sentimiento
plt.figure(figsize=(8, 5))
df['etiqueta_sentimiento'].value_counts().plot(kind='bar', color=['salmon', 'grey', 'lightgreen'])
plt.title('Distribución de Etiquetas de Sentimiento (sentiment_analysis_spanish)')
plt.xlabel('Sentimiento')
plt.ylabel('Cantidad')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'sentimiento_etiquetas_spanish.png'))
plt.show()
