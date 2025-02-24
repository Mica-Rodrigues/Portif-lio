import random
import string

def gerar_senha(tamanho=12):
    """Gera uma senha segura com o tamanho especificado."""
    if tamanho < 4:
        raise ValueError("O tamanho da senha deve ser no mínimo 4 caracteres.")
    
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.SystemRandom().choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    """Solicita ao usuário o tamanho da senha e a exibe."""
    try:
        tamanho = int(input("Digite o tamanho da senha desejada: "))
        senha_gerada = gerar_senha(tamanho)
        print(f"Senha gerada: {senha_gerada}")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()