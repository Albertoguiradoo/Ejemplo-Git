#bucle while
'''
i = 0
num =0 
num = int(input("Dime un múnero:\n"))

bandera= True
while (bandera == True):
    i = i+1
    print(num,"x",i,"=",num*(i+1))
    if(i==10):
        bandera = False
'''
#juego
'''
contraSECRETA= "alberto"
contra = input("Dime la contraseña :\n")
while(contra != contraSECRETA):
    print("contraseña incorrecta")
    contra = input("Dime la contraseña :\n")

print("Felicidades has ganado")
'''
#bucle for
#lista=[1,2,3,4,5,6,7,8,9,10]
vNombres = ["Ángel, Alberto , Elena"]
for num in vNombres:
    print(num)