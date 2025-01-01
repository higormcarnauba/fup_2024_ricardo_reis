# Transformando números em letras
O número 1 corresponde à carta “A” (Ás).
Os números 11, 12 e 13 correspondem às cartas “J”, “Q” e “K” (Valete, Rainha e Rei), respectivamente.
Os outros números permanecem os mesmos.
Leia um vetor contendo a mão de cartas de um jogador e mostre as cartas para o usuário de forma legível, substituindo os números especiais (1, 11, 12, 13) por suas respectivas letras.

## Entrada
A primeira linha contém um número inteiro N (0 ≤ N ≤ 13) representando a quantidade de cartas na mão.
A segunda linha contém N números inteiros representando as cartas do jogador, separados por espaço. Os valores estão entre 1 e 13.
## Saída
Imprima o vetor das cartas formatado entre colchetes [ ], onde cada carta é separada por uma vírgula e um espaço. Substitua os números 1, 11, 12 e 13 por “A”, “J”, “Q” e “K”, respectivamente.

```Python
def corrigirCartas(lista):
    nova_Lista = [i for i in lista]
    for i, valor in enumerate(nova_Lista):
        if valor == 1:
            nova_Lista[i] = 'A'
        elif valor == 11:
            nova_Lista[i] = 'J'
        elif valor == 12:
            nova_Lista[i] = 'Q'
        elif valor == 13:
            nova_Lista[i] = 'K'
    return nova_Lista

qtdCartas = int(input())
cartas = []
#se não for 0, executa
if not qtdCartas == 0:
    cartas = list(map(int, input().split()))
    
print(f'[{", ".join(map(str, corrigirCartas(cartas)))}]')
```