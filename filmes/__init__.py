import validacoes

def adicionar_filme(dicFilmes):
    while True:
        codigo_filme = validacoes.validacao_campo('Digite um código pro filme:')
        if codigo_filme in dicFilmes:
            print('Código existente. Tente novamente.')
        else:
            break

    while True:
        nome_filme = validacoes.validacao_campo('Digite o nome do filme:')
        nome_cadastrado = False

        for filme in dicFilmes:
            if dicFilmes[filme][0] == nome_filme:
                nome_cadastrado = True
                break
        if nome_cadastrado:
            print('Filme cadastrado. Tente novamente.')
        else:
            break

    descricao_filme = validacoes.validacao_campo('Digite a descrição do filme:')
    genero_filme = validacoes.validacao_campo('Digite o gênero do filme:')
    duracao_filme = validacoes.validacao_campo('Digite a duração do filme: ')

    while True:
        sala_filme = int(validacoes.validacao_campo('Digite a sala do filme:'))
        sala_indisponivel = False
        for filme in dicFilmes:
            if dicFilmes[filme][4] == sala_filme:
                sala_indisponivel = True
                break

        if sala_indisponivel:
            print('Sala indisponível. Tente novamente.')
        else:
            break

    capacidade_sala = 50
    horario_filme = validacoes.validacao_campo('Digite o horário de exibição do filme:')
    valor_ingresso = float(validacoes.validacao_valor('Digite o valor do ingresso:'))

    dicFilmes[codigo_filme] = [nome_filme, descricao_filme, genero_filme, duracao_filme, sala_filme, capacidade_sala, horario_filme, valor_ingresso, 0]

    print('\nFilme cadastrado.')

def buscar_filmes(dicFilmes):
    busca = input('Digite o nome do filme: ')
    busca = busca.upper()
    encontrado = False

    for codigo_filme, filme in dicFilmes.items():
        nome_filme = filme[0].upper()

        if busca in nome_filme:
            print(f'\nCódigo: {codigo_filme} - Nome: {filme[0]}')
            encontrado = True

    if not encontrado:
        print('Filme não encontrado.')

    return encontrado

def atualizar_filme(dicFilmes):
    codigo_filme = validacoes.validacao_campo('Digite o código do filme a ser atualizado: ')

    if codigo_filme not in dicFilmes.items():
        print('Filme não encontrado.')
        return

    campos_validos = ['nome', 'sinopse', 'genero', 'duracao', 'sala', 'capacidade', 'horario', 'valor']
    campo = validacoes.validacao_campo('Digite o campo a ser atualizado (nome, sinopse, genero, duracao, sala, horario, valor): ')

    if campo not in campos_validos:
        print('Campo inválido.')
        return

    novo_valor = validacoes.validacao_campo('Digite o novo conteúdo: ')

    if campo == 'nome':
        for filme_cod, filme_nome in dicFilmes.items():
            if novo_valor == filme_nome:
                print('O nome do filme já está em uso.')
                return
    elif campo == 'sala':
        for filme_cod, filme_sala in dicFilmes.items():
            if novo_valor == filme_sala[4]:
                print('A sala do filme já está em uso.')
                return
    if campo == 'valor':
        for filme_id, filme_info in dicFilmes.items():
            novo_valor = float(novo_valor)

    dicFilmes[codigo_filme][campos_validos[campo]] = novo_valor
    print(f'{campo} do filme atualizado com sucesso.')


def remover_filme(dicFilmes, filmes_excluidos):
    if filmes_excluidos in dicFilmes:
        dicFilmes.pop(filmes_excluidos)
        print('\nFilme removido com sucesso.')
    else:
        print('\nFilme não encontrado.')

def mostrar_filmes(dicFilmes):
    filmes_disponiveis = len(dicFilmes) > 0
    if not filmes_disponiveis:
        print('Não há filmes disponíveis.')
    else:
        print('Filmes disponíveis:')
        for x in dicFilmes:
            print(f'\n{dicFilmes[x][0]}')
            print(f'Descrição: {dicFilmes[x][1]}')
            print(f'Gênero: {dicFilmes[x][2]}')
            print(f'Duração: {dicFilmes[x][3]}')
            print(f'Sala: {dicFilmes[x][4]}')
            print(f'Capacidade da sala: {dicFilmes[x][5]}')
            print(f'Horário: {dicFilmes[x][6]}')
            print(f'Valor: {dicFilmes[x][7]}')

import matplotlib.pyplot as mpl
def grafico_filmes_populares(dicFilmes):
    filmes = []
    ingressos_vendidos = []

    for filme in dicFilmes.values():
        filmes.append(filme[0])
        if len(filme) < 9:
            ingressos_vendidos.append(0)
        else:
            ingressos_vendidos.append(filme[8])

    mpl.figure(figsize=(10, 5))
    mpl.bar(filmes, ingressos_vendidos, color='red')
    mpl.xlabel('Filmes')
    mpl.ylabel('Ingressos Vendidos')
    mpl.title('Filmes Mais Assistidos')
    mpl.xticks(rotation=45, ha='right')
    mpl.tight_layout()
    mpl.show()