import filmes
import ingressos
import menus
import rendimento
import validacoes
usuarios = {}
dicFilmes = {}
filmesExcluidos = []
loginCliente = []

print('Seja bem-vindo(a) ao Cine Sertão!')
while True:
    menus.menu_principal()
    valor = validacoes.validacao_campo('\nDigite a opção desejada: ')

    if valor == '1':
        print('-' * 20)
        print('Faça login.\n')
        loginNome = validacoes.validacao_campo('Digite seu usuário: ')
        email = validacoes.validacao_campo('DIgite seu email: ')
        senha = validacoes.validacao_campo('Diite sua senha: ')

        if validacoes.login_usuario(usuarios, loginNome, email, senha) and usuarios[loginNome][2] == '1':
            print('\nLogin concluído.')

            while True:
                menus.menu_administrador()
                op = input('\nDigite a opção desejada: ')
                if op == '0':
                    break

                elif op == '1':
                    print('-' * 20)
                    filmes.adicionar_filme(dicFilmes)

                elif op == '2':
                    print('-' * 20)
                    filmes.buscar_filmes(dicFilmes)

                elif op == '3':
                    print('-' * 20)
                    filmes.buscar_filmes(dicFilmes)
                    filmes.atualizar_filme(dicFilmes)

                elif op == '4':
                    print('-' * 20)
                    filmes.buscar_filmes(dicFilmes)
                    filmesExcluidos = validacoes.validacao_campo('\nDigite o código do filme que deseja remover: ')
                    filmes.remover_filme(dicFilmes, filmesExcluidos)

                elif op == '5':
                    print('-' * 20)
                    filmes.mostrar_filmes(dicFilmes)

                elif op == '6':
                    print('-' * 20)
                    rendimento.ver_rendimento_do_dia(dicFilmes)

                elif op == '7':
                    print('-' * 20)
                    rendimento.ingressos_vendidos_total(dicFilmes)

                elif op == '8':
                    print('-' * 20)
                    rendimento.ingressos_vendidos_por_filme(dicFilmes)

                elif op == '9':
                    print('-' * 20)
                    rendimento.relatorio_de_desempenho(dicFilmes)

        else:
            print('\nUsuário ou senha ou acesso inválidos.')

    elif valor == '2':
        print('-' * 20)
        print('Faça login.\n')
        loginNome = validacoes.validacao_campo('Insira seu usuário: ')
        email = validacoes.validacao_campo('Insira seu email: ')
        senha = validacoes.validacao_campo('Insira sua senha: ')

        if validacoes.login_usuario(usuarios, loginNome, email, senha) and usuarios[loginNome][2] == '2':
            print('\nLogin concluído.')
            while True:
                menus.menu_cliente()
                op = validacoes.validacao_campo('\nDigite a opção desejada: ')
                if op == '0':
                    break
                elif op == '1':
                    print('-' * 20)
                    filmes.mostrar_filmes(dicFilmes)
                elif op == '2':
                    print('-' * 20)
                    ingressos.ingressosVendidosPorCliente(dicFilmes, loginNome)
                elif op == '3':
                    print('-' * 20)
                    filmes.grafico_filmes_populares(dicFilmes)
                elif op == '4':
                    ingressos.comprar_ingresso(dicFilmes, loginNome)

        else:
            print('\nUsuário ou senha inválidos ou não cadastrados como Cliente.')

    elif valor == '3':
        validacoes.cadastro_user(usuarios)

    elif valor == '4':
        print('--------------------------------------')
        print('Saindo do sistema.')
        break

    else:
        print('--------------------------------------')
        print('Opção inválida.')