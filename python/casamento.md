# Maior e menor

Escreva um programa onde receba um vetor de tamanho 5 e que dê como saída a soma do maior e do menor elemento deste vetor. Assuma que você não conhece o limite superior ou inferior dos elementos que estão no vetor.

### Entrada
Um vetor possuindo 5 elementos.
### Saída
A soma do maior elemento com o menor.

## Código da resolução

```Python
vetor = list(map(int, input().split()))
maior = vetor[0]
menor = vetor[0]

for i in vetor:
    if i >= maior:
        maior = i
    if i <= menor:
        menor = i
        
        
print(maior+menor)
```