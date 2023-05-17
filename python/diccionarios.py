#Para poder examinar la palabra clave del dicionario podemos usar items()
dictionary=dict({
    "Hello": "Hola",
    "What?": "Que?",
    "Lastname": "Apellido"
})

for english, español in dictionary.items():
    print("Ing/Esp ->", english, ": ", español)

#Para comprovar si una clave existe podemos usar la clave reservada in
dictionary = { 
    "Hello": "Hola",
    "What?": "QUe?",
    "Name": "Nombre"
}

if "Hello" in dictionary: #Si la palabra existe en el dicionario debe decir que existe sino debe decir inexistente
    print("Existente")
else:
    print("Inexistente")


#Para eliminar un elemento se usa del pero para eliminar todos los elemtos usamos clear
#del
dictionary = { #Creamos el dicionario 
    "Hello": "Hola",
    "What?": "QUe?",
    "Name": "Nombre"
}

print(len(dictionary))
del dictionary["Hello"] #Borramos solo una palabra
print(dictionary)

#clear
dictionary = { #Creamos el dicionario 
    "Hello": "Hola",
    "What?": "QUe?",
    "Name": "Nombre"
}

dictionary.clear() #Borramos todo el dicionario
print(len(dictionary))

del dictionary