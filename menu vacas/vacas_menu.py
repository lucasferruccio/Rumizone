from customtkinter import *
from funcApp import *
from crud import *

class btsvacas:
    def __init__(self,frame):
        def janela_vaca(info):

            #Atualiza os dados das vacas. OBS: Só atualiza se o usuario preencher todos as caixas
            def atualizar():
                atualizar_vaca(info[0], entry_manejo.get(), entry_comida.get(), entry_peso.get(),
                            entry_comp.get(), entry_vacinas.get(), entry_saude.get())
                
            telavaca = CTkToplevel()
            telavaca.title("vacas")
            telavaca.geometry("900x270")
            fundo = CTkFrame(telavaca)
            fundo.grid(row = 0, column = 0)

            #Primeira linha, informando oq é cada coluna

            label_col1 = CTkLabel(fundo,width=300, text= "Informação", height=30)
            label_col1.grid(row=0, column = 0)
            label_col2 = CTkLabel(fundo,width=300, text= "Atual", height=30)
            label_col2.grid(row=0, column = 1)
            label_col3 = CTkLabel(fundo,width=300, text= "Novos Valores", height=30)
            label_col3.grid(row=0, column = 2)

            #Exibe o codigo de identficação da vaca na tela

            label_cod = CTkLabel(fundo,width=300, text= "Código de Identificação:", height=30)
            label_cod.grid(row=1, column = 0)
            entry_cod = CTkLabel(fundo,width=300, text= info[0], height=30)
            entry_cod.grid(row=1, column = 1)

            #Exibe como se encontra o estado de manejo da vaca na tela

            label_manejo1 = CTkLabel(fundo,width=300, text= "Manejo:", height=30)
            label_manejo1.grid(row=2, column = 0)
            label_manejo2 = CTkLabel(fundo,width=300, text= info[2], height=30)
            label_manejo2.grid(row=2, column = 1)
            entry_manejo = CTkEntry(fundo, placeholder_text=info[2])
            entry_manejo.grid(row=2, column = 2)

            #Exibe a quantidade de comida consumida pela vaca diariamente na tela

            label_comida1 = CTkLabel(fundo,width=300, text= "Comida(kg):", height=30)
            label_comida1.grid(row=3, column = 0)
            label_comida2 = CTkLabel(fundo,width=300, text= info[3], height=30)
            label_comida2.grid(row=3, column = 1)
            entry_comida = CTkEntry(fundo, placeholder_text=str(info[3]))
            entry_comida.grid(row=3, column = 2)

            #Exibe o peso da vaca na tela

            label_peso1 = CTkLabel(fundo,width=300, text= "Peso(kg):", height=30)
            label_peso1.grid(row=4, column = 0)
            label_peso2 = CTkLabel(fundo,width=300, text= info[4], height=30)
            label_peso2.grid(row=4, column = 1)
            entry_peso = CTkEntry(fundo, placeholder_text=str(info[4]))
            entry_peso.grid(row=4, column = 2)

            #Exibe o estado de saúde da vaca na tela

            label_saude1= CTkLabel(fundo,width=300, text= "Saúde:", height=30)
            label_saude1.grid(row=5, column = 0)
            label_saude2 = CTkLabel(fundo,width=300, text= info[7], height=30)
            label_saude2.grid(row=5, column = 1)
            entry_saude = CTkEntry(fundo, placeholder_text=info[7])
            entry_saude.grid(row=5, column = 2)

            #Exibe o estado de comportamento da vaca na tela

            label_comp1 = CTkLabel(fundo,width=300, text= "Comportamento:", height=30)
            label_comp1.grid(row=6, column = 0)
            label_comp2 = CTkLabel(fundo,width=300, text= info[5], height=30)
            label_comp2.grid(row=6, column = 1)
            entry_comp = CTkEntry(fundo, placeholder_text=info[5])
            entry_comp.grid(row=6, column = 2)

            #Exibe o estado da vaca em relação as vacinas da vaca na tela

            label_vacinas1 = CTkLabel(fundo,width=300, text= "Vacina:", height=30)
            label_vacinas1.grid(row=7, column = 0)
            label_vacinas2 = CTkLabel(fundo,width=300, text= info[6], height=30)
            label_vacinas2.grid(row=7, column = 1)
            entry_vacinas = CTkEntry(fundo, placeholder_text=info[6])
            entry_vacinas.grid(row=7, column = 2)

            #Exibe o botão de atualizar informações da vaca na tela

            btn_atualizar = CTkButton(fundo,text=("Atualizar"), command=atualizar)
            btn_atualizar.grid(row=8, column = 1)
            

        self.ids_vacas = [id[0] for id in select("id_vaca", "vacas")]
        for aux1 in range(len(self.ids_vacas)):
            info  = botao_vaca(self.ids_vacas[aux1])
            info_completa = info_vaca(info[0])
            btvaca = CTkButton(frame,text=("Identificação: " + str(info[0]) + "\n" + "Comportamento: " + info[1] + "\n" + "Saude: " + info[2]), command=lambda aux2 = info_completa: janela_vaca(aux2))
            btvaca.grid(row=0, column = aux1)
