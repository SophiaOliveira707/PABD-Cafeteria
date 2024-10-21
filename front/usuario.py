import tkinter as tk

class Tela_usuario(tk.Frame):
    def __init__(self, app):
        super().__init__()
        self.app = app
    
    def carregar(self):
        # Título
        tk.Label(self, text=f"Editando usuário {self.app.usuario.nome}").pack(pady=5)

        # Campo de entrada para novo nome
        tk.Label(self, text="Novo Nome:").pack(pady=5)
        self.entrada_nome = tk.Entry(self)
        self.entrada_nome.pack(pady=5)

        # Campo de entrada para nova senha
        tk.Label(self, text="Nova Senha:").pack(pady=5)
        self.entrada_senha = tk.Entry(self, show="*")  # Oculta a senha
        self.entrada_senha.pack(pady=5)

        # Botão para alterar dados do usuário
        self.btn_alterar = tk.Button(self, text="Alterar Dados", command=self.alterar_dados)
        self.btn_alterar.pack(pady=5)

        # Botão para apagar o usuário
        self.btn_apagar = tk.Button(self, text="Apagar Usuário", command=self.apagar_usuario)
        self.btn_apagar.pack(pady=5)

    def alterar_dados(self):
        novoUsuario = self.entrada_nome.get()
        if novoUsuario == '':
            novoUsuario = self.app.usuario.nome

        novaSenha = self.entrada_senha.get()
        if novaSenha == '':
            novaSenha = self.app.usuario.senha

        self.app.banco_de_dados.executar(f"UPDATE usuarios SET nome='{novoUsuario}', senha='{novaSenha}' WHERE cod_usuario={self.app.usuario.cod}")
        self.voltar()

    def apagar_usuario(self):
        self.app.banco_de_dados.executar(f"DELETE FROM usuarios WHERE cod_usuario={self.app.usuario.cod}")
        self.voltar()

    def voltar(self):
        tela_login = self.app.telas[0]
        self.app.trocar_tela(tela_login)

        for widget in self.winfo_children():#destroi todas as crianças do frame
            widget.destroy()