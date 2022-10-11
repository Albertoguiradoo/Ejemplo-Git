#Listas en opython
#Definición e inicialización
vNOMBRES = []

#Insertar un dato
vNOMBRES.insert(0,"Juan")
vNOMBRES.insert(1,"Pepe")
vNOMBRES.insert(2,"Inés")
vNOMBRES.insert("Minerva")
vNOMBRES.insert(1,"Rufino")

##Eliminar un elemento
    #vNOMBRES.clear()
vNOMBRES.remove("Pepe")
print("EL nombre borrado es", vNOMBRES.pop(1))

#Ordenar una lista
#Con reverse puedo ordenar en inverso
vNOMBRES.sort(reverse=True)

#Contar en el números de elementos de la lista
print("Minerva aparece: ",vNOMBRES.count("Minerva"),"veces")
print("La lista tiene", len(vNOMBRES),"nombres")

print(vNOMBRES)