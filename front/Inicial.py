import tkinter as tk
from PIL import Image, ImageTk
from entidades.produto import *

class Tela_inicial(tk.Frame):
    def __init__(self, app):
        super().__init__()
        self.app = app

        botao_usuario = tk.Button(self, text="usuario", bg="pink", fg="white",command=self.acessar_usuario)
        botao_usuario.pack(anchor='ne',padx=10,pady=10)

        # Criar um Canvas e uma barra de rolagem
        canvas = tk.Canvas(self)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        # Configurar o Frame scrollável
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Posicionar Canvas e Scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Lista de self.produtos (caminho da imagem, preço)
        self.app.banco_de_dados.executar('SELECT * FROM produtos')
        self.produtos = self.app.banco_de_dados.pegar_valores()

        # Definindo o layout com duas colunas
        for i, (cod,nome,preco,tamanho,sabor,caminho_imagem) in enumerate(self.produtos):
            # Criando um frame para cada produto
            frame = tk.Frame(scrollable_frame, width=150, height=200, borderwidth=2, relief='solid')
            frame.grid(row=i // 2, column=i % 2, padx=10, pady=10)

            # Adicionando a imagem do produto
            img = Image.open(caminho_imagem)  # Carrega a imagem
            img = img.resize((100, 100))  # Redimensionando a imagem
            img_tk = ImageTk.PhotoImage(img)
            img_label = tk.Label(frame, image=img_tk)
            img_label.image = img_tk  # Manter uma referência da imagem
            img_label.pack(pady=5)

            # Adicionando o evento de clique na imagem
            img_label.bind("<Button-1>", lambda e, index=i: self.acessar_produto(index))

            # Adicionando o preço do produto
            preco_label = tk.Label(frame, text=f"R$ {preco}", font=("Arial", 12))
            preco_label.pack(pady=5)

    # Método para acessar o produto
    def acessar_produto(self, index):
        tela_produto = self.app.telas[2]
        self.app.trocar_tela(tela_produto)
        
        produto = Produto(self.produtos[index])
        tela_produto.carregar(produto)

    def acessar_usuario(self):
        tela_usuario = self.app.telas[4]
        self.app.trocar_tela(tela_usuario)
        tela_usuario.carregar()