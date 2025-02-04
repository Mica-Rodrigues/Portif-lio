def obter_sexo():
    """Solicita ao usuário um sexo válido (M ou H) e retorna seu valor normalizado (M/H)."""
    while True:
        sexo = input("Digite o sexo (M para Mulher, H para Homem): ").strip().upper()
        if sexo in ("M", "H"):
            return sexo
        print("Erro: Digite apenas 'M' para Mulher ou 'H' para Homem.")

def obter_idade():
    """Solicita ao usuário uma idade válida e retorna seu valor como inteiro."""
    while True:
        try:
            idade = int(input("Digite a idade: "))
            if idade > 0:
                return idade
            else:
                print("Erro: A idade deve ser um número positivo.")
        except ValueError:
            print("Erro: Digite um número inteiro válido.")

def calcular_dados(qtd_pessoas):
    """Recebe um número de pessoas e calcula a quantidade de mulheres e a média de idade delas."""
    qtd_mulheres = 0
    soma_idades_mulheres = 0

    for _ in range(qtd_pessoas):
        sexo = obter_sexo()
        idade = obter_idade()

        if sexo == "M":
            qtd_mulheres += 1
            soma_idades_mulheres += idade

    if qtd_mulheres > 0:
        media_idade_mulheres = soma_idades_mulheres / qtd_mulheres
    else:
        media_idade_mulheres = None  # Evita divisão por zero

    return qtd_mulheres, media_idade_mulheres

def main():
    """Função principal do programa."""
    print("=" * 40)
    print(" Contagem de Mulheres e Média de Idade ")
    print("=" * 40)

    qtd_pessoas = int(input("Quantas pessoas deseja cadastrar? "))

    if qtd_pessoas <= 0:
        print("Erro: O número de pessoas deve ser maior que zero.")
        return

    qtd_mulheres, media_idade_mulheres = calcular_dados(qtd_pessoas)

    print("\n=== Resultados ===")
    print(f"Quantidade de mulheres: {qtd_mulheres}")

    if media_idade_mulheres is not None:
        print(f"Média de idade das mulheres: {media_idade_mulheres:.2f}")
    else:
        print("Nenhuma mulher cadastrada, média de idade não calculada.")

if __name__ == "__main__":
    main()
