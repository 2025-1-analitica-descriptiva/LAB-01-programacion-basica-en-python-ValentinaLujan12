"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    """
    suma_por_letra_col4 = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for linea in file:
            partes = linea.strip().split("\t") 
            col2 = int(partes[1])
            col4 = partes[3]

            letras_col4 = col4.split(",") 
            for letra in letras_col4:
                if letra in suma_por_letra_col4:
                    suma_por_letra_col4[letra] += col2
                else:
                    suma_por_letra_col4[letra] = col2

    return dict(sorted(suma_por_letra_col4.items()))

if __name__ == "__main__":
    print(pregunta_11())
