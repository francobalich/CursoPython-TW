lista=["A","B","C","D"]

diccionario={"A":["1","2","3"],"B":"BBBBBB","C":"CCCCCC"}

for i in diccionario:
    print(diccionario[i])
    if diccionario[i]=="BBBBBB":
        diccionario[i]="Hola"

print(diccionario)
