from tkinter import messagebox
from models.ConexaoBD import ConexaoBd


class Insert:

    def InsereVenda(self, id_usuario, id_produto, nome, quantidade, valor_total, data_vendas):

        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('INSERT INTO VENDAS (ID_USUARIO, ID_PRODUTO, NOME, QUANTIDADE, PRECO_TOTAL, '
                               'DATA_VENDA) VALUES ({},{},"{}",{},{},"{}")'.format(id_usuario, id_produto,
                                                                                   nome, quantidade, valor_total,
                                                                                   data_vendas))
                self.conexao.commit()
                messagebox.showinfo('Mensagem', 'Produto cadastrado com sucesso!')
        except:
            messagebox.showinfo('Erro', 'Erro ao inserir pedido no banco de dados!')

    def InserePizza(self, nome, ingredientes, grupo, preco):

        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT * FROM PIZZAS WHERE NOME = %s', nome)
                check = cursor.fetchall()
                if check:
                    messagebox.showinfo('Erro', 'Produto já cadastrado')
                    return
        except:
            pass

        # Inserir pizza
        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                query = 'INSERT INTO PIZZAS (NOME, INGREDIENTES, GRUPO, PRECO)' \
                             ' VALUES ("{}","{}","{}",{})'.format(nome, ingredientes, grupo, preco)
                cursor.execute(query)
                self.conexao.commit()
                messagebox.showinfo('Mensagem', 'Produto cadastrado com sucesso!')
        except FileExistsError as error:
            messagebox.showinfo('Erro', 'Erro ao inserir produto no banco de dados')

    def InsereCliente(self, nome, endereco, telefone):

        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT * FROM CLIENTES WHERE NOME = %s', nome)
                check = cursor.fetchall()
                if check:
                    messagebox.showinfo('Erro', 'Cliente já cadastrado')
                    return
        except:
            pass

        # Insert client
        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('INSERT INTO CLIENTES (NOME, ENDERECO, TELEFONE)'
                               'VALUES (%s,%s,%s)', (nome, endereco, telefone))
                self.conexao.commit()
                messagebox.showinfo('Mensagem', 'Cliente cadastrado com sucesso!')
        except:
            messagebox.showinfo('Erro', 'Erro ao registrar cliente')

    def InserePedido(self, cliente, combo, data_entrega, pizza):

        # Get ID Cliente

        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT ID_CLIENTE FROM CLIENTES WHERE NOME = %s', cliente)
                id_cliente = cursor.fetchall()[0]['ID_CLIENTE']
        except:
            pass

        # Get ID Candy

        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT ID_PIZZA FROM PIZZAS WHERE NOME = %s', pizza)
                id_pizza = cursor.fetchall()[0]['ID_PIZZA']
        except:
            pass

        # Price Candy

        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT PRECO FROM PIZZAS WHERE NOME = %s', pizza)
                preco = cursor.fetchall()[0]['PRECO']
        except:
            pass

        # Insert request

        ConexaoBd.AbreConexao(self)

        query = 'INSERT INTO ENCOMENDAS (id_cliente, id_pizza, combo, data_entrega)' \
                ' VALUES ("{}","{}",{},"{}")'.format(id_cliente, id_pizza, combo, data_entrega)

        try:
            with self.conexao.cursor() as cursor:

                cursor.execute(query)

                self.conexao.commit()

                messagebox.showinfo('Mensagem', 'Encomenda cadastrado com sucesso!')
        except:
            messagebox.showinfo('Erro', 'Erro ao cadastrar pedido')