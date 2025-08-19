from Categoria import Categoria
from Produto import Produto

c1 = Categoria()
c2 = Categoria("Eletrônicos")

# p1 = Produto()
p2 = Produto("Arroz")
p3 = Produto("Feijão", categ=c1)
p4 = Produto("Farinha", 4.39)
p5 = Produto("Mouse", 19.9, c2)
p5 = Produto("Café", 29.9, c1)


print(c1)
print("-------------")
print(p3)
