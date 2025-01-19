import os

#cadastrar, remover e vizualizar itens
cadastro_itens = []
i = 0 # variavel para cadastro... indice

while True:

    print(50 * '--')
    print('Inventory System')
    print(50 * '--')
    
    servico_escolha = input('Deseja \n[C]adastrar \n[R]emover \n[V]izualizar \nQual das opcoes deseja? [ C  -  R  -  V ]: ')
    print(50 * '--')

    if servico_escolha.lower().startswith('c'):
        os.system('cls')
        while True:
            print(50 * '--')
            print('Cadastro de itens.')
            print(50 * '--')
            itens = input('Digite o nome do item que deseja cadastra: ')
            print(50 * '--')
            if itens in cadastro_itens:
                print(f'O produto {itens} ja foi cadastrado anteriormente!')
                continue
            else:
                cadastro_itens.append(itens)
                print(f'Produto cadastrado: {cadastro_itens[i]}')

            continuar_cadastro = input('Deseja continuar cadastro de itens? [S]im ou [N]ao: ')
            if continuar_cadastro.lower().startswith('s'):
                os.system('cls')
                print(next(enumerate(cadastro_itens)))
                i += 1
                continue
            elif continuar_cadastro.startswith('n'):
                os.system('cls')
                break
            else:
                os.system('cls')
                print('opcao invalida, tente novamente.')
                break
    elif servico_escolha.startswith('r'):
        os.system('cls')
        print(50 * '--')
        print('Removedor de itens cadastrados.')
        print(50 * '--')
        if enumerate(cadastro_itens):
            for indice, produto in enumerate(cadastro_itens):
                print(indice, produto)
                print(50 * '--')

        removedor_itens = input('Deseja remover qual item? Digite apenas o numero como na tabela acima: ').lower()
        indice_removedor = int(removedor_itens)
        if removedor_itens.isdigit():
            del cadastro_itens[ indice_removedor]
        else:
            os.system('cls')
            print('Nao ha itens para ser removido!')
            print(50 * '--')
    elif servico_escolha.startswith('v'):
        os.system('cls')
        print(50 * '--')
        for indice, produto in enumerate(cadastro_itens):
            print(indice, produto)
            print(50 * '--')
    else:
        print('Ops, Esta opcao ainda nao esta liberada, tente uma opcao valida')
        continue

    continuar_programa = input('Deseja [E]ncerrar ou [F]icar no programa: ')
    os.system('cls')
    if continuar_programa.lower().startswith('e'):
        print('O sistema foi encerrado...')
        break
    elif continuar_programa.lower().startswith('f'):
        continue
    else:
        print('Esta opcao nao e valida, o programa sera finalizado')
        break