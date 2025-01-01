# Abastecimento de agua
Imprima o vetor com a quantidade de água que cada casa foi abastecida.

## Entrada
N (quantidade de casas) e Q (quantidade decaminhões)

Nas próximas Q linhas: o ponto A, B e a quantidade inteira L de água de cada caminhão.

## Saída
Vetor com o total de água de cada casa.

## Código da resolução

```Python
qtd = list(map(int, input().split()))
vetor = [0]*(qtd[0])

for i in range(qtd[1]):
    pontos = list(map(int, input().split()))
    for j in range(pontos[0], pontos[1]+1):
        vetor[j] += pontos[2]
        
print(f'{" ".join(map(str, vetor))}')
```