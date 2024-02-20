from tarefas import AdicionarAluno, RemoverAluno, AtualizarAluno, VerAluno, Sair

def MostrarMenu():
    print('='*61)
    print('='*15, 'SISTEMA DE CADASTRO DE ALUNOS', '='*15)
    print('='*61)
    print('Escolha uma tarefa: ')
    print('01. Adicionar')
    print('02. Remover')
    print('03. Atualizar')
    print('04. Ver Lista')
    print('05. Sair')
    print('='*61)

def MostrarOpcao(opcao):
    match opcao:
        case 1:
            AdicionarAluno()
        case 2:
            RemoverAluno()
        case 3:
            AtualizarAluno()
        case 4:
            VerAluno()
        case 5:
            Sair()