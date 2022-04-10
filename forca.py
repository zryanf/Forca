import random
 
def comeca_tabuleiro(stick):
    print(" "+"  "+"_____________")
    print(" "+" |"+"             "+"|")
    print(" "+" |"+"             "+stick[0])        
    print(" "+" |"+"            "+stick[2]+stick[1]+stick[3])
    print(" "+" |"+"            "+stick[4]+" "+stick[5])
    print(" "+" |")
    print(" "+" |")
    print("_"+"_|"+"_________________")

def escolha_palavra():
    palavras = []
    with open("palavras.txt", "r", encoding="utf-8") as arquivo:
        arquivo = arquivo.readlines()
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].lower()
    return palavra_secreta



def escreva_palavra(palavra):
    write = ["_" for i in palavra] #list comprehension
    return write

def checa_letra():
    letra = input("Uma Letra: ")
    return letra.lower()

def checa_letra_palavra(letra_certa,tentativa,palavra):
    posicao = 0
    for letra in palavra:
        if letra == tentativa:
            letra_certa[posicao] = letra
        posicao += 1

def derrota(erros):
    stick = ["","","","","",""]
    if erros == 1:
        stick = ["O","","","","",""]
        return stick
    elif erros == 2:
        stick = ["O","|"," "," "," "," "]
        return stick
    elif erros == 3:
        stick = ["O","|","/"," "," "," "]
        return stick 
    elif erros == 4:
        stick = ["O","|","/","\\"," "," "]
        return stick 
    elif erros == 5:
        stick = ["O","|","/","\\","/"," "]
        return stick 
    elif erros == 6:
        stick = ["O","|","/","\\","/","\\"]
        return stick 

def repetir():
    return input("Deseja repetir, sim ou não? ").upper().startswith('S')

def jogar():
    while True:
        palavra = escolha_palavra()
        palavra_certa = escreva_palavra(palavra)
        vencedor = False
        perdedor = False
        erros = 0
        print(palavra_certa)
        while not vencedor and not perdedor:
            pede_letra = checa_letra()
            if pede_letra in palavra:
                checa_letra_palavra(palavra_certa, pede_letra ,palavra)
                qnt_ifen = palavra_certa.count("_")
                print("Você acertou a letra!")
                if qnt_ifen == 0:
                    vencedor = True
                    print(f"Parabéns, você acertou a palavra secreta: {palavra.upper()}")
            else:
                erros += 1
                derrotado = derrota(erros)
                comeca_tabuleiro(derrotado)
                if erros == 6:
                    perdedor = True
                    print(f"Você perdeu, a palavra era: {palavra.upper()}!")
            print(palavra_certa)
        if not repetir():
            break
if __name__ == '__main__':
    jogar()