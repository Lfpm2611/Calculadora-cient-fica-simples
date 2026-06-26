numero1 = float(input("primeiro numero do calculo: "))
numero2 = float(input("segundo numero do calculo: "))
calculo = input("qual operação que você desejaria fazer (soma, subtração, multiplicação, divisão, fatoração, porcentagem, raiz,): ")
if calculo == "soma":
    print(f"{(numero1 + numero2):.2f}")
elif calculo == "subtração":
    print(f"{(numero1 - numero2):.2f}")
elif calculo == "multiplicação":
    print(f"{(numero1 * numero2):.2f}")
elif calculo == "divisão":
    print(f"{(numero1 / numero2):.2f}")
elif calculo == "fatoração":
    print(f"{(numero1 ** numero2):.2f}")
elif calculo == "porcentagem":
    print(f"{(numero1 * numero2 / 100):.2f}")
elif calculo == "raiz":
    if numero2 == 0 or numero1 == 0:
        print("Não é possível calcular a raiz de índice 0.")
    else:
        print(f"{(numero1 ** (1/numero2)):.2f}")
else:
    print("Operação inválida")