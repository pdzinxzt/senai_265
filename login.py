login = input("Login: ")
senha = input("Senha: ")

while login == "":
    print("Você não digitou o login.")
    login = input("Por favor, digite o login: ")

while senha == "":
    print("Você não digitou a senha.")
    senha = input("Por favor, digite a senha: ")

if login == "admin" and senha == "1234":
    print("Acesso permitido")
else:
    print("Acesso negado")