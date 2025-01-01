# Rubens comendo no Brolio
Dado o número de dias que Rubens registrou seu consumo calórico e as calorias consumidas em cada dia, escreva um programa que calcule a média de calorias consumidas ao longo desses dias.

## Entrada
A primeira linha contém um inteiro N representando o número de dias que ele registrou as calorias.
Nas próximas N linhas, cada linha contém um inteiro X, representando o consumo de calórico no dia.
## Saída
A saída deve ser a média das calorias consumidas ao longo dos dias aferidos, com uma casa decimal.

## Código da resolução

```Python
dias = int(input())
soma = 0

for i in range(dias):
    soma+= int(input())

print(soma/dias)
```