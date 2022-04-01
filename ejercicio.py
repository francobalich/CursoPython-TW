estado=True
total=0

def suma(numA,numB):
    resultado=numA+numB
    return resultado

try:
    while(estado):
        dato=input("Ingrese el valor del producto o ingrese (S) para salir:")
        if(dato!='S'):
            total=suma(total,int(dato))
        else:
            estado=False
    print("El total es de $",total)
except ValueError:
    print("El valor que ingreso no es valido, intente otra vez.")
except Exception as error:
    print(error)