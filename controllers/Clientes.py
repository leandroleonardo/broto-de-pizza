from tkinter import *
from models.Update import Atualiza
from models.Consulta import Consulta
from models.Delete import Delete
from models.Insert import Insert


class Cliente:

    def __init__(self):
        Cliente.CarregarDados(self)
        nome = ''
        endereco = ''
        telefone = ''

    def Cadastrar(self):

        nome = self.nome.get()
        endereco = self.endereco.get()
        telefone = self.telefone.get()

        Insert.InsereCliente(self, nome, endereco, telefone)

        Cliente.CarregarDados(self)

    def QuantidadeClientes(self):

        qtn_clientes = Consulta.Clientes(self)

        return len(qtn_clientes)

    def CarregarDados(self):

        resultados = Consulta.Clientes(self)

        self.tree.delete(*self.tree.get_children())

        linhaV = []

        for linha in resultados:
            linhaV.append(linha['nome'])
            linhaV.append(linha['endereco'])
            linhaV.append(linha['telefone'])

            self.tree.insert('', END, values=linhaV, iid=linha['id_cliente'], tag='1')

            linhaV.clear()

    def Remover(self):

        id_cliente = int(self.tree.selection()[0])
        Delete.RemoverID(self, 'CLIENTES', 'ID_CLIENTE', id_cliente)
        Cliente.CarregarDados(self)

    def CarregarNomes(self):

        resultados = Consulta.Clientes(self)

        linhaV = []

        for linha in resultados:
            linhaV.append(linha['nome'])

        return linhaV

    def ConsultaClientes(self):

        resultados = Consulta.FiltroClientes(self)

        self.tree.delete(*self.tree.get_children())

        linhaV = []

        for linha in resultados:
            linhaV.append(linha['nome'])
            linhaV.append(linha['endereco'])
            linhaV.append(linha['telefone'])

            self.tree.insert('', END, values=linhaV, iid=linha['id_cliente'], tag='1')

            linhaV.clear()

    def Atualiza(self):

        id_cliente = int(self.tree.selection()[0])
        Atualiza.AtualizaCliente(self, id_cliente)
        Cliente.CarregarDados(self)
