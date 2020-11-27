# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
'''
Comentario multilínea con comillas
'''



def diccionarios():
    ejemplo_diccionario = {
        "str": "esto es un string",
        "float": 1.540,
        "int": 1
    }
    for key,val in ejemplo_diccionario.items():
        print(f"{key}={val}")


def printstring():
    string = "hola de nuevo"
    print(string)

def iterate():
    for x in range(0, 6, 2):
        print(x)
        if x == 14:
            break


def print_hi(name):
    print(f'Hi, {name}')
    print('lo que yo quiera')


# __name__ variable implícita dentro de cada programa de python
if __name__ == '__main__':
    print_hi('María Belén')
    iterate()
    printstring()
    diccionarios()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
