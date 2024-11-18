# String sem repetição

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