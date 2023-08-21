from customtkinter import *
from tkinter import messagebox
from PIL import Image
from MySQLdb import*
from crud import *
import os
from pathlib import Path
from funcApp import *

verde_fundo = "#172526"
verde_botao = "#3d9079"
branco = "#FFFFFF"
preto = "#000000"
verde = "#20CD8D"

#Inicio da classe do aplicativo
class rumizone(CTk):

    #Função inical que abre o primeiro frame:

    def __init__(self, root):
        self.root = root
        #Titulo do app
        self.root.title("Rumizone")
        #Tamanho da tela
        self.root.geometry("1200x700")
        #Não permite mudança no tamanho da tela
        self.root.resizable(width=False, height=False)
        #Deixa o aplicativo no modo escuro(Muito mais bonito)
        set_appearance_mode("dark")
        #Abre a tela de login
        self.login()

    #Função que fecha os frames ao mudar de tela, sendo sempre necessário chama-lo quando se abre uma janela.

    def destruir_frames(self):
        for x in root.winfo_children():
            x.destroy()

    #Frame inicial

    def login(self):
        #Informações do Frame de Login
        self.frame_um = CTkFrame(master=self.root, width=1200, height=700, fg_color=verde_fundo)
        self.frame_um.pack()

        #Logo Rumizone
        custom_font_title = CTkFont(family="Roboto", size=40, weight="bold")
        self.rumizone_centro = CTkLabel(master=self.root, text="Rumizone", width=0, fg_color=verde_fundo, font=custom_font_title)
        self.rumizone_centro.place(x=500, y=40)

        #Texto de Login
        custom_font_label = CTkFont(family="Roboto", size=20, weight="bold")
        self.txtlogin = CTkLabel(master=self.root, text="Login", width=0, fg_color=verde_fundo, text_color=verde, font=custom_font_label)
        self.txtlogin.place(x=570, y=200)

        #Caixa de Login
        self.cxlogin = CTkEntry(master=self.root, width=300, height=30, fg_color=branco, text_color=preto)
        self.cxlogin.place(x=450, y=250)

        #texto da Senha
        custom_font = CTkFont(family="Roboto", size=20, weight="bold")
        self.txtsenha = CTkLabel(master=self.root, text="Senha", width=0, fg_color=verde_fundo, text_color=verde, font=custom_font)
        self.txtsenha.place(x=570, y=335)
        #Caixa da senha
        self.cxsenha = CTkEntry(master=self.root, width=300, height=30, fg_color=branco, text_color=preto, show="*")
        self.cxsenha.place(x=450, y=400)

        #botão de verificação
        self.btn_login = CTkButton(master=self.root,text="Entrar", width=100, height=40, fg_color =verde, command=self.verificar)
        self.btn_login.place(x=610, y=480)

        #botão de cadastro
        self.btn_login = CTkButton(master=self.root,text="Cadastrar", width=100, height=40, fg_color =verde, )
        self.btn_login.place(x=490, y=480)

    #Verifica se o usuário é cadastrado e se a senha é válida. Caso negado, um erro será impresso na tela

    def verificar(self):
        result_login = logar(self.cxlogin.get(), self.cxsenha.get())
        if result_login == True:
            self.menu()
        else:
            messagebox.showerror("Erro no login!", result_login)
            
    #Frame do menu de acesso a todos as funções do aplicativo

    def menu(self):
        #Fecha o frame passado
        self.destruir_frames()

        #Informações do Frame do menu
        self.menu = CTkFrame(master=self.root, width=1200, height=700, fg_color=verde_fundo)
        self.menu.pack()

        #Logo Rumizone
        custom_font_title = CTkFont(family="Roboto", size=40, weight="bold")
        self.rumizone_centro = CTkLabel(master=self.root, text="Rumizone", width=0, fg_color=verde_fundo, font=custom_font_title)
        self.rumizone_centro.place(x=480, y=40)

        #Botão para o Frame da Conta

        self.btconta = CTkButton(master=self.root, image=btn_conta,text="",fg_color=verde_fundo, width= 100,height= 70)
        self.btconta.place(x=300,y=100)

        #Botão para o Frame dos animais
        self.btboi = CTkButton(master=self.root, image=btn_animais,text="", fg_color=verde_fundo, width= 100,height= 70, command=self.btn_animais)
        self.btboi.place(x=650,y=100)
        self.btboi["font"] = ("Verdana", "15")

        #Botão para o Frame de Registros
        self.btmonitoramento = CTkButton(master=self.root, image=btn_monitoramento,text="", fg_color=verde_fundo, width= 100,height= 70)
        self.btmonitoramento.place(x=300,y=380)

        #Botão para o Frame de Análise Comportamental
        self.btrendimento = CTkButton(master=self.root, image=btn_registros,text="", fg_color=verde_fundo, width= 100,height= 70)
        self.btrendimento.place(x=650,y=380)

    #Animais:

    #Botão de acesso ao Frame de animais.
    def btn_animais(self):
        self.animais()

    def animais(self):
        #Fecha o frame passado
        self.destruir_frames()

        #Informações do Frame dos animais
        self.menu = CTkFrame(master=self.root, width=1200, height=700, fg_color=verde_fundo)
        self.menu.pack()

        #Coleta de alguns dados para a criação dos botões, para retirar a quantidade e os ids das vacas no DB
        
        ids_vacas = [id[0] for id in select("id_vaca", "vacas")]
        #Botão bonito:
        ''' 
        self.

        #Criação de botões iguais aos numéros de ids(único para cada animal)
        for contagem_vacas in range(len(ids_vacas)):
            #Coleta de dados básicos para a aparição no botão
            info_vaca_botao = botao_vaca(ids_vacas[contagem_vacas])
            #Coleta de todos os dados das vacas
            info_vaca_completa = info_vaca(info_vaca_botao[0])
            #Criação dos botões
            self.btn_vaca = CTkButton(master=self.root, text=("teste"), image=vaca_img, compound="top", width=200, height=200, fg_color=verde_botao)
            self.btn_vaca.grid() '''

#Carregamento das imagens:
path = os.path.dirname(__file__)
path_barras = path.replace('\\', '/')
pathFinal = path_barras + "/imagens"
btn_conta = CTkImage(Image.open(pathFinal + "/caixa conta.png"), size=(200,200))
btn_animais = CTkImage(Image.open(pathFinal + "/caixa_boi.png"), size=(200,200))
btn_monitoramento = CTkImage(Image.open(pathFinal + "/caixa monitoramento.png"), size=(200,200))
btn_registros = CTkImage(Image.open(pathFinal + "/caixa_rendimento.png"), size=(200,200))
vaca_img = CTkImage(Image.open(pathFinal + "/vaca.png"), size=(100,100))
    
        
#Iniciação do sistema, segundo Thiago é bom manter ele assim.

if __name__ == "__main__":
    root = CTk()
    app = rumizone(root)
    root.mainloop()
