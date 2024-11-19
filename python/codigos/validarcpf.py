"""
Questão:
Escreva um programa em Python que leia um CPF (Cadastro de Pessoa Física) 
e verifique se ele é válido. Um CPF válido possui 11 dígitos e deve seguir 
a fórmula de validação dos dígitos verificadores.

Regras para validação do CPF:

1. O CPF possui 11 dígitos, sendo os dois últimos os dígitos verificadores.


2. O primeiro dígito verificador é calculado da seguinte forma:

Multiplique os primeiros 9 dígitos por números decrescentes de 10 a 2.

Some todos os resultados.

Calcule o resto da divisão da soma por 11.

Se o resto for menor que 2, o dígito verificador é 0; caso contrário, é 11 - resto.



3. O segundo dígito verificador é calculado da seguinte forma:

Multiplique os primeiros 10 dígitos (incluindo o primeiro dígito verificador) 
por números decrescentes de 11 a 2.

Some todos os resultados.

Calcule o resto da divisão da soma por 11.

Se o resto for menor que 2, o dígito verificador é 0; caso contrário, é 11 - resto.




O programa deve:

Ler o CPF do usuário como uma string.

Verificar se o CPF possui exatamente 11 dígitos e se todos são números.

Validar o CPF usando a fórmula descrita.

Exibir se o CPF é válido ou inválido.


Exemplo de execução:

Digite o CPF (apenas números): 12345678909
CPF inválido.

Digite o CPF (apenas números): 52998224725
CPF válido.

Dica:

Para facilitar, você pode usar fatias (slicing) de strings e o método isdigit() 
para verificar se o CPF possui apenas números.
"""
def qualDigito(i, aux):
    soma = 0
    
    for dig in i:
        soma += int(dig)*aux
        aux-=1
        
    div = soma%11
    return "0" if div<2 else f"{11-div}"

while True:
    cpf = input("Insira o cpf: \n")
    cpf = cpf.replace(".","").replace("-","")
    cpfTeste = cpf[:-2]

    if (len(cpf)==11):
        cpfTeste += qualDigito(cpfTeste, 10)
        cpfTeste += qualDigito(cpfTeste, 11)
        print("CPF Válido" if cpf==cpfTeste else "CPF Inválido")
        break
    else:
        print("Insira o CPF de forma correta")

