try:
    idade = int(input("Insira sua idade: "))

    if idade >= 18:
        print("Idade maior ou igual a 18 anos")
    else:
        print("Idade menor que 18 anos")

except ValueError:
    print("Por favor, insira um número válido.")

print("Fim")
