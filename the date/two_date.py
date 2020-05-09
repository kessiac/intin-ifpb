import tkinter as tkinter
from three_date import *
from two_adm import *
from tkinter import messagebox

class Two_date(tk.Frame):

	def __init__(self, master=None):
		tk.Frame.__init__(self, master=None, bg='#2b383e')

		self.create = tk.Button(self, font=("Times", 12, 'bold'), text="CONTRATAR", foreground='#26dbba', bg='#2b383e', padx=50, command=self.contract)
		self.create.pack(fill=tk.X)
		self.adm = tk.Button(self, font=("Times", 12, 'bold'), text="ADM", foreground='#26dbba', bg='#2b383e', padx=50, command=self.dataLogin)
		self.adm.pack(fill=tk.X)


	def contract(self):
		self.destroy()
		contract_form = Contract()
		contract_form.place(x=60, y=260)

	def dataLogin(self):
		self.create.destroy()
		self.adm.destroy()

		self.user = tk.Label(self, font=("Times", 12, 'bold'), text="USER", foreground='#26dbba', bg='#2b383e')
		self.user.grid(row=0, column=0, ipadx=25)
		self.userEntry = tk.Entry(self, font=("Times", 12), foreground='#26dbba', bg='#2b383e')
		self.userEntry.grid(row=1, column=0, ipadx=25)

		self.password = tk.Label(self, font=("Times", 12, 'bold'), text="PASSWORD", foreground='#26dbba', bg='#2b383e')
		self.password.grid(row=2, column=0, ipadx=25)
		self.passwordEntry = tk.Entry(self, font=("Times", 12), show='•', foreground='#26dbba', bg='#2b383e')
		self.passwordEntry.grid(row=3, column=0, ipadx=25)

		self.loginBD = tk.Button(self, font=("Times", 12, 'bold'), text="LOGIN", foreground='#26dbba', bg='#2b383e', padx=50, command=self.loginView)
		self.loginBD.grid(row=4, column=0, ipadx=25)

	def loginView(self):
		conexao = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='1407')
		cursor = conexao.cursor()
		cursor.execute("SELECT * FROM login")
		result = cursor.fetchall()
		for x in result:
			if self.userEntry.get() == x[0]:
				if self.passwordEntry.get() == x[1]:
					self.dataBD()
				else:
					messagebox.showinfo('INCORRETO', 'SENHA INVÁLIDA')
			else:
				messagebox.showinfo('INCORRETO', 'USUÁRIO NÃO CADASTRADO')

	def dataBD(self):
		self.destroy()
		self.screen = Service(self)
		self.screen.place(x=78, y=280)

	def changeScreen(self, screen):
		self.screen = screen
		self.screen.place(x=0, y=0)

