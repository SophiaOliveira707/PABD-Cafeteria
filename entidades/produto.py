class Produto:
    def __init__(self,tupla):
        self.cod = tupla[0]
        self.nome = tupla[1]
        self.preco = tupla[2]
        self.tamanho = tupla[3]
        self.sabor = tupla[4]
        self.imagem = tupla[5]