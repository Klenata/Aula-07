def imprimeNome(nome):
    print(f"Nome: {nome}")

def solicitarNome():
    nome = input("Digite seu nome: ")
    return nome

def piramide(num):
    for i in range(1, num + 1, 1):
        for x in range(0, i):
            print(i, end=" ")
        print()