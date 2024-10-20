from funcoes.sql import *

def login(bancoDeDados:Bd_cafe,usuario,senha):
    bancoDeDados.executar(f'SELECT * FROM usuarios WHERE usuario = {usuario} AND senha = {senha}')
    usuarios = bancoDeDados.pegarValores()
    if usuarios != None:
        #faz login (muda a tela)
        pass
