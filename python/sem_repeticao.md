# String sem repetição
    Faça uma função que receba uma string, e elimine as palavras repetidas dessa string.


## Código da resolução

```Python
ls = "eu moro em uma casa azul em uma casa azul"
y = ls.split()

o = ""
for x in y:
    if (not x in o):
        o+= x+" "
print(o)
```