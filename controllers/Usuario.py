from tkinter import messagebox

import self

from models.Consulta import Consulta
from views.Home import Home


class Usuario:

    def __init__(self):
        self.telaLogin = None
        self.root = None
        self.senha = None
        self.username = None

    def Dados(self):
        dados = Consulta.Login(self)
        
        usuario = self.username.get()
        senha = "b'{}'".format(self.senha.get())

        if usuario == dados[0]['login'] and senha == str(dados[0]['senha']):
            self.telaLogin.destroy()
            Tela = Home
            Home.__init__(self)
        else:
            messagebox.showinfo('Mensagem', 'Senha ou usuário inválido.')