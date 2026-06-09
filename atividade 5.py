#Calculadora Basica
print("=== Calculadora ===\n")

num1 =float(input("Digite o Primeiro Numero:"))
operador = input("Digite o operador:(+, -,/, *")
num2 = float(input("Digite o segundo numero:"))

if operador == "+":
    print(num1+num2)
elif operador == "-":
    print(num1-num2)
elif operador == "/":
    print(num1/num2)
else:
    print("Operador Inexistente")

