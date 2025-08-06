import os

restaurantes = [{'nome': 'Restaurante A', 'categoria': 'Italiana', 'ativo': False}, 
                {'nome': 'Restaurante B', 'categoria': 'Japonesa', 'ativo': False}, 
                {'nome': 'Restaurante C', 'categoria': 'Brasileira', 'ativo': True}
                ]

def exibir_nome_do_programa():
      print("Sabor Express - Sistema de Entrega de Alimentos\n")

def exibir_menu():
      print('1. Cadastrar restaurante')
      print('2. Listar restaurantes')
      print('3. Ativar restaurante')
      print('4. Sair')

def voltar_ao_menu_principal():
      input('\nPressione Enter para voltar ao menu principal...')
      os.system('cls')
      main()

def exibir_subtitulo(texto):
      os.system('cls')
      print(f'*** {texto} ***\n')

def finalizar_programa():
      exibir_subtitulo('Finalizando o programa')
      print('Obrigado por usar o Sabor Express!')

def escolher_opcao():
      try:
            opcao_escolhida = int(input('\nEscolha uma opção: '))
            print(f'\nVocê escolheu a opção: {opcao_escolhida}\n' )
            match opcao_escolhida:
                  case 1:
                        cadastrar_restaurante()
                  case 2:
                        listar_restaurantes()
                  case 3:
                        print('Ativar Restaurante')
                        nome_restaurante = input('Digite o nome do restaurante a ser ativado: ')
                        print(f'\nRestaurante {nome_restaurante} ativado com sucesso!')
                  case 4:
                        finalizar_programa()
                  case _:
                        opcao_invalida()
      except:
            opcao_invalida()

def opcao_invalida():
      print('Opção inválida. Por favor, escolha uma opção válida.')
      voltar_ao_menu_principal()

def cadastrar_restaurante():
      exibir_subtitulo('Cadastro de restaurante')
      nome_restaurante = input('Digite o nome do restaurante: ')
      restaurantes.append(nome_restaurante)
      print(f'Restaurante {nome_restaurante} cadastrado com sucesso!')
      voltar_ao_menu_principal()

def listar_restaurantes():
      exibir_subtitulo('Lista de Restaurantes')
      for i, restaurante in enumerate(restaurantes, start=1):
            nome_restaurante = restaurante['nome']
            categoria_restaurante = restaurante['categoria']
            ativo_restaurante = 'Ativo' if restaurante['ativo'] else 'Inativo'
            print(f'{i}. {nome_restaurante} | Categoria: {categoria_restaurante} | Status: {ativo_restaurante}')
      voltar_ao_menu_principal()

def main():
      exibir_nome_do_programa()
      exibir_menu()
      escolher_opcao()

if __name__ == "__main__":
      main()