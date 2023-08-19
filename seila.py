from customtkinter import*
vacal = {"mimoza": ["gay", "gorda"], "leiteira": ["branca", "preta"]}
coluna = -1
tela = CTk()
tela.geometry("1200x700")
frame = CTkFrame(tela, width=1200, height= 700)
frame.grid(row = 0, column = 0)
def entrar(vacas, info):
    print(vacas)
    telavaca = CTkToplevel()
    telavaca.title(vacas)
    telavaca.geometry("300x600")
    fundo = CTkFrame(telavaca,width=300, height= 600)
    fundo.grid(row = 0, column = 0)
    textp = CTkLabel(fundo,width=300, text= "comportamento : "+info[0], height=30)
    textp.grid(row=0, column = 0)
    textp2 = CTkLabel(fundo,width=300, text= "status de saude : "+info[1], height=30)
    textp2.grid(row=1, column = 0)
    
for vaca, infos in vacal.items(): 
    coluna += 1
    comportamento = infos[0]
    saude = infos[1]
    btvaca = CTkButton(frame,text=("%s \n %s \n %s" %(vaca, comportamento, saude)),command= lambda v = vaca, i = infos: entrar(v, i))
    btvaca.grid(row=0, column = coluna)
tela.mainloop()