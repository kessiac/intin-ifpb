import psycopg2
import tkinter as tk
import sys
from tkinter import messagebox

class ViewBD(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master=None, bg='#2b383e', width=390, height=562)

        self.img = tk.PhotoImage(file="the date.png")
        self.img = self.img.subsample(4, 4)

        self.background = tk.Label(self, image=self.img, bd=0)
        self.background.place(x=0, y=0)
        self.background.image = self.img
        
        self.scrollbar = tk.Scrollbar()
        self.scrollbar.place(x=353, y=26, relheight=0.85)

        self.textbox = tk.Text(font=("Times", 12), foreground='#26dbba', bg='#2b383e')
        self.textbox.place(x=25, y=26, width=328, height=478)

        conexao = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='1407')
        cursor = conexao.cursor()
        cursor.execute('SELECT * from contratos')
        self.resultado = cursor.fetchall()
        for i in self.resultado:
            self.textbox.insert(tk.INSERT, (f'CODIGO: {i[0]}\nNOME: {i[1]}\nCONTATO: {i[2]}\nLOCAL: {i[3]}\nDATA: {i[4]}\nHORÁRIO: {i[5]}.\n====================================\n'))
        self.textbox.config(state="disabled")
        self.textbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.textbox.yview)

        self.backButton= tk.Button(self, font=("Times", 12, 'bold'), text="CONCLUIR", foreground='#26dbba', bg='#2b383e', padx=50, command=self.serviceDelete2)
        self.backButton.place(x=25, y=502, relwidth=0.888)
     
    def serviceDelete2(self):
        self.backButton.destroy()
        self.textbox.destroy()
        self.scrollbar.destroy()
                
        self.codClient2 = tk.Label(self, font=("Times", 12, 'bold'), text="CÓDIGO DO CLIENTE", foreground='#26dbba', bg='#2b383e')
        self.codClient2.place(x=115, y=260)
        self.codEntry2 = tk.Entry(self, font=("Times", 12, 'bold'), foreground='#26dbba', bg='#2b383e')
        self.codEntry2.place(x=118, y=284)

        self.btDelete2 = tk.Button(self, font=("Times", 12, 'bold'), text="CONCLUIR", foreground='#26dbba', bg='#2b383e', padx=35, command=self.deleteCod2)
        self.btDelete2.place(x=117, y=306)

        self.exitBt = tk.Button(self, font=("Times", 12, 'bold'), text="SAIR", foreground='#26dbba', bg='#2b383e', padx=58, command=self.exit)
        self.exitBt.place(x=117, y=339)

    def deleteCod2(self):

        conexao = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='1407')
        cursor = conexao.cursor()
        cursor.execute(f'DELETE FROM contratos WHERE id = ({self.codEntry2.get()})')
        conexao.commit()
        conexao.close()
        messagebox.showinfo('CONCLUIDO', 'Parabéns, um contrato concluido.')

    def exit (self):
        exiApp = messagebox.askquestion("THE DATE", "TEM CERTEZA?")
        if exiApp == 'yes':
            sys.exit()
