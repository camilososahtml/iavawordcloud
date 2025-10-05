# iavawordcloud, google collab
Wordcloud de opiniones del IAVA en un thread de reddit 

Este proyecto permite generar una wordcloud o nube de palabras a partir de opiniones recopiladas en un archivo CSV. Las palabras más frecuentes se muestran, facilitando el análisis de opiniones.


Librerías utilizadas

pandas
  Librería para manipulación de datos. Se utiliza para leer el archivo CSV con las opiniones y combinar todas las opiniones en un único texto para el WordCloud.

wordcloud  
  Librería principal para generar nubes de palabras. Permite personalizar tamaño, colores, forma, fondo y palabras a ignorar (stopwords).

matplotlib  
  Librería de visualización. Se usa para mostrar el WordCloud en pantalla o guardarlo como imagen.

stopwords(opcional y recmoendado)  
  Conjunto de palabras comunes que se ignoran al generar la nube (por ejemplo, “el”, “la”, “y”, “de”) para que el WordCloud destaque palabras más relevantes. Loa uruguayos usamos muchas muletillas.

- re (expresiones regulares, opcional
  Se puede usar para limpiar el texto, eliminando caracteres no deseados, emojis, links o puntuación innecesaria.
