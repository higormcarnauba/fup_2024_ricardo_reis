# Botas trocadas - OBI 2017
Escreva um programa que, dada a lista contendo a descrição de cada bota entregue, determina quantos pares corretos de botas poderão ser formados no total.

## Entrada
A primeira linha da entrada contém um inteiro N indicando o número de botas individuais entregues. Cada uma das N linhas seguintes descreve uma bota, contendo um número inteiro M e uma letra L, separados por um espaço em branco. M indica o número do tamanho da bota e L indica o pé da bota: L= ‘D’ indica que a bota é para o pé direito, L= ‘E’ indica que a bota é para o pé esquerdo.
## Saída
Seu programa deve imprimir uma única linha contendo um único número inteiro indicando o número total de pares corretos de botas que podem ser formados.

## Código da resolução

```Python
qtdBotas = int(input())
paresDeBotas = {}
qtdParBotas = 0

for i in range(qtdBotas):
    vetor = input().split()
    if vetor[0] in paresDeBotas:
        if vetor[1] not in paresDeBotas[vetor[0]]:
            paresDeBotas[vetor[0]].update({vetor[1]: 1})
        else:
            paresDeBotas[vetor[0]][vetor[1]] += 1
    else:
        paresDeBotas[vetor[0]] = {vetor[1]:1}

for chave, valor in paresDeBotas.items():
    if 'D' in valor and 'E' in valor:
        if valor['D']>=1 and valor['E']>=1:
                if valor['D']>=valor['E']:
                    qtdParBotas += valor['E']
                else:
                    qtdParBotas += valor['D']

print(qtdParBotas)
```