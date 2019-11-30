

from cassandra.cluster import Cluster, PlainTextAuthProvider
from config import BASE_DIR, CASSANDRA_HOST, CASSANDRA_PORT, CASSANDRA_USER, CASSANDRA_PASS


class Cassandra:
    def connect(keyspace):
        try:
            cluster = Cluster(
                cloud={
                    'secure_connect_bundle': 'secure-connect-atividade6.zip'
                },
                auth_provider=PlainTextAuthProvider(CASSANDRA_USER, CASSANDRA_PASS)
            )
            return cluster.connect()
            
        except Exception as e:
            # @todo tratamento de erros, error handler
            raise e


class Notas:
    def __init__(self):
        self.keyspace = 'ativ6'
        self.tabela = 'nfiscais'
        self.db = Cassandra.connect(self.keyspace)
        self.db.set_keyspace(self.keyspace)

    def get_itens_da_nota(self, id_nota):
        cql = """SELECT * 
                   FROM {}
                  WHERE codigonota = '{}'
                  ALLOW FILTERING;""".format(self.tabela, id_nota)
        try:
            return self.db.execute(cql)
        except Exception as e:
            # @todo
            raise e
    


if __name__ == "__main__":
    n = Notas();
    for nota in n.get_itens_da_nota(1918):
        print('Cod: {}, Nome Cliente: {}'.format(nota.codigonota, nota.clientnome))

