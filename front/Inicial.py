import tkinter as tk
from tkinter import messagebox
from PIL import Image

# Função para redirecionar para a tela de pagamento
def pagar(produto):
    messagebox.showinfo("Pagamento", f"Pagamento para {produto}")

# Criando a janela principal
class Tela_inicial(tk.Frame):
    def __init__(self, app):
        super().__init__()
        self.app = app

        botao_voltar = tk.Button(self, text="voltar", command=self.voltar)
        botao_voltar.pack()

    def voltar(self):
        tela_login = self.app.telas[0]
        self.app.trocar_tela(tela_login)

        

        '''
        # Frame para organizar os produtos em grade
        frame_produtos = tk.Frame(self)
        frame_produtos.pack(pady=20)

        # Adicionando botões com imagens
        produtos = [
            {"nome": "Produto 1", "preco": "R$10,00", "imagem": "imagens/download (5).jpeg"},
            {"nome": "Produto 2", "preco": "R$10,00", "imagem": "imagens/download 2(5).jpeg"},
        ]

        # Função auxiliar para criar cada produto com sua imagem e botão de preço
        def criar_produto(frame, produto, row, col):
            # Carregar imagem (substituir por seus caminhos de imagem)
            img = tk.PhotoImage(file=produto["imagem"])
            btn_imagem = tk.Button(frame, image=img, command=lambda: pagar(produto["nome"]))
            btn_imagem.image = img  # Evitar que a imagem seja deletada pelo garbage collector
            btn_imagem.grid(row=row, column=col)

            # Label para o preço
            lbl_preco = tk.Label(frame, text=produto["preco"])
            lbl_preco.grid(row=row + 1, column=col)

        # Adicionando os produtos no grid (2 colunas por linha)
        for i, produto in enumerate(produtos):
            row, col = divmod(i, 2)
            criar_produto(frame_produtos, produto, row * 2, col)
        '''