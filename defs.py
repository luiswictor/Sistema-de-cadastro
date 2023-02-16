import json
import time


local_arquivo = r'\Users\Luis Wictor\Desktop\Projeto II\projetoModuloII.json'
with open(local_arquivo, 'r', encoding='utf-8') as cadastro:
    dados = json.load(cadastro)


def inserir_usuario(nome, telefone='Não informado', endereco='Não informado'):
    alterou = False
    for i in dados:
        if nome == dados[i]['Nome'] and telefone == dados[i]['Telefone'] and endereco == dados[i]['Endereço']:
            dados[i]['Status'] = True
            alterou = True

    if not alterou:
        adic_usuarios = dict()
        adic_usuarios['Status'] = True
        adic_usuarios['Nome'] = nome
        adic_usuarios['Telefone'] = telefone
        adic_usuarios['Endereço'] = endereco
        dados[(len(dados.keys()) + 1)] = adic_usuarios

        


def escrever_arquivo():
    with open(local_arquivo, 'w+', encoding='utf-8') as cadastro:
        json.dump(dados, cadastro, indent=4, ensure_ascii=False)



def cadastro_input():
    while True:
        nome = str(input('Digite seu nome'))
        while True:
            if nome == '':
                print('Você não digitou seu nome')
                nome = str(input('Digite seu nome'))
            else:
                break
        telefone = input('Digite seu telefone:')
        endereco = str(input('Digite seu endereço'))
        if telefone == '' and endereco == '':
            inserir_usuario(nome)
        elif endereco == '' and telefone != '':
            inserir_usuario(nome, telefone)
        elif endereco != '' and telefone == '':
            inserir_usuario(nome, endereco)
        else:
            inserir_usuario(nome, telefone, endereco)
            time.sleep(1)
        resposta = input('Quer adicionar mais algum usuario? S/N?').upper()
        if resposta == 'N':
            escrever_arquivo()
            break

def exclusao_logica():
    while True:
        ID = input('Digite aqui o id do usuario que você quer acessar:')
        if ID in dados:
            dados[ID]['Status'] = False
            escrever_arquivo()
            time.sleep(1)
            print('Usuario excluido')
            break
        elif ID not in dados:
            time.sleep(1)
            print('usuario não encontrado')



    time.sleep(1)

def atualizar_usuario():
    while True:
        ID = input('Digite aqui o id do usuario que você quer acessar:')
        if ID not in dados:
            print('usuario não encontrado')
        else:
            print('Usuario encontrado')
            break

    alterar = int(input('Qual informação do usuario você deseja alterar? [1-Nome] [2-Telefone] [3-Endereço]'))
    if alterar == 1:
            nome = input('insira o nome:')
            dados[ID]['Nome'] = nome
            escrever_arquivo()
            time.sleep(1)
            print('nome alterado com sucesso')
    elif alterar == 2:
            telefone = input('insira o telefone:')
            dados[ID]['Telefone'] = telefone
            escrever_arquivo()
            time.sleep(1)
            print('Telefone alterado com sucesso')
    elif alterar == 3:
            endereco = input('insira o endereço:')
            dados[ID]['Endereço'] = endereco
            escrever_arquivo()
            time.sleep(1)
            print('Endereço alterado com sucesso')

def exibir_informacoes(ID):
    if ID not in dados:
        print('usuario não encontrado')
    else:
        print('Usuario encontrado')
        print(f'Nome: {dados[ID]["Nome"]} ')
        print(f'Telefone: {dados[ID]["Telefone"]} ')
        print(f'Endereço {dados[ID]["Endereço"]} ')

    time.sleep(1)


    time.sleep(1)

def todos_usuarios():
    for i in dados:
        if dados[i]['Status'] == True:
            print(f'ID: {i}')
            print(f'Nome: {dados[i]["Nome"]} ')
            print(f'Telefone: {dados[i]["Telefone"]} ')
            print(f'Endereço: {dados[i]["Endereço"]}\n ')
            time.sleep(1)


    time.sleep(2)

def sair():
    print('tchau e obrigado')