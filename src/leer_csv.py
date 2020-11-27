import csv


def leer_csv():
    ruta_archivo = 'data/empleados.csv'
    with open(ruta_archivo) as archivo_csv:
        lector = csv.reader(archivo_csv)
        for linea in lector:
            print(linea)

def convertir_a_diccionario():
    ruta_archivo = 'data/empleados.csv'
    with open(ruta_archivo) as archivo_csv:
        lector_dic = csv.DictReader(archivo_csv)
        for mapa in lector_dic:
            print(mapa)

if __name__ == '__main__':
    convertir_a_diccionario()
