import random
print("=== Adivinha um numero ===")
secreto = random.randint(1,100)
tentativas = 0
palpite = 0
while palpite != secreto:
    palpite = int(input("Seu palpite (1-100)"))
    tentativas += 1
    if palpite < secreto:
        print("Muito Baixo!")
    elif palpite > secreto:
        print("Muito Alto!")
    else:
        print(f"Parabens! acertou em (tentativas)")