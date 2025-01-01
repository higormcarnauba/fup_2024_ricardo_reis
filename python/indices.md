# Para onde foi cada valor
Você recebe uma vetor A de inteiros não negativos de tamanho n. Sua tarefa é ordernar o vetor em ordem crescente e imprimir os índices originais do novo vetor ordenado.

## Entrada
A primeira linha de entrada consiste no tamanho da vetor A. A próxima linha consiste no vetor de tamanho n.

## Saída
A saída consiste em uma única linha de inteiros representando os índices originais de cada elemento no vetor ordenado entre [ ]

## Código da resolução

```Python
tamanho = int(input())
vetor = list(map(int, input().split()))
dicionario = {valor: i for i, valor in enumerate(vetor)}
vetor.sort()
indOri = []
for i in vetor:
    indOri.append(dicionario[i])
    
result = ' '.join(map(str, indOri))
print(f'[ {result} ]')
```