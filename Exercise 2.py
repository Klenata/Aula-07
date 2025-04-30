from biblioteca import valorEstoque
produto = input("Digite o nome do produto: ")
quantidade = int(input("Insira a quantidade de estoque do produto: "))
valor = float(input("Insira o valor unitário do produto: "))

valorEstoque(produto, valor, quantidade)