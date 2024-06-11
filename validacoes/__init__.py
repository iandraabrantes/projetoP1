
def validacao_valor(texto):
    campo = float(input(texto))
    while campo < 0:
        campo = float(input(texto))
    return campo

def validacao_campo(texto):
    campo = input(texto)
    while len(campo) == 0:
        campo = input(texto)
    return campo

def cadastro_user(usuarios):
    print('-' * 20)
    print('------CADASTRO------')
    print('-' * 20)
    user = input('Digite seu nome de usuário: ')
    if user in usuarios:
        print('\nCadastro já existente, tente novamente!')
        return False

    email = validacao_campo('Digite seu email: ')
    senha = validacao_campo('Digite sua senha: ')
    acesso = ''
    while acesso != '1' and acesso != '2':
        acesso = validacao_campo('Digite "1" para se cadastrar como administrador ou "2" para se cadastrar como cliente.')
        if acesso != '1' and acesso != '2':
            print('Inválido. Insira 1 para se cadastrar como administrador ou 2 para se cadastrar como cliente.')
    usuarios[user] = [email, senha, acesso]
    print('\nCadastrado com sucesso.')

def login_usuario(usuarios, user, email, senha):
    return user in usuarios and usuarios[user][0] == email and usuarios[user][1] == senha