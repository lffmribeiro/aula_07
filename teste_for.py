# teste para o for

def input_do_usuario():
    i = 0
    palavras = [] 
    while i < 3:
        palavra = input('Digite uma palavra: ')
        palavras.append(palavra)
        i+=1
    return palavras

def printar_palavra_e_tamanho(lista):
    for palavra in lista:
        print(f'a palavra "{palavra}" possui {len(palavra)} caracteres')

def pipeline_teste_for():
    lista = input_do_usuario()
    printar_palavra_e_tamanho(lista)

pipeline_teste_for()