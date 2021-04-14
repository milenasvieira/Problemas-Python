senha = input()
senha = int(senha)

senha_incorreta = True

while senha_incorreta:
    if senha == 2002:
        senha_incorreta = False
        print ("Acesso Permitido")
    else:
        print ("Senha Invalida")
        senha = input()
        senha = int(senha)
