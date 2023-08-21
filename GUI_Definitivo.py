from customtkinter import *
from tkinter import messagebox
from PIL import Image
from MySQLdb import*
from crud import *
import os
from pathlib import Path
from funcApp import *

verde_fundo = "#172526"
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
        self.destruir_frames()

        #Informações do Frame do menu
        self.menu = CTkFrame(master=self.root, width=1200, height=700, fg_color=verde_fundo)
        self.menu.pack()

        #Logo Rumizone
        custom_font_title = CTkFont(family="Roboto", size=40, weight="bold")
        self.rumizone_centro = CTkLabel(master=self.root, text="Rumizone", width=0, fg_color=verde_fundo, font=custom_font_title)
        self.rumizone_centro.place(x=500, y=40)

        #Botão para o Frame da Conta

        self.btconta = CTkButton(master=self.root, image=caixa_conta,text="",fg_color=verde_fundo, width= 100,height= 70)
        self.btconta.place(x=300,y=100)

        #Botão para o Frame dos animais
        self.btboi = CTkButton(master=self.root, image=caixa_vaca,text="", fg_color=verde_fundo, width= 100,height= 70)
        self.btboi.place(x=650,y=100)
        self.btboi["font"] = ("Verdana", "15")

        #Botão para o Frame de Registros
        self.btmonitoramento = CTkButton(master=self.root, image=caixa_monitoramento,text="", fg_color=verde_fundo, width= 100,height= 70)
        self.btmonitoramento.place(x=300,y=380)

        #Botão para o Frame de Análise Comportamental
        self.btrendimento = CTkButton(master=self.root, image=caixa_rendimento,text="", fg_color=verde_fundo, width= 100,height= 70)
        self.btrendimento.place(x=650,y=380)


#Carregamento das imagens:
path = os.path.dirname(__file__)
path_barras = path.replace('\\', '/')
pathFinal = path_barras + "/imagens"
caixa_conta = CTkImage(Image.open(pathFinal + "/caixa conta.png"), size=(200,200))
caixa_vaca = CTkImage(Image.open(pathFinal + "/caixa_boi.png"), size=(200,200))
caixa_monitoramento = CTkImage(Image.open(pathFinal + "/caixa monitoramento.png"), size=(200,200))
caixa_rendimento = CTkImage(Image.open(pathFinal + "/caixa_rendimento.png"), size=(200,200))
    
        
#Iniciação do sistema, segundo Thiago é bom manter ele assim.

if __name__ == "__main__":
    root = CTk()
    app = rumizone(root)
    root.mainloop()
