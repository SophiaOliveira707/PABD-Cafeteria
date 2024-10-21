import tkinter as tk
from tkinter import messagebox
from entidades.usuario import *

class Tela_login(tk.Frame):
    def __init__(self, app):#Executa quando iniciar a classe
        super().__init__()#Roda o __init__ do tk.Frame para construir a classe corretamente
        self.app = app

        #caxinha para a gente escrever dentro
        texto_usuario = tk.Label(self, text="Usuário:")
        texto_usuario.pack(pady=(20, 0))

        self.usuario = tk.Entry(self)
        self.usuario.pack(pady=(0, 10))

        texto_senha = tk.Label(self, text="Senha:")
        texto_senha.pack(pady=(10, 0))

        self.senha = tk.Entry(self, show="*")
        self.senha.pack(pady=(0, 20))

        # Botão 
        botao_login = tk.Button(self, text="Login", bg="pink", fg="white",command=self.login)
        botao_login.pack()

    #obtem o valo de usuario e senha
    def login(self):
        usuario = self.usuario.get()
        senha = self.senha.get()

        #Pega no banco de dados todos os usuários com o nome e senha digitados
        self.app.banco_de_dados.executar(f"SELECT * FROM usuarios WHERE nome='{usuario}' AND senha='{senha}'")
        correspondencias = self.app.banco_de_dados.pegar_valores()

        try:#Tentando acessar o usuário com o nome e senha digitados
            self.app.usuario = Usuario(correspondencias[0])

            tela_inicial = self.app.telas[1]
            self.app.trocar_tela(tela_inicial)
        except:#Caso esse usuário não exista, exibe um erro
            messagebox.showerror("Login", "Usuário ou senha incorretos.")