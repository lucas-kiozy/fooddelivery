import os

def exibir_nome_do_programa():
      print("Sabor Express - Sistema de Entrega de Alimentos\n")

def exibir_menu():
      print('1. Cadastrar restaurante')
      print('2. Listar restaurantes')
      print('3. Ativar restaurante')
      print('4. Sair')


def finalizar_programa():
      os.system('cls')
      print('Encerrando o programa. Obrigado por usar o Sabor Express!')
      print('...\n')

def escolher_opcao():
      opcao_escolhida = int(input('\nEscolha uma opção: '))
      print(f'\nVocê escolheu a opção: {opcao_escolhida}\n' )
      match opcao_escolhida:
            case 1:
                  print('Cadastrar Restaurante')
                  nome_restaurante = input('Digite o nome do restaurante: ')
                  print(f'\nRestaurante {nome_restaurante} cadastrado com sucesso!')
            case 2:
                  print('Listar Restaurantes')
            case 3:
                  print('Ativar Restaurante')
                  nome_restaurante = input('Digite o nome do restaurante a ser ativado: ')
                  print(f'\nRestaurante {nome_restaurante} ativado com sucesso!')
            case 4:
                  finalizar_programa()
            case _:
                  print('Opção inválida. Encerrando o programa.')
                  finalizar_programa()

def main():
      exibir_nome_do_programa()
      exibir_menu()
      escolher_opcao()

if __name__ == "__main__":
      main()