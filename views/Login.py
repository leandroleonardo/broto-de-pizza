import customtkinter
from tkinter import Label
from self import self
from controllers.Usuario import Usuario
from PIL import ImageTk, Image

from views import Config


class Login:

    def __init__(self):
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.telaLogin = customtkinter.CTk()
        self.telaLogin.geometry("600x700")

        frame = customtkinter.CTkFrame(master=self.telaLogin)
        frame.pack(pady=30, padx=60, fill="both", expand=True)

        imagem = Image.open("logo.png")
        imagem_tk = ImageTk.PhotoImage(imagem)

        label_imagem = Label(self.telaLogin, image=imagem_tk)
        label_imagem.pack(pady=12, padx=10)

        self.telaLogin.iconbitmap(
            'icone.ico')

        self.telaLogin.title('Login')

        label = customtkinter.CTkLabel(master=frame, text="Broto de Pizza", font=('Arial', 22))
        label.pack(pady=12, padx=10)

        self.username = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
        self.username.pack(pady=12, padx=10)

        self.senha = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
        self.senha.pack(pady=12, padx=10)

        button = customtkinter.CTkButton(master=frame, command=lambda: Usuario.Dados(self),
                                         fg_color='#cb9b2f', hover_color='#bc9643', text='Login')
        button.pack(pady=12, padx=10)

        config_bd = customtkinter.CTkButton(master=frame, text="Configuração", font=('Arial', 12), fg_color='#212121', hover_color='#212121', command=Config.Conexao)
        config_bd.pack(pady=15, padx=10)

        self.telaLogin.mainloop()


Tela = Login
Login.__init__(self)