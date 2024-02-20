dicionario_alunos = {}

def AdicionarAluno():
    nome = input('Digite o nome: ')
    matricula = input('Digite a matrícula: ')
    dicionario_alunos[matricula] = nome
    print(f'Cadastro concluído: Nome: {nome} - Matrícula: {matricula}')

def RemoverAluno():
    matricula = input('Digite a matrícula a ser removida: ')
    if matricula in dicionario_alunos:
        del dicionario_alunos[matricula]
        print(f'Aluno com matrícula {matricula} removida')
    else:
        print('Matrícula não encontrada')

def AtualizarAluno():
    matricula = input('Digite a matrícula a ser atualizada: ')
    if matricula in dicionario_alunos:
        nome_atualizado = input('Digite um novo nome: ')
        dicionario_alunos[matricula] = nome_atualizado
        print(f'Cadastro atualizado: Nome: {nome_atualizado} - Matrícula: {matricula}')
    else:
        print('Matricula não encontrada')

def VerAluno():
    print('Alunos Matriculados')
    for matricula, nome in dicionario_alunos.items():
        print(f'Matricula: {matricula} - Nome: {nome}')

def Sair():
    print('Programa Encerrado')
    

    