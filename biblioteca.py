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

def contaVogais(texto):
    cont = 0
    for i in range(len(texto)):
        if texto[i] in "aeiouáéíóúâêîôûàèìòùãõü":
            cont += 1
    print(cont)

def valorEstoque(produto, valor, quantidade):
    total = valor * quantidade
    print()
    print(f"O item {produto}, tem um total de R${total} de estoque")