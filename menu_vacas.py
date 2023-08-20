from customtkinter import*
from funcApp import *
from crud import *

tela = CTk()
tela.geometry("1200x700")
frame = CTkFrame(tela, width=1200, height= 700)
frame.grid(row = 0, column = 0)
def janela_vaca(info):
    telavaca = CTkToplevel()
    telavaca.title("vacas")
    telavaca.geometry("300x600")
    fundo = CTkFrame(telavaca,width=300, height= 600)
    fundo.grid(row = 0, column = 0)
    text_cod = CTkLabel(fundo,width=300, text= "Código de Identificação : " + str(info[0]), height=30)
    text_cod.grid(row=1, column = 0)
    text_manejo = CTkLabel(fundo,width=300, text= "Manejo : " + info[2], height=30)
    text_manejo.grid(row=2, column = 0)
    text_comida = CTkLabel(fundo,width=300, text= "Comida(kg) : " + str(info[3]), height=30)
    text_comida.grid(row=3, column = 0)
    text_peso = CTkLabel(fundo,width=300, text= "Peso(kg) : " + str(info[4]), height=30)
    text_peso.grid(row=4, column = 0)
    text_saude = CTkLabel(fundo,width=300, text= "Saúde : " + info[5], height=30)
    text_saude.grid(row=5, column = 0)
    text_comp = CTkLabel(fundo,width=300, text= "Comportamento : " + info[6], height=30)
    text_comp.grid(row=6, column = 0)
    text_vacinas = CTkLabel(fundo,width=300, text= "Vacina : " + info[7], height=30)
    text_vacinas.grid(row=7, column = 0)

ids_vacas = [id[0] for id in select("id_vaca", "vacas")]
for aux1 in range(len(ids_vacas)):
    info  = botao_vaca(ids_vacas[aux1])
    info_completa = info_vaca(info[0])
    btvaca = CTkButton(frame,text=("Identificação: " + str(info[0]) + "\n" + "Comportamento: " + info[1] + "\n" + "Saude: " + info[2]), command=lambda aux2 = info_completa: janela_vaca(aux2))
    btvaca.grid(row=0, column = aux1)
tela.mainloop()
