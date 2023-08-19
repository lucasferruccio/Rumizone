from customtkinter import *
from PIL import *
from MySQLdb import*
from crud import *
from login_cadastro import*
marrom = "#172526"
branco = "#FFFFFF"
preto = "#000000"
verde = "#20CD8D"
#tela de login
class telalog:
    def __init__(self, telai):
        self.fundo = CTkFrame(master= telai, width=1200, height= 700,fg_color = marrom)
        self.fundo.grid(row= 1, column=0)
        #Texto "Rumizone"
        self.rumizone_centro = CTkLabel(self.fundo,text="Rumizone", width=0, fg_color =marrom)
        self.rumizone_centro.place(x=500, y=40)
        # Texto "Login" com fonte personalizada
        custom_font_label = CTkFont(family="Roboto", size=20, weight="bold")
        self.txtlogin = CTkLabel(self.fundo, text="Login", width=0, text_color=verde, font=custom_font_label)
        self.txtlogin.place(x=570, y=130)
        #caixa de login
        self.cxlogin = CTkEntry(self.fundo, width=300, height=30, fg_color=branco, text_color=preto)
        self.cxlogin.place(x=450, y=200)
        # Texto "Senha" com fonte personalizada
        custom_font = CTkFont(family="Roboto", size=20, weight="bold")
        self.txtsenha = CTkLabel(self.fundo, text="Senha", width=0, text_color=verde, font=custom_font)
        self.txtsenha.place(x=570, y=335)
        #caixa de senha
        self.cxsenha = CTkEntry(self.fundo, width=300, height=30, fg_color=branco, text_color=preto)
        self.cxsenha.place(x=450, y=400)
        #botão de verificação
        self.btlog = CTkButton(self.fundo,text="Entrar", width=100, height=40, fg_color =verde, command= self.verificar)
        self.btlog.place(x=550, y=480)
        #Texto "Rumizone" com fonte personalizada
        custom_font_title = CTkFont(family="Roboto", size=40, weight="bold")
        self.rumizone_centro = CTkLabel(self.fundo, text="Rumizone", width=0, fg_color=marrom, font=custom_font_title)
        self.rumizone_centro.place(x=500, y=40)
    #verificar as informações de login
    def verificar(self):
        if logar(self.cxlogin.get(), self.cxsenha.get()) == True:
            telamenu(tela)
        else:
            self.txterro = CTkLabel(tela,text="senha ou login errado", width=0, fg_color =branco, text_color= preto)
            self.txterro.place(x=600, y=500)
            print("senha ou login errado")
#tela de menu

class telamenu:
    def __init__(self, telam):
        self.fundo = CTkFrame(telam, width=1200, height= 700,fg_color = marrom)
        self.fundo.grid(row= 1, column=0)
        #botão tela conta
        self.btconta = CTkButton(self.fundo, image=caixa_conta,text="",fg_color =marrom, command=self.avancarconta,width= 100,height= 70)
        self.btconta.place(x=300,y=60)
        #botão tela animais
        self.btboi = CTkButton(self.fundo, image=caixa_vaca,text="", fg_color =marrom, command=self.avancaranimais,width= 100,height= 70)
        self.btboi.place(x=650,y=60)
        self.btboi["font"] = ("Verdana", "15")
        #botão tela monitoramento
        self.btmonitoramento = CTkButton(self.fundo, image=caixa_monitoramento,text="", fg_color =marrom, command=self.avancarmonitoramento,width= 100,height= 70)
        self.btmonitoramento.place(x=300,y=340)
        #botão tela rendimento
        self.btrendimento = CTkButton(self.fundo, image=caixa_rendimento,text="", fg_color =marrom, command=self.avancarrendimento,width= 100,height= 70)
        self.btrendimento.place(x=650,y=340)
    def avancarconta(self):
        telaconta(tela)
    def avancaranimais(self):
        telaboi(tela)
    def avancarmonitoramento(self):
        telamonitoramento(tela)
    def avancarrendimento(self):
        telaredimento(tela)

class telaconta:
    def __init__(self,telac):
        #fundo
        self.fundo= CTkFrame(telac,width=1200, height= 700,fg_color = marrom)
        self.fundo.grid(row=1,column=0)
        #botão para voltar para o menu
        self.btv = CTkButton(self.fundo,text="voltar",width=0, command= self.voltar)
        self.btv.place(x=1,y=0)
    def voltar(self):
        telamenu(tela)
class telaboi:
    def __init__(self,telab):
        self.fundo = CTkFrame(telab,width=1200, height= 700,fg_color = marrom)
        self.fundo.grid(row=1,column=0)
        self.btv = CTkButton(self.fundo,text="voltar",width=0, command= self.voltar)
        self.btv.place(x=1,y=0)
    def voltar(self):
        telamenu(tela)
class telamonitoramento:
    def __init__(self,telamoni):
        self.fundo = CTkFrame(telamoni,width=1200, height= 700,fg_color = marrom)
        self.fundo.grid(row=1,column=0)
        self.btv = CTkButton(self.fundo,text="voltar",width=0, command = self.voltar)
        self.btv.place(x=1,y=0)
    def voltar(self):
        telamenu(tela)
class telaredimento:
    def __init__(self,telar):
        self.fundo = CTkFrame(telar,width=1200, height= 700,fg_color = marrom)
        self.fundo.grid(row=1,column=0)
        self.btv = CTkButton(self.fundo,text="voltar",width=0, command= self.voltar)
        self.btv.place(x=1,y=0)
    def voltar(self):
        telamenu(tela)
#predefinições padrão da janela         
tela = CTk()
tela.geometry("1200x700")
tela.title("Rumizone")
#imagens
caixa_conta = CTkImage(Image.open("C:/Users/Salga/OneDrive/Documentos/Rumizone/imagens/caixa conta.png"), size=(200,200))
caixa_vaca = CTkImage(Image.open("C:/Users/Salga/OneDrive/Documentos/Rumizone/imagens/caixa_boi.png"), size=(200,200))
caixa_monitoramento = CTkImage(Image.open("C:/Users/Salga/OneDrive/Documentos/Rumizone/imagens/caixa monitoramento.png"), size=(200,200))
caixa_rendimento = CTkImage(Image.open("C:/Users/Salga/OneDrive/Documentos/Rumizone/imagens/caixa_rendimento.png"), size=(200,200))
telalog(tela)
tela.mainloop()
