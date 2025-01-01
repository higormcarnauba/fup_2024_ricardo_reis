# Invertendo vetor

## Entrada
Um número inteiro N (1 ≤ N ≤ 50), representando a quantidade de elementos no vetor.
N números inteiros, separados por espaços, representando os elementos do vetor.

## Saida
Imprima o vetor invertido, entre colchetes, com os elementos separados por espaços.

## Código da resolução

```Python
tamanhoVetor = int(input())
vetor = list(map(int, input().split()))
a = 0
for i in range(tamanhoVetor-1,(tamanhoVetor//2)-1,-1):
    if a<i:
        vetor[i], vetor[a] = vetor[a], vetor[i]
    a+=1
    
print(vetor)
```