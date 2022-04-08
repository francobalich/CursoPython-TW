var=100

tupla=("A","B","C","D")
listaNums=range(1,9)
chat=["Angel","Raptor","drkbugs","franco"]

num=0
for i in listaNums:
    print(i)

while num < len(tupla):
    if(tupla[num]=="A"):
        tupla[num]="Z"
    print(tupla[num])
    num=num+1

print(tupla)