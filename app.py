import os
print("Sabor Express - Sistema de Entrega de Alimentos")
print('1. Cadastrar restaurante')
print('2. Listar restaurantes')
print('3. Ativar restaurante')
print('4. Sair')

opcao_escolhida = int(input('\nEscolha uma opção: '))
print(f'\nVocê escolheu a opção: {opcao_escolhida}\n' )
print(type(opcao_escolhida))

if opcao_escolhida == 1:
    print('Cadastrar Restaurante')
    nome_restaurante = input('Digite o nome do restaurante: ')
    print(f'\nRestaurante {nome_restaurante} cadastrado com sucesso!')
elif opcao_escolhida == 2:
      print('Listar Restaurantes')
elif opcao_escolhida == 3:
      print('Ativar Restaurante')
      nome_restaurante = input('Digite o nome do restaurante a ser ativado: ')
      print(f'\nRestaurante {nome_restaurante} ativado com sucesso!')
else:
      os.system('cls')
      print('Encerrando o programa. Obrigado por usar o Sabor Express!')
      print('...\n')