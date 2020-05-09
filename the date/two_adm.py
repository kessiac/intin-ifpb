import psycopg2
import tkinter as tk
from tkinter import messagebox
from three_adm import *
import sys

class Service(tk.Frame):

        def __init__(self, master=None):

                tk.Frame.__init__(self, master=None, bg='#2b383e')
                self.master = master

                self.viewC = tk.Button(self, font=("Times", 12, 'bold'), text="CONTRATOS", foreground='#26dbba', bg='#2b383e', padx=65, command=self.view)
                self.viewC.pack(fill=tk.X)

                self.okService = tk.Button(self, font=("Times", 12, 'bold'), text="CONCLUIDOS", foreground='#26dbba', bg='#2b383e', padx=65, command=self.serviceDelete)
                self.okService.pack(fill=tk.X)
                
        def view (self):

                self.master.changeScreen(ViewBD(self.master))
                self.destroy()
		
        def serviceDelete(self):
                self.viewC.destroy()
                self.okService.destroy()
                
                self.codClient = tk.Label(self, font=("Times", 12, 'bold'), text="CÓDIGO DO CLIENTE", foreground='#26dbba', bg='#2b383e')
                self.codClient.pack(fill=tk.X)
                self.codEntry = tk.Entry(self, font=("Times", 12, 'bold'), foreground='#26dbba', bg='#2b383e')
                self.codEntry.pack(fill=tk.X)

                self.btDelete = tk.Button(self, font=("Times", 12, 'bold'), text="CONCLUIR", foreground='#26dbba', bg='#2b383e', padx=58, command=self.deleteCod)
                self.btDelete.pack(fill=tk.X)

                self.btView = tk.Button(self, font=("Times", 12, 'bold'), text="CONTRATOS", foreground='#26dbba', bg='#2b383e', padx=58, command=self.viewNew)
                self.btView.pack(fill=tk.X)

        def deleteCod(self):

                conexao = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='1407')
                cursor = conexao.cursor()
                cursor.execute(f'DELETE FROM contratos WHERE id = ({self.codEntry.get()})')
                conexao.commit()
                conexao.close()
                messagebox.showinfo('CONCLUIDO', 'Parabéns, um contrato concluido.')

        def viewNew(self):
                self.master.changeScreen(ViewBD(self.master))
                self.destroy()
