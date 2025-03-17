# Análisis de Sentimientos en Tweets (Español)

Este proyecto utiliza la librería [sentiment-analysis-spanish](https://pypi.org/project/sentiment-analysis-spanish/) para analizar el sentimiento en tweets escritos en español. Se procesa el texto (limpieza de URLs, menciones, hashtags, números y más), se evalúan los puntajes de sentimiento y se clasifican los tweets como **positivo**, **negativo** o **neutro**. Además, se explora la relación entre la longitud del tweet y su puntaje de sentimiento mediante visualizaciones.

## Requisitos

- Python 3.x
- [pandas](https://pandas.pydata.org/)
- [matplotlib](https://matplotlib.org/)
- [scikit-learn](https://scikit-learn.org/)
- [sentiment-analysis-spanish](https://pypi.org/project/sentiment-analysis-spanish/)

Para instalar las dependencias, ejecuta:

pip install pandas matplotlib scikit-learn sentiment-analysis-spanish

Uso
Datos:
Coloca el archivo tweets.csv dentro de la carpeta data/ con los tweets que deseas analizar.

Ejecución:
Ejecuta el script principal:

python tweet_sentiment_analysis.py

El script realiza lo siguiente:

Limpia los tweets (eliminando URLs, menciones, hashtags, números, etc.).
Calcula el puntaje de sentimiento para cada tweet utilizando el analizador para español.
Clasifica los tweets en positivo, negativo o neutro (con umbrales ajustables).
Genera y guarda visualizaciones en la carpeta outputs/.
Visualizaciones:
El proyecto genera:

Histograma de Puntajes: Muestra la distribución de los puntajes de sentimiento.
Distribución de Etiquetas: Gráfico de barras que indica la cantidad de tweets clasificados en cada categoría.
Relación Longitud vs. Sentimiento: Gráfica de dispersión que relaciona la longitud (número de caracteres) de cada tweet con su puntaje de sentimiento.
Análisis y Conclusiones
Limpieza del Texto:
El proceso de limpieza elimina ruido y elementos innecesarios, permitiendo que el analizador se enfoque en el contenido relevante del tweet.

Resultados del Análisis:
La herramienta para español proporciona puntajes que se traducen en clasificaciones de sentimiento. En el dataset analizado, se observa una tendencia mayor hacia tweets negativos, con un porcentaje menor de positivos y muy pocos neutros.

Distribución de Puntajes:
El histograma revela que la mayoría de los tweets tienen puntajes concentrados en rangos bajos, lo que indica una tonalidad negativa predominante.

Relación Longitud vs. Sentimiento:
La gráfica de dispersión sugiere que, en algunos casos, los tweets más largos pueden transmitir sentimientos más definidos. Aunque la relación no es muy marcada, se recomienda realizar análisis estadísticos adicionales (por ejemplo, correlación de Pearson o Spearman) para profundizar en esta relación.
