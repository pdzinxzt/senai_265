def formatar_real(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# Uso:
preco_hospedagem = float(input("Digite o valor da Hospedagem"))
print(formatar_real(preco_hospedagem))  # Saída: R$ 49,90
