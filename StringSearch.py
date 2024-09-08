def verificar_letra_a(texto):
    contagem_a = texto.count('a') + texto.count('A')

    if contagem_a > 0:
        print(f"A letra 'a' aparece {contagem_a} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")



entrada = input("Digite uma string: ")

verificar_letra_a(entrada)
