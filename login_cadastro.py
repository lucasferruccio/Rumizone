from customtkinter import *
from PIL import Image
from MySQLdb import*
from crud import *
import os
from pathlib import Path
from funcApp import *

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
        self.fundo.grid(row=0,column=0)
        #botão para voltar para o menu
        self.btv = CTkButton(self.fundo,text="voltar",width=0, command= self.voltar)
        self.btv.place(x=1,y=0)
    def voltar(self):
        telamenu(tela)
class telaboi:
    def janela_vaca(self, info, telaJanela):
    #Atualiza os dados das vacas. OBS: Só atualiza se o usuario preencher todos as caixas
        def atualizar():
            atualizar_vaca(info[0], entry_manejo.get(), entry_comida.get(), entry_peso.get(),
                        entry_comp.get(), entry_vacinas.get(), entry_saude.get())

        self.telavaca = CTkToplevel()
        self.telavaca.title("vacas")
        self.telavaca.geometry("900x270")
        self.fundo = CTkFrame(self.telavaca)
        self.fundo.grid(row = 0, column = 0)

        #Primeira linha, informando oq é cada coluna

        self.col1 = CTkLabel(self.fundo,width=300, text= "Informação", height=30)
        self.col1.grid(row=0, column = 0)
        self.col2 = CTkLabel(self.fundo,width=300, text= "Atual", height=30)
        self.col2.grid(row=0, column = 1)
        self.col3 = CTkLabel(self.fundo,width=300, text= "Novos Valores", height=30)
        self.col3.grid(row=0, column = 2)

        #Exibe o codigo de identficação da vaca na tela

        self.cod = CTkLabel(self.fundo,width=300, text= "Código de Identificação:", height=30)
        self.cod.grid(row=1, column = 0)
        entry_cod = CTkLabel(self.fundo,width=300, text= info[0], height=30)
        entry_cod.grid(row=1, column = 1)

        #Exibe como se encontra o estado de manejo da vaca na tela

        self.manejo1 = CTkLabel(self.fundo,width=300, text= "Manejo:", height=30)
        self.manejo1.grid(row=2, column = 0)
        self.manejo2 = CTkLabel(self.fundo,width=300, text= info[2], height=30)
        self.manejo2.grid(row=2, column = 1)
        entry_manejo = CTkEntry(self.fundo, placeholder_text=info[2])
        entry_manejo.grid(row=2, column = 2)

        #Exibe a quantidade de comida consumida pela vaca diariamente na tela

        self.comida1 = CTkLabel(self.fundo,width=300, text= "Comida(kg):", height=30)
        self.comida1.grid(row=3, column = 0)
        self.comida2 = CTkLabel(self.fundo,width=300, text= info[3], height=30)
        self.comida2.grid(row=3, column = 1)
        entry_comida = CTkEntry(self.fundo, placeholder_text=str(info[3]))
        entry_comida.grid(row=3, column = 2)

        #Exibe o peso da vaca na tela

        self.peso1 = CTkLabel(self.fundo,width=300, text= "Peso(kg):", height=30)
        self.peso1.grid(row=4, column = 0)
        self.peso2 = CTkLabel(self.fundo,width=300, text= info[4], height=30)
        self.peso2.grid(row=4, column = 1)
        entry_peso = CTkEntry(self.fundo, placeholder_text=str(info[4]))
        entry_peso.grid(row=4, column = 2)

        #Exibe o estado de saúde da vaca na tela

        self.saude1= CTkLabel(self.fundo,width=300, text= "Saúde:", height=30)
        self.saude1.grid(row=5, column = 0)
        self.saude2 = CTkLabel(self.fundo,width=300, text= info[7], height=30)
        self.saude2.grid(row=5, column = 1)
        entry_saude = CTkEntry(self.fundo, placeholder_text=info[7])
        entry_saude.grid(row=5, column = 2)

        #Exibe o estado de comportamento da vaca na tela

        self.comp1 = CTkLabel(self.fundo,width=300, text= "Comportamento:", height=30)
        self.comp1.grid(row=6, column = 0)
        self.comp2 = CTkLabel(self.fundo,width=300, text= info[5], height=30)
        self.comp2.grid(row=6, column = 1)
        entry_comp = CTkEntry(self.fundo, placeholder_text=info[5])
        entry_comp.grid(row=6, column = 2)

        #Exibe o estado da vaca em relação as vacinas da vaca na tela

        self.vacinas1 = CTkLabel(self.fundo,width=300, text= "Vacina:", height=30)
        self.vacinas1.grid(row=7, column = 0)
        self.vacinas2 = CTkLabel(self.fundo,width=300, text= info[6], height=30)
        self.vacinas2.grid(row=7, column = 1)
        entry_vacinas = CTkEntry(self.fundo, placeholder_text=info[6])
        entry_vacinas.grid(row=7, column = 2)

        #Exibe o botão de atualizar informações da vaca na tela

        btn_atualizar = CTkButton(self.fundo,text=("Atualizar"), command=atualizar)
        btn_atualizar.grid(row=8, column = 1)

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
def __init__(self, telab):
    self.fundo = CTkFrame(telab, width=1200, height= 700, fg_color = marrom)
    self.fundo.grid(row=1,column=0)
    self.btv = CTkButton(self.fundo,text="voltar",width=0, command= self.voltar)
    self.btv.place(x=1,y=0)
    ids_vacas = [id[0] for id in select("id_vaca", "vacas")]
    aux2 = 1
    row = 2
    for aux1 in range(len(ids_vacas)):
        info  = botao_vaca(ids_vacas[aux1])
        info_completa = info_vaca(info[0])
        self.btvaca = CTkButton(self.fundo, text=("Identificação: " + str(info[0]) + "\n" + "Comportamento: " + info[1] + "\n" + "Saude: " + info[2]), width=200, command=lambda aux2 = info_completa: self.janela_vaca(aux2, tela))
        self.btvaca.place(x=(aux1 + 1)*210, y = row*20)
        if aux2 % 5 == 0:
            row += 1
        aux2 += 1
def voltar(self):
    telamenu(tela)
#predefinições padrão da janela         
tela = CTk()
tela.geometry("1200x700")
tela.title("Rumizone")
#imagens
path = os.path.dirname(__file__)
path_barras = path.replace('\\', '/')
pathFinal = path_barras + "/imagens"
caixa_conta = CTkImage(Image.open(pathFinal + "/caixa conta.png"), size=(200,200))
caixa_vaca = CTkImage(Image.open(pathFinal + "/caixa_boi.png"), size=(200,200))
caixa_monitoramento = CTkImage(Image.open(pathFinal + "/caixa monitoramento.png"), size=(200,200))
caixa_rendimento = CTkImage(Image.open(pathFinal + "/caixa_rendimento.png"), size=(200,200))
telalog(tela)
tela.mainloop()
