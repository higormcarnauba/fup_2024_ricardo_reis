# Sapinho 2 morrendo no poço
O sapo começa no fundo de um poço de profundidade P cm.
A cada salto ele sobe S centímetros.
Enquanto se recupera para o próximo salto, ele escorrega E centímetros.
A cada salto o sapinho fica mais cansado e o próximo salto será 10 cm menor.
Se ele ficar abaixo da agua ele morrerá afogado.

## Entrada
P, S, E inteiros, um por linhas.

## Saída
as posições de salto e aterrissagem do sapinho até que ele saia ou morra afogado.

## Código da resolução

```Python
tamanhoPoco = int(input())
puloDoSapo = int(input())
cmEscorregados = int(input())
posicaoSapo = 0

while posicaoSapo<=tamanhoPoco:
    if posicaoSapo<0:
        print(posicaoSapo, 'morreu')
        break
    elif posicaoSapo+puloDoSapo>=tamanhoPoco:
        print(posicaoSapo, 'saiu')
        break
    else:
        print(posicaoSapo, posicaoSapo+puloDoSapo)
    posicaoSapo+=puloDoSapo-cmEscorregados
    if puloDoSapo>=10:
        puloDoSapo-=10
```