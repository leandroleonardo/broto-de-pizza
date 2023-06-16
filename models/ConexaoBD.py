import json
import pymysql.cursors
from tkinter import messagebox


class ConexaoBd:

    def __init__(self):
        self.conexao = None

    def AbreConexao(self):

        # Abre o arquivo JSON
        with open('config.json') as f:
            data = json.load(f)

        # Obtém os valores das informações sensíveis
        host = data['host']
        user = data['user']
        password = data['password']
        database = data['database']

        try:
            self.conexao = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                cursorclass=pymysql.cursors.DictCursor
            )

            return 1

        except:
            messagebox.showinfo('Error', 'Erro ao tentar conectar banco de dados')
            return False


ConexaoBd().AbreConexao()
