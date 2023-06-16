from tkinter import messagebox
import customtkinter
import json
from models.ConexaoBD import ConexaoBd


class Conexao:

    def __init__(self):
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.config = customtkinter.CTk()
        self.config.geometry("550x350")

        frame = customtkinter.CTkFrame(master=self.config)
        frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.config.iconbitmap(
            'icone.ico')

        self.config.title('Configuração')

        label = customtkinter.CTkLabel(master=frame, text="Conexão com banco de dados", font=('Arial', 20))
        label.pack(pady=12, padx=20)

        self.host = customtkinter.CTkEntry(master=frame, placeholder_text="host")
        self.host.pack(pady=12, padx=10)

        self.user = customtkinter.CTkEntry(master=frame, placeholder_text="user", show="*")
        self.user.pack(pady=12, padx=10)

        self.password = customtkinter.CTkEntry(master=frame, placeholder_text="password", show="*")
        self.password.pack(pady=12, padx=10)

        self.database = customtkinter.CTkEntry(master=frame, placeholder_text="database", show="*")
        self.database.pack(pady=12, padx=10)

        button = customtkinter.CTkButton(master=frame, command=lambda: Conexao.Conectar(self),
                                         fg_color='#cb9b2f', hover_color='#bc9643', text='Conectar')
        button.pack(pady=12, padx=10)

        self.config.mainloop()

    def Conectar(self):

        # Abre o arquivo JSON
        with open('config.json', 'r') as f:
            data = json.load(f)

        # Atualiza informações
        data['host'] = self.host.get()
        data['user'] = self.user.get()
        data['password'] = self.password.get()
        data['database'] = self.database.get()

        # Grava no JSON
        with open('config.json', 'w') as f:
            json.dump(data, f, indent=4)

        valor = ConexaoBd.AbreConexao(self)

        if valor == 1:
            self.config.destroy()
            messagebox.showinfo('Sucesso', 'Conectado com sucesso ao database:  '+ data['database'])