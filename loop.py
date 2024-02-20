from menu import MostrarMenu, MostrarOpcao

if __name__ == '__main__':

    while True:
        MostrarMenu()
        opcao = int(input('Escolha uma opção:  '))
        MostrarOpcao(opcao)
        if opcao == '5':
            break

    