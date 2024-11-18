ls = "eu moro em uma casa azul em uma casa azul"
y = ls.split()

o = ""
for x in y:
    if (not x in o):
        o+= x+" "
print(o)

# for x in y:
#     qtd = 0
#     ind = 0
#     for y in y:
#         if (x==y):
#             qtd+=1
#             if(qtd>1):
#                 y.pop(ind)
#         ind+=1
# print(y)

# for a in y:
#     if y.count(a)>1:
#         y.pop(y.index(a))

# print(' '.join(y))

