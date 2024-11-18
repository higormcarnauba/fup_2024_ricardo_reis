# def collatz(i):
#     qtd = 1
#     while(i!=1):
#         if(i%2==0):
#             i/=2
#             print(f"{i:.0f}", end=' ')
#             qtd+=1
#         else:
#             i = ((i*3)+1)/2
#             print(f"{i:.0f}", end=' ')
#             qtd+=1
#     print('\n')
#     return qtd


# maior = 0
# indMaior = 0
# for i in range(2, 1001):
#     print(f"A sequência de collatz do número {i} é: ")
#     a = collatz(i)
#     if (a>maior):
#         maior = a
#         indMaior = i
        
# print(f'A maior sequencia de collatz foi do número {indMaior} e o intervalo foi de {maior} números')

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

