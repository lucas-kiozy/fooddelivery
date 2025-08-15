import os

restaurantes = [{'nome': 'Restaurante A', 'categoria': 'Italiana', 'ativo': False}, 
                {'nome': 'Restaurante B', 'categoria': 'Japonesa', 'ativo': False}, 
                {'nome': 'Restaurante C', 'categoria': 'Brasileira', 'ativo': True}
                ]

def exibir_nome_do_programa():
      '''Essa função exibe o nome do programa no console.'''
      print("Sabor Express - Sistema de Entrega de Alimentos\n")

def exibir_menu():
      '''Essa função exibe o menu principal do programa, apresentando as 4 opções disponíveis para o usuário.'''
      print('1. Cadastrar restaurante')
      print('2. Listar restaurantes')
      print('3. Ativar restaurante')
      print('4. Sair')

def voltar_ao_menu_principal():
      '''Essa função aguarda o usuário pressionar Enter para voltar ao menu principal e limpa a tela do console.'''
      input('\nPressione Enter para voltar ao menu principal...')
      os.system('cls')
      main()

def exibir_subtitulo(texto):
      '''Essa função exibe um subtítulo formatado no console.
      
      Inputs:
      - texto: String que será exibida como subtítulo.
      Outputs:
      - Exibe o subtítulo formatado no console.
      '''
      os.system('cls')
      #os.system('cls')
      print(f'\n*** {texto} ***\n')

def finalizar_programa():
      '''Essa função exibe uma mensagem de finalização do programa e encerra a execução.'''
      exibir_subtitulo('Finalizando o programa')
      print('Obrigado por usar o Sabor Express!\n')

def escolher_opcao():
      '''Essa função solicita ao usuário que escolha uma opção do menu e executa a ação correspondente.
      
      Inputs:
      - opcao_escolhida: Número da opção escolhida pelo usuário.
      Outputs:
      - Executa a ação correspondente à opção escolhida, como cadastrar restaurante, listar restaurantes, ativar/desativar restaurante ou finalizar o programa.
      '''
      exibir_menu()
      try:
            opcao_escolhida = int(input('\nEscolha uma opção: '))
            print(f'\nVocê escolheu a opção: {opcao_escolhida}\n' )
            match opcao_escolhida:
                  case 1:
                        cadastrar_restaurante()
                  case 2:
                        listar_restaurantes()
                        voltar_ao_menu_principal()
                  case 3:
                        alternar_estado_restaurante()
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
      '''Essa função é responsável por cadastrar um novo restaurante.
      
      Inputs:
      - nome_restaurante: Nome do restaurante a ser cadastrado.
      - categoria: Categoria do restaurante a ser cadastrada.

      Outputs:
      - dados_restaurante: Dicionário contendo os dados do restaurante cadastrado.
      - restaurantes: Lista atualizada com o novo restaurante adicionado.
      '''
      exibir_subtitulo('Cadastro de restaurante')
      nome_restaurante = input('Digite o nome do restaurante: ')
      categoria = input(f'Digite a categoria do restaurante {nome_restaurante}:')
      dados_restaurante = {
            'nome': nome_restaurante,
            'categoria': categoria,
            'ativo': False
      }
      restaurantes.append(dados_restaurante)
      print(f'\nRestaurante {nome_restaurante} cadastrado com sucesso!')
      voltar_ao_menu_principal()

def listar_restaurantes():
      '''Essa função é responsável por listar os restaurantes cadastrados.
      
      Outputs:
      - restaurantes: Lista de dicionários contendo os dados dos restaurantes cadastrados.'''
      exibir_subtitulo('Lista de Restaurantes')
      print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(15)} | Status')
      for i, restaurante in enumerate(restaurantes, start=1):
            nome_restaurante = restaurante['nome']
            categoria_restaurante = restaurante['categoria']
            ativo_restaurante = 'Ativo' if restaurante['ativo'] else 'Inativo'
            print(f'{i}. {nome_restaurante.ljust(19)} | {categoria_restaurante.ljust(15)} | {ativo_restaurante}')

def alternar_estado_restaurante():
      '''Essa função é responsável por ativar ou desativar um restaurante, alternando seu estado atual.
      
      Inputs:
      - numero_restaurante: Número do restaurante a ser ativado ou desativado, escolhido pelo usuário.
      
      Outputs:
      - restaurante: Dicionário do restaurante cujo estado foi alterado.
      - status: String indicando o novo estado do restaurante (Ativado ou Desativado).
      '''
      listar_restaurantes()
      exibir_subtitulo('Ativar/Desativar Restaurante')
      numero_restaurante = int(input('\nDigite o número do restaurante que deseja ativar/desativar: '))
      if 1 <= numero_restaurante <= len(restaurantes):
            restaurante = restaurantes[numero_restaurante - 1]
            restaurante['ativo'] = not restaurante['ativo']

            if restaurante['ativo'] :
                  status = 'Ativado' 
            else:
                  status = 'Desativado'
            print(f'\nRestaurante {restaurante["nome"]} foi {status} com sucesso!')
      voltar_ao_menu_principal()

def main():
      exibir_nome_do_programa()
      exibir_menu()
      escolher_opcao()

if __name__ == "__main__":
      main()