import pymysql


class DataBase(object):
    def __init__(self):
        self.host = 'localhost'
        self.usuario = 'root'
        self.db = 'locafacil'
        self.password = 'lucas12'
        self.conexao = None
        self.cursor = None

    def connect(self):
        self.conexao = pymysql.connect(host=self.host, db=self.db, user=self.usuario, passwd=self.password)
        self.cursor = self.conexao.cursor(pymysql.cursors.DictCursor) # Os resultados vem em dicionario

    def disconnect(self):
        self.conexao.close()

    def select(self, fields, tables, where=None):
        query = "SELECT " + fields + " FROM " + tables

        if(where):
            query = query + " WHERE " + where

        self.cursor.execute(query)
        return self.cursor.fetchall() #pega todos os resultados da execução acima e retorna
        
    def insert_user(self, dic):
        self.cursor.execute ('INSERT INTO user( nome, cpf, telefone, email, sexo, usuario, senha ) VALUES (%s, %s, %s, %s, %s, %s, %s)',(  dic['nome'], dic['cpf'], dic['telefone'], dic['email'], dic['sexo'], dic['usuario'], dic['senha'] ))
        self.conexao.commit()
    
    def insert_rent(self, dic):
        self.cursor.execute ('INSERT INTO rent(descricao, bairro, situacao, rua, numero, complemento, cep, preco, qualidade, id_user ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (dicio['desc'], dicio['bairro'], dicio['sit'], dicio['rua'], dicio['numero'], dicio['complemento'], dicio['cep'], dicio['preco'], dicio['quality'], dicio['id_user']))
        self.conexao.commit()

    def update(self, dic, table, where=None): #dic vai ser um dicionário (field = value)
        query = "UPDATE " + table
        query = query + " SET " + ",".join([field + " = '" + value + "'" for field, value in dic.items()])
        
        if(where):
            query = query + " WHERE " + where

        print(query)
        self.cursor.execute(query)
        self.conexao.commit()

    def create_tables(self):
        sql = """ CREATE TABLE IF NOT EXISTS user(
        iduser integer AUTO_INCREMENT,
        nome text NOT NULL,
        cpf VARCHAR(11) NOT NULL,
        telefone VARCHAR(11) NOT NULL,
        email VARCHAR(45) NOT NULL,
        sexo VARCHAR(9) NOT NULL,
        usuario VARCHAR(20) NOT NULL,
        senha VARCHAR(32) NOT NULL,
        PRIMARY KEY (iduser, cpf) )"""
        self.cursor.execute(sql)

        sql = """ CREATE TABLE IF NOT EXISTS rent(
        idrent integer AUTO_INCREMENT,
        descricao VARCHAR(200) NULL,
        bairro VARCHAR(45) NOT NULL,
        situacao TINYINT NOT NULL,
        rua VARCHAR(45) NOT NULL,
        numero INT NOT NULL,
        complemento VARCHAR(45) NULL,
        cep VARCHAR(7) NOT NULL,
        preco FLOAT NOT NULL,
        qualidade FLOAT NOT NULL,
        id_user INT NOT NULL,
        PRIMARY KEY (idrent, id_user),
        CONSTRAINT id_user
            FOREIGN KEY (id_user)
            REFERENCES user(iduser)
            ON DELETE CASCADE
            ON UPDATE NO ACTION) """
        self.cursor.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS images(
        origem VARCHAR(200) NOT NULL,
        id_rent INT NOT NULL,
        PRIMARY KEY (id_rent),
        CONSTRAINT id_rent
            FOREIGN KEY (id_rent)
            REFERENCES rent (idrent)
            ON DELETE CASCADE
            ON UPDATE NO ACTION)"""
        self.cursor.execute(sql)




data = DataBase()
data.connect()


#--------- Deu certo ----------------
a = data.select("nome, cpf", "user", "iduser = 1")
print(a)
a = data.select("nome, cpf", "user")
print(a)
#-------------------------------------

dic = dict()

dic['nome'] = "Sousa"
dic['cpf'] = "12345678910"
dic['telefone'] = "89999329025"
dic['email'] = "lucas@gmail.com"
dic['sexo'] = "masculino"
dic['usuario'] = "lucas"
dic['senha'] = "lucasous"

#--------- Deu certo ----------------
# data.insert_user(dic)
#-------------------------------------


dicio= dict()
dicio['desc'] = "Pais Tropical"
dicio['bairro'] = "Junco"
dicio['sit'] = 1
dicio['rua'] = "Avenida Piauí"
dicio['numero'] = 338
dicio['complemento'] = "Em frente a Igreja São Francisco"
dicio['cep'] = "6460784"
dicio['preco'] = 500.00
dicio['quality'] = 5
dicio['id_user'] = 1

#--------- Deu certo ----------------
# data.insert_rent(dicio)
#-------------------------------------

data.update({'senha': '@naosei123'}, "user", "iduser = 1")

data.disconnect()