valor = int(input("Digite um valor: "))

fibo = [0, 1]
aux = 1

while fibo[aux] < valor:
    fibo.append(fibo[aux-1]+fibo[aux])
    aux = aux + 1

aux2 = 0

for e in fibo:
    if e == valor:
        print("Número informado pertence a sequência de Fibonacci")
        aux2 = 1
        break

if(aux2 == 0):
    print("Número informado não pertence a sequência de Fibonacci")