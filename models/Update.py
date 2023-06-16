from tkinter import messagebox
from models.ConexaoBD import ConexaoBd
from models.Consulta import Consulta


class Atualiza:

    def AtualizaPedido(self, tabela, campo, id):

        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('DELETE FROM {} WHERE {} = "{}"'.format(tabela, campo, id))
                self.conexao.commit()
        except:
            messagebox.showinfo('Erro', 'Erro ao remover dado!')

    def AtualizaCliente(self, id_cliente):

        ConexaoBd.AbreConexao(self)

        cliente = self.nome.get()
        endereco = self.endereco.get()
        telefone = self.telefone.get()

        # Monta filtro para Query

        params = 0
        filterQuery = "UPDATE CLIENTES SET "

        if cliente != "":
            filterQuery += 'NOME = "{}" '.format(cliente)
            params += 1
        if endereco != "":
            if params >= 1:
                filterQuery += ' , ENDERECO = "{}" '.format(endereco)
            else:
                filterQuery += ' ENDERECO = "{}" '.format(endereco)
        if telefone != "":
            if params >= 1:
                filterQuery += ' , TELEFONE = "{}" '.format(telefone)
            else:
                filterQuery += ' TELEFONE = "{}" '.format(telefone)

        # Monta consulta

        if filterQuery != "UPDATE CLIENTES SET ":
            query = filterQuery + "WHERE ID_CLIENTE = {}".format(id_cliente) + ";"
        else:
            return
        # Busca dados de pedido no banco de dados

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute(query)
                resultados = cursor.fetchall()
                self.conexao.commit()
                return resultados
        except:
            Consulta.Pedidos(self)

        Consulta.Pedidos(self)

    def AtualizaPizza(self, id_pizza):

        ConexaoBd.AbreConexao(self)

        cliente = self.nome.get()
        ingredientes = self.ingredientes.get()
        grupo = self.grupo.get()
        preco = self.preco.get()

        # Monta filtro para Query

        params = 0
        filterQuery = "UPDATE PIZZAS SET "

        if cliente != "":
            filterQuery += 'NOME = "{}" '.format(cliente)
            params += 1
        if ingredientes != "":
            if params >= 1:
                filterQuery += ' , INGREDIENTES = "{}" '.format(ingredientes)
            else:
                filterQuery += ' INGREDIENTES = "{}" '.format(ingredientes)
        if grupo != "":
            if params >= 1:
                filterQuery += ' , GRUPO = "{}" '.format(grupo)
            else:
                filterQuery += ' GRUPO = "{}" '.format(grupo)
        if preco != "":
            if params >= 1:
                filterQuery += ' , PRECO = {} '.format(preco)
            else:
                filterQuery += ' PRECO = {} '.format(preco)

        # Monta consulta

        if filterQuery != "UPDATE PIZZAS SET ":
            query = filterQuery + "WHERE ID_PIZZA = {}".format(id_pizza) + ";"
        else:
            return
        # Busca dados de pedido no banco de dados

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute(query)
                resultados = cursor.fetchall()
                self.conexao.commit()
                return resultados
        except:
            Consulta.Pedidos(self)

        Consulta.Pizzas(self)

    def AtualizaEncomenda(self, id_encomenda):

        ConexaoBd.AbreConexao(self)

        data_entrega = self.data
        cliente = self.cliente.get()
        pizza = self.pizza.get()
        combo = self.combo.get()

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT ID_PIZZA FROM PIZZAS WHERE NOME = %s', pizza)
                id_pizza = cursor.fetchall()[0]['ID_PIZZA']
        except:
            pass

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT ID_CLIENTE FROM CLIENTES WHERE NOME = %s', cliente)
                id_cliente = cursor.fetchall()[0]['ID_CLIENTE']
        except:
            pass

        # Monta filtro para Query

        params = 0
        filterQuery = "UPDATE ENCOMENDAS SET "

        if cliente != "":
            filterQuery += 'id_cliente = "{}" '.format(id_cliente)
            params += 1
        if data_entrega != "":
            if params >= 1:
                filterQuery += ' , data_entrega = "{}" '.format(data_entrega)
            else:
                filterQuery += ' data_entrega = "{}" '.format(data_entrega)
                params += 1
        if combo != "":
            if params >= 1:
                filterQuery += ' , combo = "{}" '.format(combo)
            else:
                filterQuery += ' combo = "{}" '.format(combo)
                params += 1
        if pizza != "" and pizza != "Nenhum":
            if params >= 1:
                filterQuery += ' , id_pizza = {} '.format(id_pizza)
            else:
                filterQuery += ' id_pizza = {} '.format(id_pizza)
                params += 1

        # Monta consulta

        if filterQuery != "UPDATE ENCOMENDAS SET ":
            query = filterQuery + "WHERE id_encomenda = {}".format(id_encomenda) + ";"
        else:
            return
        # Busca dados de pedido no banco de dados


        try:
            with self.conexao.cursor() as cursor:
                cursor.execute(query)
                resultados = cursor.fetchall()
                self.conexao.commit()
                return resultados
        except:
            Consulta.Pedidos(self)

        Consulta.Pizzas(self)
