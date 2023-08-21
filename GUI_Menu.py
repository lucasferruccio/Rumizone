from tkinter import *

def dentro():
    #Criação de Controles:
    class Application:
        def __init__(self, master=None):
            self.FrameMaster = Frame(master)
            self.FrameMaster.pack()
            self.msg = Label(self.FrameMaster, text="Conseguiu!")
            self.msg.pack()

            self.btn = Button(self.FrameMaster)
            self.btn["text"] = "Sair"
            self.btn["font"] = ("Calibri", "10")
            self.btn["width"] = 5
            self.btn["command"] = self.opa
            self.btn.pack()

        def opa(self):
            root.destroy()

    #Permite a utilização de Widgets
    root = Tk()

    #Construtor do método da Classe
    Application(root)

    #Exive a tela
    root.mainloop()
