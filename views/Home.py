import sys

from tkcalendar import Calendar
from datetime import date
from tkinter import Tk, NO, ttk
from customtkinter import CTkLabel, CTkButton, CTkEntry, CTkFrame, CTkOptionMenu, CTkScrollableFrame
import customtkinter

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

from controllers.Estatisticas import Estatistica
from controllers.Encomendas import Encomenda
from controllers.Pizzas import Pizza
from controllers.Clientes import Cliente
from controllers.Dados import Dado


class Home:

    def __init__(self):

        self.label = None
        self.btnLoad = None
        self.frame_btn_graph = None
        self.btns = None
        self.frame_grafico = None
        self.btnGrafico = None
        self.modeloGrafico = None
        self.frame_grafico_barra = None
        self.frame_graficos = None
        self.frame_title = None

        self.frame_active = 'None'

        customtkinter.set_appearance_mode("Dark")

        # Config date
        self.data = date.today()
        self.contData = 0

        self.root = customtkinter.CTk()

        self.root.attributes('-fullscreen', True)

        # Config theme Dark
        style = ttk.Style(self.root)
        self.root.tk.call("source", "forest-dark.tcl")
        style.theme_use("forest-dark")

        self.largura = 1280
        self.altura = 600

        # Config da frame
        self.frame = CTkFrame(self.root)
        self.frame.place(x=15, y=100)

        self.root.title('Cadastro de produtos')

        self.root.geometry('1280x720')
        self.root.minsize(950, 500)

        CTkLabel(self.root, text='Broto De Pizza', font=('Arial', 20)) \
            .grid(row=1, column=1, padx=25, pady=25)

        # Menu
        CTkButton(self.root, text='Home', fg_color='#cb9b2f', hover_color='#bc9643',
                  command=lambda: Home.FrameHome(self, self.root, self.frame_active)) \
            .grid(row=2, column=1, padx=10, pady=10)
        CTkButton(self.root, text='Clientes', fg_color='#cb9b2f', hover_color='#bc9643',
                  command=lambda: Home.FrameClientes(self, self.root)) \
            .grid(row=3, column=1, padx=10, pady=10)
        CTkButton(self.root, text='Encomenda', fg_color='#cb9b2f', hover_color='#bc9643',
                  command=lambda: Home.FrameEncomendas(self, self.root)) \
            .grid(row=4, column=1, padx=10, pady=10)
        CTkButton(self.root, text='Pizzas', fg_color='#cb9b2f', hover_color='#bc9643',
                  command=lambda: Home.FramePizzas(self, self.root)) \
            .grid(row=5, column=1, padx=10, pady=10)
        CTkButton(self.root, text='Exportar Dados', fg_color='#cb9b2f', hover_color='#bc9643',
                  command=lambda: Home.FrameExportarDados(self, self.root)) \
            .grid(row=6, column=1, padx=10, pady=10)
        CTkButton(self.root, text='Sair', fg_color='#cb9b2f', hover_color='#bc9643',
                  command=lambda: Home.FecharPrograma(self)) \
            .grid(row=7, column=1, padx=10, pady=400)

        self.frame_active = Home.FrameHome(self, self.root, self.frame_active)

        self.root.mainloop()

    # Components
    def Graficos(self):

        try:
            self.frame.destroy()
            self.frame = CTkFrame(self.root)
            self.frame.place(x=200, y=100)  # 200 / 100
        except:
            pass

        # Graficos
        dados = Estatistica.GerarEstatistica(self)

        pizzas = dados[0]
        precos = dados[1]

        # Criar uma figura do Matplotlib
        fig = plt.figure(figsize=(14, 7.5), dpi=70)

        # Adicionar um subplot
        ax = fig.add_subplot(111)
        ax.set_title('Lucro por pizza')
        ax.set_xlabel('Pizzas')
        ax.set_ylabel('Valor')

        # Adicionar dados ao subplot
        x = pizzas
        y = precos

        if self.modeloGrafico.get() == 'Linha':
            ax.plot(x, y, color='#cd9a2f')
        else:
            ax.bar(x, y, color='#cd9a2f')

        # Criar um objeto FigureCanvasTkAgg para exibir a figura do Matplotlib no Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        fig.set_facecolor('#a5a5a5')
        ax.set_facecolor('#4c4c4c')

    def Calendario(self):

        # Config
        self.calendario = Tk()
        self.calendario.title('Calendário')

        dataAtual = str(date.today()).split('-')

        # Calendar config

        cal = Calendar(self.calendario,
                       selectmode='day',
                       year=int(dataAtual[0]),
                       month=int(dataAtual[1]),
                       day=int(dataAtual[2]))

        cal.grid(row=0, column=0, columnspan=2, pady=20, padx=10)

        # Date formatting

        def pegaData():
            self.data = cal.get_date()

            dataFormatado = str(self.data).split('/')

            ano = dataFormatado[2]
            dia = dataFormatado[1]
            mes = dataFormatado[0]

            dataFormatada = ano + '/' + mes + '/' + dia

            self.data = dataFormatada

            self.calendario.destroy()

            self.contData += 1

        # Date config

        def limpaData():
            self.data = ""
            self.calendario.destroy()

        CTkButton(self.calendario, text='Confirmar', width=20, command=pegaData) \
            .grid(row=1, column=1, columnspan=2, pady=20, padx=10)

        CTkButton(self.calendario, text='Limpar data', width=20, command=limpaData) \
            .grid(row=1, column=2, columnspan=2, pady=25, padx=10)

    def FecharPrograma(self):
        sys.exit()

    def Cleaning(self):

        try:
            self.modeloGrafico.place(x=5000, y=100)
            self.btnLoad.place(x=5000, y=100)
            self.label.destroy()
            self.frame.destroy()
            self.frame_title()
        except:
            pass

    # Frames

    def FrameExportarDados(self, tela):

        if self.frame_active == 'Dados':
            return

        Home.Cleaning(self)

        self.root = tela

        self.frame = CTkFrame(self.root)
        self.frame.place(x=200, y=100)

        # Titles

        self.root.title('Pizza')

        CTkLabel(self.frame_title, text="          Dados 🎲          ", font=('Arial', 30)) \
            .grid(row=1, column=0, columnspan=4, padx=15, pady=6, ipady=15)

        CTkLabel(self.frame, text="👤", font=('Arial', 30)) \
            .grid(row=2, column=0, padx=10, pady=10)

        CTkLabel(self.frame, text="🍕", font=('Arial', 30)) \
            .grid(row=2, column=1, padx=10, pady=10)

        CTkLabel(self.frame, text="📝", font=('Arial', 30)) \
            .grid(row=2, column=2, padx=10, pady=10)

        CTkButton(self.frame, text='Clientes', fg_color='#cb9b2f', hover_color='#bc9643',
                  command=lambda: Dado.ExportarDados(self,'Clientes')) \
            .grid(row=3, column=0, padx=10, pady=10)

        CTkButton(self.frame, text='Pizzas', fg_color='#cb9b2f', hover_color='#bc9643',
                  command=lambda: Dado.ExportarDados(self,'Pizzas')) \
            .grid(row=3, column=1, padx=10, pady=10)

        CTkButton(self.frame, text='Encomendas', fg_color='#cb9b2f', hover_color='#bc9643',
                  command=lambda: Dado.ExportarDados(self,'Encomendas')) \
            .grid(row=3, column=2, padx=10, pady=10)

        self.frame_active = 'Dados'

        self.root.mainloop()

    def FramePizzas(self, tela):

        if self.frame_active == 'Pizzas':
            return

        # Screen config

        Home.Cleaning(self)

        self.root = tela

        self.frame = CTkFrame(self.root)
        self.frame.place(x=200, y=100)

        self.frame.place_forget()

        # Titles

        self.root.title('Pizza')

        CTkLabel(self.frame, text='Informações de Pizza', font=('Arial', 19)).grid(row=5, column=0, columnspan=4,
                                                                                   padx=15,
                                                                                   pady=6, ipady=15)

        CTkLabel(self.frame_title, text="          Pizzas 🍕          ", font=('Arial', 30)) \
            .grid(row=1, column=0, columnspan=4, padx=15, pady=6, ipady=15)

        # Buttons and inputs

        # Name
        CTkLabel(self.frame, text='Nome').grid(row=6, column=0, columnspan=1, pady=5, padx=5)
        self.nome = CTkEntry(self.frame)
        self.nome.grid(row=6, column=1, padx=5, pady=5)

        # Ingredients
        CTkLabel(self.frame, text='Ingredientes').grid(row=7, column=0, columnspan=1, pady=5, padx=5)
        self.ingredientes = CTkEntry(self.frame)
        self.ingredientes.grid(row=7, column=1, padx=5, pady=5)

        # Groups
        CTkLabel(self.frame, text='Grupo').grid(row=8, column=0, columnspan=1, pady=5, padx=5)
        self.grupo = CTkEntry(self.frame)
        self.grupo.grid(row=8, column=1, padx=5, pady=5)

        # Price
        CTkLabel(self.frame, text='Preço').grid(row=9, column=0, columnspan=1, pady=5, padx=5)
        self.preco = CTkEntry(self.frame)
        self.preco.grid(row=9, column=1, padx=5, pady=5)

        # Buttons command=lambda: cliente.cadastrar(self)

        CTkButton(self.frame, text='Cadastrar', command=lambda: Pizza.Cadastrar(self), fg_color="#64c23b",
                  hover_color="#2fad2d").grid(row=12, column=0,
                                              padx=15, pady=7)

        CTkButton(self.frame, text='Excluir', command=lambda: Pizza.Remover(self), fg_color="#ea6960",
                  hover_color="#c93434").grid(row=12, column=1, padx=0,
                                              pady=0)

        CTkButton(self.frame, text='Atualizar', command=lambda: Pizza.Atualiza(self)).grid(row=13, column=0, padx=15,
                                                                                           pady=17)

        CTkButton(self.frame, text='Filtrar', command=lambda: Pizza.Filtra(self), fg_color='#cb9b2f',
                  hover_color='#bc9643').grid(row=13, column=1, padx=15,
                                              pady=17)

        # Table

        self.tree = ttk.Treeview(self.frame, selectmode="browse", columns=("c1", "c2", "c3", "c4"),
                                 show="headings")

        self.tree.configure()

        self.tree.column("c1", width=170, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='Nome')

        self.tree.column("c2", width=320, minwidth=500, stretch=NO)
        self.tree.heading('#2', text='Ingredientes')

        self.tree.column("c3", width=150, minwidth=500, stretch=NO)
        self.tree.heading('#3', text='Grupo')

        self.tree.column("c4", width=100, minwidth=500, stretch=NO)
        self.tree.heading('#4', text='Preço')

        self.tree.grid(row=6, column=5, padx=10, pady=10, columnspan=3, rowspan=6)

        Pizza.CarregarDados(self)
        self.frame.place(x=200, y=100)

        self.frame_active = 'Pizzas'

        self.root.mainloop()

    def FrameClientes(self, tela):

        if self.frame_active == 'Clientes':
            return

        # Screen config

        self.root = tela

        Home.Cleaning(self)

        CTkLabel(self.frame_title, text="        Clientes 👥         ", font=('Arial', 30)) \
            .grid(row=1, column=0, columnspan=4, padx=15, pady=6, ipady=15)

        self.frame = CTkFrame(self.root)
        self.frame.place(x=200, y=100)
        self.frame.place_forget()

        # Titles

        self.root.title('Clientes')

        CTkLabel(self.frame, text='Cadastro de Cliente', font=('Arial', 19)) \
            .grid(row=5, column=0, columnspan=4, padx=15, pady=5, ipady=15)
        # Buttons and inputs

        # Name
        CTkLabel(self.frame, text='Nome').grid(row=6, column=0, columnspan=1, pady=5, padx=5)
        self.nome = CTkEntry(self.frame)
        self.nome.grid(row=6, column=1, padx=5, pady=5)

        # Addres
        CTkLabel(self.frame, text='Endereco').grid(row=7, column=0, columnspan=1, pady=5, padx=5)
        self.endereco = CTkEntry(self.frame)
        self.endereco.grid(row=7, column=1, padx=5, pady=5)

        # Phone
        CTkLabel(self.frame, text='Telefone').grid(row=8, column=0, columnspan=1, pady=5, padx=5)
        self.telefone = CTkEntry(self.frame)
        self.telefone.grid(row=8, column=1, padx=5, pady=5)

        # Buttons
        CTkButton(self.frame, text='Cadastrar', fg_color="#64c23b", hover_color="#2fad2d",
                  command=lambda: Cliente.Cadastrar(self)).grid(row=9, column=0, padx=15, pady=7)

        CTkButton(self.frame, text='Excluir', fg_color="#ea6960", hover_color="#c93434",
                  command=lambda: Cliente.Remover(self)).grid(row=9, column=1, padx=0, pady=0)

        CTkButton(self.frame, text='Atualizar',
                  command=lambda: Cliente.Atualiza(self)).grid(row=10, column=0, padx=15, pady=17)

        CTkButton(self.frame, text='Filtrar', fg_color='#cb9b2f', hover_color='#bc9643',
                  command=lambda: Cliente.ConsultaClientes(self)).grid(row=10, column=1, padx=15, pady=17)

        # Table

        self.tree = ttk.Treeview(self.frame, selectmode="browse", columns=("c1", "c2", "c3"),
                                 show="headings")

        self.tree.configure()

        self.tree.column("c1", width=170, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='Nome')

        self.tree.column("c2", width=350, minwidth=500, stretch=NO)
        self.tree.heading('#2', text='Endereco')

        self.tree.column("c3", width=170, minwidth=500, stretch=NO)
        self.tree.heading('#3', text='Telefone')

        self.tree.grid(row=6, column=5, padx=10, pady=10, columnspan=3, rowspan=6)

        Cliente.CarregarDados(self)
        self.frame.place(x=200, y=100)

        self.frame_active = 'Clientes'

        self.root.mainloop()

    def FrameEncomendas(self, tela):

        if self.frame_active == 'Encomendas':
            return

        # Screen config

        self.root = tela

        Home.Cleaning(self)

        CTkLabel(self.frame_title, text="Encomenda 📖", font=('Arial', 30)) \
            .grid(row=1, column=0, columnspan=4, padx=15, pady=6, ipady=15)

        self.frame = CTkFrame(self.root)
        self.frame.place(x=200, y=100)
        self.frame.place_forget()

        # Titles
        self.root.title('Encomenda')
        CTkLabel(self.frame, text='Informações encomendas', font=('Arial', 19)) \
            .grid(row=5, column=0, columnspan=4, padx=15, pady=5, ipady=15)

        # Buttons and inputs

        # Date
        CTkLabel(self.frame, text='Data') \
            .grid(row=6, column=0, columnspan=1, pady=0, padx=0)
        self.data_entrega = CTkButton(self.frame, text='Selecionar data', command=lambda: Home.Calendario(self),
                                      fg_color='#7c7979', hover_color='#919191')
        self.data_entrega.grid(row=6, column=1, padx=0, pady=0)

        # Name
        CTkLabel(self.frame, text='Cliente') \
            .grid(row=7, column=0, columnspan=1, pady=5, padx=5)
        self.cliente = CTkEntry(self.frame)
        self.cliente.grid(row=7, column=1, padx=5, pady=5)

        # Pizzas
        CTkLabel(self.frame, text='Pizzas') \
            .grid(row=8, column=0, columnspan=1, pady=5, padx=5)
        self.pizza = CTkOptionMenu(self.frame, values=Pizza.Nomes(self), dynamic_resizing=False, fg_color='#cb9b2f',
                                   button_color='#cb9b2f', hover='#cb9b32')
        self.pizza.grid(row=8, column=1, padx=5, pady=5)

        # Amount
        CTkLabel(self.frame, text='Combo') \
            .grid(row=9, column=0, columnspan=1, pady=5, padx=5)
        self.combo = CTkEntry(self.frame)
        self.combo.grid(row=9, column=1, padx=5, pady=5)

        CTkButton(self.frame, text='Cadastrar', fg_color="#64c23b",
                  command=lambda: Encomenda.Cadastrar(self)).grid(row=11, column=0, padx=15, pady=7)

        CTkButton(self.frame, text='Excluir', fg_color="#ea6960", hover_color="#ea6990",
                  command=lambda: Encomenda.Remover(self)).grid(row=11, column=1, padx=0, pady=0)

        CTkButton(self.frame, text='Atualizar', fg_color="#7575fc",
                  command=lambda: Encomenda.Atualiza(self)).grid(row=12, column=0, padx=15, pady=17)

        CTkButton(self.frame, text='Filtrar', fg_color="#eabe64",
                  command=lambda: Encomenda.Filtra(self)).grid(row=12, column=1, padx=15, pady=17)
        # Table

        self.tree = ttk.Treeview(self.frame, selectmode="browse", columns=("c1", "c2", "c3", "c4", "c5", "c6", "c7"),
                                 show="headings")

        self.tree.configure()

        self.tree.column("c1", width=100, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='Nome')

        self.tree.column("c2", width=150, minwidth=500, stretch=NO)
        self.tree.heading('#2', text='Endereco')

        self.tree.column("c3", width=75, minwidth=500, stretch=NO)
        self.tree.heading('#3', text='Celular')

        self.tree.column("c4", width=200, minwidth=500, stretch=NO)
        self.tree.heading('#4', text='Pizzas')

        self.tree.column("c5", width=44, minwidth=500, stretch=NO)
        self.tree.heading('#5', text='Combo')

        self.tree.column("c6", width=50, minwidth=500, stretch=NO)
        self.tree.heading('#6', text='Valor')

        self.tree.column("c7", width=75, minwidth=500, stretch=NO)
        self.tree.heading('#7', text='Data')

        self.tree.grid(row=6, column=5, padx=10, pady=10, columnspan=3, rowspan=6)

        Encomenda.CarregarDados(self)
        self.frame.place(x=200, y=100)

        self.frame_active = 'Encomendas'

        self.root.mainloop()

    def FrameHome(self, tela, frame_active):

        if self.frame_active == 'Home':
            return

        # Screen config

        self.root = tela

        try:
            self.frame.destroy()
            self.frame_title.destroy()
            self.frame_title()
            self.btnLoad.destroy()
        except:
            pass

        # Titles

        self.frame_title = CTkFrame(self.root)
        self.frame_title.place(x=25, y=-50)

        qt_cliente = Cliente.QuantidadeClientes(self)
        qt_encomendas = Encomenda.QuantidadeEncomendas(self)
        qt_lucro = Encomenda.lucroEncomendar(self)[0]['SUM(PR.preco)']

        # Update text on screen

        self.frame_title.destroy()

        # Recreate component

        self.frame_title = CTkFrame(self.root)
        self.frame_title.place(x=200, y=10)

        # Print text
        CTkLabel(self.frame_title, text="        Estatísticas 📈         ", font=('Arial', 30)) \
            .grid(row=1, column=0, columnspan=4, padx=15, pady=6, ipady=15)

        # menu

        self.frame = CTkFrame(self.root)
        self.frame.place(x=200, y=100)  # 200 / 100

        self.modeloGrafico = CTkOptionMenu(self.root, values=['Barra', 'Linha'], dynamic_resizing=False,
                                           fg_color='#cb9b2f',
                                           button_color='#cb9b2f',
                                           hover='#cb9b2f')
        self.modeloGrafico.place(x=1200, y=100)

        self.btnLoad = CTkButton(self.root, text='Carregar', fg_color="#cb9b2f", hover_color="#cb9b2f",
                                 command=lambda: Home.Graficos(self))
        self.btnLoad.place(x=1200, y=150)

        Home.Graficos(self)

        text = 'Clientes: {}\tPedidos: {}\tLucro: R$ {}'.format(qt_cliente, qt_encomendas, qt_lucro)

        self.label = CTkLabel(self.root, text=text, font=("Arial", 18))
        self.label.place(x=200, y=650)

        self.frame_active = 'Home'

        self.root.mainloop()