from crud import *

# Função para formatação do dados recebido pela query do banco de dados

def formatacao(query):
    aux = []
    for i in query:
        aux.append(i[0])
    return aux

#Cadastro de usuário:

def cadastrar(nome, cargo, cpf, email, endereço, fazenda, login, senha):
    valores = []
    # Seleção dos dados a serem comparados(Dados únicos que não podem ser repetidos ou, no caso da fazenda que não exista):
    # ID_Fazenda
    query_fazenda = select('idfazenda', 'fazenda')
    ids_fazendas = formatacao(query_fazenda)
    # login
    query_login = select('login', 'usuario')
    logins = formatacao(query_login)
    # cpf
    query_cpf = select('cpf', 'usuario')
    cpfs = formatacao(query_cpf)
    #Checagem para ver se a fazenda em que o usuário está sendo cadastrado está disponível:
    if fazenda in ids_fazendas:
        if cpf not in cpfs:
            if login not in logins:
                # Caso ela esteja, o programa faz a formatação das informações a serem enviadas.
                aux  = "DEFAULT, '"+ nome + "', '" + cargo + "', '" + cpf + "', '" + email + "', '" + endereço + "', " + str(fazenda) + ", '" + login + "', '" + senha + "'"
                valores.append(aux)
                insert(valores, 'usuario')
            else:
                print("Username já cadastrado!")
        else:
            print("Usuário já cadastrado!")
    else:
        print("Fazenda  não cadastrada!")


# Lógica para login de usuário:

def logar(login, senha):
    query_login = select('login', 'usuario')
    logins = formatacao(query_login)
    #Checa se o login existe
    if login in logins:
        senha_banco = formatacao(select("senha", "usuario", "login=" + "'" + login + "'"))
        # Checa se a senha bate com o do banco de dados
        if senha in senha_banco:
            print("Logado!")
        else:
            print("Senha Errada!")
    else:
        print("username não cadastrado!")


login = "lucasferruccio14"
senha = "123456"

try:
    logar(login, senha)
except:
    print("Não foi possível")