# É permutação
Verifique se um número é permutacao de outro
Dados 2 Inteiros, retornar se ambos são permutação entre si.

## Entrada
2 Inteiros , A e B.
## Saída
“True”, se A é permutação de B.
“False”, se A não é permutação de B.

## Código da resolução

```Python
def ehperm(lista1):
    if len(lista1[0]) != len(lista1[1]):
        return False
    for i in lista1[0]:
            if not i in lista1[1]:
                return False
    return True
    
vetor = input().split()
print(ehperm(vetor))
```