listauno = []
lista_primos = []
lista_primos_srt=[]
lista_primos_srt_a=[]
lista_primos_srt_a_int=[]
lista_final=[]
i=1
while i != 101:
    listauno.append(i)
    i+=1
conteo=len(listauno)
for i in range(conteo):
    ver=0
    for m in range(conteo):
        if listauno[i]%listauno[m]==0:
            ver+=1
    if ver==2:
        lista_primos.append(listauno[i])

for i in range(len(lista_primos)):
    lista_primos_srt.append(str(lista_primos[i]))


for i in range(len(lista_primos_srt)):
    chequeo= lista_primos_srt[i]
    con=len(chequeo)
    a_chq=chequeo[con::-1]
    lista_primos_srt_a.append(a_chq) 


for i in range(len(lista_primos_srt_a)):
    lista_primos_srt_a_int.append(int(lista_primos_srt_a[i]))

for i in range (len(lista_primos_srt_a_int)):
    for m in range(len(lista_primos)):
        if lista_primos[i]==lista_primos_srt_a_int[m]:
            lista_final.append(lista_primos[i])

print(lista_final)