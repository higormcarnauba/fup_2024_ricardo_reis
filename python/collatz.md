# Função Collatz de 2 a 1000

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