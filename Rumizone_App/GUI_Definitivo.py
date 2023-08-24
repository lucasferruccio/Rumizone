from customtkinter import *
from tkinter import messagebox
from PIL import Image
from MySQLdb import *
from crud import *
import os
from pathlib import Path
from funcApp import *
from monitoramento.main import monitoramento
import datetime


verde_fundo = "#172526"
verde_botao = "#47a98e"
verde_botao_fundo = "#2e6d5c"
branco = "#FFFFFF"
preto = "#000000"
verde = "#20CD8D"

login_usuario = ""

# Inicio da classe do aplicativo


class rumizone(CTk):

    # Função inical que abre o primeiro frame:

    def __init__(self, root):
        self.root = root
        # Titulo do app
        self.root.title("Rumizone")
        # Tamanho da tela
        self.root.geometry("1200x700")
        # Não permite mudança no tamanho da tela
        self.root.resizable(width=False, height=False)
        # Deixa o aplicativo no modo escuro(Muito mais bonito)
        set_appearance_mode("dark")
        # Abre a tela de login
        self.login()

    # Função que fecha os frames ao mudar de tela, sendo sempre necessário chama-lo quando se abre uma janela.

    def destruir_frames(self):
        for x in root.winfo_children():
            x.destroy()

    # Frame inicial

    def login(self):
        self.destruir_frames()
        # Informações do Frame de Login
        self.frame_login = CTkFrame(
            master=self.root, width=1200, height=700, fg_color=verde_fundo)
        self.frame_login.pack()
        self.frame_info = CTkFrame(master=self.frame_login, width=550, height=700,
                                   border_width=2, border_color=verde_botao_fundo, fg_color="#1C1C1C")
        self.frame_info.place(x=650, y=0)
        # Logo Rumizone
        custom_font_title = CTkFont(family="Roboto", size=40, weight="bold")
        self.rumizone_centro = CTkLabel(master=self.root, text="Rumizone", width=0,
                                        fg_color=verde_fundo, font=custom_font_title, text_color=verde_botao)
        self.rumizone_centro.place(x=250, y=25)

        # texto abaixo da logo
        custom_font_title = CTkFont(family="Roboto", size=20, weight="bold")
        self.label_definicao = CTkLabel(master=self.root, text="Especialistas em monitoramento e comportamento animal",
                                        width=0, font=custom_font_title, text_color="white", fg_color=verde_fundo)
        self.label_definicao.place(x=50, y=100)

        # imagem abaixo da logo
        self.img_vacas = CTkLabel(master=self.root, image=vacas_img, text="")
        self.img_vacas.place(x=100, y=150)

        # txt "Sistema de Login
        custom_font_title = CTkFont(family="Roboto", size=40, weight="bold")
        self.txt_sistema = CTkLabel(master=self.frame_login, text="Sistema de Login",
                                    width=0, font=custom_font_title, bg_color="#1C1C1C")
        self.txt_sistema.place(x=800, y=100)

        # Caixa de Login
        self.cxlogin = CTkEntry(
            master=self.frame_login, width=300, height=40, placeholder_text="Nome de Usuário")
        self.cxlogin.place(x=810, y=200)
        self.txt_alertalogin = CTkLabel(
            master=self.frame_login, text="*O campo nome de usuario é de carater obrigatorio.", text_color="green", fg_color="#1C1C1C")
        self.txt_alertalogin.place(x=810, y=250)

        # Caixa da senha
        self.cxsenha = CTkEntry(master=self.frame_login, width=300,
                                height=40, placeholder_text="Senha do Usuário", show="*")
        self.cxsenha.place(x=810, y=300)
        self.txt_alertasenha = CTkLabel(
            master=self.frame_login, text="*O campo senha do usuario é de carater obrigatorio.", text_color="green", bg_color="#1C1C1C")
        self.txt_alertasenha.place(x=810, y=350)

        # checkbox inútil
        self.checkbox = CTkCheckBox(
            master=self.frame_login, text="Lembrar-se", bg_color="#1C1C1C")
        self.checkbox.place(x=810, y=400)

        # botão de verificação
        self.btn_login = CTkButton(master=self.frame_login, text="login",
                                   width=300, height=40, fg_color=verde, command=self.verificar)
        self.btn_login.place(x=810, y=450)

        # botão de cadastro
        self.txt_cadastro = CTkLabel(
            master=self.frame_login, text="ainda não tem uma conta?", bg_color="#1C1C1C")
        self.txt_cadastro.place(x=810, y=550)
        self.btn_cadastro = CTkButton(master=self.frame_login, text="Cadastre-se",
                                      width=150, height=30, fg_color=verde, command=self.cadastro)
        self.btn_cadastro.place(x=975, y=550)

    def cadastro(self):
        # fechando o frame passado
        self.destruir_frames()

        # informações do Frame Cadastro
        self.frame1_cadastro = CTkFrame(
            master=self.root, width=1200, height=700, fg_color=verde_fundo)
        self.frame1_cadastro.pack()
        self.frame2_cadastro = CTkFrame(master=self.frame1_cadastro, width=550, height=700,
                                        border_width=2, border_color=verde_botao_fundo, fg_color="#1C1C1C")
        self.frame2_cadastro.place(x=650, y=0)
        # Logo Rumizone
        custom_font_title = CTkFont(family="Roboto", size=40, weight="bold")
        self.rumizone_centro = CTkLabel(master=self.root, text="Rumizone", width=0,
                                        fg_color=verde_fundo, font=custom_font_title, text_color=verde_botao)
        self.rumizone_centro.place(x=250, y=25)

        # texto abaixo da logo
        custom_font_title = CTkFont(family="Roboto", size=20, weight="bold")
        self.label_definicao = CTkLabel(master=self.root, text="Especialistas em monitoramento e comportamento animal",
                                        width=0, font=custom_font_title, text_color="white", fg_color=verde_fundo)
        self.label_definicao.place(x=50, y=100)

        # imagem abaixo da logo
        self.img_vacas = CTkLabel(master=self.root, image=vacas_img, text="")
        self.img_vacas.place(x=100, y=150)

        # texto do sistema de cadastro
        custom_font_title = CTkFont(family="Roboto", size=40, weight="bold")
        self.txt_sistema = CTkLabel(master=self.frame1_cadastro, text="Sistema de Cadastro",
                                    width=0, font=custom_font_title, fg_color="#1C1C1C")
        self.txt_sistema.place(x=750, y=50)
        self.txt_aviso = CTkLabel(master=self.frame1_cadastro, text="**Por favor preencha todos os campos**",
                                  width=0, fg_color="#1C1C1C", text_color="#DCDCDC")
        self.txt_aviso.place(x=800, y=100)

        # caixa do campo para preenchimento de login

        # Inserir nome
        self.cxnome = CTkEntry(master=self.frame1_cadastro,
                               width=300, height=40, placeholder_text="Nome Completo")
        self.cxnome.place(x=780, y=150)

        # Inserir cargo
        self.cxcargo = CTkEntry(master=self.frame1_cadastro, width=300,
                                height=40, placeholder_text="Cargo na empresa")
        self.cxcargo.place(x=780, y=200)

        # Inserir cpf
        self.cxcpf = CTkEntry(master=self.frame1_cadastro,
                              width=300, height=40, placeholder_text="CPF")
        self.cxcpf.place(x=780, y=250)

        # Inserir e-mail
        self.cxemail = CTkEntry(
            master=self.frame1_cadastro, width=300, height=40, placeholder_text="Email")
        self.cxemail.place(x=780, y=300)

        # Inserir endereço
        self.cxendereco = CTkEntry(
            master=self.frame1_cadastro, width=300, height=40, placeholder_text="Endereço")
        self.cxendereco.place(x=780, y=350)

        # Inserir login
        self.cxlogin = CTkEntry(
            master=self.frame1_cadastro, width=300, height=40, placeholder_text="Login")
        self.cxlogin.place(x=780, y=400)
        self.cxsenha = CTkEntry(
            master=self.frame1_cadastro, width=300, height=40, placeholder_text="Senha")
        self.cxsenha.place(x=780, y=450)

        # checkbox dos termos e condições
        self.checkbox = CTkCheckBox(
            master=self.frame1_cadastro, text="Aceito os Termos e Políticas", bg_color="#1C1C1C")
        self.checkbox.place(x=780, y=550)

        # botôes de voltar e fazer o cadastro
        self.btnvoltar = CTkButton(master=self.frame1_cadastro, text="Voltar",
                                   fg_color="#808080", width=100, height=30, command=self.login)
        self.btnvoltar.place(x=780, y=600)
        self.btncadastrar = CTkButton(master=self.frame1_cadastro, text="Cadastrar",
                                      fg_color="green", width=200, height=30, command=self.cadastrar_pessoa)

        self.btncadastrar.place(x=900, y=600)

    # Função para cadastrar pessoas no sistema

    def cadastrar_pessoa(self):
        # Coleta de dados
        nome = self.cxnome.get()
        cargo = self.cxcargo.get()
        cpf = self.cxcpf.get()
        email = self.cxemail.get()
        endereco = self.cxendereco.get()
        fazenda = 1
        login = self.cxlogin.get()
        senha = self.cxsenha.get()

        # Cadastro
        resposta = cadastrar(nome, cargo, cpf, email,
                             endereco, fazenda, login, senha)
        if resposta == True:
            messagebox.showinfo("CADASTRO", "Cadastrado com sucesso!!")
            self.login()
        else:
            messagebox.showerror("CADASTRO", resposta)

    # Verifica se o usuário é cadastrado e se a senha é válida. Caso negado, um erro será impresso na tela
    def verificar(self):
        global login_usuario
        login_usuario = self.cxlogin.get()
        senha_usuario = self.cxsenha.get()
        result_login = logar(login_usuario, senha_usuario)
        if result_login == True:
            self.menu()
        else:
            messagebox.showerror("Erro no login!", result_login)

    # Frame do menu de acesso a todos as funções do aplicativo

    def menu(self):
        # Fecha o frame passado
        self.destruir_frames()

        # Informações do Frame do menu
        self.frame_menu = CTkFrame(
            master=self.root, width=1200, height=700, fg_color=verde_fundo)
        self.frame_menu.pack()

        # Logo Rumizone
        custom_font_title = CTkFont(family="Roboto", size=40, weight="bold")
        self.rumizone_centro = CTkLabel(
            master=self.root, text="Rumizone", width=0, fg_color=verde_fundo, font=custom_font_title)
        self.rumizone_centro.place(x=480, y=40)

        # Botão para o Frame da Conta

        self.btconta = CTkButton(master=self.root, image=btn_conta, text="",
                                 fg_color=verde_fundo, width=100, height=70, command=self.menu_conta)
        self.btconta.place(x=300, y=100)

        # Botão para o Frame dos animais
        self.btboi = CTkButton(master=self.root, image=btn_animais, text="",
                               fg_color=verde_fundo, width=100, height=70, command=self.btn_animais)
        self.btboi.place(x=650, y=380)
        self.btboi["font"] = ("Verdana", "15")

        # Botão para o Frame de Análise Comportamental
        self.btmonitoramento = CTkButton(master=self.root, image=btn_monitoramento, text="",
                                         fg_color=verde_fundo, width=100, height=70, command=self.monitoramento_comportamento)
        self.btmonitoramento.place(x=650, y=100)

        # Botão para o Frame de Registros
        self.btregistros = CTkButton(master=self.root, image=btn_registros, text="",
                                     fg_color=verde_fundo, width=100, height=7, command=self.relatorios)
        self.btregistros.place(x=300, y=380)

    # Minha conta:
    # Botão para o Frame de Análise Comportamental
        self.btrendimento = CTkButton(master=self.root, image=btn_animais, text="",
                                      fg_color=verde_fundo, width=100, height=70, command=self.animais)
        self.btrendimento.place(x=650, y=380)

    # Conta:
    def menu_conta(self):
        global login_usuario
        id_usuario = puxar_id(login_usuario)
        # Fecha o frame passado
        self.destruir_frames()

        # Informações do Frame do menu_conta
        self.menu_conta_Frame = CTkFrame(
            master=self.root, width=1200, height=700, fg_color=verde_fundo)
        self.menu_conta_Frame.grid(row=0, column=0)

        # Informações da conta

        informacoes = info_conta(id_usuario[0])

        # Frame das informações da conta na tela

        custom_font_label = CTkFont(family="Roboto", size=20, weight="bold")
        aviso = CTkFont(family="Roboto", size=10, weight="bold")
        self.frame_info_conta = CTkFrame(
            master=self.menu_conta_Frame, width=900, height=400, fg_color=verde, border_width=2, border_color=verde)
        self.frame_info_conta.place(x=150, y=150)

        # Infomações:

        # Nome
        self.texto_nome = CTkLabel(
            master=self.frame_info_conta, text="Nome: " + informacoes[0], font=custom_font_label)
        self.texto_nome.place(x=20, y=31)

        # Cargo
        self.texto_cargo = CTkLabel(
            master=self.frame_info_conta, text="Cargo: " + informacoes[1], font=custom_font_label)
        self.texto_cargo.place(x=20, y=91)

        # cpf
        self.texto_cpf = CTkLabel(master=self.frame_info_conta,
                                  text="CPF: " + str(informacoes[2]), font=custom_font_label)
        self.texto_cpf.place(x=20, y=152)

        # Email
        self.texto_email = CTkLabel(
            master=self.frame_info_conta, text="Email: " + str(informacoes[3]), font=custom_font_label)
        self.texto_email.place(x=20, y=213)

        # Endereço
        self.texto_endereco = CTkLabel(
            master=self.frame_info_conta, text="Endereço: " + str(informacoes[4]), font=custom_font_label)
        self.texto_endereco.place(x=20, y=274)

        # Login
        self.texto_login = CTkLabel(
            master=self.frame_info_conta, text="Login: " + str(informacoes[5]), font=custom_font_label)
        self.texto_login.place(x=20, y=335)

        # Texto aviso
        self.texto_aviso = CTkLabel(
            master=self.menu_conta_Frame, text="Para entrar em contato com o suporte ligue para: 2101-1111", font=aviso)
        self.texto_aviso.place(x=850, y=670)

        # Botão para voltar ao menu
        self.btn_voltar_menu = CTkButton(
            master=self.root, text="Voltar", fg_color="#123529", width=75, height=25, command=self.voltar_menu)
        self.btn_voltar_menu.place(x=10, y=10)

        # Botão para editar informações da conta

        self.btn_cadastrar_animal = CTkButton(master=self.root, text="Atualizar", fg_color="#123529", width=75, height=25,
                                              command=self.atualizar_conta_frame)
        self.btn_cadastrar_animal.place(x=1115, y=10)

    # Frame de atualizar conta

    def atualizar_conta_frame(self):
        global login_usuario
        id_usuario = puxar_id(login_usuario)
        # Fecha o frame passado
        self.destruir_frames()

        # Informações do Frame do menu_conta
        self.menu_conta_Frame = CTkFrame(
            master=self.root, width=1200, height=700, fg_color=verde_fundo)
        self.menu_conta_Frame.grid(row=0, column=0)

        # Informações da conta

        informacoes = info_conta(id_usuario[0])

        # Frame das informações da conta na tela

        custom_font_label = CTkFont(family="Roboto", size=20, weight="bold")
        aviso = CTkFont(family="Roboto", size=10, weight="bold")
        self.frame_info_conta = CTkFrame(
            master=self.menu_conta_Frame, width=900, height=400, fg_color=verde, border_width=2, border_color=verde)
        self.frame_info_conta.place(x=150, y=150)

        # Infomações:

        # Nome
        self.texto_nome = CTkLabel(
            master=self.frame_info_conta, text="Nome: ", font=custom_font_label)
        self.texto_nome.place(x=20, y=31)
        self.entry_nome = CTkEntry(
            master=self.frame_info_conta, placeholder_text=informacoes[0])
        self.entry_nome.place(x=100, y=31)

        # Cargo
        self.texto_cargo = CTkLabel(
            master=self.frame_info_conta, text="Cargo: ", font=custom_font_label)
        self.texto_cargo.place(x=20, y=91)
        self.entry_cargo = CTkEntry(
            master=self.frame_info_conta, placeholder_text=informacoes[1])
        self.entry_cargo.place(x=100, y=91)

        # cpf
        self.texto_cpf = CTkLabel(
            master=self.frame_info_conta, text="CPF: " + informacoes[2], font=custom_font_label)
        self.texto_cpf.place(x=20, y=152)

        # Email
        self.texto_email = CTkLabel(
            master=self.frame_info_conta, text="Email: ", font=custom_font_label)
        self.texto_email.place(x=20, y=213)
        self.entry_email = CTkEntry(
            master=self.frame_info_conta, placeholder_text=informacoes[3])
        self.entry_email.place(x=90, y=213)

        # Endereço
        self.texto_endereco = CTkLabel(
            master=self.frame_info_conta, text="Endereço: ", font=custom_font_label)
        self.texto_endereco.place(x=20, y=274)
        self.entry_endereco = CTkEntry(
            master=self.frame_info_conta, placeholder_text=informacoes[4])
        self.entry_endereco.place(x=120, y=274)

        # Login
        self.texto_login = CTkLabel(
            master=self.frame_info_conta, text="Login: " + informacoes[5], font=custom_font_label)
        self.texto_login.place(x=20, y=335)

        # Botão para voltar ao menu
        self.btn_voltar_menu = CTkButton(
            master=self.root, text="Cancelar", fg_color="#123529", width=75, height=25, command=self.menu_conta)
        self.btn_voltar_menu.place(x=10, y=10)

        # Botão para salvar as edições da conta

        self.btn_cadastrar_animal = CTkButton(master=self.root, text="Salvar", fg_color="#123529", width=75, height=25,
                                              command=self.atualizar_conta)
        self.btn_cadastrar_animal.place(x=1115, y=10)

        # Texto aviso
        self.texto_aviso = CTkLabel(
            master=self.menu_conta_Frame, text="Para entrar em contato com o suporte ligue para: 2101-1111", font=aviso)
        self.texto_aviso.place(x=850, y=670)

    # Função de atualizar dados da conta

    def atualizar_conta(self):
        global login_usuario
        id = puxar_id(login_usuario)

        # Coleta de dado
        nome = self.entry_nome.get()
        cargo = self.entry_cargo.get()
        email = self.entry_email.get()
        endereco = self.entry_endereco.get()
        valores = {"nome": nome, "cargo": cargo,
                   "email": email, "endereco": endereco}
        resposta = atualizar_dados_conta(valores, id[0])
        if resposta == True:
            messagebox.showinfo("Atualizar Conta",
                                "Conta atualizada com sucesso!")
            self.menu_conta()
        else:
            messagebox.showerror("Atualizar Conta", resposta)

    # Animais:

    # Botão de acesso ao Frame de animais.
    def btn_animais(self):
        self.animais()

    def animais(self):
        # Fecha o frame passado
        self.destruir_frames()

        # Informações do Frame dos animais
        self.animais_Frame = CTkFrame(
            master=self.root, width=1200, height=700, fg_color=verde_fundo)
        self.animais_Frame.grid(row=0, column=0)

        # Coleta de alguns dados para a criação dos botões, para retirar a quantidade e os ids das vacas no DB

        ids_vacas = [id[0] for id in select("id_vaca", "vacas")]

        # Criação de botões iguais aos numéros de ids(único para cada animal)
        aux = 0  # Conta o número de botões por linha
        aux_x = 0  # Ajuda a organizar o valor de x do botão
        aux_y = 1  # Ajuda a organizar o valor de y do botão
        if len(ids_vacas) != 0:
            for contagem_relatorios in range(len(ids_vacas)):
                if (contagem_relatorios % 4) == 0 and contagem_relatorios != 0:
                    aux_x = 0
                    aux_y += 10
                # Coleta de dados básicos para a aparição no botão
                info_vaca_botao = botao_vaca(ids_vacas[contagem_relatorios])
                # Coleta de todos os dados das vacas
                info_vaca_completa = info_vaca(info_vaca_botao[0])
                # Criação dos botões
                self.btn_vaca = CTkButton(master=self.animais_Frame, text=("Cód: " + str(info_vaca_botao[0]) + "\n" + "Comportamento: " + info_vaca_botao[1] + "\n" + "Status de Saúde: " + info_vaca_botao[2]),
                                          image=vaca_img, compound="top", width=200, height=180,
                                          fg_color=verde_botao, border_width=3, border_color=verde_botao_fundo,
                                          command=lambda info_vaca=info_vaca_completa: self.informacoes_vacas(info_vaca))
                self.btn_vaca.place(x=(aux_x + 1)*215, y=(aux_y*20))
                aux_x += 1
                aux += 1

        # Botão para voltar ao menu
        self.btn_voltar_menu = CTkButton(
            master=self.root, text="Voltar", fg_color="#123529", width=75, height=25, command=self.voltar_menu)
        self.btn_voltar_menu.place(x=10, y=10)

        # Botão adicionar um anima na lista de animais

        self.btn_cadastrar_animal = CTkButton(master=self.root, text="Adicionar", fg_color="#123529", width=75, height=25,
                                              command=self.cadastro_animal)
        self.btn_cadastrar_animal.place(x=1115, y=10)

    # Função que chama o frame do menu
    def voltar_menu(self):
        self.menu()

    # Vai mostrar todas as informações sobre a vaca escolhida

    def informacoes_vacas(self, info):
        # Fecha o frame passado
        self.destruir_frames()

        # Informações do frame de vaca selecionada
        self.frame_info_vaca = CTkFrame(
            master=self.root, width=1200, height=700, fg_color=verde_fundo)
        self.frame_info_vaca.pack()

        self.frame_info = CTkFrame(master=self.frame_info_vaca, width=600, height=600,
                                   fg_color=verde_botao_fundo, border_width=2, border_color=verde_botao_fundo)
        self.frame_info.place(x=300, y=50)
        custom_font_label = CTkFont(family="Roboto", size=15, weight="bold")

        # Informações da vaca

        # Informações colunas

        self.info_1 = CTkLabel(master=self.frame_info, width=300, text="Informação",
                               height=50, font=custom_font_label, fg_color="#1B4D3B")
        self.info_1.place(x=0, y=0)
        self.info_2 = CTkLabel(master=self.frame_info, width=300, text="Atual",
                               height=50, font=custom_font_label, fg_color="#1B4D3B")
        self.info_2.place(x=300, y=0)

        # Codigo identificação vaca

        self.cod_identificacao_1 = CTkLabel(
            master=self.frame_info, width=300, text="Código de Identificação:", height=50, font=custom_font_label)
        self.cod_identificacao_1.place(x=0, y=50)
        self.cod_identificacao_2 = CTkLabel(
            master=self.frame_info, width=300, text=info[0], height=50, font=custom_font_label, text_color="#A9A9A9")
        self.cod_identificacao_2.place(x=300, y=50)

        # Manejo

        self.manejo_1 = CTkLabel(master=self.frame_info, width=300,
                                 text="Data de Manejo:", height=50, font=custom_font_label)
        self.manejo_1.place(x=0, y=100)
        self.manejo_2 = CTkLabel(master=self.frame_info, width=300,
                                 text=info[2], height=50, font=custom_font_label, text_color="#A9A9A9")
        self.manejo_2.place(x=300, y=100)

        # Quantidade de Comida

        self.comida_1 = CTkLabel(master=self.frame_info, width=300,
                                 text="Comida(kg):", height=50, font=custom_font_label)
        self.comida_1.place(x=0, y=150)
        self.comida_2 = CTkLabel(master=self.frame_info, width=300,
                                 text=info[3], height=50, font=custom_font_label, text_color="#A9A9A9")
        self.comida_2.place(x=300, y=150)

        # O peso da vaca

        self.peso_1 = CTkLabel(master=self.frame_info, width=300,
                               text="Peso(kg):", height=50, font=custom_font_label)
        self.peso_1.place(x=0, y=200)
        self.peso_2 = CTkLabel(master=self.frame_info, width=300,
                               text=info[4], height=50, font=custom_font_label, text_color="#A9A9A9")
        self.peso_2.place(x=300, y=200)

        # Estado de saude da vaca

        self.saude_1 = CTkLabel(master=self.frame_info, width=300,
                                text="Saúde:", height=50, font=custom_font_label)
        self.saude_1.place(x=0, y=250)
        self.saude_2 = CTkLabel(master=self.frame_info, width=300,
                                text=info[7], height=50, font=custom_font_label, text_color="#A9A9A9")
        self.saude_2.place(x=300, y=250)

        # Estado de comportamento da vaca

        self.comportamento_1 = CTkLabel(
            master=self.frame_info, width=300, text="Comportamento:", height=50, font=custom_font_label)
        self.comportamento_1.place(x=0, y=300)
        self.comportamento_2 = CTkLabel(master=self.frame_info, width=300,
                                        text=info[5], height=50, font=custom_font_label, text_color="#A9A9A9")
        self.comportamento_2.place(x=300, y=300)

        # Exibe a situação das vacas em relação as vacinas

        self.vacinas_1 = CTkLabel(
            master=self.frame_info, width=300, text="Vacina:", height=50, font=custom_font_label)
        self.vacinas_1.place(x=150, y=350)
        self.vacinas_2 = CTkTextbox(
            master=self.frame_info, width=500, height=125, fg_color="#1B4D3B")
        self.vacinas_2.place(x=50, y=400)
        self.vacinas_2.insert("0.0", info[6])

        # Botão para deletar o animal
        self.btn_deletar_animal = CTkButton(master=self.frame_info, text="Deletar", fg_color="#123529", width=100, height=50,
                                            command=lambda id=info[0]: self.deletar(id))
        self.btn_deletar_animal.place(x=110, y=530)

        # Botão para atualizar
        self.btn_atualizar_animal = CTkButton(master=self.frame_info, text="Atualizar", fg_color="#123529", width=100, height=50,
                                              command=lambda info_vaca=info: self.atualizar_vacas(info_vaca))
        self.btn_atualizar_animal.place(x=410, y=530)

        # Botão voltar para a lista de animais

        self.btn_voltar_animal = CTkButton(
            master=self.root, text="Voltar", fg_color="#123529", width=75, height=25, command=self.voltar_animal_escolha)
        self.btn_voltar_animal.place(x=10, y=10)

    # Volta para a tela de escolha do animal

    def voltar_animal_escolha(self):
        self.animais()

    # Deleta o animal

    def deletar(self, id):
        resposta = deletar_vaca(id)
        if resposta == True:
            messagebox.showinfo("Deletar", "Animal removido com sucesso.")
            self.animais()
        else:
            messagebox.showerror("Deletar", resposta)

    def cadastro_animal(self):
        # Fecha o frame passado
        self.destruir_frames()

        # Informações do frame de vaca selecionada
        self.frame_cadastrar_vaca = CTkFrame(
            master=self.root, width=1200, height=700, fg_color=verde_fundo)
        self.frame_cadastrar_vaca.pack()

        self.frame_info = CTkFrame(master=self.frame_cadastrar_vaca, width=600, height=600,
                                   fg_color=verde_botao_fundo, border_width=2, border_color=verde_botao_fundo)
        self.frame_info.place(x=300, y=50)
        custom_font_label = CTkFont(family="Roboto", size=15, weight="bold")

        # Informações da vaca:

        # Informações colunas

        self.info_1 = CTkLabel(master=self.frame_info, width=600, text="PARA CADASTRAR PREENCHA TODOS OS CAMPOS!!",
                               height=50, font=custom_font_label, fg_color="#1B4D3B")
        self.info_1.place(x=0, y=0)

        # Manejo

        self.manejo_1 = CTkLabel(master=self.frame_info, width=300,
                                 text="Data de Manejo:", height=50, font=custom_font_label)
        self.manejo_1.place(x=0, y=100)
        self.manejo_2 = CTkEntry(master=self.frame_info, width=300,  height=50,
                                 font=custom_font_label, text_color="#A9A9A9", fg_color="#1B4D3B")
        self.manejo_2.place(x=300, y=100)

        # Quantidade de Comida

        self.comida_1 = CTkLabel(master=self.frame_info, width=300,
                                 text="Comida(kg):", height=50, font=custom_font_label)
        self.comida_1.place(x=0, y=150)
        self.comida_2 = CTkEntry(master=self.frame_info, width=300, height=50,
                                 font=custom_font_label, text_color="#A9A9A9", fg_color="#1B4D3B")
        self.comida_2.place(x=300, y=150)

        # O peso da vaca

        self.peso_1 = CTkLabel(master=self.frame_info, width=300,
                               text="Peso(kg):", height=50, font=custom_font_label)
        self.peso_1.place(x=0, y=200)
        self.peso_2 = CTkEntry(master=self.frame_info, width=300,  height=50,
                               font=custom_font_label, text_color="#A9A9A9", fg_color="#1B4D3B")
        self.peso_2.place(x=300, y=200)

        # Estado de saude da vaca

        self.saude_1 = CTkLabel(master=self.frame_info, width=300,
                                text="Saúde:", height=50, font=custom_font_label)
        self.saude_1.place(x=0, y=250)
        self.saude_2 = CTkEntry(master=self.frame_info, width=300, height=50,
                                font=custom_font_label, text_color="#A9A9A9", fg_color="#1B4D3B")
        self.saude_2.place(x=300, y=250)

        # Estado de comportamento da vaca

        self.comportamento_1 = CTkLabel(
            master=self.frame_info, width=300, text="Comportamento:", height=50, font=custom_font_label)
        self.comportamento_1.place(x=0, y=300)
        self.comportamento_2 = CTkEntry(master=self.frame_info, width=300, height=50,
                                        font=custom_font_label, text_color="#A9A9A9", fg_color="#1B4D3B")
        self.comportamento_2.place(x=300, y=300)

        # Exibe a situação das vacas em relação as vacinas

        self.vacinas_1 = CTkLabel(
            master=self.frame_info, width=300, text="Vacina:", height=50, font=custom_font_label)
        self.vacinas_1.place(x=150, y=350)
        self.vacinas_2 = CTkTextbox(
            master=self.frame_info, width=500, height=125, fg_color="#1B4D3B")
        self.vacinas_2.place(x=50, y=400)
        self.vacinas_2.insert("0.0", "")

        # Botão para cancelar e voltar as informações do animal
        self.btn_cancelar_cadastro = CTkButton(master=self.frame_info, text="Cancelar", fg_color="#123529", width=100, height=50,
                                               command=self.animais)
        self.btn_cancelar_cadastro.place(x=110, y=530)

        # Botão para salvar
        self.btn_cadastrar_animal = CTkButton(master=self.frame_info, text="Cadastrar", fg_color="#123529", width=100, height=50,
                                              command=self.cadastrar_animal)
        self.btn_cadastrar_animal.place(x=410, y=530)

    def cadastrar_animal(self):
        # Checa para ver se o número de vacas já atinigiu o valor máximo que o programa suporta
        quantidade = select("count(*)", 'vacas')
        if quantidade[0][0] < 12:
            # Coletando as informações a serem passadas
            valores = []
            valores.append(self.manejo_2.get())
            valores.append(self.comida_2.get())
            valores.append(self.peso_2.get())
            valores.append(self.comportamento_2.get())
            valores.append(self.vacinas_2.get("1.0", "end-1c"))
            valores.append(self.saude_2.get())
            # Manda pro banco de dados
            resposta = adicionar_vaca(valores)
            if resposta == True:
                messagebox.showinfo("Cadastro Animal",
                                    "O animal foi cadastrado com sucesso!")
                self.animais()
            else:
                messagebox.showerror("Cadastro Animal", resposta)
        else:
            messagebox.showerror(
                "Cadastro Animal", "Número máximo de aniamis atingido")
            self.animais()

    # Atualizar

    def atualizar_vacas(self, info):
        # Fecha o frame passado
        self.destruir_frames()

        # Informações do frame de vaca selecionada
        self.frame_atualizar_vaca = CTkFrame(
            master=self.root, width=1200, height=700, fg_color=verde_fundo)
        self.frame_atualizar_vaca.pack()

        self.frame_info = CTkFrame(master=self.frame_atualizar_vaca, width=600, height=600,
                                   fg_color=verde_botao_fundo, border_width=2, border_color=verde_botao_fundo)
        self.frame_info.place(x=300, y=50)
        custom_font_label = CTkFont(family="Roboto", size=15, weight="bold")

        # Informações da vaca:

        # Informações colunas

        self.info_1 = CTkLabel(master=self.frame_info, width=600, text="PARA ATUALIZAR PREENCHA TODOS OS CAMPOS!!",
                               height=50, font=custom_font_label, fg_color="#1B4D3B")
        self.info_1.place(x=0, y=0)

        # Codigo identificação vaca

        self.cod_identificacao_1 = CTkLabel(
            master=self.frame_info, width=300, text="Código de Identificação:", height=50, font=custom_font_label)
        self.cod_identificacao_1.place(x=0, y=50)
        self.cod_identificacao_2 = CTkLabel(
            master=self.frame_info, width=300, text=info[0], height=50, font=custom_font_label, text_color="#A9A9A9")
        self.cod_identificacao_2.place(x=300, y=50)

        # Manejo

        self.manejo_1 = CTkLabel(master=self.frame_info, width=300,
                                 text="Data de Manejo:", height=50, font=custom_font_label)
        self.manejo_1.place(x=0, y=100)
        self.manejo_2 = CTkEntry(master=self.frame_info, width=300,
                                 placeholder_text=info[2], height=50, font=custom_font_label, text_color="#A9A9A9", fg_color="#1B4D3B")
        self.manejo_2.place(x=300, y=100)

        # Quantidade de Comida

        self.comida_1 = CTkLabel(master=self.frame_info, width=300,
                                 text="Comida(kg):", height=50, font=custom_font_label)
        self.comida_1.place(x=0, y=150)
        self.comida_2 = CTkEntry(master=self.frame_info, width=300,
                                 placeholder_text=info[3], height=50, font=custom_font_label, text_color="#A9A9A9", fg_color="#1B4D3B")
        self.comida_2.place(x=300, y=150)

        # O peso da vaca

        self.peso_1 = CTkLabel(master=self.frame_info, width=300,
                               text="Peso(kg):", height=50, font=custom_font_label)
        self.peso_1.place(x=0, y=200)
        self.peso_2 = CTkEntry(master=self.frame_info, width=300,
                               placeholder_text=info[4], height=50, font=custom_font_label, text_color="#A9A9A9", fg_color="#1B4D3B")
        self.peso_2.place(x=300, y=200)

        # Estado de saude da vaca

        self.saude_1 = CTkLabel(master=self.frame_info, width=300,
                                text="Saúde:", height=50, font=custom_font_label)
        self.saude_1.place(x=0, y=250)
        self.saude_2 = CTkEntry(master=self.frame_info, width=300,
                                placeholder_text=info[7], height=50, font=custom_font_label, text_color="#A9A9A9", fg_color="#1B4D3B")
        self.saude_2.place(x=300, y=250)

        # Estado de comportamento da vaca

        self.comportamento_1 = CTkLabel(
            master=self.frame_info, width=300, text="Comportamento:", height=50, font=custom_font_label)
        self.comportamento_1.place(x=0, y=300)
        self.comportamento_2 = CTkEntry(master=self.frame_info, width=300,
                                        placeholder_text=info[5], height=50, font=custom_font_label, text_color="#A9A9A9", fg_color="#1B4D3B")
        self.comportamento_2.place(x=300, y=300)

        # Exibe a situação das vacas em relação as vacinas

        self.vacinas_1 = CTkLabel(
            master=self.frame_info, width=300, text="Vacina:", height=50, font=custom_font_label)
        self.vacinas_1.place(x=150, y=350)
        self.vacinas_2 = CTkTextbox(
            master=self.frame_info, width=500, height=125, fg_color="#1B4D3B")
        self.vacinas_2.place(x=50, y=400)
        self.vacinas_2.insert("0.0", info[6])

        # Botão para cancelar e voltar as informações do animal
        self.btn_deletar_animal = CTkButton(master=self.frame_info, text="Cancelar", fg_color="#123529", width=100, height=50,
                                            command=lambda info_vaca=info: self.voltar_animal(info_vaca))
        self.btn_deletar_animal.place(x=110, y=530)

        # Botão para salvar
        self.btn_atualizar_animal = CTkButton(master=self.frame_info, text="Salvar", fg_color="#123529", width=100, height=50,
                                              command=lambda id=info[0]: self.atualizar_dados_vaca(id))
        self.btn_atualizar_animal.place(x=410, y=530)

    # Volta para a tela do animal escolhido

    def voltar_animal(self, info):
        self.informacoes_vacas(info)

    # Atualiza as informações do animal no DB
    def atualizar_dados_vaca(self, id):

        # Coletando as informações a serem passadas
        manejo = self.manejo_2.get()
        comida = self.comida_2.get()
        peso = self.peso_2.get()
        comportamento = self.comportamento_2.get()
        vacinas = self.vacinas_2.get("1.0", "end-1c")
        saude = self.saude_2.get()

        # Manda pro banco de dados
        resposta = atualizar_vaca(
            id, manejo, comida, peso, comportamento, vacinas, saude)

        # Caso o banco de dadso tenha sido atualizado ele exibe uma mensagem dizendo que foi possível atualizar
        if resposta == True:
            self.animais()
            messagebox.showinfo("Atualização", "Atualização concluída!")
        else:
            # Se não conseguir mostra uma mensagem de erro
            messagebox.showerror("Atualização", resposta)

    def monitoramento_comportamento(self):
        # Fecha o frame passado
        self.destruir_frames()

        # Informações do Frame dos animais
        self.monitoramento_Frame = CTkFrame(
            master=self.root, width=1200, height=700, fg_color=verde_fundo)
        self.monitoramento_Frame.grid(row=0, column=0)
        custom_font_label = CTkFont(family="Roboto", size=20, weight="bold")

        # Gerando os botões para a seleção da câmera
        for cameras in range(4):
            self.btn_camera = CTkButton(master=self.root, text=("Câmera:" + str(cameras + 1)), font=custom_font_label,
                                        image=camera_img, compound="left", width=200, height=180,
                                        fg_color=verde_botao, border_width=3, border_color=verde_botao_fundo,
                                        command=lambda camera=cameras: self.chamar_camera(camera))
            self.btn_camera.place(x=(cameras + 1)*210, y=20)

        # Botão para voltar ao menu
        self.btn_voltar_menu = CTkButton(
            master=self.root, text="Voltar", fg_color="#123529", width=75, height=25, command=self.voltar_menu)
        self.btn_voltar_menu.place(x=10, y=10)

    def chamar_camera(self, camera):
        if camera == 0:
            monitoramento("monitoramento/vacas1.mp4")
        elif camera == 1:
            monitoramento("monitoramento/vacas2.mp4")
        elif camera == 2:
            monitoramento("monitoramento/vacas3.mp4")
        elif camera == 3:
            monitoramento("monitoramento/vacas4.mp4")

    def relatorios(self):
        def puxar_nome(id):
            aux = select("nome", "usuario", "id_usuario=" + str(id))
            return aux[0][0]
        # Detruir frame anterior
        self.destruir_frames()

        # Informaçoes frames

        # Informações do Frame dos animais
        self.relatorios_frames = CTkFrame(
            master=self.root, width=1200, height=700, fg_color=verde_fundo)
        self.relatorios_frames.grid(row=0, column=0)
        custom_font_label = CTkFont(family="Roboto", size=12, weight="bold")

        # Coleta de todos os dados das vacas
        info_relatorio_completa = relatorio()

        # Quantidade de realatorios

        aux = select("count(*)", "relatorios")
        quant_relatorios = int(aux[0][0])

        # Criação de botões iguais aos numéros de ids(único para cada animal)
        num_btn = 0  # Conta o número de botões por linha
        aux_x = 0  # Ajuda a organizar o valor de x do botão
        aux_y = 1  # Ajuda a organizar o valor de y do botão

        if quant_relatorios != 0:
            for contagem_relatorios in range(quant_relatorios):
                if (contagem_relatorios % 4) == 0 and contagem_relatorios != 0:
                    aux_x = 0
                    aux_y += 10

                # Coleta as informações de cada relátorio
                valores = info_relatorio_completa[contagem_relatorios]

                # A variável com a data
                data_variavel = valores[4]

                # Formatação da data como string no formato desejado
                data_formatada = data_variavel.strftime("%d/%m/%Y")
                nome = puxar_nome(valores[1])
                texto = "Título: " + \
                    valores[2] + "\n" + "-" + \
                        str(data_formatada) + "\n" + "-" + str(nome)

                # Criação dos botões
                self.btn_vaca = CTkButton(master=self.relatorios_frames, text=texto,
                                          width=200, height=100, fg_color=verde_botao, border_width=3, border_color=verde_botao_fundo, font=custom_font_label,
                                          command=lambda info=valores, nome=nome: self.relatorio_pagina(info, nome))
                self.btn_vaca.place(x=(aux_x + 1)*215, y=(aux_y*12))
                aux_x += 1
                num_btn += 1

        # Botão para voltar ao menu
        self.btn_voltar_menu = CTkButton(
            master=self.root, text="Voltar", fg_color="#123529", width=75, height=25, command=self.voltar_menu)
        self.btn_voltar_menu.place(x=10, y=10)

        # Botão voltar para adicionar um relatorio

        self.btn_cadastrar_relatorio = CTkButton(
            master=self.root, text="Adicionar", fg_color="#123529", width=75, height=25, command=self.criar_relatorio_frame)
        self.btn_cadastrar_relatorio.place(x=1115, y=10)

    def relatorio_pagina(self, info, nome):
        # Detruir frame anterior
        self.destruir_frames()

        # Informaçoes frames do relatório
        self.adicionar_relatorio_frames = CTkFrame(
            master=self.root, width=1200, height=700, fg_color=verde_fundo)
        self.adicionar_relatorio_frames.grid(row=0, column=0)
        custom_font_label = CTkFont(family="Roboto", size=12, weight="bold")

        # Frame que vai conter as informações
        self.frame_info_relatorio = CTkFrame(master=self.adicionar_relatorio_frames, width=600,
                                             height=600, fg_color=verde_botao_fundo, border_width=2, border_color=verde_botao_fundo)
        self.frame_info_relatorio.place(x=300, y=50)

        # Informações:
        self.titulo_1 = CTkLabel(master=self.frame_info_relatorio, width=500, text="Assunto: " + info[2], height=50, font=custom_font_label,
                                 bg_color="#1B4D3B", anchor="w", padx=5, corner_radius=5)
        self.titulo_1.place(x=50, y=20)

        # Exibe a situação das vacas em relação as vacinas

        self.texto_1 = CTkLabel(master=self.frame_info_relatorio, width=100,
                                text="Relatório:", height=50, font=custom_font_label, anchor="w")
        self.texto_1.place(x=50, y=70)
        self.texto_2 = CTkTextbox(
            master=self.frame_info_relatorio, width=500, height=300, fg_color="#1B4D3B")
        self.texto_2.place(x=50, y=120)
        self.texto_2.insert("0.0", info[3])

        # Botão para deletar o animal
        self.btn_deletar_relatorio = CTkButton(master=self.frame_info_relatorio, text="Deletar", fg_color="#123529", width=100, height=50,
                                               command=lambda id=info[0]: self.relatorio_deletar(id))
        self.btn_deletar_relatorio.place(x=110, y=530)

        # Botão para atualizar
        self.btn_atualizar_relatorio = CTkButton(master=self.frame_info_relatorio, text="Atualizar", fg_color="#123529", width=100, height=50,
                                                 command=lambda info_vaca=info, nome=nome: self.atualizar_relatorio_frame(info_vaca, nome))
        self.btn_atualizar_relatorio.place(x=410, y=530)

        # Informações da pessoa que escreveu

        data = info[4]
        data_formatada = data.strftime("%d/%m/%Y")
        self.info_relatorio = CTkLabel(master=self.frame_info_relatorio, text=data_formatada +
                                       ", " + nome, fg_color="#1B4D3B", width=200, anchor="w", padx=10, corner_radius=5)
        self.info_relatorio.place(x=50, y=450)

        # Botão para voltar paro  a pagina de relatorios

        self.btn_voltar_relatorio = CTkButton(
            master=self.root, text="Voltar", fg_color="#123529", width=75, height=25, command=self.voltar_relatorio)
        self.btn_voltar_relatorio.place(x=10, y=10)

    def atualizar_relatorio_frame(self, info, nome):
        # Detruir frame anterior
        self.destruir_frames()

        # Informaçoes frames do relatório
        self.adicionar_relatorio_frames = CTkFrame(
            master=self.root, width=1200, height=700, fg_color=verde_fundo)
        self.adicionar_relatorio_frames.grid(row=0, column=0)
        custom_font_label = CTkFont(family="Roboto", size=12, weight="bold")

        # Frame que vai conter as informações
        self.frame_info_relatorio = CTkFrame(master=self.adicionar_relatorio_frames, width=600,
                                             height=600, fg_color=verde_botao_fundo, border_width=2, border_color=verde_botao_fundo)
        self.frame_info_relatorio.place(x=300, y=50)

        # Informações:
        self.titulo_1 = CTkLabel(master=self.frame_info_relatorio, width=500, text="Assunto: ", height=50, font=custom_font_label,
                                 bg_color="#1B4D3B", anchor="w", padx=5, corner_radius=5)
        self.titulo_1.place(x=50, y=20)
        self.titulo_2 = CTkEntry(master=self.frame_info_relatorio, width=400, placeholder_text=info[2], height=40, font=custom_font_label,
                                 bg_color="#1B4D3B", corner_radius=5, fg_color=branco, text_color="#000000")
        self.titulo_2.place(x=130, y=25)

        # Exibe o relatorio das vacas

        self.texto_1 = CTkLabel(master=self.frame_info_relatorio, width=100,
                                text="Relatório:", height=50, font=custom_font_label, anchor="w")
        self.texto_1.place(x=50, y=70)
        self.texto_2 = CTkTextbox(master=self.frame_info_relatorio,
                                  width=500, height=300, fg_color=branco, text_color="#000000")
        self.texto_2.place(x=50, y=120)
        self.texto_2.insert("0.0", info[3])

        # Botão para cancelar
        self.btn_cancelar_relatorio = CTkButton(master=self.frame_info_relatorio, text="Cancelar", fg_color="#123529", width=100, height=50,
                                                command=lambda info_vaca=info, nome=nome: self.relatorio_pagina(info_vaca, nome))
        self.btn_cancelar_relatorio.place(x=110, y=530)

        # Botão para atualizar
        self.btn_atualizar_relatorio = CTkButton(master=self.frame_info_relatorio, text="Salvar", fg_color="#123529", width=100, height=50,
                                                 command=lambda info_vaca=info: self.atualizar_relatorio_dados(info_vaca))
        self.btn_atualizar_relatorio.place(x=410, y=530)

    def relatorio_deletar(self, id):
        resposta = deletar_relatorio(id)
        if resposta == True:
            messagebox.showinfo("Exclusão Registro",
                                "Exclusão completa com sucesso!")
            self.relatorios()
        else:
            messagebox.showerror("Exclusão Registro", resposta)

    def atualizar_relatorio_dados(self, info):
        id = info[0]
        titulo = self.titulo_2.get()
        relatorio = self.texto_2.get("1.0", "end-1c")
        valores = {"titulo": titulo, "assunto": relatorio}
        resposta = atualizar_relatorio(id, valores, relatorio)
        if resposta == True:
            messagebox.showinfo("Atualizar Registro",
                                "Atualização completa com sucesso!")
            self.relatorios()
        else:
            messagebox.showerror("Atualizar Registro", resposta)

    def voltar_relatorio(self):
        self.relatorios()

    def criar_relatorio_frame(self):
        # Detruir frame anterior
        self.destruir_frames()

        # Informaçoes frames do relatório
        self.adicionar_relatorio_frames = CTkFrame(
            master=self.root, width=1200, height=700, fg_color=verde_fundo)
        self.adicionar_relatorio_frames.grid(row=0, column=0)
        custom_font_label = CTkFont(family="Roboto", size=12, weight="bold")

        # Frame que vai conter as informações
        self.frame_info_relatorio = CTkFrame(master=self.adicionar_relatorio_frames, width=600,
                                             height=600, fg_color=verde_botao_fundo, border_width=2, border_color=verde_botao_fundo)
        self.frame_info_relatorio.place(x=300, y=50)

        # Informações:
        self.titulo_1 = CTkLabel(master=self.frame_info_relatorio, width=500, text="Assunto: ", height=50, font=custom_font_label,
                                 bg_color="#1B4D3B", anchor="w", padx=5, corner_radius=5)
        self.titulo_1.place(x=50, y=20)
        self.titulo_2 = CTkEntry(master=self.frame_info_relatorio, width=400, height=40, font=custom_font_label,
                                 bg_color="#1B4D3B", corner_radius=5, fg_color=branco, text_color="#000000", placeholder_text="Digite Aqui")
        self.titulo_2.place(x=130, y=25)

        # Exibe o relatorio das vacas

        self.texto_1 = CTkLabel(master=self.frame_info_relatorio, width=100,
                                text="Relatório:", height=50, font=custom_font_label, anchor="w")
        self.texto_1.place(x=50, y=70)
        self.texto_2 = CTkTextbox(master=self.frame_info_relatorio,
                                  width=500, height=300, fg_color=branco, text_color="#000000")
        self.texto_2.place(x=50, y=120)
        self.texto_2.insert("0.0", "Digite Aqui")

        # Botão para cancelar
        self.btn_cancelar_relatorio = CTkButton(master=self.frame_info_relatorio, text="Cancelar", fg_color="#123529", width=100, height=50,
                                                command=self.relatorios)
        self.btn_cancelar_relatorio.place(x=110, y=530)

        # Botão para atualizar
        self.btn_atualizar_relatorio = CTkButton(master=self.frame_info_relatorio, text="Salvar", fg_color="#123529", width=100, height=50,
                                                 command=self.relatorio_criar)
        self.btn_atualizar_relatorio.place(x=410, y=530)

    def relatorio_criar(self):
        global login_usuario
        aux = login_usuario
        id = puxar_id(aux)
        titulo = self.titulo_2.get()
        relatorio = self.texto_2.get("1.0", "end-1c")
        data = datetime.date.today()
        data_formatada = data.strftime("%Y-%m-%d")
        resposta = adicionar_relatorio(
            id[0], titulo, relatorio, data_formatada)
        if resposta == True:
            messagebox.showinfo("Adionar Relátorios", "Relátorio adicionado")
            self.relatorios()
        else:
            messagebox.showerror("Adionar Relátorios", resposta)


# Carregamento das imagens:
path = os.path.dirname(__file__)
path_barras = path.replace('\\', '/')
pathFinal = path_barras + "/imagens"
btn_conta = CTkImage(Image.open(
    pathFinal + "/caixa_conta.png"), size=(200, 200))
btn_animais = CTkImage(Image.open(
    pathFinal + "/caixa_animais.png"), size=(200, 200))
btn_monitoramento = CTkImage(Image.open(
    pathFinal + "/caixa_monitoramento.png"), size=(200, 200))
btn_registros = CTkImage(Image.open(
    pathFinal + "/caixa_relatorio.png"), size=(200, 200))
vaca_img = CTkImage(Image.open(pathFinal + "/vaca.png"), size=(50, 50))
camera_img = CTkImage(Image.open(pathFinal + "/camera.png"), size=(50, 50))
vacas_img = CTkImage(Image.open(pathFinal + "/vacas_img.png"), size=(450, 450))


# Iniciação do sistema, segundo Thiago é bom manter ele assim.

if __name__ == "__main__":
    root = CTk()
    app = rumizone(root)
    root.mainloop()
