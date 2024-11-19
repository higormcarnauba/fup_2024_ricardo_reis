# Função Collatz
    Faça uma função que receba um número, se esse número for par, divida ele por 2,
    Se for ímpar multiplique ele por 3, some 1, e depois divida por 2
    Depois adicione esse número a uma lista, até que o número se torne um, Depois retorne essa lista
    e imprima na tela.
    
    Desafio: Você pode tentar fazer de uma forma que descubra entre 2 a 1000 qual número possui
    a maior sequência da função de collatz, e dizer qual é o intervalo dessa sequência


## Código da resolução

```Python
def collatz(i):
    lista = [i]
    while i>1 :
        if (i%2==0):
            i= i//2
        else:
            i = (i*3+1)//2
        lista.append(i)
    return lista

if __name__ == "__main__":
    for i in range(20):
        print(collatz(i))
```