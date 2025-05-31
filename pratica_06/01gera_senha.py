# GERADOR DE SENHAS ALEATÓRIAS

import random
import string

def gerar_senha(tamanho=8):
   
    caracteres = string.ascii_letters + string.digits + "!@#$%&*"
        
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    
    return senha

def main():
    print("--- GERADOR DE SENHAS SEGURAS ---")
    print()
        
    try:
        tamanho_senha = int(input("Digite o tamanho da senha desejada (mínimo 4): "))        
        # Verificando se o tamanho é válido
        if tamanho_senha < 4:
            print("Tamanho muito pequeno! Usando tamanho mínimo de 4 caracteres.")
            tamanho_senha = 4
            
    except ValueError:        
        print("Valor inválido! Usando tamanho padrão de 8 caracteres.")
        tamanho_senha = 8
        
    nova_senha = gerar_senha(tamanho_senha)
    
    
    print()
    print("Senha gerada com sucesso!")
    print(f"Sua nova senha é: {nova_senha}")
    print()

if __name__ == "__main__":
    main()