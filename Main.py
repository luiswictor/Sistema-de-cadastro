import defs

def menu():
    while True:
        print("""Bem-vindo(a) ao nosso sistema:

         Digite o numero conforme a opcao desejada
    
            1 - Inserir usuario
            2 - Excluir usuario
            3 - Atualizar usuario
            4 - Informacos de um usuario                                                       
            5 - Informacoes de todos os usuarios
            6 - Sair """)
        opcao = int(input("Insira o numero aqui: "))
        if opcao == 1:
            print('Seguindo para inserçao de usuario')
            defs.cadastro_input()
        elif opcao == 2:
            print('Seguindo para exclusao de usuario')
            defs.exclusao_logica()
        elif opcao == 3:
            print('Seguindo para atualizaçao de usuario')
            defs.atualizar_usuario()
        elif opcao == 4:
            print('Informaçoes de um usuarios')
            ID = input('Digite o Id do usuario desejado:')
            defs.exibir_informacoes(ID)
        elif opcao == 5:
            print('Informaçao de todos os usuarios')
            defs.todos_usuarios()
        elif opcao == 6:
            print('Encerrando programa, Ate a proxima')
            defs.sair()
            break
        else:
            print('Opçao Invalida, Digite um numero valido')


menu()
