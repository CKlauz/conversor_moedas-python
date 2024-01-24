import tkinter as tk
import requests
import json
import customtkinter
from api import siglas_moedas

#Cores
azul = '#3153de'
branco = '#ffffff'

#Configs|Tema

#Funções
customtkinter.set_appearance_mode('system')

def entrada_val(valor):
        entrada = float(valor_convert.get())
        valor_final = entrada * valor
        return valor_final

def inserir_texto(texto, simb):
        text_convert.configure(state='normal')
        text_convert.delete('0.0', 'end')
        text_convert.insert('0.0', f'{simb}{texto:.2f}')
        text_convert.configure(state='disabled')

def realizar_convercao():
        cont = 0
        moeda_de = ''
        moeda_para = ''
        simbolo = ''
        moe_d = como_box_1.get()
        moe_p = como_box_2.get()
        
        for l in moe_d: #Pegar apenas os 3 primeiros caracteres das Moeda
                moeda_de = moeda_de + l
                cont += 1
                if cont >= 3:
                        break
        cont = 0
        for l in moe_p: #Pegar apenas os 3 primeiros caracteres das Moeda
                moeda_para = moeda_para + l
                cont += 1
                if cont >= 3:
                        break
        
        if moeda_para == 'USD' or moeda_para =='ARS':
                simbolo = '$'
        elif moeda_para == 'BRL':
                simbolo = 'R$'
        elif moeda_para == 'EUR':
                simbolo == 'Є'
        
        resquisicao = requests.get(f'https://economia.awesomeapi.com.br/last/{moeda_de}-{moeda_para}')
        resquisicao = resquisicao.json()
        cotacao_i = float(resquisicao[moeda_de + moeda_para]['bid'])
        
        cotacao_final = entrada_val(cotacao_i)
        inserir_texto(cotacao_final, simbolo)
        
      

#principal Janela tkinter
window = customtkinter.CTk()
window.title('Conversor')
window.geometry('400x400')
window.resizable(height=False, width=False)


#frames
frm_top = customtkinter.CTkFrame(
        window,
        width=340,
        height=70,
)
frm_top.place(x=0, y=0)
frm_mid = customtkinter.CTkFrame(window,
        width=340,
        height=120,
)
frm_mid.place(x=0, y=70)
frm_convert = customtkinter.CTkFrame(
        window,
        width=340,
        height=120,
)
frm_convert.place(x=0, y=190)
frm_bot = customtkinter.CTkFrame(
        window,
        width=340,
        height=90,
)
frm_bot.place(x=0, y=310)


#Labels
label_title = customtkinter.CTkLabel(
        frm_top,
        text='Conversor de moedas',
        font=('calibri', 30, 'bold'),
        text_color=branco,
)

text_cm = customtkinter.CTkLabel(
        frm_convert,
        text='De:',
        font=('calibri', 12, 'bold'),  
        text_color=branco,        
)
text_cm_2 = customtkinter.CTkLabel(
        frm_convert,
        text='Para:',
        font=('calibri', 12, 'bold'),
        text_color=branco,
)
#textos
text_convert = customtkinter.CTkTextbox(
        frm_mid,
        font=('calibri', 30, 'bold'),
        width=150,
        height=100,
        border_spacing=10,
        state='disabled',
        text_color=branco
)
#entrada de valores
valor_convert = customtkinter.CTkEntry(
        frm_convert,
        width=140,
        height=30,
        font=('calibri', 20, 'bold'),
        text_color=branco,
        placeholder_text='Ex:10.50'
)
#Botão 
btn_convert = customtkinter.CTkButton(
        frm_bot,
        text='Converter',
        height=45,  
        font=('calibri', 20, 'bold'),
        fg_color=azul,
        text_color=branco,
        command=realizar_convercao
)
#Como box
como_box_1 = customtkinter.CTkComboBox(
        frm_convert,
        values=siglas_moedas,
        font=('calibri', 15, 'bold'),
        dropdown_font=('calibri', 12, 'bold'),
        width=120,
        text_color=branco
)
como_box_1.set("BRL")
como_box_2 = customtkinter.CTkComboBox(
        frm_convert,
        values=siglas_moedas,
        font=('calibri', 15, 'bold'),
        dropdown_font=('calibri', 12, 'bold'),
        width=120,
        text_color=branco
)
como_box_2.set("USD")

#Pos dos widgets por frames

#Frame |TOPO
label_title.place(x=20, y=15,)

#Frame |MID
text_convert.place(relx=0.27, rely=0.1)

#Frame |CONVERTER
como_box_1.place(x=10, y=30)
como_box_2.place(x=170, y=30)
text_cm.place(x=15, y=8)
text_cm_2.place(x=175, y=8)
btn_convert.place(x=90, y=10)
valor_convert.place(x=90, y=80)

window.mainloop()