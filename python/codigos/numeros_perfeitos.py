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

print("Número Perfeito" if numerosDiferentes(y) == True else "Número NÃO é Perfeito")