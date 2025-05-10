"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    resultado = []

    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for linea in file:
            partes = linea.strip().split("\t")
            letra = partes[0]
            col4 = partes[3].split(",") if partes[3] else []
            col5 = partes[4].split(",") if partes[4] else []
            resultado.append((letra, len(col4), len(col5)))

    return resultado

if __name__ == "__main__":
    print(pregunta_10())