def suma(numA,numB):
    resultado=numA+numB
    return resultado

precioA=int(input("Ingrese el valor del primer producto:"))
precioB=int(input("Ingrese el valor del segundo producto:"))
total=suma(precioA,precioB)
print("El total es de $",total)