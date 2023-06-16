from tkinter import *
from models.Update import Atualiza
from models.Consulta import Consulta
from models.Delete import Delete
from models.Insert import Insert

class Encomenda:

    def __init__(self):
        nome = ''
        ingrediente = ''
        grupo = ''
        preco = ''

    def Cadastrar(self):

        cliente = self.cliente.get()
        combo = int(self.combo.get())
        data_entrega = self.data
        pizza = self.pizza.get()

        Insert.InserePedido(self, cliente, combo, data_entrega, pizza)

        Encomenda.CarregarDados(self)

    def CarregarDados(self):

        resultados = Consulta.Pedidos(self)

        self.tree.delete(*self.tree.get_children())

        linhaV = []

        for linha in resultados:
            linhaV.append(linha['NOME'])
            linhaV.append(linha['ENDERECO'])
            linhaV.append(linha['TELEFONE'])
            linhaV.append(linha['PIZZAS.NOME'])
            linhaV.append(linha['COMBO'])
            linhaV.append(linha['PRECO'])
            linhaV.append(linha['DATA_ENTREGA'])

            self.tree.insert('', END, values=linhaV, iid=linha['ID_ENCOMENDA'], tag='1')

            linhaV.clear()

    def Remover(self):

        id_pedido = int(self.tree.selection()[0])
        Delete.RemoverID(self, 'ENCOMENDAS', 'ID_ENCOMENDA', id_pedido)
        Encomenda.CarregarDados(self)

    def Nomes(self):

        resultados = Consulta.Doces(self)

        linhaV = []

        for linha in resultados:
            linhaV.append(linha['nome'])

        return linhaV

    def CarregarDadosFiltro(self):

        resultados = Consulta.FiltroPedidos(self)

        self.tree.delete(*self.tree.get_children())

        linhaV = []

        for linha in resultados:
            linhaV.append(linha['NOME'])
            linhaV.append(linha['ENDERECO'])
            linhaV.append(linha['TELEFONE'])
            linhaV.append(linha['DOCES.NOME'])
            linhaV.append(linha['QUANTIDADE'])
            linhaV.append(linha['PRECO_TOTAL'])
            linhaV.append(linha['DATA_ENTREGA'])

            self.tree.insert('', END, values=linhaV, iid=linha['ID_PEDIDO'], tag='1')

            linhaV.clear()

    def AtualizarDados(self):

        id_pedido = int(self.tree.selection()[0])

        nome = self.cliente.get()
        quantidade = int(self.quantidade.get())
        data_entrega = self.data
        doce = self.doce.get()

        Atualiza.AtualizaPedido(self, nome, quantidade, data_entrega, doce)

        Encomenda.CarregarDados(self)

    def lucroEncomendar(self):

        lucro_vendas = Consulta.FiltroLucroVendas(self)

        return lucro_vendas

    def QuantidadeEncomendas(self):

        qtn_encomendas = Consulta.Pedidos(self)

        return len(qtn_encomendas)

    def Atualiza(self):

        id_encomenda = int(self.tree.selection()[0])
        Atualiza.AtualizaEncomenda(self, id_encomenda)
        Encomendas.CarregarDados(self)

    def Filtra(self):

        resultados = Consulta.FiltroEncomendas(self)

        self.tree.delete(*self.tree.get_children())

        linhaV = []

        for linha in resultados:
            linhaV.append(linha['NOME'])
            linhaV.append(linha['ENDERECO'])
            linhaV.append(linha['TELEFONE'])
            linhaV.append(linha['P.NOME'])
            linhaV.append(linha['COMBO'])
            linhaV.append(linha['PRECO'])
            linhaV.append(linha['DATA_ENTREGA'])

            self.tree.insert('', END, values=linhaV, iid=linha['ID_ENCOMENDA'], tag='1')

            linhaV.clear()