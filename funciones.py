estado=True
total=0

def suma(numA,numB):
    resultado=numA+numB
    return resultado
    
while(estado):
    precio=int(input("Ingrese el valor del producto:"))
    total=suma(total,precio)
    respuesta=input("Desea continuar?(Y/N)")
    if(respuesta=='N'):
        estado=False

print("El total es de $",total)