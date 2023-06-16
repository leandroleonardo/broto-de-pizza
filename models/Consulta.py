from tkinter import messagebox
from models.ConexaoBD import ConexaoBd


class Consulta:

    # Select

    def Tabela(self, nome):

        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT * FROM ' + nome)
                resultados = cursor.fetchall()
        except:
            return

        return resultados

    def Login(self):

        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT login, AES_DECRYPT(senha, "chave-aleatoria") AS senha FROM USUARIOS;')
                resultados = cursor.fetchall()
        except:
            return

        return resultados

    def TabelaParams(self, tabela, conteudo):

        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT * FROM {} WHERE NOME = "{}"'.format(tabela, conteudo))
                resultados = cursor.fetchall()
        except:
            return

        return resultados

    def Pedidos(self):

        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:

                query = 'SELECT ID_ENCOMENDA, CLIENTES.NOME,CLIENTES.ENDERECO,CLIENTES.TELEFONE, PIZZAS.NOME, COMBO, ' \
                        'PIZZAS.PRECO, ' \
                        'DATE_FORMAT (`DATA_ENTREGA`,"%d/%m/%Y") AS DATA_ENTREGA FROM ENCOMENDAS ' \
                        'INNER JOIN CLIENTES ON ENCOMENDAS.ID_CLIENTE = CLIENTES.ID_CLIENTE ' \
                        'INNER JOIN PIZZAS ON ENCOMENDAS.ID_PIZZA = PIZZAS.ID_PIZZA;'

                cursor.execute(query)

                resultados = cursor.fetchall()

                return resultados
        except:
            return

    def Pizzas(self):

        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT * FROM PIZZAS')
                resultados = cursor.fetchall()
                return resultados
        except:
            messagebox.showinfo('Erro', 'Erro ao consultar banco de dados')

    def Clientes(self):

        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT * FROM CLIENTES')
                resultados = cursor.fetchall()
                return resultados
        except:
            messagebox.showinfo('Erro', 'Erro ao consultar banco de dados')

    def DadosEstatisticas(self):

        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute(
                    'SELECT PR.nome, PR.preco FROM ENCOMENDAS E INNER JOIN PIZZAS PR ON PR.id_pizza = E.id_pizza;')
                vendas = cursor.fetchall()
                return vendas
        except:
            messagebox.showinfo('Erro', 'Erro ao fazer consulta no banco de dados')

    # Filter

    def FiltroEncomendas(self):

        data = ""

        ConexaoBd.AbreConexao(self)

        data = self.data
        cliente = self.cliente.get()
        pizza = self.pizza.get()
        combo = self.combo.get()

        # Monta filtro para Query

        params = 0
        filterQuery = " WHERE "

        if cliente != "":
            filterQuery += 'C.NOME LIKE "{}%" '.format(cliente)
            params += 1
        if data != "":
            if params >= 1:
                filterQuery += ' AND data_entrega = "{}" '.format(data)
            else:
                filterQuery += ' data_entrega = "{}" '.format(data)
                params += 1
        if combo != "":
            if params >= 1:
                filterQuery += ' AND combo LIKE "{}%" '.format(combo)
            else:
                filterQuery += ' combo LIKE "{}%" '.format(combo)
                params += 1
        if pizza != "Nenhum":
            if params >= 1:
                filterQuery += ' AND P.NOME LIKE "{}%" '.format(pizza)
            else:
                filterQuery += ' P.NOME LIKE "{}%" '.format(pizza)
                params += 1

        # Monta consulta

        query = 'SELECT ID_ENCOMENDA, C.NOME,C.ENDERECO,C.TELEFONE, P.NOME, COMBO, P.PRECO, DATE_FORMAT ( ' \
                '`DATA_ENTREGA`,"%d/%m/%Y") ' \
                'AS DATA_ENTREGA FROM ENCOMENDAS AS E ' \
                'INNER JOIN CLIENTES AS C ON E.ID_CLIENTE = C.ID_CLIENTE ' \
                'INNER JOIN PIZZAS AS P ON E.ID_PIZZA = P.ID_PIZZA'

        if filterQuery != " WHERE ":
            query += filterQuery + ";"

        # Busca dados de pedido no banco de dados

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute(query)
                resultados = cursor.fetchall()
                return resultados
        except:
            Consulta.Pedidos(self)

        Consulta.Pedidos(self)

    def FiltroClientes(self):

        data = ""

        ConexaoBd.AbreConexao(self)

        cliente = self.nome.get()
        endereco = self.endereco.get()
        telefone = self.telefone.get()

        # Monta filtro para Query

        params = 0
        filterQuery = " WHERE "

        if cliente != "":
            filterQuery += 'NOME LIKE "{}%" '.format(cliente)
            params += 1
        if endereco != "":
            if params >= 1:
                filterQuery += ' AND ENDERECO LIKE "{}%" '.format(endereco)
            else:
                filterQuery += ' ENDERECO LIKE "{}%" '.format(endereco)
        if telefone != "":
            if params >= 1:
                filterQuery += ' AND TELEFONE LIKE "{}%" '.format(telefone)
            else:
                filterQuery += ' TELEFONE LIKE "{}%" '.format(telefone)

        # Monta consulta

        query = 'SELECT * FROM CLIENTES'

        if filterQuery != " WHERE ":
            query += filterQuery + ";"

        # Busca dados de pedido no banco de dados

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute(query)
                resultados = cursor.fetchall()
                return resultados
        except:
            Consulta.Pedidos(self)

        Consulta.Pedidos(self)

    def FiltroPizzas(self):

        data = ""

        ConexaoBd.AbreConexao(self)

        nome = self.nome.get()
        ingredientes = self.ingredientes.get()
        grupo = self.grupo.get()
        preco = self.preco.get()

        # Monta filtro para Query

        params = 0
        filterQuery = " WHERE "

        if nome != "":
            filterQuery += 'NOME LIKE "{}%" '.format(nome)
            params += 1
        if ingredientes != "":
            if params >= 1:
                filterQuery += ' AND INGREDIENTES LIKE "{}%" '.format(ingredientes)
            else:
                filterQuery += ' INGREDIENTES LIKE "{}%" '.format(ingredientes)
        if grupo != "":
            if params >= 1:
                filterQuery += ' AND GRUPO LIKE "{}%" '.format(grupo)
            else:
                filterQuery += ' GRUPO LIKE "{}%" '.format(grupo)
        if preco != "":
            if params >= 1:
                filterQuery += ' AND PRECO LIKE "{}%" '.format(preco)
            else:
                filterQuery += ' PRECO LIKE "{}%" '.format(preco)

        # Monta consulta

        query = 'SELECT * FROM PIZZAS'

        if filterQuery != " WHERE ":
            query += filterQuery + ";"

        # Busca dados de pedido no banco de dados

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute(query)
                resultados = cursor.fetchall()
                return resultados
        except:
            Consulta.Pizzas(self)

        Consulta.Pizzas(self)

    def FiltroLucroVendas(self):

        query = 'SELECT SUM(PR.preco) FROM ENCOMENDAS E INNER JOIN PIZZAS PR ON PR.id_pizza = E.id_pizza;'

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
        except:
            messagebox.showinfo('Erro', 'Erro ao fazer consulta no banco de dados')