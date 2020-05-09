import sqlite3
from contextlib import closing

class Film():    
    def __init__(self):
        self.nome = input('Filme: ')
        self.diretor = input ('Diretor: ')
        self.sinopse = input('Sinopse: ')
        self.categoria = input('Categoria: ')

class ArmazenarFilm(Film):
    def add(self):
        conexao = sqlite3.connect('fornecer_film.db')
        cursor = conexao.cursor()
        cursor.execute('INSERT INTO Fornecer_Film VALUES (?, ?, ?, ?)', (self.nome, self.diretor, self.sinopse, self.categoria))
        print('='*28)
        print('Adicionado com sucesso.')
        conexao.commit()
        cursor.close()
        conexao.close()

class ExibirList():
    def visudd(self):
        conexao = sqlite3.connect('Fornecer_Film.db')
        cursor = conexao.cursor()
        cursor.execute(f'SELECT * from Fornecer_Film')
        resultado = cursor.fetchall()
        for dado in resultado:
            print('='*10)
            print(f'FILME: {dado[0]}')
            print('='*10)
            print(f'DIRETOR: {dado[1]}\n==========\nSINOPSE: {dado[2]}\n==========\nCATEGORIAS: {dado[3]}')
        cursor.close()
        conexao.close()

    def deletar(self):
        with sqlite3.connect('Fornecer_Film.db') as conexao:
            with closing (conexao.cursor()) as cursor:
                delt = input('Nome do Filme a ser deletado: ')
                cursor.execute(f'DELETE FROM Fornecer_Film WHERE FILME = "{delt}"')
                resultado = cursor.fetchall()
                if cursor.rowcount == 1:
                    conexao.commit()
                    print('='*28)
                    print('Deletado com sucesso.')
                    
                else:
                    print('Não encontrado.')

if __name__=='__main__':
    print('='*28)
    op = int(input('1 - Adicionar mais filmes ao banco.\n2 - Deletar Filme do Banco.\n3 - Todos os Filmes.\n0 - Sair.\n -> '))
    while op!=0:
        if op == 1:
            armazenar = ArmazenarFilm()
            armazenar.add()
            print('='*28)
            op = int(input('1 - Adicionar mais filmes ao banco.\n2 - Deletar Filme do Banco.\n3 - Todos os Filmes.\n0 - Sair.\n -> '))
            
        elif op == 2:
            exibir = ExibirList()
            exibir.deletar()
            print('='*28)
            op = int(input('1 - Adicionar filmes ao banco.\n2 - Deletar Filme do Banco.\n3 - Todos os Filmes\n0 - Sair.\n -> '))
        
        elif op == 3:
            exibir = ExibirList()
            exibir.visudd()
            print('='*28)
            op = int(input('1 - Adicionar filmes ao banco.\n2 - Todos os filmes novamente.\n0 - Sair.\n -> '))

