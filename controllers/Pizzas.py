from tkinter import *
from models.Consulta import Consulta
from models.Delete import Delete
from models.Insert import Insert
from models.Update import Atualiza


class Pizza:

    def __init__(self):
        nome = ''
        ingrediente = ''
        grupo = ''
        preco = ''

    def Cadastrar(self):

        nome = self.cliente.get()
        ingredientes = self.ingredientes.get()
        grupo = self.grupo.get()
        preco = self.preco.get()

        Insert.InserePizza(self, nome, ingredientes, grupo, preco)

        Pizza.CarregarDados(self)

    def CarregarDados(self):

        resultados = Consulta.Pizzas(self)

        self.tree.delete(*self.tree.get_children())

        linhaV = []

        for linha in resultados:
            linhaV.append(linha['nome'])
            linhaV.append(linha['ingredientes'])
            linhaV.append(linha['grupo'])
            linhaV.append(linha['preco'])

            self.tree.insert('', END, values=linhaV, iid=linha['id_pizza'], tag='1')

            linhaV.clear()

    def Atualiza(self):
        id_cliente = int(self.tree.selection()[0])
        Atualiza.AtualizaPizza(self, id_cliente)
        Pizza.CarregarDados(self)

    def Filtra(self):

        resultados = Consulta.FiltroPizzas(self)

        self.tree.delete(*self.tree.get_children())

        linhaV = []

        for linha in resultados:
            linhaV.append(linha['nome'])
            linhaV.append(linha['ingredientes'])
            linhaV.append(linha['grupo'])
            linhaV.append(linha['preco'])

            self.tree.insert('', END, values=linhaV, iid=linha['id_pizza'], tag='1')

            linhaV.clear()

    def Remover(self):

        id_pizza = int(self.tree.selection()[0])
        Delete.RemoverID(self, 'PIZZAS', 'ID_PIZZA', id_pizza)
        Pizza.CarregarDados(self)

    def Nomes(self):

        resultados = Consulta.Pizzas(self)

        linhaV = ["Nenhum"]

        for linha in resultados:
            linhaV.append(linha['nome'])

        return linhaV