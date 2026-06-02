import random 

simbolos = ["🐱‍👤","✔","🐱‍🏍","🎁","🎉"]
saldo = 20.0
print("==== Cassino do Senai ===\n")
while saldo >= 2:
    input("\npressione ENTER para girar (custa R$ 2)...")
    saldo -= 2

    resultado = [random.choice(simbolos) for _ in range(3)]
    print(" | ".join(resultado))

    if resultado[0] == resultado[1] == resultado [2]:
     premio = 20
     saldo += premio
    print(f" JAKPOT!!! Você ganhou R$ {premio}!")

else:
    print("Não foi dessa vez...")

    print(f"Saldo atual: R$ {saldo:.2f}")
