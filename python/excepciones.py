#Ejercicios Errores con excepciones
#ZeroDivisiorError
while True:
    try:
        number = int(input("Ingresa un valor: "))
        print(15/number)
        break
    except ZeroDivisionError:
        print("El valor ingresado no es valido...")
    except:
        print("Lo siento. Se me hace imposible realizar una division con 0...")

#ValueError
while True:
    try:
        number = int(input("Digita un valor: "))
        print(7/number)
        break
    except ValueError:
        print("Lo siento no detectamos el valor...")
    except:
        print("Advertencia: El valor digitado no es valida porfavor cambiarlo...")

#TypeError


#AttributeError


#SyntaxError

