#nova função de cadastrar pessoas
def cadastrar_pessoa(self):
    nome = self.cxnome.get()
    cargo = self.cxcargo.get()
    cpf = self.cxcpf.get()
    email = self.cxemail.get()
    endereco = self.cxendereco.get()
    fazenda = 1
    login = self.cxlogin.get()
    senha = self.cxsenha.get()
    resposta = cadastrar(nome,cargo,cpf,email,endereco,fazenda,login,senha,self.checkbox_termos.get())
    if resposta==True and self.checkbox_termos.get() == True: 
        messagebox.showinfo("CADASTRO","Cadastrado com sucesso!!")
        self.login()    
    else:
        if self.checkbox_termos.get() == False:
            messagebox.showinfo("CADASTRO","Você deve aceitar os termos")
        else:   
            messagebox.showerror("CADASTRO",resposta)
#nova função de cadastrar em funcAPP.py
def cadastrar(nome, cargo, cpf, email, endereço, fazenda, login, senha,checkbox_termos):
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
    if int(fazenda) in ids_fazendas:
        if cpf not in cpfs:
            if login not in logins and checkbox_termos == True:
                # Caso ela esteja, o programa faz a formatação das informações a serem enviadas.
                aux = "DEFAULT, '" + nome + "', '" + cargo + "', '" + cpf + "', '" + email + \
                    "', '" + endereço + "', " + \
                    str(fazenda) + ", '" + login + "', '" + senha + "'"
                valores.append(aux)
                insert(valores, 'usuario')
                return True
            else:
                return "Username já cadastrado!"
        else:
            return "Usuário já cadastrado!"
    else:
        return "Fazenda  não cadastrada!"