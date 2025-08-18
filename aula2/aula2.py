# Aula2 - Exercício Algoritmo e Estrutura de Dados

class Retangulo:

    # altura = 0
    # largura = 0

    def __init__(self, altura, largura):
        self.altura = int(altura)
        self.largura = int(largura)

    def calcularAreaRetangulo(self):
        resultCalculoArea = self.altura * self.largura
        print (f"Area do Retangulo é:   {resultCalculoArea}")

    def imprimirValores(self):
        print (f"A altura Retangulo é:  {self.altura} - A largura é:  - {self.largura}")


# altura = 10
# largura = 5
