import tkinter as tk

# Função para aumentar e diminuir a quantidade
def aumentar():
    quantidade.set(quantidade.get() + 1)

def diminuir():
    if quantidade.get() > 1:
        quantidade.set(quantidade.get() - 1)

# Configurando a janela principal
root = tk.Tk()
root.title("Tela de Confirmação")
root.geometry("300x400")

# Criando o frame principal
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(expand=True, fill='both')

# Campo Cartão
tk.Label(frame, text="Cartão").pack(anchor='w')
entry_cartao = tk.Entry(frame)
entry_cartao.pack(fill='x')

# Campo Quantidade
tk.Label(frame, text="Quantidade").pack(anchor='w')
quantidade = tk.IntVar(value=1)
quantidade_frame = tk.Frame(frame)
quantidade_frame.pack(fill='x')
botao_menos = tk.Button(quantidade_frame, text="-", command=diminuir)
botao_menos.pack(side='left')
quantidade_label = tk.Label(quantidade_frame, textvariable=quantidade)
quantidade_label.pack(side='left', padx=5)
botao_mais = tk.Button(quantidade_frame, text="+", command=aumentar)
botao_mais.pack(side='left')

# Campo Endereço
tk.Label(frame, text="Endereço").pack(anchor='w')
entry_endereco = tk.Entry(frame)
entry_endereco.pack(fill='x')

# Campo Cupom
tk.Label(frame, text="Cupom").pack(anchor='w')
entry_cupom = tk.Entry(frame)
entry_cupom.pack(fill='x')

# Botão Confirmar
confirmar_btn = tk.Button(frame, text="Confirmar", bg="lightblue", padx=5, pady=5)
confirmar_btn.pack(pady=20)

