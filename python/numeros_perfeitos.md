# Descubra se o número é perfeito
    Faça um função que receba um número aleatório, e verifique se esse número possui digitos repetidos
    se possuir, imprima que o Número não é perfeito, se não possuir digitos repetidos retorne que o número
    é perfeito

## Código da resolução

```Python
def numerosDiferentes(i):
    digitosVistos = []
    while i > 1:
        digito = i%10
        if digito in digitosVistos:
            return False
        digitosVistos.append(digito)
        i //= 10
    return True

y = 9876543210

if numerosDiferentes(y) == True:
    print("Número Perfeito")
else:
    print("Número NÃO é Perfeito")
```