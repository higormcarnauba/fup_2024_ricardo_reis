# O segredo do cofre - OBI 2017

O sistema de segredo para abrir esse cofre é bastante complexo. Ao invés de girar um botão várias vezes, como a gente vê normalmente nos filmes, o dono do cofre tem que deslizar um controle para a esquerda e para a direita, em cima de uma barra, várias vezes, parando em determinadas posições. A barra possui N posições e cada posição contém um número inteiro entre 0 e 9, inclusive. No exemplo da figura, a barra tem 14 posições e o controle está na posição 1.

O segredo vai depender de quantas vezes cada um dos dez inteiros entre 0 e 9 vai aparecer dentro do controle. Por exemplo, suponha que o dono deslize o controle da posição inicial 1 até a posição 9, depois para a posição 4, depois para a posição 11 e por fim até a posição 13. Veja que o inteiro 1, por exemplo, vai aparecer seis vezes dentro do controle; e o inteiro 9 vai aparecer quatro vezes.

Dada a sequência de inteiros na barra e a sequência de posições entre as quais o dono desliza o controle, começando da posição inicial 1, seu programa deve contar quantas vezes cada inteiro, entre 0 e 9, vai aparecer dentro do controle.

## Entrada
A primeira linha da entrada contém dois inteiros N e M, representando o número de posições na barra do cofre e o número de posições na sequência que o dono vai seguir para deslizar o controle. A segunda linha contém N inteiros entre 0 e 9, definindo a barra do cofre. A terceira linha contém M inteiros representando a sequência de posições que o dono vai seguir. A primeira posição nessa sequência é sempre 1 e não há duas posições consecutivas iguais.
## Saída
Seu programa deve imprimir uma linha contendo 10 inteiros, representando o número de vezes que cada inteiro, entre 0 e 9, vai aparecer no controle da barra.

## Código da resolução

```Python
variaveis = list(map(int, input().split()))
barraCofre = list(map(int, input().split()))
sequenciaPosicoes = list(map(int, input().split()))
vetor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

sequenciaPosicoes = [i-1 for i in sequenciaPosicoes] 

for i in range(variaveis[1]-1):
    indiceAtual = sequenciaPosicoes[i]
    proximoIndice = sequenciaPosicoes[i+1]
    
    if indiceAtual > proximoIndice:
        indiceAtual, proximoIndice = proximoIndice, indiceAtual
    
    for j, valor in enumerate(barraCofre[indiceAtual:proximoIndice+1]):
        vetor[valor] += 1
        
    if i >0:
        vetor[barraCofre[sequenciaPosicoes[i]]] -= 1
        

print(f'[ {" ".join(map(str, vetor))} ]')
```