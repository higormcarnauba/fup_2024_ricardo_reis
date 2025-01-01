# Busca intervalada

Dado uma lista de número e um intervalo, calcule quantas vezes um número cai dentro do intervalo fechado. Em um intervalo fechado os valores inferior e superior também fazem parte do intervalo.

## Entrada
1a linha Quantidade N de elementos do vetor, Limite inferior e limite superior.
Próximas linhas: N números inteiros.
## Saída
Números inteiros que estão dentro do intervalo, incluindo os limites.

## Código da resolução

```Python
def dentroIntervalo(lista):
    qtdDentro = 0
    for n in range(lista[0]):
        num = int(input())
        if num >= lista[1] and num <= lista[2]:
            qtdDentro+=1
    return qtdDentro

lista = list(map(int, input().split()))
print(dentroIntervalo(lista))
```