'''
13. Consumo de API Simulado
Objetivo: Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
'''

def input_user():
    try:
        nun1 = int(input('digite um número inteiro: '))
        nun2 = int(input('digite outro número inteiro: '))
        if nun1 < nun2:
            nun_ant = nun1
            nun_dep = nun2
        else:
            nun_ant = nun2
            nun_dep = nun1
        return nun_ant, nun_dep
    except:
        print('Você digitou algo errado. Tente novamente.')
        nun_ant, nun_dep = input_user()
        return nun_ant, nun_dep
    
def print_telas_percorridas(nun_ant, nun_dep):
    while nun_ant <= nun_dep:
        print(f'Você está na página {nun_ant} de um total de {nun_dep}')
        nun_ant+=1
    print('Todas as telas foram processadas')

def pipeline_exer_13():
    nun_ant, nun_dep = input_user()
    print_telas_percorridas(nun_ant, nun_dep)

pipeline_exer_13()