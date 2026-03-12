while True:
    usuario = input("digite o nome de usuario: ")
    senha = input("digite a senha: ")
    
    if usuario == "admin" and senha == "1234":
        print("Login bem-sucedido!")
        break
    else:
        print("usuario ou senha incorretos, tente novamente")