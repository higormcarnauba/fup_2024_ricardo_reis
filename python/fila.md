# - Separar Pares e Ímpares
Dado um conjunto de números, divida-os em duas listas: uma contendo os números ímpares (alunos) e outra contendo os números pares (servidores). Imprima as listas na ordem em que os números foram inseridos.

## Entrada
Um número inteiro N (1 ≤ N ≤ 50), representando a quantidade de pessoas na fila.
N números inteiros, onde números ímpares representam alunos e números pares representam servidores.
## Saída
Na primeira linha, imprima os números ímpares (alunos) na ordem em que foram inseridos, entre colchetes e separados por espaços.
Na segunda linha, imprima os números pares (servidores) na ordem em que foram inseridos, entre colchetes e separados por espaços.

## Código da resolução

```Python
qtdPessoas = int(input())
vetor = []
if qtdPessoas != 0:
    vetor = list(map(int, input().split()))
impar = []
par = []

for i in vetor:
    if i % 2 == 0:
        par.append(i)
    elif i % 2 !=0:
        impar.append(i)
    else:
        pass
impar = f"[ {' '.join(map(str, impar))} ]" if impar else '[ ]'
par = f"[ {' '.join(map(str, par))} ]" if par else '[ ]'
print(impar)
print(par)
```