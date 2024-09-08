from sympy import isprime, fibonacci, symbols, Eq, solve


def next_in_sequence(sequence):
    length = len(sequence)

    # Checar se é uma sequência aritmética
    if length > 1:
        diffs = [sequence[i] - sequence[i - 1] for i in range(1, length)]
        if len(set(diffs)) == 1:
            return sequence[-1] + diffs[0]

    # Checar se é uma sequência geométrica
    if length > 1 and sequence[0] != 0:
        ratios = [sequence[i] / sequence[i - 1] for i in range(1, length)]
        if len(set(ratios)) == 1:
            return int(sequence[-1] * ratios[0])

    # Checar se é uma sequência de Fibonacci
    if length >= 2:
        if sequence[-1] == sequence[-2] + sequence[-3]:
            return sequence[-1] + sequence[-2]

    # Checar se é uma sequência de quadrados
    if all(x == i ** 2 for i, x in enumerate(sequence)):
        return (length + 1) ** 2

    # Checar se é uma sequência de quadrados de números pares
    if all(x == (2 * i + 2) ** 2 for i, x in enumerate(sequence)):
        return (2 * length + 2) ** 2

    # Usar SymPy para identificar o próximo número com base em equações
    n = symbols('n')
    expr = sequence[0]
    for i in range(1, length):
        expr = expr + n - sequence[i]
    sol = solve(expr, n)

    if sol:
        return sol[0]

    return "Padrão não identificado"


# Testar com algumas sequências
sequences = {
    'a': [1, 3, 5, 7],
    'b': [2, 4, 8, 16, 32, 64],
    'c': [0, 1, 4, 9, 16, 25, 36],  #erro
    'd': [4, 16, 36, 64],
    'e': [1, 1, 2, 3, 5, 8],
    'f': [2, 10, 12, 16, 17, 18, 19]  #erro
}

for key, seq in sequences.items():
    print(f"Próximo elemento da sequência {key}: {next_in_sequence(seq)}")
