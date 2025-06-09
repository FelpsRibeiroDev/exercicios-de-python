email = 'felipe@gmail.com'
senha = 'felipe123'

email_conta = input('Digite seu email: ')
senha_conta = input('Digite sua senha: ')

if email_conta == email and senha_conta == senha:
    print('Acesso liberado!')
else:
    print('Acesso negado!')