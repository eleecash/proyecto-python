"""
Programa principal para analizar datos de vinos
"""

from functions import read_data, split, reduce, silhouette
import os

def main():
    """
    Función principal que demuestra el uso de las funciones para análisis de vinos.
    """
    try:
        # 1. Leer los datos del archivo CSV
        print("Leyendo datos del archivo winequality.csv...")
        ruta_archivo = os.path.join(os.path.dirname(__file__), "winequality.csv")
        datos = read_data(ruta_archivo)
        print(f"Se han cargado {len(datos)} muestras de vino.\n")
        
        # Mostrar la primera muestra como ejemplo
        print("Ejemplo de la primera muestra:")
        primera_clave = list(datos.keys())[0]
        for atributo, valor in datos[primera_clave].items():
            print(f"  {atributo}: {valor}")
        print()
        
        # 2. Separar los datos por tipo de vino
        print("Separando los datos por tipo de vino...")
        vinos_blancos, vinos_tintos = split(datos)
        print(f"Se encontraron {len(vinos_blancos)} vinos blancos y {len(vinos_tintos)} vinos tintos.\n")
        
        # 3. Extraer valores de atributos específicos
        print("Extrayendo valores de atributos...")
        
        # Extraer valores de alcohol para vinos blancos
        alcohol_blancos = reduce(vinos_blancos, "alcohol")
        print(f"Valores de alcohol para vinos blancos (primeros 5): {alcohol_blancos[:5]}")
        
        # Extraer valores de pH para vinos blancos
        ph_blancos = reduce(vinos_blancos, "pH")
        print(f"Valores de pH para vinos blancos (primeros 5): {ph_blancos[:5]}")
        
        # Extraer valores de alcohol para vinos tintos
        alcohol_tintos = reduce(vinos_tintos, "alcohol")
        print(f"Valores de alcohol para vinos tintos (primeros 5): {alcohol_tintos[:5]}")
        
        # Extraer valores de pH para vinos tintos
        ph_tintos = reduce(vinos_tintos, "pH")
        print(f"Valores de pH para vinos tintos (primeros 5): {ph_tintos[:5]}\n")
        
        # 4. Calcular el coeficiente de Silhouette
        print("Calculando el coeficiente de Silhouette...")
        
        # Comparar alcohol de vinos blancos vs tintos
        silhouette_alcohol = silhouette(alcohol_blancos, alcohol_tintos)
        print(f"Coeficiente de Silhouette para alcohol de vinos blancos: {silhouette_alcohol:.4f}")
        
        # Comparar pH de vinos blancos vs tintos
        silhouette_ph = silhouette(ph_blancos, ph_tintos)
        print(f"Coeficiente de Silhouette para pH de vinos blancos: {silhouette_ph:.4f}")
        
    except FileNotFoundError as e:
        print(f"Ha ocurrido la excepción FileNotFoundError")
    except ValueError as e:
        print(f"Ha ocurrido la excepción ValueError")
    except Exception as e:
        print(f"Ha ocurrido la excepción {type(e).__name__}")

if __name__ == "__main__":
    main()
