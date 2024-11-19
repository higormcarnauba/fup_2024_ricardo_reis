def numZeroNoRabo(i):
    ultimoDig= 0
    qtdZero = 0
    while ultimoDig == 0:
        ultimoDig = i % 10
        if (ultimoDig==0):
            qtdZero+=1
        i//=10
    return qtdZero

fatorial = 1

for num in range(1, 1001):
    fatorial *= num
print(numZeroNoRabo(fatorial))
