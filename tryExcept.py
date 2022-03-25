# Una funcion
def funcionDePrueba():
    print("Hola")

# Try - Except
try:
    funcionDePrueba()
except Exception as error:
    print(error)
finally:
    print("Finalizo")