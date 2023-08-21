from customtkinter import *

variavel = 0

#Inicio da classe do aplicativo
class rumizone(CTk):

    #Função inical que abre o primeiro frame:

    def __init__(self, root):
        self.root = root
        #Titulo do app
        self.root.title("Teste")
        #Tamanho da tela
        self.root.geometry("800x600")
        #Não permite mudança no tamanho da tela
        self.root.resizable(width=False, height=False)
        #Deixa o aplicativo no modo escuro(Muito mais bonito)
        set_appearance_mode("dark")
        #Abre o primeiro frame
        self.frame1()

    #Função que fecha os frames ao mudar de tela, sendo sempre necessário chama-lo quando se abre uma janela.

    def destruir_frames(self):
        for x in root.winfo_children():
            x.destroy()

    #Frame inicial

    def frame1(self):
        global variavel
        #Informações do Frame 1
        self.frame_um = CTkFrame(master=self.root, width=800, height=600)
        self.frame_um.pack()

        #Codigo besta tava só testando como usar vairaveis globais aqui

        self.L = CTkLabel(master=self.root, text="Frame 1:" + str(variavel), text_color="white")
        self.L.place(x=10, y=10)

        self.btn = CTkButton(master=self.root, width=100,
                             text="ir", command=self.botao)
        self.btn.place(x=100, y=100)

    #Botão ir

    def botao(self):
        global variavel
        variavel += 1
        self.frame2()
        

    #Segundo Frame que é aberto ao clicar o botão

    def frame2(self):
        global variavel
        self.destruir_frames()
        self.frame_dois = CTkFrame(master=self.root, width=800, height=600)
        self.frame_dois.pack()

        self.L = CTkLabel(master=self.root, text="Frame 2:" + str(variavel), text_color="white")
        self.L.place(x=10, y=10)

        self.voltar = CTkButton(master=self.frame_dois,
                                width=100, text="Voltar", command=self.fun_voltar)
        self.voltar.place(x=100, y=100)

    #Botão voltar

    def fun_voltar(self):
        global variavel
        variavel += 1
        self.destruir_frames()
        self.frame1()
    
    
        
#Iniciação do sistema, segundo Thiago é bom manter ele assim.

if __name__ == "__main__":
    root = CTk()
    app = rumizone(root)
    root.mainloop()
