from customtkinter import *
from PIL import *
from MySQLdb import*
from crud import *
from login_cadastro import*
marrom = "#5C4033"
branco = "#FFFFFF"
preto = "#000000"
#tela de login
class telalog:
    def __init__(self, telai):
        self.fundo = CTkFrame(master= telai, width=1200, height= 700,fg_color = marrom)
        self.fundo.grid(row= 1, column=0)
        #Texto "Rumizone"
        self.rumizone_centro = CTkLabel(self.fundo,text="Rumizone", width=0, fg_color =marrom)
        self.rumizone_centro.place(x=455, y=50)
        self.rumizone_centro["font"] = ("Verdana", "34")
        #textologin
        self.txtlogin = CTkLabel(self.fundo,text="login", width=0, fg_color =marrom)
        self.txtlogin.place(x=440, y=125)
        self.txtlogin["font"] = ("Verdana", "30")
        #caixa de login
        self.cxlogin = CTkEntry(self.fundo, width=300, height=30)
        self.cxlogin.place(x=313, y=200)
        self.cxlogin["font"] = ("Verdana", "50")
        #textosenha
        self.txtsenha = CTkLabel(self.fundo,text="senha", width=0, fg_color =marrom)
        self.txtsenha.place(x=440, y=325)
        self.txtsenha["font"] = ("Verdana", "30")
        #caixa de senha
        self.cxsenha = CTkEntry(self.fundo, width=300, height=30)
        self.cxsenha.place(x=313, y=400)
        self.cxsenha["font"] = ("Verdana", "15")
        #botão de verificação
        self.btlog = CTkButton(self.fundo,text="fazer login", width=0, height= 1, command= self.verificar)
        self.btlog.place(x=440, y=500)
        self.btlog["font"] = ("Verdana", "15")
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
caixa_conta = CTkImage(Image.open("d:/pedro/Programação/Python/Imagens/caixa conta.png"), size=(200,200))
caixa_vaca = CTkImage(Image.open("d:/pedro/Programação/Python/Imagens/caixa_boi.png"), size=(200,200))
caixa_monitoramento = CTkImage(Image.open("d:/pedro/Programação/Python/Imagens/caixa monitoramento.png"), size=(200,200))
caixa_rendimento = CTkImage(Image.open("d:/pedro/Programação/Python/Imagens/caixa monitoramento.png"), size=(200,200))
telalog(tela)
tela.mainloop()
