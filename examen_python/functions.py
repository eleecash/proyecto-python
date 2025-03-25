# 1. Crea una función read_data que recibe el nombre de un fichero csv con muestras
# de vino (pruébalo con el fichero winequality.csv o con un csv similar) y devuelve un diccionario
# con el formato que aparece a continuación. A modo de ejemplo, se muestra cómo deberá devolver
# la información de la primera muestra del fichero (primera fila), siendo dato1 una clave que se
# irá incrementando (es decir, dato1, dato2, dato3, etc.). Si hay alguna muestra que tiene algún
# atributo vacío, la muestra no se insertará en el diccionario. Por ejemplo, la segunda muestra del
# fichero no tiene valor en el atributo (volatile acidity) y por tanto, esta muestra (esta fila entera)
# no debería aparecer en el fichero devuelto. Si el fichero tiene menos de 10 líneas con valor en todos
# los atributos, se emitirá un error de tipo ValueError.
# {
# 'dato1': {'type': 'white',
# 'fixed acidity': '7',
# 'volatile acidity': '0.27',
# 'citric acid': '0.36',
# 'residual sugar': '20.7',
# 'chlorides': '0.045',
# 'free sulfur dioxide': '45',
# 'total sulfur dioxide': '170',
# 'density': '1.001',
# 'PH': '3',
# 'sulphates': '0.45',
# 'alcohol': '8.8',
# ...
# }
import pandas as pd # Importar pandas para leer el fichero CSV
import os # Importar os para comprobar si el fichero existe
import math # Importar math para calcular la distancia

def read_data(file):
   
    # Comprobar si el fichero existe
    if not os.path.exists(file):
        raise FileNotFoundError(f"El fichero {file} no existe.")

    # Leer el fichero CSV
    df = pd.read_csv(file)  
    
    # Crear el diccionario
    data_dict = {}
    contador_filas_validas = 0
    
    # Versión mejorada del bucle
    for i in range(len(df)):
        # Obtener la fila actual
        fila = df.iloc[i]
        
        # Verificar si la fila tiene valores nulos
        if fila.isnull().any():
            continue
        
        # Crear diccionario para esta fila
        datos_fila = {}
        
        # Procesar cada columna
        for columna in df.columns:
            datos_fila[columna] = fila[columna]
        
        # Añadir al diccionario principal
        data_dict[f"dato{contador_filas_validas + 1}"] = datos_fila
        contador_filas_validas += 1
    
    # Verificar si hay al menos 10 filas con valores completos
    if contador_filas_validas < 10:
        raise ValueError("El fichero debe tener al menos 10 filas con valores completos.")
    
    return data_dict


# 3. (2 puntos). Crea una función split que recibe un diccionario como el que devuelve el ejercicio
# anterior y devuelve dos diccionarios. El primero es un diccionario con las muestras que tengan el
# valor white en el atributo type y el segundo es un diccionario con los datos que tengan el valor
# red en este atributo. El atributo type se eliminará de cada dato en estos diccionarios devueltos.

def split(diccionario):
    # Crear los diccionarios para white y red
    dict_white = {}
    dict_red = {}
    
    # Recorrer todos los datos del diccionario
    for clave, datos in diccionario.items():
        # Verificar si el dato tiene el atributo type
        if 'type' in datos:
            # Hacer una copia del diccionario de datos para no modificar el original
            datos_copia = datos.copy()
            
            # Obtener el valor de type
            tipo = datos_copia['type']
            
            # Eliminar el atributo type
            del datos_copia['type']
            
            # Añadir al diccionario correspondiente
            if tipo == 'white':
                dict_white[clave] = datos_copia
            elif tipo == 'red':
                dict_red[clave] = datos_copia
    
    return dict_white, dict_red


# 4. (2 puntos). Crea una función reduce que recibe un diccionario con el formato de los que devuelve
# el ejercicio anterior y un string que corresponde al nombre de un atributo. Esta función devuelve
# una lista con los valores de ese atributo. Si el atributo que se le pasa no existe en el diccionario,
# se emitirá un error de tipo ValueError. A modo de ejemplo, si le pasamos un diccionario con los
# datos que son de tipo white y con el atributo alcohol, la lista devuelta será:
# [8.8, 10.1, 9.9, etc.]

def reduce(diccionario, atributo):
    # Lista para almacenar los valores
    valores = []
    
    # Verificar que el diccionario no esté vacío
    if not diccionario:
        raise ValueError(f"El diccionario está vacío.")
    
    # Verificar si el atributo existe en al menos un dato
    atributo_existe = False
    for datos in diccionario.values():
        if atributo in datos:
            atributo_existe = True
            break
    
    # Si el atributo no existe en ningún dato, emitir error
    if not atributo_existe:
        raise ValueError(f"El atributo '{atributo}' no existe en el diccionario.")
    
    # Recorrer todos los datos y extraer los valores del atributo
    for datos in diccionario.values():
        if atributo in datos:
            # Convertir el valor a float de Python
            valores.append(float(datos[atributo]))
    
    return valores


# 5. (2.5 puntos). Crea una función silhouette que recibe dos listas como la que devuelve el ejercicio
# anterior y devuelve el coeficiente de Silhouette de la primera de las listas. Este coeficiente se
# calcula siguiendo la siguiente fórmula:
#
# Silhouette(lista) = media(S(i))
#
# donde S(i) es un coeficiente para cada uno de los datos i de esta lista y que se calcula con la
# siguiente fórmula:
#
# S(i) = [b(i) - a(i)] / maximo[a(i), b(i)]
#
# donde:
# - a(i) es la distancia media entre i y el resto de valores de su lista, donde la distancia entre i y
#   un j≠i se calcularía como √|i-j|².
# - b(i) es la distancia media entre i y todos los valores de la otra lista, calculada de la misma manera.
def silhouette(lista1, lista2):
    
    # Función para calcular la distancia entre dos elementos
    def calcular_distancia(i, j):
        return math.sqrt(abs(i - j)**2)  # Simplificando, esto es igual a abs(i - j), los dos asteriscos son para elevar al cuadrado
    
    # Calcular S(i) para cada elemento i de la primera lista
    valores_s = []
    
    for i_index, i in enumerate(lista1):
        # Calcular a(i): distancia media entre i y el resto de valores de su lista
        suma_distancias_a = 0
        contador_a = 0
        
        for j_index, j in enumerate(lista1):
            if i_index != j_index:  # Excluir el propio elemento i
                suma_distancias_a += calcular_distancia(i, j)
                contador_a += 1
        
        # Evitar división por cero en caso de que la lista solo tenga un elemento
        if contador_a > 0:
            a_i = suma_distancias_a / contador_a
        else:
            a_i = 0
        
        # Calcular b(i): distancia media entre i y todos los valores de la otra lista
        suma_distancias_b = 0
        contador_b = 0
        
        for j in lista2:
            suma_distancias_b += calcular_distancia(i, j)
            contador_b += 1
        
        # Evitar división por cero en caso de que la segunda lista esté vacía
        if contador_b > 0:
            b_i = suma_distancias_b / contador_b
        else:
            b_i = 0
        
        # Calcular S(i) = [b(i) - a(i)] / máximo[a(i), b(i)]
        if max(a_i, b_i) > 0:  # Evitar división por cero
            s_i = (b_i - a_i) / max(a_i, b_i)
            valores_s.append(s_i)
    
    # Calcular la media de todos los S(i)
    if valores_s:  # Verificar que la lista no esté vacía
        return sum(valores_s) / len(valores_s)
    else:
        return 0  # Si la lista está vacía, devolver 0 como valor por defecto
