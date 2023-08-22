from crud import *

# Função para formatação do dados recebido pela query do banco de dados


def formatacao_login(query):
    aux = []
    for i in query:
        aux.append(i[0])
    return aux

# Cadastro de usuário:


def cadastrar(nome, cargo, cpf, email, endereço, fazenda, login, senha):
    valores = []
    # Seleção dos dados a serem comparados(Dados únicos que não podem ser repetidos ou, no caso da fazenda que não exista):
    # ID_Fazenda
    query_fazenda = select('idfazenda', 'fazenda')
    ids_fazendas = formatacao_login(query_fazenda)
    # login
    query_login = select('login', 'usuario')
    logins = formatacao_login(query_login)
    # cpf
    query_cpf = select('cpf', 'usuario')
    cpfs = formatacao_login(query_cpf)
    # Checagem para ver se a fazenda em que o usuário está sendo cadastrado está disponível:
    if fazenda in ids_fazendas:
        if cpf not in cpfs:
            if login not in logins:
                # Caso ela esteja, o programa faz a formatação das informações a serem enviadas.
                aux = "DEFAULT, '" + nome + "', '" + cargo + "', '" + cpf + "', '" + email + \
                    "', '" + endereço + "', " + \
                    str(fazenda) + ", '" + login + "', '" + senha + "'"
                valores.append(aux)
                insert(valores, 'usuario')
                return "cadastrado"
            else:
                return "Username já cadastrado!"
        else:
            return "Usuário já cadastrado!"
    else:
        return "Fazenda  não cadastrada!"


# Lógica para login de usuário:

def logar(login, senha):
    query_login = select('login', 'usuario')
    logins = formatacao_login(query_login)
    # Checa se o login existe
    if login in logins:
        senha_banco = formatacao_login(
            select("senha", "usuario", "login=" + "'" + login + "'"))
        # Checa se a senha bate com o do banco de dados
        if senha in senha_banco:
            return True
        else:
            return "Senha Errada!"
    else:
        return "Login não cadastrado!"


# Função para formatação do dados recebido pela query do banco de dados

def formatacao_btn(query):
    aux = []
    aux.append(query[0])
    return aux

# Puxa e formata os valores para serem dispostos nos botões


def botao_vaca(id):
    valores = "id_vaca, comportamento, saude"
    query = select(valores, "vacas", "id_vaca = " + str(id))
    return (formatacao_btn(query)[0])

# Puxa as informações completas das vacas

def info_vaca(id,where = None):
    valores = "*"
    query = select(valores, "vacas", "id_vaca=" + str(id))
    return (formatacao_btn(query)[0])

# Atualiza as informações da vacas


def atualizar_vaca(id, manejo, comida, peso, comportamento, vacinas, saude):
    valores = {"manejo": manejo, "comida": str(comida), "peso": str(peso),
               "comportamento": comportamento, "vacinas": vacinas, "saude": saude}
    try:
        update(valores, "vacas", "id_vaca = " + str(id))
        return True
    except:
        return "Não foi possível executar a atualização!"

def deletar_vaca(id):
    try:
        delete("vacas", "id_vaca="+str(id))
        return True
    except:
        return "Falha no processo de exclusão"
    
def adicionar_vaca(infos):
    valores = "(" + "DEFAULT, 1, '" + "', '".join([str(aux) for aux in infos]) + "')"
    try:
        insert(valores, "vacas")
        return True
    except:
        return "Falha no processo de adição"
