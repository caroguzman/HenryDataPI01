from fastapi import FastAPI
import pandas as pd

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('./Dataset/datosMoviesPI01.csv',  encoding='latin-1')
#instanciamos la clase
app = FastAPI()

@app.get("/")
def index():
    return "Bienvenidos al sistema de Recomendación de Películas de Henry"

@app.get("/peliculas_idioma/{idioma}")
def peliculas_idioma( idioma: str ):
    # Filtro las películas que coincidan con el idioma ingresado
    peliculas_filtradas = df[df['original_language'] == idioma]

    # Obtener la cantidad de películas producidas en el idioma especificado
    cantidad_peliculas = len(peliculas_filtradas)

    # Retornar la cantidad de películas
    return cantidad_peliculas

@app.get("/peliculas_duracion/{pelicula}")
def peliculas_duracion( pelicula: str ):
    # Buscar la película en el DataFrame
    pelicula_filtrada = df[df['title'] == pelicula]

    # Verificar si se encontró la película
    if len(pelicula_filtrada) > 0:
        # Obtener la duración y el año de lanzamiento
        duracion = pelicula_filtrada['runtime'].values[0]
        anio = pelicula_filtrada['release_year'].values[0]

        # Devolver el resultado formateado
        return f"{pelicula}. Duración: {duracion} minutos. Año: {anio}"
    else:
        return "La película no fue encontrada."
    
    
@app.get("/franquicia/{franquicia}")
def franquicia( franquicia: str ):
    franquicia_filtrada = df[df['franquicia'] == franquicia]

    # Verificar si se encontraron películas de la franquicia
    if len(franquicia_filtrada) > 0:
        # Obtener la cantidad de películas, ganancia total y ganancia promedio
        cantidad_peliculas = len(franquicia_filtrada)
        ganancia_total = franquicia_filtrada['revenue'].sum()
        ganancia_promedio = franquicia_filtrada['revenue'].mean()

        # Devolver el resultado formateado
        return f"La franquicia {franquicia} posee {cantidad_peliculas} películas, una ganancia total de {ganancia_total} y una ganancia promedio de {ganancia_promedio}"
    else:
        return "La franquicia no fue encontrada o no tiene películas asociadas."
    
@app.get("/peliculas_pais/{pais}")
def peliculas_pais( pais: str ):
    # Filtrar el DataFrame por el país
    peliculas_pais_filtradas = df[df['paises'].apply(lambda x: pais in x)]

    # Obtener la cantidad de películas producidas en el país
    cantidad_peliculas = len(peliculas_pais_filtradas)

    # Devolver el resultado formateado
    return f"Se produjeron {cantidad_peliculas} películas en el país {pais}"

@app.get("/productoras_exitosas/{productora}")
def productoras_exitosas( productora: str ):
    # Filtrar el DataFrame por la productora
    peliculas_productora = df[df['productoras'].apply(lambda x: productora in x)]
    # Calcular el revenue total
    revenue_total = peliculas_productora['revenue'].sum()
    # Obtener la cantidad de películas realizadas
    cantidad_peliculas = len(peliculas_productora)
    # Devolver el resultado formateado
    return f"La productora {productora} ha tenido un revenue de {revenue_total} y ha realizado {cantidad_peliculas} películas."

@app.get("/get_director/{nombre _director}")
def get_director(nombre_director):
    director_df = df[df['directores'].apply(lambda x: nombre_director in x)]
    # Verificar si se encontró al director
    if len(director_df) > 0:
        # Calcular el éxito del director
        exito = director_df['return'].sum()
        # Crear una lista con los datos requeridos
        lista = []
        for index, director in director_df.iterrows():
            nombre = director['title']
            fecha_release = director['release_date']
            retorno = director['return']
            costo = director['budget']
            ganancia = director['revenue']
            lista.append([nombre, fecha_release, retorno, costo, ganancia])
        
        # Devolver el resultado formateado
        return f"El éxito del director {nombre_director} es: {exito}. Películas: {lista}"
    else:
        return "Director no ha sido encontrado en el dataset"