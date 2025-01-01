# Cabo de Guerra

Você recebe uma entrada que é um vetor de tamanho T de numeros positivos entre 1 e 10. (T, sempre par, entre 0 e 50). O valor do número representa a força do participante. A primeira metade do vetor representa os participantes do lado Jedi. A segunda metade do vetor representa os participantes do lado Sith. Analise o vetor somando a força dos participantes e escreva o nome do lado que ganhou ou empate (“Jedi”, “Sith”, “Empate”).

## Entrada
1ª linha: número de elementos
Próximas linhas: valor dos elementos.
## Saída
“Jedi”, “Sith”, ou “Empate”

## Código da resolução

```Python
def jogo(tamanho):
    jedi = 0
    sith = 0
    for i in range(tamanho):
        if i < tamanho/2:
            jedi+=int(input())
        else:
            sith+=int(input())
    return 'Jedi' if jedi>sith else 'Empate' if jedi==sith else 'Sith'

tamanho = int(input())
print(jogo(tamanho))
```