import tkinter as tk
from tkinter import messagebox
from entidades.produto import *

class Tela_pagamento (tk.Frame):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.produto = None

        # Campo Cartão
        tk.Label(self, text="Cartão").pack(anchor='w')
        entry_cartao = tk.Entry(self)
        entry_cartao.pack(fill='x')

        # Campo Quantidade
        tk.Label(self, text="Quantidade").pack(anchor='w')
        quantidade_self = tk.Frame(self)
        quantidade_self.pack(fill='x')

        botao_menos = tk.Button(quantidade_self, text="-", command=self.diminuir)
        botao_menos.pack(side='left')

        self.quantidade_label = tk.Label(quantidade_self, text='1')
        self.quantidade_label.pack(side='left', padx=5)

        botao_mais = tk.Button(quantidade_self, text="+", command=self.aumentar)
        botao_mais.pack(side='left')

        # Campo Endereço
        tk.Label(self, text="Endereço").pack(anchor='w')
        self.entry_endereco = tk.Entry(self)
        self.entry_endereco.pack(fill='x')

        # Campo Cupom
        tk.Label(self, text="Cupom").pack(anchor='w')
        entry_cupom = tk.Entry(self)
        entry_cupom.pack(fill='x')

        # Botão Confirmar
        confirmar_btn = tk.Button(self, text="Confirmar", bg="pink", fg="white", padx=5, pady=5, command=self.confirmar)
        confirmar_btn.pack(pady=20)

    def carregar(self, produto:Produto):
        self.produto = produto

    def aumentar(self):
        quantidade = int(self.quantidade_label.cget('text'))
        self.quantidade_label.config(text = str(quantidade + 1))
        
    def diminuir(self):
        quantidade = int(self.quantidade_label.cget('text'))
        if quantidade > 1:
            self.quantidade_label.config(text = str(quantidade - 1))

    def confirmar(self):
        quantidade = int(self.quantidade_label.cget('text'))
        self.app.banco_dados.executar(f"INSERT INTO pagamentos (cod_usuario,cod_produto,quantidade,endereco) VALUES ({self.app.usuario.cod},{self.produto.cod},{quantidade},{self.entry_endereco.get()})")
        messagebox.showinfo("Sucesso", "Compra realizada com sucesso")
        tela_produtos = self.app.telas[2]
        self.app.trocar_tela(tela_produtos)