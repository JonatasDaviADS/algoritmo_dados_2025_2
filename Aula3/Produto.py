from Categoria import Categoria


class Produto:
    def __init__(self, nome, preco=10, categ=Categoria("Alimentos")):
        self.nome = nome
        self.preco = preco
        self.categoria = categ

    def __str__(self):
        txt = "Produto: " + self.nome
        txt += "\nPreço: " + str(self.preco)
        # txt += "\nCategorria: " + self.categoria.nome
        txt += "\n" + str(self.categoria)
        return txt
