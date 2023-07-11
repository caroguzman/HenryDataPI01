<em> #PROYECTO INDIVIDUAL Nº1</em>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

## Objetivo
Crear un modelo de ML que soluciona un problema de negocio de en una start-up que provee servicios de agregación de plataformas de streaming.
## Deesarrollo
Para llevar a cabo el proyecto se definieron diferentes etapas de desarrollo:
- **`Transformaciones`**_(Extract, Transform, and Load-ETL)_
  Se llevó a cabo los procesos de transformación de los datos que nos entrega la empresa, depurando cada columna del dataset como nos fue indicado.
  (https://henry-pi01.onrender.com/docs)
- **`Desarrollo API`** _(FastAPI)_
  Se desarrollaron 6 funciones para los endpoints de la api:
    - def **peliculas_idioma( *`Idioma`: str* )**:
      Se ingresa un idioma (como están escritos en el dataset) y retorna la cantidad de películas producidas en ese idioma.
    - def **peliculas_duracion( *`Pelicula`: str* )**:
      Se ingresa una pelicula y retorna la duracion y el año de la película.
    - def **franquicia( *`Franquicia`: str* )**:
      Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio.
    - def **peliculas_pais( *`Pais`: str* )**:
      Se ingresa un país (como están escritos en el dataset) y retorna la cantidad de peliculas producidas en el país ingresado.
    - def **productoras_exitosas( *`Productora`: str* )**:
      Se ingresa la productora y la función retorna el revunue total y la cantidad de peliculas que realizó.
    - def **get_director( *`nombre_director`* )**:
      Se ingresa el nombre de un director que se encuentre dentro del dataset y devuelve el éxito del mismo medido a través del retorno. El nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma, en formato lista.
- **`Deployment`**_(render)_
  (https://henry-pi01.onrender.com/docs)
  Para llevar a cabo el deployment de la API se utilizó render.
- **`Análisis exploratorio de los datos`**: _(Exploratory Data Analysis-EDA)_
  Se investiga las relaciones que hay entre las variables de los datasets, se buscan outliers o anomalías, se normalizan las variables que van a ser utilizadas en el modelo.Se realiza un diagrama de nube de palabras. 
- **`Sistema de recomendación`**: Se implementó Similitud del coseno y se puede consumir desde la API con la función:
  - def **recomendacion( *`titulo`* )**:
    donde se ingresa el nombre de una película y el sistema te recomienda las películas similares en una lista de 5 valores.
- **`Video`**: Se realiza un video mostrando el resultado de las consultas propuestas y del modelo de ML entrenado.

## Documentación
[EDA](https://medium.com/swlh/introduction-to-exploratory-data-analysis-eda-d83424e47151)
[Cosine Similarity and TFIDF](https://medium.com/web-mining-is688-spring-2021/cosine-similarity-and-tfidf-c2a7079e13fa) <br>
[Finding Word Similarity using TF-IDF and Cosine in a Term-Context Matrix from Scratch in Python](https://towardsdatascience.com/finding-word-similarity-using-tf-idf-in-a-term-context-matrix-from-scratch-in-python-e423533a407)<br>

[FastAPI](https://www.youtube.com/watch?v=J0y2tjBz2Ao)<br>
[render](https://github.com/HX-FNegrete/render-fastapi-tutorial)

## Conclusiones
El modelo se entrena con el dataset reducido debido a la memoria requerida. En un futuro sería oportuno mejorar el modelo para poder entrenarlo con el dataset completo.Y también poder incorporar más variables al desarrollo del modelo. También se podría profundizar en el EDA en la normalización de las variables.
