consonantes="qwrtypsdfghjklñzxcvbnm"
vocales="aeiou"
signos="+-*/°!#$%&/()='¿?¡¨*+[]{};.,"
estado=True

def contador(letra,lista):
    cant=0
    for j in range(len(lista)):
            if(letra==lista[j]):
                cant+=1
    return cant

def contarLetras(frase):
    cantConsonantes=0
    cantVocales=0
    cantSignos=0
    for i in range(len(frase)):
        cantConsonantes+=contador(frase[i],consonantes)
        cantVocales+=contador(frase[i],vocales)
        cantSignos+=contador(frase[i],signos)
                   
    print("  Cantidad de consonantes:",cantConsonantes)
    print("  Cantidad de vocales:",cantVocales)
    print("  Cantidad de signos:",cantSignos)

try:
    while(estado):
        frase=input("Ingrese un frase (S para salir):")
        
        if(frase=="S"):
            estado=False
            print("Se esta cerrando el programa")
        else:
            print("Frase original:",frase)
            contarLetras(frase.lower())
except Exception as error:
    print(error)

