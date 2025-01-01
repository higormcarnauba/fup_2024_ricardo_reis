# Ingrid quer chegar no céu
A professora Ingrid conta que, em suas brincadeiras de criança, uma das suas atividades favoritas era pular amarelinha. Na versão simplificada, a criança joga a pedra em um número e depois tem que ir pulando um número por vez, sem pisar no número onde a pedra caiu, até chegar ao fim da trilha.

Na brincadeira, o primeiro número é o 0 e o último número é o 10, que as crianças chamam de “céu”.

Vamos ajudá-la a simular essa brincadeira, listando os números que ela deve dizer, excluindo o número onde a pedra caiu.

Dado um número N onde a pedra caiu, você deve imprimir os números que a criança deve dizer, do 0 até o “céu” (representado pelo número 10), excluindo o número onde a pedra caiu.

Se a pedra cair no número 10, não há necessidade de imprimir “céu”, pois o número 10 é o último da sequência.

## Entrada
Um número inteiro N representando onde a pedra caiu.
## Saída
Uma lista de números inteiros entre 0 e 9, substituindo o número 10 por “céu”, excluindo o número N.
## Código da resolução

```Python
pedra = int(input())
amaralinha = [0,1,2,3,4,5,6,7,8,9,'ceu']

amaralinha.pop(pedra)


resposta = ' '.join(map(str, amaralinha))
print(f'[ {resposta} ]')
```