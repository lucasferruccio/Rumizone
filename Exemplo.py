from tkinter import *
from GUI_Menu import *
from login_cadastro import *

#Criação de Controles:
class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 10
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 10
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 10
        self.quartoContainer.pack()

        self.titulo =Label(self.primeiroContainer, text="Rumizone:")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    #Puxa de outro arquivo .py a confirmação se o usuario já é cadastrado ou não.

    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        confirmacao = logar(usuario, senha)
        if confirmacao == "Logado!":
            print("Opa logado")
        else:
            print(confirmacao)

    def cadastro(self):
        nome = self.nome.get()
        cargo = self.cargo.get()
        cpf = self.cpf.get() 
        email = self.email.get()
        endereço = self.endereço.get()
        fazenda = self.fazenda.get()
        login = self.login.get()
        senha = self.senha.get()
        confirmacao = cadastrar(nome, cargo, cpf, email, endereço, fazenda, login, senha)
        if confirmacao == "cadastrado":
            print("Cadastrado")
        else:
            print(confirmacao)

#Permite a utilização de Widgets
root = Tk()

#Construtor do método da Classe
Application(root)

#Exive a tela
root.mainloop()
