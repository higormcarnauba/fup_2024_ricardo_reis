# Arca quantos exemplares

Faça um programa que retorne uma
nova lista contendo apenas um número de cada.
Devolva um novo vetor, sem números repetidos e ordenado.
Não use uma função de ordenar pronta.

## Entrada
linha 1: um número com a quantidade de elementos do vetor
linha 2: o vetor de inteiros

## Saída
O novo vetor ordenado contendo um exemplar de cada elemento.

## Código da resolução

```Python
tamanhoVet = int(input())
vet = list(map(int, input().split()))
numeros = [0]*10
vetSemRep = []
for i in vet:
    if i<len(numeros):
        numeros[i]+=1
    else:
        while(i>len(numeros)):
            numeros.append(0)
        numeros[i]+=1

for i in range(len(numeros)):
    if numeros[i]>0:
        vetSemRep.append(i)

print(f"{' '.join(map(str, vetSemRep))}")
```