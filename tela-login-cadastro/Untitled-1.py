#Frame inicial

def login(self):
    self.destruir_frames()
    #Informações do Frame de Login
    self.frame_login = CTkFrame(master=self.root, width=1200, height=700, fg_color=verde_fundo)
    self.frame_login.pack()
    self.frame_info = CTkFrame(master=self.frame_login, width=550, height=700, border_width=2, border_color=verde_botao_fundo,fg_color="#1C1C1C")
    self.frame_info.place(x=650,y=0)
    #Logo Rumizone
    custom_font_title = CTkFont(family="Roboto", size=40, weight="bold")
    self.rumizone_centro = CTkLabel(master=self.root, text="Rumizone", width=0, fg_color=verde_fundo, font=custom_font_title,text_color= verde_botao)
    self.rumizone_centro.place(x=250, y=25)
    
    #texto abaixo da logo
    custom_font_title = CTkFont(family="Roboto", size=20, weight="bold")
    self.label_definicao = CTkLabel(master=self.root, text="Especialistas em monitoramento e comportamento animal", width=0, font=custom_font_title,text_color= "white",fg_color=verde_fundo)
    self.label_definicao.place(x=50, y=100)
    
    #imagem abaixo da logo
    self.img_vacas = CTkLabel(master=self.root,image=vacas_img, text="")
    self.img_vacas.place(x=100, y=150)
    
   
   
    #txt "Sistema de Login
    custom_font_title = CTkFont(family="Roboto", size=40, weight="bold")
    self.txt_sistema = CTkLabel(master=self.frame_login, text="Sistema de Login", width=0, font=custom_font_title,bg_color="#1C1C1C")
    self.txt_sistema.place(x=800, y=100)


    #Caixa de Login
    self.cxlogin = CTkEntry(master=self.frame_login, width=300,height=40,placeholder_text= "Nome de Usuário")
    self.cxlogin.place(x=810, y=200)
    self.txt_alertalogin = CTkLabel(master=self.frame_login, text="*O campo nome de usuario é de carater obrigatorio.",text_color="green",fg_color="#1C1C1C")
    self.txt_alertalogin.place(x=810, y=250)
    
   
    #Caixa da senha
    self.cxsenha = CTkEntry(master=self.frame_login, width=300, height=40,placeholder_text="Senha do Usuário",show="*")
    self.cxsenha.place(x=810, y=300)
    self.txt_alertasenha = CTkLabel(master=self.frame_login, text="*O campo senha do usuario é de carater obrigatorio.",text_color="green",bg_color="#1C1C1C")
    self.txt_alertasenha.place(x=810, y=350)
    
    #checkbox inútil
    self.checkbox=CTkCheckBox(master=self.frame_login,text="Lembrar-se de mim sempre",bg_color="#1C1C1C")
    self.checkbox.place(x=810,y=400)

    #botão de verificação
    self.btn_login = CTkButton(master=self.frame_login,text="login", width=300, height=40, fg_color =verde, command=self.verificar)
    self.btn_login.place(x=810, y=450)

    #botão de cadastro
    self.txt_cadastro = CTkLabel(master=self.frame_login,text="ainda não tem uma conta?",bg_color="#1C1C1C")
    self.txt_cadastro.place(x=810,y=550)
    self.btn_cadastro = CTkButton(master=self.frame_login,text="Cadastre-se", width=150, height=30, fg_color =verde,command = self.cadastro)
    self.btn_cadastro.place(x=975, y=550)

#Verifica se o usuário é cadastrado e se a senha é válida. Caso negado, um erro será impresso na tela

def verificar(self):
    result_login = logar(self.cxlogin.get(), self.cxsenha.get())
    if result_login == True:
        self.menu()
    else:
        messagebox.showerror("Erro no login!", result_login)
        
#Frame do menu de acesso a todos as funções do aplicativo


def cadastro(self):
    #fechando o frame passado
    self.destruir_frames()
    
    #informações do Frame Cadastro
    self.frame1_cadastro = CTkFrame(master=self.root, width=1200, height=700, fg_color=verde_fundo)
    self.frame1_cadastro.pack()
    self.frame2_cadastro = CTkFrame(master=self.frame1_cadastro, width=550, height=700, border_width=2, border_color=verde_botao_fundo,fg_color="#1C1C1C")
    self.frame2_cadastro.place(x=650,y=0)
     #Logo Rumizone
    custom_font_title = CTkFont(family="Roboto", size=40, weight="bold")
    self.rumizone_centro = CTkLabel(master=self.root, text="Rumizone", width=0, fg_color=verde_fundo, font=custom_font_title,text_color= verde_botao)
    self.rumizone_centro.place(x=250, y=25)
    
    #texto abaixo da logo
    custom_font_title = CTkFont(family="Roboto", size=20, weight="bold")
    self.label_definicao = CTkLabel(master=self.root, text="Especialistas em monitoramento e comportamento animal", width=0, font=custom_font_title,text_color= "white",fg_color=verde_fundo)
    self.label_definicao.place(x=50, y=100)
    
    #imagem abaixo da logo
    self.img_vacas = CTkLabel(master=self.root,image=vacas_img, text="")
    self.img_vacas.place(x=100, y=150)
    
    #texto do sistema de cadastro
    custom_font_title = CTkFont(family="Roboto", size=40, weight="bold")
    self.txt_sistema = CTkLabel(master=self.frame1_cadastro, text="Sistema de Cadastro", width=0, font=custom_font_title,fg_color="#1C1C1C")
    self.txt_sistema.place(x=750, y=50)
    self.txt_aviso= CTkLabel(master=self.frame1_cadastro,text="**Por favor preencha todos os campos**",width=0,fg_color="#1C1C1C",text_color="#DCDCDC")
    self.txt_aviso.place(x=800,y=100)
    #caixa do campo para preenchimento de login
    self.cxnome = CTkEntry(master=self.frame1_cadastro, width=300,height=40,placeholder_text= "Nome Completo")
    self.cxnome.place(x=780, y=150)
    self.cxcargo = CTkEntry(master=self.frame1_cadastro, width=300,height=40,placeholder_text= "Cargo na empresa")
    self.cxcargo.place(x=780, y=200)
    self.cxcpf = CTkEntry(master=self.frame1_cadastro, width=300,height=40,placeholder_text= "CPF")
    self.cxcpf.place(x=780, y=250)
    self.cxemail= CTkEntry(master=self.frame1_cadastro, width=300,height=40,placeholder_text= "Email")
    self.cxemail.place(x=780, y=300)
    self.cxendereco = CTkEntry(master=self.frame1_cadastro, width=300,height=40,placeholder_text= "Endereço")
    self.cxendereco.place(x=780, y=350)
    self.cxlogin = CTkEntry(master=self.frame1_cadastro, width=300,height=40,placeholder_text= "Login")
    self.cxlogin.place(x=780, y=400)
    self.cxsenha = CTkEntry(master=self.frame1_cadastro, width=300,height=40,placeholder_text= "Senha")
    self.cxsenha.place(x=780, y=450)
    
    #checkbox dos termos e condições
    self.checkbox = CTkCheckBox(master=self.frame1_cadastro,text="Aceito os Termos e Políticas",bg_color="#1C1C1C")
    self.checkbox.place(x=780,y=550)
    
    #botôes de voltar e fazer o cadastro
    self.btnvoltar = CTkButton(master=self.frame1_cadastro,text="Voltar",fg_color="#808080", width=100, height=30,command = self.login)
    self.btnvoltar.place(x=780,y=600)
    self.btncadastrar = CTkButton(master=self.frame1_cadastro,text="Cadastrar",fg_color="green", width=200, height=30,command = self.cadastrar_pessoa)
    
    self.btncadastrar.place(x=900,y=600)
def cadastrar_pessoa(self):
    nome = self.cxnome.get()
    cargo = self.cxcargo.get()
    cpf = self.cxcpf.get()
    email = self.cxemail.get()
    endereco = self.cxendereco.get()
    fazenda = 1
    login = self.cxlogin.get()
    senha = self.cxsenha.get()
    resposta = cadastrar(nome,cargo,cpf,email,endereco,fazenda,login,senha)
    if resposta==True: 
        messagebox.showinfo("CADASTRO","Cadastrado com sucesso!!")
        self.login()
    else:
        messagebox.showerror("CADASTRO",resposta)