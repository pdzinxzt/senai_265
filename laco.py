# exemplo de codigo para controlar o cenario
sinal =input

# input ("Digite a cor do Sinal:")
sinal = input("Digite a cor do Sinal: ")

# if e elif para verificar a cor do sinal e imprimir a mensagem correspondente
if sinal == "vermelho":
    print("Pare!!!!")
elif sinal == "amarelo":
    print("ATENCÃO!") 
elif sinal == "verde":
    print("Pode Passar!!!!")
else:
    print("Cor Invalida")
