import psycopg2
import tkinter as tk
from tkinter import messagebox
import sys

class Contract(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master=None, bg='#2b383e')

        self.name = tk.Label(self, font=("Times", 12, 'bold'), text="NOME", foreground='#26dbba', bg='#2b383e')
        self.name.grid(row=0,column=0)
        self.nameEntry = tk.Entry(self, font=("Times", 12), foreground='#26dbba', bg='#2b383e')
        self.nameEntry.grid(row=0,column=1)

        self.phone = tk.Label(self, font=("Times", 12, 'bold'), text="CONTATO", foreground='#26dbba', bg='#2b383e')
        self.phone.grid(row=1,column=0)
        self.phoneEntry = tk.Entry(self, font=("Times", 12), foreground='#26dbba', bg='#2b383e')
        self.phoneEntry.grid(row=1,column=1)
        self.exPhone = tk.Label(self, font=("Times", 10), text="Ex: (99) 99999-9999", foreground='black', bg='#2b383e')
        self.exPhone.grid(row=2,column=1)

        self.local = tk.Label(self, font=("Times", 12, 'bold'), text="LOCAL", foreground='#26dbba', bg='#2b383e')
        self.local.grid(row=3,column=0)
        self.localEntry = tk.Entry(self, font=("Times", 12), foreground='#26dbba', bg='#2b383e')
        self.localEntry.grid(row=3,column=1)

        self.date = tk.Label(self, font=("Times", 12, 'bold'), text="DATA", foreground='#26dbba', bg='#2b383e')
        self.date.grid(row=4,column=0)
        self.dateEntry = tk.Entry(self, font=("Times", 12), foreground='#26dbba', bg='#2b383e')
        self.dateEntry.grid(row=4,column=1)
        self.exData = tk.Label(self, font=("Times", 10), text="Ex: 08/05/2020", foreground='black', bg='#2b383e')
        self.exData.grid(row=5,column=1)
        
        self.time = tk.Label(self, font=("Times", 12, 'bold'), text="HORÁRIO", foreground='#26dbba', bg='#2b383e')
        self.time.grid(row=6,column=0)
        self.timeEntry = tk.Entry(self, font=("Times", 12), foreground='#26dbba', bg='#2b383e')
        self.timeEntry.grid(row=6,column=1)
        self.exTime = tk.Label(self, font=("Times", 10), text="Ex: 17:00 / 09:30)", foreground='black', bg='#2b383e')
        self.exTime.grid(row=7,column=1)

        self.contractButton= tk.Button(self, font=("Times", 12, 'bold'), text="ENVIAR", foreground='#26dbba', bg='#2b383e', padx=46, command=self.backup)
        self.contractButton.grid(row=8, column=1)

        self.exitButton= tk.Button(self, font=("Times", 12, 'bold'), text="SAIR", foreground='#26dbba', bg='#2b383e', padx=58, command=self.exit)
        self.exitButton.grid(row=9, column=1)

    def backup(self):
        conexao = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='1407')
        cursor = conexao.cursor()
        cursor.execute(
            'INSERT INTO contratos VALUES (DEFAULT, %s, %s, %s, %s, %s)',
            (
                self.nameEntry.get(), 
                self.phoneEntry.get(), 
                self.localEntry.get(), 
                self.dateEntry.get(), 
                self.timeEntry.get()
                )
            )

        conexao.commit()
        cursor.close()
        conexao.close()
        messagebox.showinfo('ENVIADO', 'Seu formulario foi enviado, o acompanhante entrará em contato em breve.')
        
    def exit (self):
        exiApp = messagebox.askquestion("THE DATE", "TEM CERTEZA?")
        if exiApp == 'yes':
            sys.exit()
