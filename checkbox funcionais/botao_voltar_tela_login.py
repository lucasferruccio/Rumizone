#botão pra botar na tela de "minha conta"
self.btn_sair_conta = CTkButton(master=self.root,width=80,height=50,text="sair da conta",bg_color="red",command=self.limpar_dados,text_color="black")
self.btn_sair_conta.place(x=100,y=50)
#funcao para limpar os arquivos de texto
def limpar_dados(self):
    with open('lembre_de_mim.txt','w') as arquivo:
        linha = "{} {} {} \n".format("0","0","0")
        arquivo.write(linha)
    self.login() 