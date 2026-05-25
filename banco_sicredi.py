saldo = 0.0

print("Bem Vindo Ao Banco Sicredi!")
while True:
print("\n Eescolha uma opção:")
print("1 - Depositar")
print("2 - Sacar")
print("3 - Ver saldo")
print("4 - Sair")

op = input("Escolha: ")
if op == "1":
    valor = float(input("Quanto você deseja sacar?: "))
    saldo += valor
    print(f"Depositado Saldo Atual:{saldo:.2f}")
    elif op == "2":
        valor = float(input("Valor Para Sacar: R$ "))
        

