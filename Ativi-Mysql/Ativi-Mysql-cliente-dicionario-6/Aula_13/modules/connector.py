import mysql.connector

#classe com as conexoes no banco de dados utilizando a biblioteca mysql.connector
class InterfaceDB:
    usuario, senha, host, banco = "", "", "", ""
    
    def __init__(self, usuario, senha, host, banco):
        # """Construtor da classe interface_db

        # Args:
        #     usuario (string): usuario para conexao ao banco
        #     senha (string): senha para acesso ao banco
        #     host (string): string contendo o endereco do host
        #     banco (string): string contendo o nome do banco
        # """
        try:
            self.usuario = usuario
            self.senha = senha
            self.host = host
            self.banco = banco
        except Exception as e:
            print(str(e))

    #conexao com o banco de dados
    def conectar(self):
        try:
            con = mysql.connector.connect(user=self.usuario, password=self.senha, host=self.host, database=self.banco)
            cursor = con.cursor()
            return con, cursor
        except Exception as e:
            print(str(e))
    
    #desconexao do banco de dados
    def desconectar(self, con, cursor):
        try:
            cursor.close()
            con.commit()
            con.close()
        except Exception as e:
            print(str(e))
    
    #metodo para gerar a query
    def selecionar(self, query):
        try:
            con, cursor = self.conectar()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar(con, cursor)

    #metodo para executar a inclusao de dado
    def executar(self, query):
        try:
            con, cursor = self.conectar()
            result = cursor.execute(query)
            return result
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar(con, cursor)

#funcao para as informacoes necessarias para acesso ao banco de dados
def get_db_info():
    try:
        user = "root"
        password = "senha12345"
        host = "127.0.0.1"
        database = "provedor"
        return user, password, host, database
    except Exception as e:
        print(str(e))