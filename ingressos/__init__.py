import filmes
import menus
import validacoes
dicFilmes = {}
ingressosVendidosPorCliente = {}

def comprar_ingresso(dicFilmes, login_nome):
    if not filmes.buscar_filmes(dicFilmes):
        return
    while True:
        codigo_filme = validacoes.validacao_campo('\nDigite o código do filme: ')
        if codigo_filme in dicFilmes:
            break
        else:
            print('Filme não encontrado.')
            return

    while True:
        cliente = validacoes.validacao_campo('\nDigite seu nome de usuário: ')
        if cliente == login_nome:
            break
        else:
            print('Nome de usuário inválido. Insira o mesmo nome utilizado para login.')


    filme = dicFilmes[codigo_filme]
    capacidade_disponivel = filme[5]

    if capacidade_disponivel > 0:
        quant = int(validacoes.validacao_campo('\nDigite a quantidade de ingressos: '))

        if capacidade_disponivel >= quant:
            valor_total = filme[7] * quant
            pagamento(valor_total)
            filme[5] -= quant
            filme[8] += quant
            if cliente not in ingressosVendidosPorCliente:
                ingressosVendidosPorCliente[cliente] = []
            ingressosVendidosPorCliente[cliente].append((codigo_filme, quant))
            return True
        else:
            print('Não há ingressos disponíveis.')
    else:
        print('Não há ingressos disponíveis para este filme.')
    return False

def ingressos_cliente(cliente):
    def ingressosVendidosPorCliente(codigo_filme):
        if codigo_filme not in dicFilmes:
            print('Filme não encontrado.')
            return

        nome_filme = dicFilmes[codigo_filme][0]
        total_vendido = 0
        relatorio = f'Relatório de Ingressos Vendidos para o Filme: {nome_filme}\n'
        relatorio += '-' * 50 + '\n'

        for cliente, filmes in ingressosVendidosPorCliente.items():
            if codigo_filme in filmes:
                quant = filmes[codigo_filme]
                total_vendido += quant
                valor_total = dicFilmes[codigo_filme][7] * quant
                relatorio += f'Cliente: {cliente}, Quantidade: {quant}, Total: R${valor_total:.2f}\n'

        relatorio += '-' * 50 + '\n'
        relatorio += f'Total de Ingressos Vendidos: {total_vendido}\n'

        with open(f'{codigo_filme}_relatorio_ingressos.txt', 'w') as arquivo:
            arquivo.write(relatorio)

        print(f'Relatório de ingressos vendidos para o filme {nome_filme} gerado com sucesso.')


def pagamento(valor_total):
    while True:
        menus.menu_pagamento()
        op_pagamento = input('\nDigite a opção desejada: ')

        if op_pagamento == '1':
            print(f'Pagamento de R${valor_total} realizado via cartão de crédito.')
            break
        elif op_pagamento == '2':
            print(f'Pagamento de R${valor_total} realizado via cartão de débito.')
            break
        elif op_pagamento == '3':
            print(f'Pagamento de R${valor_total} realizado via pix.')
            break
        else:
            print('Opção Inválida.')