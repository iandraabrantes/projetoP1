import filmes
import validacoes

def ver_rendimento_do_dia(dicFilmes):
    total = 0
    for codigo_filme, filme in dicFilmes.items():
        total += filme[8] * filme[7]
    print(f'\nRendimento do dia: R${total}\n')

def ingressos_vendidos_total(dicFilmes):
    print('\nIngressos vendidos por filme:')
    for codigo_filme in dicFilmes:
        filme = dicFilmes[codigo_filme]
        print(f'Filme: {filme[0]}, Ingressos vendidos: {filme[8]}')

def ingressos_vendidos_por_filme(dicFilmes):
    if not filmes.buscar_filmes(dicFilmes):
        return
    codigo_filme = validacoes.validacao_campo('Digite o código do filme: ')
    encontrado = False
    for codigo in dicFilmes:
        if codigo == codigo_filme:
            filme = dicFilmes[codigo]
            ingressos = (f'\nFilme: {filme[0]}, Ingressos vendidos: {filme[8]}')
            print(ingressos)
            arquivo = open('ingressos_vendidos_por_filme.txt', 'w')
            arquivo.write(ingressos)
            arquivo.close()
            encontrado = True
            break

    if not encontrado:
        print('Filme não encontrado.')

def relatorio_de_desempenho(dicFilmes):
    ingressos_vendidos = 0
    filme_mais_vendido = ''
    maximo_vendas = 0

    for codigo_filme in dicFilmes:
        filme = dicFilmes[codigo_filme]
        ingressos_vendidos += filme[8]
        if filme[8] > maximo_vendas:
            maximo_vendas = filme[8]
            filme_mais_vendido = filme[0]

    print(f'Total de ingressos vendidos: {ingressos_vendidos}')
    print(f'Filme mais vendido: {filme_mais_vendido} com {maximo_vendas} ingressos.')