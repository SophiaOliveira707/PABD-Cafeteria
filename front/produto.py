import tkinter as tk
from PIL import Image, ImageTk
from entidades.produto import *

# Função para criar a interface
class Tela_produto(tk.Frame):
    def __init__(self,app):
        super().__init__()
        self.app = app

    def carregar(self,produto:Produto):
        img = Image.open(produto.imagem)  # Substitua pelo caminho da sua imagem
        img = img.resize((150, 150))  # Redimensionando a imagem
        img_tk = ImageTk.PhotoImage(img)

        img_label = tk.Label(self, image=img_tk)
        img_label.image = img_tk  # Manter uma referência da imagem
        img_label.grid(row=0, column=0, rowspan=4, padx=10)

        # Título do produto
        titulo = tk.Label(self, text=produto.nome, font=("Arial", 16, "bold"))
        titulo.grid(row=0, column=1, sticky='w')

        # Parágrafos com informações
        preco_label = tk.Label(self, text=f"Preço: R$ {produto.preco}", font=("Arial", 12))
        preco_label.grid(row=1, column=1, sticky='w')

        sabor_label = tk.Label(self, text=f"Sabor: {produto.sabor}", font=("Arial", 12))
        sabor_label.grid(row=2, column=1, sticky='w')

        tamanho_label = tk.Label(self, text=f"Tamanho: {produto.tamanho}", font=("Arial", 12))
        tamanho_label.grid(row=3, column=1, sticky='w')

        # Botão de comprar
        botao_comprar = tk.Button(self, text="Comprar", font=("Arial", 12), bg="pink", fg="white")
        botao_comprar.grid(row=0, column=2, rowspan=4, padx=10)