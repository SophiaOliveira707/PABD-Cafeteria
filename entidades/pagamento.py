class Pagamento:
    def __init__(self,tupla):
        self.cod_pagamento = tupla[0]
        self.cod_usuario = tupla[1]
        self.cod_produto = tupla[2]
        self.qnt= tupla[3]
        self.cartao_cred = tupla[4]
        self.endereco = tupla[5]