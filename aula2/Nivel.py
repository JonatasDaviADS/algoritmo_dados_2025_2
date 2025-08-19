# Construir a classe Prduto, que possui o atributo nome.
# Criar uma instância de Produtos e printar essa instância

# ANOTAÇÕES
# self é a instância que tá chamando o metodo

class Produto:
    def __init__(self, name):  # __init__ é um metodo construtor
        self.nome = name
        # self.preco = preco
        # self.categoria = categoria


p = Produto("Coca-Cola")

print (p)

# p2 = Produto("Fanta")
# print(p.nome)
