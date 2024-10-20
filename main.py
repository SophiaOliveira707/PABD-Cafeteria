import tkinter as tk
from front.login import Tela_login
from front.inicial import Tela_inicial
from funcoes.sql import *
from front.produto import Tela_produto

class App(tk.Tk):
    def __init__(self,title,geometry):
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        self.banco_de_dados = Bd_cafe()
        self.usuario = None
        self.resizable(False,False)

        self.telas = [Tela_login(app=self), Tela_inicial(app=self),Tela_produto(app=self)]

        self.tela_ativa = self.telas[1]
        self.tela_ativa.pack(fill="both", expand=True)

    def trocar_tela(self,tela):
        self.tela_ativa.pack_forget() #Paro de mostrar a tela ativa
        tela.pack(fill="both", expand=True) #Mostro a tela que eu pedi
        self.tela_ativa = tela #Atualiza a tela ativa

app = App(title='Cafeteria',geometry='450x400') #janela pricipal

app.mainloop()