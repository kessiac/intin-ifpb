import sqlite3
from contextlib import closing

class Filme():
    def __init__(self):
        self.sala = int(input('Sala: '))
        self.filme = input('Filme: ')
        self.data = input('Data: ')
        self.horario = input('Horario: ')

class Armazem(Filme):
    def arm_filme(self):
        conexao = sqlite3.connect('fornecer_film.db')
        cursor = conexao.cursor()
        cursor.execute('INSERT INTO Cinemark VALUES (?, ?, ?, ?)', (self.sala, self.filme, self.data, self.horario))
        print('='*23)
        print('Adicionado com sucesso.')
        conexao.commit()
        cursor.close()
        conexao.close()

class ExPes():
    def pesquisarFilm(self):
        with sqlite3.connect('Fornecer_Film.db') as conexao:
            with closing (conexao.cursor()) as cursor:
                print('='*15)
                self.pesf = input('FILME: ')
                cursor.execute(f'SELECT * FROM Fornecer_Film WHERE Filme = "{self.pesf}"')
                resultado = cursor.fetchall()
                for dado in resultado:
                    if dado[0] == self.pesf:
                        print('='*15)
                        print(f'FILME: {dado[0]}\nDIRETOR: {dado[1]}\nSINOPSE: {dado[2]}\nCATEGORIA: {dado[3]}')

                    else:
                        print('='*15)
                        print('Não encontrado.')

                cursor.execute(f'SELECT * FROM Cinemark WHERE FILME = "{self.pesf}"')
                resultado = cursor.fetchall()
                for dado in resultado:
                    if dado[1] == self.pesf:
                        print('='*15)
                        print(f'SALA: {dado[0]}\nDATA: {dado[2]}\nHORARIO: {dado[3]}')

                    else:
                        print('='*15)
                        print('Não encontrado.')

    def visul(self):
        conexao = sqlite3.connect('Fornecer_Film.db')
        cursor = conexao.cursor()
        cursor.execute(f'SELECT * from Cinemark')
        resultado = cursor.fetchall()
        for dado in resultado:
            print('='*15)
            print(f'FILME: {dado[0]}')
            print('='*15)
            print(f'DIRETOR: {dado[1]}\nSINOPSE: {dado[2]}\nCATEGORIA: {dado[3]}')
        conexao.commit()
        cursor.close()
        conexao.close()

    def deletar(self):
        with sqlite3.connect('Fornecer_Film.db') as conexao:
            with closing (conexao.cursor()) as cursor:
                delt = input('Filme: ')
                cursor.execute(f'DELETE FROM Cinemark WHERE FILME = "{delt}"')
                resultado = cursor.fetchall()
                if cursor.rowcount == 1:
                    conexao.commit()
                    print('Deletado com sucesso.')
                    
                else:
                    print('Não encontrado.')  

class Login():
    def __init__(self):
        print('='*10)
        self.user = input('User: ')
        print('='*10)
        self.key = input('Key: ')
        conexao = sqlite3.connect('Fornecer_Film.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * from LOGIN')
        resultado = cursor.fetchall()
        for dado in resultado:
            if dado[0] == self.user and dado[1] == self.key:
                print('='*27)
                print("Login efetuado com sucesso.")
            
            else:
                print('='*15)
                print('Login inválido!')
                    
            cursor.close()
            conexao.close()

if __name__ == '__main__':
    print('='*3)
    op = int(input('1 - Filmes do mês.\n2 - Pesquisar Filme.\n3 - Login ADM\n0 - Sair\n -> '))
    while op!=0:
        if op == 1:
            expes = ExPes()
            expes.visul()
            print('='*3)
            op = int(input('2 - Pesquisar Filme.\n6 - Menu Principal.\n -> '))

        elif op == 2:
            expes = ExPes()
            expes.pesquisarFilm()
            print('='*3)
            op = int(input('6 - Menu Principal.\n -> '))

        elif op == 3:
            login = Login()
            print('='*27)
            op = int(input('4 - Adicionar Filme\n5 - Deletar Informações sobre Filme.\n6 - Logout\n -> '))

        elif op == 4:
            armazem = Armazem()
            armazem.arm_filme()
            print('='*23)
            op = int(input('4 - Adicionar mais.\n7 - Voltar.\n -> '))

        elif op == 5:
            expes = ExPes()
            expes.deletar()
            op = int(input('5 - Deletar mais.\n7 - Voltar.\n -> '))

        elif op == 6:
            op = int(input('1 - Filmes do mês.\n2 - Pesquisar Filme.\n3 - Login ADM\n0 - Sair\n -> '))

        elif op == 7:
            op = int(input('4 - Adicionar Filme\n5 - Deletar Filme.\n6 - Logout\n -> '))
