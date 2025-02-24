import random

palavras = ["python", "programacao", "desenvolvimento", "inteligencia", "computador", "tecnologia"]

def escolher_palavra():
    """Escolhe uma palavra aleatória da lista."""
    return random.choice(palavras).upper()

def exibir_palavra_oculta(palavra, letras_corretas):
    """Exibe a palavra com as letras descobertas e underscores para as não reveladas."""
    return ' '.join(letra if letra in letras_corretas else '_' for letra in palavra)

def jogo_da_forca():
    """Executa o jogo da forca."""
    palavra = escolher_palavra()
    letras_corretas = set()
    letras_erradas = set()
    tentativas = 6
    
    print("Bem-vindo ao Jogo da Forca!")
    
    while tentativas > 0:
        print("\nPalavra: ", exibir_palavra_oculta(palavra, letras_corretas))
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")
        
        tentativa = input("Digite uma letra: ").upper()
        
        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Por favor, insira apenas uma letra válida.")
            continue
        
        if tentativa in letras_corretas or tentativa in letras_erradas:
            print("Você já tentou essa letra.")
            continue
        
        if tentativa in palavra:
            letras_corretas.add(tentativa)
            print("Boa! Você acertou uma letra.")
        else:
            letras_erradas.add(tentativa)
            tentativas -= 1
            print("Errou! Essa letra não está na palavra.")
        
        if set(palavra) == letras_corretas:
            print("\nParabéns! Você acertou a palavra:", palavra)
            break
    else:
        print("\nFim de jogo! A palavra era:", palavra)

if __name__ == "__main__":
    jogo_da_forca()
