def obter_nota():
    """Solicita ao usuário uma nota válida e retorna seu valor como float."""
    while True:
        try:
            nota = float(input("Digite uma nota (0 a 10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Erro: A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Erro: Digite um número válido.")

def calcular_notas(qtd_notas):
    """Recebe um número de notas e calcula a média e a maior nota."""
    soma_notas = 0
    maior_nota = 0

    for i in range(qtd_notas):
        nota = obter_nota()
        soma_notas += nota
        if i == 0 or nota > maior_nota:
            maior_nota = nota

    media = soma_notas / qtd_notas
    return media, maior_nota

def main():
    """Função principal do programa."""
    print("=" * 30)
    print(" Cálculo de Média e Maior Nota ")
    print("=" * 30)

    qtd_notas = int(input("Quantas notas deseja inserir? "))

    if qtd_notas <= 0:
        print("Erro: O número de notas deve ser maior que zero.")
        return

    media, maior_nota = calcular_notas(qtd_notas)

    print("\n=== Resultados ===")
    print(f"Média das notas: {media:.2f}")
    print(f"Maior nota: {maior_nota:.2f}")

if __name__ == "__main__":
    main()

