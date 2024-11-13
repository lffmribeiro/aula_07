#Esse código tem como finalidade fazer um ensaio de condicionais

def coletar_input_do_usuario():
    try:
        x = int(input('Por favor digite um número: '))
        return x
    except:
        print('Você digitou um valor errado. Tente novamente.')
        x = coletar_input_do_usuario()
        return x
    
def pritar_para_o_usuario(x):
    if x < 0:
        print('O número é menor que zero')
    elif x == 1:
        print('O número é igual a um.')
    elif x == 2:
        print('O número é igual a dois.')
    else:
        print('O número é maior que 2.')

def pipeline_teste_condicional():
    x = coletar_input_do_usuario()
    pritar_para_o_usuario(x)

pipeline_teste_condicional()