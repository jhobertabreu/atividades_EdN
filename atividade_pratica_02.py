# EXERCÍCIO PRÁTICO 2
# Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda "Sim", se o resultado for False, responda "Não"

def verificar_palindromo(texto):
    # para que as letras fiquem minúsculas e todos os espaços sejam removidos
    texto = texto.lower().replace(" ", "")
   
    if texto == texto[::-1]:
        return "Sim"
    else:
        return "Não"

frase = input("Digite qualquer palavra ou frase: ")
resultado = verificar_palindromo(frase)
print(f"É um palíndromo? {resultado}")
