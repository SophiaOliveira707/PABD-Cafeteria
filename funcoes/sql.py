import psycopg2
#conectar ao banco de dados
class Bd_cafe:
    def __init__(self):
        self.db_connection = psycopg2.connect(
            dbname='cafeteria',
            user="postgres",
            password="pabd",
            host='localhost',
            port=5432
        )
        #criando um cursor
        self.cursor = self.db_connection.cursor()
    #executar consulta
    def executar(self,comando):
        self.cursor.execute(comando)

    def pegar_valores(self):
        return self.cursor.fetchall()