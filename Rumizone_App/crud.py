import MySQLdb

host = "localhost"
user = "teste"
password = "123456"
db = "rumizonedb"
port = 3306

# conexao e a criacao do cursor.
con = MySQLdb.connect(host, user, password, db)
c = con.cursor()

# Insert INSERT INTO tabela (campo1,...,campon) VALUES (...),(valor1,...,valorn),(...)...


def insert(valores, tabela, campo=None):
    global c, con
    query = "INSERT INTO " + tabela
    if (campo):
        query = query + " (" + campo + ") "
    query = query + " VALUES " + str(valores)
    print(query)
    c.execute(query)
    con.commit()


# SELECT (SELECT valor1,...,valorn FROM tabela WHERE valorx = valory)


def select(valores, tabela, local=None):
    global c
    query = "SELECT " + valores + " FROM " + tabela
    if (local):
        query = query + " WHERE " + local
    c.execute(query)
    return c.fetchall()


# UPDATE tabela SET campo1 = valor1, campo2 = valor2, ..., campon = valorn WHERE campox=valorx


def update(valores, tabela, local=None):
    global c, con
    # valores vem como um dicionario temos que tratar e deixar no formato: campox = valory
    query = "UPDATE " + tabela + " SET " + ",".join([campo + " = '" + valor + "'" for campo,valor in valores.items()])
    if (local):
        query = query + " WHERE " + local
    print(query)
    c.execute(query)
    con.commit()

#DELETE FROM tabela WHERE campox=valory

def delete(tabela, local):
    global c, con
    query = "DELETE FROM " + tabela + " WHERE " + local
    c.execute(query)
    con.commit()



