'''
import tkinter as tk
from PIL import Image, ImageTk

def comprar():
    # Aqui você pode adicionar a lógica para processar a compra
    tk.messagebox.showinfo("Compra", "Produto adicionado ao carrinho!")

# Criar a janela principal
root = tk.Tk()
root.title("Tela de Produto")

# Carregar a imagem do produto
image = Image.open("imagens/download (5).jpeg")  # Substitua pelo caminho da sua imagem
photo = ImageTk.PhotoImage(image)

# Criar um rótulo para a imagem
label_image = tk.Label(root, image=photo)
label_image.pack(pady=(10, 10))

# Rótulo para o nome do produto
label_name = tk.Label(root, text="Nome do Produto: Chocolate")
label_name.pack(pady=(5, 5))

# Rótulo para o preço do produto
label_price = tk.Label(root, text="Preço: R$ 10,00")
label_price.pack(pady=(5, 5))

# Rótulo para o sabor do produto
label_flavor = tk.Label(root, text="Sabor: Ao Leite")
label_flavor.pack(pady=(5, 10))

# Botão de comprar
button_buy = tk.Button(root, text="Comprar", command=comprar)
button_buy.pack(pady=(10, 20))

'''

#tela innicial
import tkinter as tk
from PIL import Image, ImageTk

# Função para criar a interface
def criar_tela():
    root = tk.Tk()
    root.title("Exibição do Produto")

    # Definindo o layout
    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack()

    # Imagem do produto
    img = Image.open("imagens/bolo.jpeg")  # Substitua pelo caminho da sua imagem
    img = img.resize((150, 150))  # Redimensionando a imagem
    img_tk = ImageTk.PhotoImage(img)

    img_label = tk.Label(frame, image=img_tk)
    img_label.image = img_tk  # Manter uma referência da imagem
    img_label.grid(row=0, column=0, rowspan=4, padx=10)

    # Título do produto
    titulo = tk.Label(frame, text="Nome do Produto", font=("Arial", 16, "bold"))
    titulo.grid(row=0, column=1, sticky='w')

    # Parágrafos com informações
    preco_label = tk.Label(frame, text="Preço: R$ 18,50", font=("Arial", 12))
    preco_label.grid(row=1, column=1, sticky='w')

    sabor_label = tk.Label(frame, text="Sabor: morango", font=("Arial", 12))
    sabor_label.grid(row=2, column=1, sticky='w')

    tamanho_label = tk.Label(frame, text="Tamanho: pequeno", font=("Arial", 12))
    tamanho_label.grid(row=3, column=1, sticky='w')

    # Botão de comprar
    botao_comprar = tk.Button(frame, text="Comprar", font=("Arial", 12), bg="pink", fg="white")
    botao_comprar.grid(row=0, column=2, rowspan=4, padx=10)


    root.mainloop()

# Chama a função para criar a tela
if __name__ == "__main__":
    criar_tela()

    
