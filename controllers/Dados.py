from models.Consulta import Consulta
import pandas as pd
from openpyxl.workbook import Workbook
import tkinter as tk
from tkinter import filedialog


class Dado:

    def ExportarDados(self, fonte):

        if fonte == 'Clientes':
            dados = Consulta.Clientes(self)
        elif fonte == 'Pizzas':
            dados = Consulta.Pizzas(self)
        else:
            dados = Consulta.Pedidos(self)

        df = pd.DataFrame(dados)

        def selecionar_local():
            root = tk.Tk()
            root.withdraw()
            local_arquivo = filedialog.asksaveasfilename(defaultextension='.xlsx')
            return local_arquivo

        local_arquivo = selecionar_local()

        df.to_excel(local_arquivo, index=False)