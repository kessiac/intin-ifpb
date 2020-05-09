import requests
from bs4 import BeautifulSoup
from datetime import datetime

class GetInfoIFPB():

    #@staticmethod
    def get_editaisGeralCZ(self):
        page = requests.get('http://www.ifpb.edu.br/cajazeiras/editais')
        soup = BeautifulSoup(page.content, 'html.parser')
        content_core = soup.find_all(id="content-core")
        editais = []
        for content in content_core:
            edital = content.find_all('a')
            for c in edital:
                dic = {}
                link = c.get('href')
                if '/editais/' not in link:
                    continue
                nome_edital = c.get_text('href')
                dic[link] = nome_edital
                editais.append(dic)
            return editais

    def get_editaisDireçãoGeralCZ(self):
        page = requests.get('http://www.ifpb.edu.br/cajazeiras/editais/direcao-geral')
        soup = BeautifulSoup(page.content, 'html.parser')
        content_core = soup.find_all(id="content-core")
        editais = []
        for content in content_core:
            edital = content.find_all('a')
            for c in edital:
                dic = {}
                link = c.get('href')
                if '/editais/' not in link:
                    continue
                nome_edital = c.get_text('href')
                dic[link] = nome_edital
                editais.append(dic)
            return editais

    def get_editaisDireçãoGeralCZAno(self):
        page = requests.get('http://www.ifpb.edu.br/cajazeiras/editais/direcao-geral/{0}'.format(op))
        soup = BeautifulSoup(page.content, 'html.parser')
        content_core = soup.find_all(id="content-core")
        editais = []
        for content in content_core:
            edital = content.find_all('a')
            for c in edital:
                dic = {}
                link = c.get('href')
                if '/editais/' not in link:
                    continue
                nome_edital = c.get_text('href')
                dic[link] = nome_edital
                editais.append(dic)
            return editais

    def get_ediatisPesquisa(self):
        page = requests.get('http://www.ifpb.edu.br/cajazeiras/editais/pesquisa')
        soup = BeautifulSoup(page.content, 'html.parser')
        content_core = soup.find_all(id="content-core")
        editais = []
        for content in content_core:
            edital = content.find_all('a')
            for c in edital:
                dic = {}
                link = c.get('href')
                if '/editais/' not in link:
                    continue
                nome_edital = c.get_text('href')
                dic[link] = nome_edital
                editais.append(dic)
            return editais

    def get_ediatisPesquisaAno(self):
        page = requests.get('http://www.ifpb.edu.br/cajazeiras/editais/pesquisa/{0}'.format(op))
        soup = BeautifulSoup(page.content, 'html.parser')
        content_core = soup.find_all(id="content-core")
        editais = []
        for content in content_core:
            edital = content.find_all('a')
            for c in edital:
                dic = {}
                link = c.get('href')
                if '/editais/' not in link:
                    continue
                nome_edital = c.get_text('href')
                dic[link] = nome_edital
                editais.append(dic)
            return editais

if __name__ == '__main__':
    ifcz = GetInfoIFPB()
    editais = ifcz.get_editaisGeralCZ()
    for pos, edital in enumerate(editais):
        for i in editais[pos]:
            print('-' * 77)
            print(f'{i}:\n {editais[pos][i]}')
    print('-' * 77)
    op = int(input('(0) - Sair\n(1) - Direção Geral:\n(2) - Editais de Ensino\n(3) - Editais de Pesquisa e de Extensão\n'))
    while op != 0:
        if op == 1:
            ifcz = GetInfoIFPB()
            editais = ifcz.get_editaisDireçãoGeralCZ()
            for pos, edital in enumerate(editais):
                for i in editais[pos]:
                    print('-' * 77)
                    print(f'{i}:\n {editais[pos][i]}')
            print('-' * 77)
            op = int(input('Digite o ano desejado: '))

            while op != 0:
                if op == 2016:
                    print('-' * 77)
                    print("Esse ano não contém editais publicados.")

                elif op > 2015 and op <= datetime.now().year:
                    ifcz = GetInfoIFPB()
                    editais = ifcz.get_editaisDireçãoGeralCZAno()
                    for pos, edital in enumerate(editais):
                        for i in editais[pos]:
                            print('-' * 77)
                            print(f'{i}:\n {editais[pos][i]}')

                else:

                    print('-' * 77)
                    print("Esse ano não contém editais publicados.")
                print('-' * 77)
                op = int(input('(0) para Sair ou\nDigite outro ano: '))

        elif op == 2:
            ifcz = GetInfoIFPB()
            editais = ifcz.get_ediatisPesquisa()
            for pos, edital in enumerate(editais):
                for i in editais[pos]:
                    print('-' * 77)
                    print(f'{i}:\n {editais[pos][i]}')
            print('-' * 77)
            op = int(input('Digite o ano desejado: '))

            while op != 0:
                if op > 2015 and op <= datetime.now().year:
                    ifcz = GetInfoIFPB()
                    editais = ifcz.get_ediatisPesquisaAno()
                    for pos, edital in enumerate(editais):
                        for i in editais[pos]:
                            print('-' * 77)
                            print(f'{i}:\n {editais[pos][i]}')

                else:
                    print('-' * 77)
                    print("Esse ano não contém editais publicados.")

                print('-' * 77)
                op = int(input('(0) para Sair ou\nDigite outro ano: '))

        elif op == 3:
            print('-' * 77)
            print("Esse ano não contém editais publicados.")

        print('-' * 77)
        op = int(input('(0) - Sair\n(1) - Direção Geral:\n(2) - Editais de Ensino\n(3) - Editais de Pesquisa e de Extensão\n'))
