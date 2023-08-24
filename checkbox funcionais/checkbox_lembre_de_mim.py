#parte para colocar no fim da tela de login
with open('lembre_de_mim.txt','r') as arquivo:
  for linha in arquivo:
    checkbox_validacao,login,senha = linha.strip().split()
    if checkbox_validacao == "1":
        result_login = logar(login,senha)
        self.menu()  
#parte pra colocar dentro da função verificar
if self.checkbox.get() == True:
    info = [self.checkbox.get(),self.cxlogin.get(),self.cxsenha.get()]
    with open('lembre_de_mim.txt','w') as arquivo:
        linha = "{} {} {} \n".format(info[0],info[1],info[2])
        arquivo.write(linha)
    self.menu()
else:
    self.menu()
     