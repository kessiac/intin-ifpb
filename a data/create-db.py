import psycopg2
'''
#tabela login
conexao = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='1407')
cursor = conexao.cursor()
cursor.execute('CREATE TABLE login (username VARCHAR(15), key VARCHAR(15))')
cursor.execute("INSERT INTO login VALUES('carvalho', '1407')")
conexao.commit()
cursor.close()
conexao.close()
print('Concluido')
'''

#tabela contratos

conexao = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='1407')
cursor = conexao.cursor()
cursor.execute('CREATE TABLE contratos (id SERIAL, name VARCHAR(25), phone VARCHAR(15), local VARCHAR(25), date VARCHAR(10), time VARCHAR(15))')
conexao.commit()
cursor.close()
conexao.close()
print('Concluido')
