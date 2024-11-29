"""
Crear una función en Python que reciba una lista de números y devuelva su media, el mayor y el
menor de los mismos.
Diseña una aplicación que llene la lista por teclado (la lista sólo contiene números positivos).
Cuando el usuario desee no introducir más números lo indicará.
Llamar a la función anterior y mostrar sus resultados por pantalla.
"""
def operaciones(listaNum):
    max = listaNum[0]
    min = listaNum[0]
    total = 0
    for i in listaNum:
        if(i > max):
            max = i
        if(i<min):
            min = i
        total+=i
    media = total/len(listaNum)
    return media,max,min

listaNumeros = []
condicion = True
condicionNumPositivo = True
while(condicion):
    while(condicionNumPositivo):
        num = int(input("Introduzca un numero positivo: "))
        if(num>0):
            condicionNumPositivo = False
            listaNumeros.append(num)
    seguir = int(input("Introduzca 1 si quiere seguir y dos si quiere dejar de introducir numeros"))
    if(seguir == 2):
        condicion = False
    else:
        condicionNumPositivo = True

media,max,min = operaciones(listaNumeros)
print("Esta es la media: " + str(media) + ", este es el maximo: " + str(max) + " y este es el minimo: " + str(min))

    