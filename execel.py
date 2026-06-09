def se(condicao, valor_se_verdadeiro, valor_se_falso):
    return valor_se_verdadeiro if condicao else valor_se_falso

alunos = [
    ("João", 40),
    ("Maria", 60),
    ("José", 94),
    ("Pedro", 100),
    ("Marcelo", 80),
    ("Lucas", 75),
    ("Ana", 55),
    ("Beatriz", 70),
    ("Carlos", 65),
    ("Daniel", 85),
    ("Eduardo", 90),
    ("Fernanda", 77),
    ("Gabriel", 82),
    ("Helena", 68),
    ("Isabela", 92),
    ("Júlio", 73),
    ("Karina", 88),
    ("Leonardo", 79),
    ("Mariana", 95),
    ("Nicolas", 61),
    ("Olívia", 84),
    ("Paulo", 72),
    ("Rafaela", 98),
    ("Ricardo", 67),
    ("Sabrina", 81),
    ("Thiago", 76),
    ("Valentina", 89),
    ("Vinícius", 93),
    ("Yasmin", 74),
    ("Bruno", 58),
    ("Camila", 87),
    ("Diego", 69),
    ("Elisa", 91),
    ("Felipe", 78),
    ("Gustavo", 83),
    ("Larissa", 96),
    ("Matheus", 71),
    ("Natália", 86),
    ("Otávio", 64),
    ("Patrícia", 99)
]

print(f"{'Aluno':^15} {'Nota':^6} {'Situação':^12}")
print("-" * 38)

for nome, nota in alunos:
    situacao = se(
        nota >= 70,
        "APROVADO",
        se(nota >= 50, "RECUPERAÇÃO", "REPROVADO")
    )

    print(f"{nome:<15} {nota:^6} {situacao:^12}")

print("-" * 38)

print("\n--- Boletim ---")

aprovados = 0
recuperacao = 0
reprovados = 0

for nome, nota in alunos:
    situacao = se(
        nota >= 70,
        "APROVADO",
        se(nota >= 50, "RECUPERAÇÃO", "REPROVADO")
    )

    if situacao == "APROVADO":
        aprovados += 1
    elif situacao == "RECUPERAÇÃO":
        recuperacao += 1
    else:
        reprovados += 1

# Exibe o resultado
print(f"Total de Aprovados: {aprovados}")
print(f"Total de Recuperação: {recuperacao}")
print(f"Total de Reprovados: {reprovados}")
