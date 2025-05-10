"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    suma_por_letra_col1 = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for linea in file:
            partes = linea.strip().split("\t")
            letra_col1 = partes[0]
            col5 = partes[4].split(",")
            
            for par in col5:
                clave, valor = par.split(":")
                suma = int(valor)
                
                if letra_col1 in suma_por_letra_col1:
                    suma_por_letra_col1[letra_col1] += suma
                else:
                    suma_por_letra_col1[letra_col1] = suma

    return dict(sorted(suma_por_letra_col1.items()))

if __name__ == "__main__":
    print(pregunta_12())