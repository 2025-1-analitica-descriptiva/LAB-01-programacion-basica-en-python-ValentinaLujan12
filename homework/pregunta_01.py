"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    total = 0
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            partes = line.strip().split("\t")
            if len(partes) > 1:
                total += int(partes[1])
    return total

if __name__ == "__main__":
    print(pregunta_01())