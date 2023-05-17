#Ejercicios Errores con excepciones
#ZeroDivisiorError

#Se escribe try para el intento de lo que queremos hacer
try:
    num=int(input("Escribe un numero: ")) #identacion
    print("El resultado es", 1/num)
#Si no puede aparecera el error
except ZeroDivisionError:
    print("Me queda muy dificil resolver una division con 0") #Lo que hace es evitar que aparecan una cantidad de texto que muestra el error

#ValueError: Este pasa cuando se digitan mal los numero en una operacion ejemplo que si en una division hay decimales o no

#Se escirbe try para el intento de lo que deseamos que haga el usuario
try:
    num=int(input("porfavor ingresar un valor: ")) #La identacion de lo que se desea reaalizar
    print("El resultado es", 1/num)
#Si no puede aparecera el siguiente error
except ValueError:
    print("Lo siento. No puedo hacer esa operacion")

#IndexError: Este se arroja cuando en una lista no se cumple con los requesitos dados

#Se crea una lista con diferentes argumentos de manera ordenada
list=[1,2,3,4,5,6]

#Se escribe try para el intento de lo que deseamos que haga el usuario
try:
    num=int(input("Ingrese un valor: ")) #El intento que se desea que el usuario ingrese colocando un numero de manera aleatoria
    print(list[num]) #Se coloca la lista y se le añaden los numeros que puede ingresar
except IndexError:
    print("Lo siento no detecto ese numero en la lista")
