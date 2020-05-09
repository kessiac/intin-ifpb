import sqlite3
from contextlib import closing

class Bd():
    def create_table(self):
        conexao = sqlite3.connect('Fornecer_Film.db')
        cursor = conexao.cursor()
        cursor.execute('CREATE TABLE Fornecer_Film(FILME TEXT, DIRETOR TEXT, SINOPSE TEXT, CATEGORIA TEXT)')
        print('Tabela/Banco Criado(a)')

    def create_table2(self):
        conexao = sqlite3.connect('Fornecer_Film.db')
        cursor = conexao.cursor()
        cursor.execute('CREATE TABLE Cinemark(SALA INTERGE, FILME TEXT, DATA TEXT, HORARIO TEXT)')
        print('Tabela/Banco Criado(a)')

    def create_table3(self):
        conexao = sqlite3.connect('Fornecer_Film.db')
        cursor = conexao.cursor()
        cursor.execute('CREATE TABLE LOGIN(USER TEXT, KEY TEXT)')
        print('Tabela/Banco Criado(a)')

class Loginn():
    def __init__(self):
        self.user = input('User desejado: ')
        self.key = input('Key desejada: ')
        conexao = sqlite3.connect('Fornecer_Film.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * from LOGIN')
        resultado = cursor.fetchall()
        if self.user not in resultado:
            cursor.execute('INSERT INTO LOGIN VALUES (?,?)', (self.user, self.key))
            print('Criado com Sucesso.')
        else:
            print('User indisponivel.\n3 - Tentar novamente\n6 - Menu Principal')
        conexao.commit()
        cursor.close()
        conexao.close()
        
if __name__=='__main__':
    bd = Bd()
    bd.create_table()
    bd.create_table2()
    bd.create_table3()

    loginn = Loginn()
