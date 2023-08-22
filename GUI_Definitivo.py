from customtkinter import *
from tkinter import messagebox
from PIL import Image
from MySQLdb import*
from crud import *
import os
from pathlib import Path
from funcApp import *

verde_fundo = "#172526"
verde_botao = "#47a98e"
verde_botao_fundo = "#2e6d5c"
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
        self.frame_login = CTkFrame(master=self.root, width=1200, height=700, fg_color=verde_fundo)
        self.frame_login.pack()

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
            global id_usuario 
            id_usuario = puxar_id(self.cxlogin.get())
            self.menu()
        else:
            messagebox.showerror("Erro no login!", result_login)
            
    #Frame do menu de acesso a todos as funções do aplicativo

    def menu(self):
        #Fecha o frame passado
        self.destruir_frames()

        #Informações do Frame do menu
        self.frame_menu = CTkFrame(master=self.root, width=1200, height=700, fg_color=verde_fundo)
        self.frame_menu.pack()

        #Logo Rumizone
        custom_font_title = CTkFont(family="Roboto", size=40, weight="bold")
        self.rumizone_centro = CTkLabel(master=self.root, text="Rumizone", width=0, fg_color=verde_fundo, font=custom_font_title)
        self.rumizone_centro.place(x=480, y=40)

        #Botão para o Frame da Conta

        self.btconta = CTkButton(master=self.root, image=btn_conta,text="",fg_color=verde_fundo, width= 100,height= 70, command=self.menu_conta)
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

#Conta:
    def menu_conta(self):
        #Fecha o frame passado
        self.destruir_frames()

        #Informações do Frame do menu_conta
        self.menu_conta_Frame = CTkFrame(master=self.root, width=1200, height=700, fg_color=verde_fundo)
        self.menu_conta_Frame.grid(row=0,column=0)

        #Informações da conta
        
        informacoes = info_conta(id_usuario[0])
        quantidade_animais = info_quantidade_animais(informacoes[3])

        #frame no meio da tela

        custom_font_label = CTkFont(family="Roboto", size=20, weight="bold")
        self.frame_info_conta = CTkFrame(master=self.menu_conta_Frame, width=470, height=600, fg_color=verde, border_width=2, border_color=verde)
        self.frame_info_conta.place(x=370, y= 50)
        self.texto_nome = CTkLabel(master=self.frame_info_conta, text="Nome: " + informacoes[0],font=custom_font_label)
        self.texto_nome.place(x=20,y=50)
        self.texto_login = CTkLabel(master=self.frame_info_conta, text="Login: " + informacoes[1],font=custom_font_label)
        self.texto_login.place(x=20,y=110)
        self.texto_cargo = CTkLabel(master=self.frame_info_conta, text="Cargo: " + informacoes [2],font=custom_font_label)
        self.texto_cargo.place(x=20,y=170)
        self.texto_fazenda = CTkLabel(master=self.frame_info_conta, text="Quant. animais: " + str(len(quantidade_animais)),font=custom_font_label)
        self.texto_fazenda.place(x=20,y=230)
        

        


        #botão para voltar para o menu
        self.btn_voltar_menu = CTkButton(master=self.root, text="Voltar", fg_color="#123529", width= 75,height= 25, command=self.voltar_menu)
        self.btn_voltar_menu.place(x=10,y=10)


    #Animais:

    #Botão de acesso ao Frame de animais.
    def btn_animais(self):
        self.animais()

    def animais(self):
        #Fecha o frame passado
        self.destruir_frames()

        #Informações do Frame dos animais
        self.animais_Frame = CTkFrame(master=self.root, width=1200, height=700, fg_color=verde_fundo)
        self.animais_Frame.grid(row=0,column=0)

        #Coleta de alguns dados para a criação dos botões, para retirar a quantidade e os ids das vacas no DB
        
        ids_vacas = [id[0] for id in select("id_vaca", "vacas")]

        #Criação de botões iguais aos numéros de ids(único para cada animal)
        aux = 0 #Conta o número de botões por linha
        aux_x = 0 #Ajuda a organizar o valor de x do botão
        aux_y = 1 #Ajuda a organizar o valor de y do botão
        for contagem_vacas in range(len(ids_vacas)):
            if (contagem_vacas % 4) == 0 and contagem_vacas != 0:
                aux_x = 0
                aux_y+=10
            #Coleta de dados básicos para a aparição no botão
            info_vaca_botao = botao_vaca(ids_vacas[contagem_vacas])
            #Coleta de todos os dados das vacas
            info_vaca_completa = info_vaca(info_vaca_botao[0])
            #Criação dos botões
            self.btn_vaca = CTkButton(master=self.animais_Frame, text=("Cód: " + str(info_vaca_botao[0]) + "\n" + "Comportamento: " + info_vaca_botao[1] + "\n" + "Status de Saúde: " + info_vaca_botao[2]),
                                       image=vaca_img, compound="top", width=200, height=180, 
                                      fg_color=verde_botao,border_width= 3, border_color=verde_botao_fundo,
                                      command=lambda info_vaca = info_vaca_completa: self.informacoes_vacas(info_vaca))
            self.btn_vaca.place(x=(aux_x + 1)*215, y=(aux_y*20))
            aux_x+=1
            aux+=1

        #Botão para voltar ao menu
        self.btn_voltar_menu = CTkButton(master=self.root, text="Voltar", fg_color="#123529", width= 75,height= 25, command=self.voltar_menu)
        self.btn_voltar_menu.place(x=10,y=10)

        #Botão voltar para a lista de animais

        self.btn_cadastrar_animal = CTkButton(master=self.root, text="Adicionar", fg_color="#123529", width= 75,height= 25, 
                                              command=self.cadastro_animal)
        self.btn_cadastrar_animal.place(x=1115,y=10)

    #Função que chama o frame do menu
    def voltar_menu(self):
        self.menu()

    #Vai mostrar todas as informações sobre a vaca escolhida

    def informacoes_vacas(self, info):
        #Fecha o frame passado
        self.destruir_frames()

        #Informações do frame de vaca selecionada
        self.frame_info_vaca = CTkFrame(master=self.root, width=1200, height=700, fg_color=verde_fundo)
        self.frame_info_vaca.pack()

        self.frame_info = CTkFrame(master=self.frame_info_vaca, width=600, height=600, fg_color=verde_botao_fundo, border_width=2, border_color=verde_botao_fundo)
        self.frame_info.place(x=300, y= 50)
        custom_font_label = CTkFont(family="Roboto", size=15, weight="bold")

        #Informações da vaca

        #Informações colunas

        self.info_1 = CTkLabel(master=self.frame_info,width=300, text= "Informação", height=50, font=custom_font_label, fg_color="#1B4D3B")
        self.info_1.place(x=0,y=0)
        self.info_2 = CTkLabel(master=self.frame_info,width=300, text= "Atual", height=50, font=custom_font_label, fg_color="#1B4D3B")
        self.info_2.place(x=300,y=0)

        #Codigo identificação vaca

        self.cod_identificacao_1 = CTkLabel(master=self.frame_info,width=300, text= "Código de Identificação:", height=50, font=custom_font_label)
        self.cod_identificacao_1.place(x=0,y=50)
        self.cod_identificacao_2 = CTkLabel(master=self.frame_info,width=300, text= info[0], height=50, font=custom_font_label, text_color="#A9A9A9")
        self.cod_identificacao_2.place(x=300,y=50)

        #Manejo

        self.manejo_1 = CTkLabel(master=self.frame_info,width=300, text= "Manejo:", height=50, font=custom_font_label)
        self.manejo_1.place(x=0,y=100)
        self.manejo_2 = CTkLabel(master=self.frame_info,width=300, text= info[2], height=50, font=custom_font_label, text_color="#A9A9A9")
        self.manejo_2.place(x=300,y=100)

        #Quantidade de Comida

        self.comida_1 = CTkLabel(master=self.frame_info,width=300, text= "Comida(kg):", height=50, font=custom_font_label)
        self.comida_1.place(x=0,y=150)
        self.comida_2 = CTkLabel(master=self.frame_info,width=300, text= info[3], height=50, font=custom_font_label, text_color="#A9A9A9")
        self.comida_2.place(x=300,y=150)

        #O peso da vaca

        self.peso_1 = CTkLabel(master=self.frame_info,width=300, text= "Peso(kg):", height=50, font=custom_font_label)
        self.peso_1.place(x=0,y=200)
        self.peso_2 = CTkLabel(master=self.frame_info,width=300, text= info[4], height=50, font=custom_font_label, text_color="#A9A9A9")
        self.peso_2.place(x=300,y=200)

        #Estado de saude da vaca

        self.saude_1= CTkLabel(master=self.frame_info,width=300, text= "Saúde:", height=50, font=custom_font_label)
        self.saude_1.place(x=0,y=250)
        self.saude_2 = CTkLabel(master=self.frame_info,width=300, text= info[7], height=50, font=custom_font_label, text_color="#A9A9A9")
        self.saude_2.place(x=300,y=250)

        #Estado de comportamento da vaca

        self.comportamento_1 = CTkLabel(master=self.frame_info,width=300, text= "Comportamento:", height=50, font=custom_font_label)
        self.comportamento_1.place(x=0,y=300)
        self.comportamento_2 = CTkLabel(master=self.frame_info,width=300, text= info[5], height=50, font=custom_font_label, text_color="#A9A9A9")
        self.comportamento_2.place(x=300,y=300)

        #Exibe a situação das vacas em relação as vacinas

        self.vacinas_1 = CTkLabel(master=self.frame_info,width=300, text= "Vacina:", height=50, font=custom_font_label)
        self.vacinas_1.place(x=150,y=350)
        self.vacinas_2 = CTkTextbox(master=self.frame_info, width=500, height=125, fg_color="#1B4D3B")
        self.vacinas_2.place(x=50, y=400)
        self.vacinas_2.insert("0.0", info[6])

        #Botão para deletar o animal
        self.btn_deletar_animal = CTkButton(master=self.frame_info, text="Deletar", fg_color="#123529", width= 100,height= 50,
                                              command=lambda id = info[0]: self.deletar(id))
        self.btn_deletar_animal.place(x=110,y=530)

        #Botão para atualizar
        self.btn_atualizar_animal = CTkButton(master=self.frame_info, text="Atualizar", fg_color="#123529", width= 100, height= 50,
                                              command=lambda info_vaca = info: self.atualizar_vacas(info_vaca))
        self.btn_atualizar_animal.place(x=410,y=530)

        #Botão voltar para a lista de animais

        self.btn_voltar_animal = CTkButton(master=self.root, text="Voltar", fg_color="#123529", width= 75,height= 25, command=self.voltar_animal_escolha)
        self.btn_voltar_animal.place(x=10,y=10)

    #Volta para a tela de escolha do animal

    def voltar_animal_escolha(self):
        self.animais()

    #Deleta o animal

    def deletar(self, id):
        resposta = deletar_vaca(id)
        print(id)
        print(resposta)
        if resposta == True:
            messagebox.showinfo("Deletar", "Animal removido com sucesso.")
            self.animais()
        else:
            messagebox.showerror("Deletar", resposta)

    def cadastro_animal(self):
        #Fecha o frame passado
        self.destruir_frames()

        #Informações do frame de vaca selecionada
        self.frame_cadastrar_vaca = CTkFrame(master=self.root, width=1200, height=700, fg_color=verde_fundo)
        self.frame_cadastrar_vaca.pack()

        self.frame_info = CTkFrame(master=self.frame_cadastrar_vaca, width=600, height=600, fg_color=verde_botao_fundo, border_width=2, border_color=verde_botao_fundo)
        self.frame_info.place(x=300, y= 50)
        custom_font_label = CTkFont(family="Roboto", size=15, weight="bold")

        #Informações da vaca:

        #Informações colunas

        self.info_1 = CTkLabel(master=self.frame_info,width=600, text= "PARA CADASTRAR PREENCHA TODOS OS CAMPOS!!", height=50, font=custom_font_label, fg_color="#1B4D3B")
        self.info_1.place(x=0,y=0)

        #Manejo

        self.manejo_1 = CTkLabel(master=self.frame_info,width=300, text= "Manejo:", height=50, font=custom_font_label)
        self.manejo_1.place(x=0,y=100)
        self.manejo_2 = CTkEntry(master=self.frame_info,width=300,  height=50, font=custom_font_label, text_color="#A9A9A9", fg_color="#1B4D3B")
        self.manejo_2.place(x=300,y=100)

        #Quantidade de Comida

        self.comida_1 = CTkLabel(master=self.frame_info,width=300, text= "Comida(kg):", height=50, font=custom_font_label)
        self.comida_1.place(x=0,y=150)
        self.comida_2 = CTkEntry(master=self.frame_info,width=300, height=50, font=custom_font_label, text_color="#A9A9A9", fg_color="#1B4D3B")
        self.comida_2.place(x=300,y=150)

        #O peso da vaca

        self.peso_1 = CTkLabel(master=self.frame_info,width=300, text= "Peso(kg):", height=50, font=custom_font_label)
        self.peso_1.place(x=0,y=200)
        self.peso_2 = CTkEntry(master=self.frame_info,width=300,  height=50, font=custom_font_label, text_color="#A9A9A9", fg_color="#1B4D3B")
        self.peso_2.place(x=300,y=200)

        #Estado de saude da vaca

        self.saude_1= CTkLabel(master=self.frame_info,width=300, text= "Saúde:", height=50, font=custom_font_label)
        self.saude_1.place(x=0,y=250)
        self.saude_2 = CTkEntry(master=self.frame_info,width=300, height=50, font=custom_font_label, text_color="#A9A9A9", fg_color="#1B4D3B")
        self.saude_2.place(x=300,y=250)

        #Estado de comportamento da vaca

        self.comportamento_1 = CTkLabel(master=self.frame_info,width=300, text= "Comportamento:", height=50, font=custom_font_label)
        self.comportamento_1.place(x=0,y=300)
        self.comportamento_2 = CTkEntry(master=self.frame_info,width=300, height=50, font=custom_font_label, text_color="#A9A9A9", fg_color="#1B4D3B")
        self.comportamento_2.place(x=300,y=300)

        #Exibe a situação das vacas em relação as vacinas

        self.vacinas_1 = CTkLabel(master=self.frame_info,width=300, text= "Vacina:", height=50, font=custom_font_label)
        self.vacinas_1.place(x=150,y=350)
        self.vacinas_2 = CTkTextbox(master=self.frame_info, width=500, height=125, fg_color="#1B4D3B")
        self.vacinas_2.place(x=50, y=400)
        self.vacinas_2.insert("0.0", "")

        #Botão para cancelar e voltar as informações do animal
        self.btn_cancelar_cadastro = CTkButton(master=self.frame_info, text="Cancelar", fg_color="#123529", width= 100,height= 50,
                                            command=self.animais)
        self.btn_cancelar_cadastro.place(x=110,y=530)

        

        #Botão para salvar
        self.btn_cadastrar_animal = CTkButton(master=self.frame_info, text="Cadastrar", fg_color="#123529", width= 100,height= 50,
                                              command=self.cadastrar_animal)
        self.btn_cadastrar_animal.place(x=410,y=530)

    def cadastrar_animal(self):
        #Coletando as informações a serem passadas
        valores = []
        valores.append(self.manejo_2.get())
        valores.append(self.comida_2.get())
        valores.append(self.peso_2.get())
        valores.append(self.comportamento_2.get())
        valores.append(self.vacinas_2.get("1.0", "end-1c"))
        valores.append(self.saude_2.get())
        #Manda pro banco de dados
        resposta = adicionar_vaca(valores)
        if resposta == True:
            messagebox.showinfo("Cadastro Animal", "O animal foi cadastrado com sucesso!")
            self.animais()
        else:
            messagebox.showerror("Cadastro Animal", resposta)
        

        
    def atualizar_vacas(self, info):
        #Fecha o frame passado
        self.destruir_frames()

        #Informações do frame de vaca selecionada
        self.frame_atualizar_vaca = CTkFrame(master=self.root, width=1200, height=700, fg_color=verde_fundo)
        self.frame_atualizar_vaca.pack()

        self.frame_info = CTkFrame(master=self.frame_atualizar_vaca, width=600, height=600, fg_color=verde_botao_fundo, border_width=2, border_color=verde_botao_fundo)
        self.frame_info.place(x=300, y= 50)
        custom_font_label = CTkFont(family="Roboto", size=15, weight="bold")

        #Informações da vaca:

        #Informações colunas

        self.info_1 = CTkLabel(master=self.frame_info,width=600, text= "PARA ATUALIZAR PREENCHA TODOS OS CAMPOS!!", height=50, font=custom_font_label, fg_color="#1B4D3B")
        self.info_1.place(x=0,y=0)

        #Codigo identificação vaca

        self.cod_identificacao_1 = CTkLabel(master=self.frame_info,width=300, text= "Código de Identificação:", height=50, font=custom_font_label)
        self.cod_identificacao_1.place(x=0,y=50)
        self.cod_identificacao_2 = CTkLabel(master=self.frame_info,width=300, text= info[0], height=50, font=custom_font_label, text_color="#A9A9A9")
        self.cod_identificacao_2.place(x=300,y=50)

        #Manejo

        self.manejo_1 = CTkLabel(master=self.frame_info,width=300, text= "Manejo:", height=50, font=custom_font_label)
        self.manejo_1.place(x=0,y=100)
        self.manejo_2 = CTkEntry(master=self.frame_info,width=300, placeholder_text=info[2], height=50, font=custom_font_label, text_color="#A9A9A9", fg_color="#1B4D3B")
        self.manejo_2.place(x=300,y=100)

        #Quantidade de Comida

        self.comida_1 = CTkLabel(master=self.frame_info,width=300, text= "Comida(kg):", height=50, font=custom_font_label)
        self.comida_1.place(x=0,y=150)
        self.comida_2 = CTkEntry(master=self.frame_info,width=300, placeholder_text= info[3], height=50, font=custom_font_label, text_color="#A9A9A9", fg_color="#1B4D3B")
        self.comida_2.place(x=300,y=150)

        #O peso da vaca

        self.peso_1 = CTkLabel(master=self.frame_info,width=300, text= "Peso(kg):", height=50, font=custom_font_label)
        self.peso_1.place(x=0,y=200)
        self.peso_2 = CTkEntry(master=self.frame_info,width=300, placeholder_text=info[4], height=50, font=custom_font_label, text_color="#A9A9A9", fg_color="#1B4D3B")
        self.peso_2.place(x=300,y=200)

        #Estado de saude da vaca

        self.saude_1= CTkLabel(master=self.frame_info,width=300, text= "Saúde:", height=50, font=custom_font_label)
        self.saude_1.place(x=0,y=250)
        self.saude_2 = CTkEntry(master=self.frame_info,width=300, placeholder_text=info[7], height=50, font=custom_font_label, text_color="#A9A9A9", fg_color="#1B4D3B")
        self.saude_2.place(x=300,y=250)

        #Estado de comportamento da vaca

        self.comportamento_1 = CTkLabel(master=self.frame_info,width=300, text= "Comportamento:", height=50, font=custom_font_label)
        self.comportamento_1.place(x=0,y=300)
        self.comportamento_2 = CTkEntry(master=self.frame_info,width=300, placeholder_text=info[5], height=50, font=custom_font_label, text_color="#A9A9A9", fg_color="#1B4D3B")
        self.comportamento_2.place(x=300,y=300)

        #Exibe a situação das vacas em relação as vacinas

        self.vacinas_1 = CTkLabel(master=self.frame_info,width=300, text= "Vacina:", height=50, font=custom_font_label)
        self.vacinas_1.place(x=150,y=350)
        self.vacinas_2 = CTkTextbox(master=self.frame_info, width=500, height=125, fg_color="#1B4D3B")
        self.vacinas_2.place(x=50, y=400)
        self.vacinas_2.insert("0.0", info[6])

        #Botão para cancelar e voltar as informações do animal
        self.btn_deletar_animal = CTkButton(master=self.frame_info, text="Cancelar", fg_color="#123529", width= 100,height= 50,
                                            command=lambda info_vaca = info: self.voltar_animal(info_vaca))
        self.btn_deletar_animal.place(x=110,y=530)

        

        #Botão para salvar
        self.btn_atualizar_animal = CTkButton(master=self.frame_info, text="Salvar", fg_color="#123529", width= 100,height= 50,
                                              command=lambda id = info[0]: self.atualizar_dados_vaca(id))
        self.btn_atualizar_animal.place(x=410,y=530)

    #Volta para a tela do animal escolhido

    def voltar_animal(self, info):
        self.informacoes_vacas(info)

    #Atualiza as informações do animal no DB
    def atualizar_dados_vaca(self, id):
        #Coletando as informações a serem passadas
        manejo = self.manejo_2.get()
        comida = self.comida_2.get()
        peso = self.peso_2.get()
        comportamento = self.comportamento_2.get()
        vacinas = self.vacinas_2.get("1.0", "end-1c")
        saude = self.saude_2.get()
        #Manda pro banco de dados
        resposta = atualizar_vaca(id, manejo, comida, peso, comportamento, vacinas, saude)
        
        #Caso o banco de dadso tenha sido atualizado ele exibe uma mensagem dizendo que foi possível atualizar
        if resposta == True:
            self.animais()
            messagebox.showinfo("Atualização", "Atualização concluída!")
        else:
            #Se não conseguir mostra uma mensagem de erro
            messagebox.showerror("Atualização", resposta)
        


        
       



#Carregamento das imagens:
path = os.path.dirname(__file__)
path_barras = path.replace('\\', '/')
pathFinal = path_barras + "/imagens"
btn_conta = CTkImage(Image.open(pathFinal + "/caixa conta.png"), size=(200,200))
btn_animais = CTkImage(Image.open(pathFinal + "/caixa_boi.png"), size=(200,200))
btn_monitoramento = CTkImage(Image.open(pathFinal + "/caixa monitoramento.png"), size=(200,200))
btn_registros = CTkImage(Image.open(pathFinal + "/caixa_rendimento.png"), size=(200,200))
vaca_img = CTkImage(Image.open(pathFinal + "/vaca.png"), size=(50,50))
    
        
#Iniciação do sistema, segundo Thiago é bom manter ele assim.

if __name__ == "__main__":
    root = CTk()
    app = rumizone(root)
    root.mainloop()
