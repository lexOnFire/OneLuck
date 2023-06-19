import ttkbootstrap as ttk
from tkinter import messagebox
import random

numero_escolhido = random.randint(1, 10)
#funçao para checar se os numeros sao iguais
def enviar_numero():
    if entrada_numero.get() == str(numero_escolhido):
        label_numero["text"] = str(numero_escolhido)
        messagebox.showinfo("PARABENS", "Voce GANHOU")
    else:
        messagebox.showinfo("ERROU", "Voce PERDEU")
    
    entrada_numero.delete(0,ttk.END)
#funcao para cada botao representar 1 numero equivalente
def criar_botao_numero(numero):
    return ttk.Button(janela_numeros, text=str(numero), width=7, bootstyle="info", command=lambda: entrada_numero.insert(0, str(numero))) # type: ignore
#criar a janela
janela_numeros = ttk.Window(themename="vapor")
janela_numeros.title("oneLuck")
janela_numeros.geometry("380x230")
janela_numeros.resizable(width=False, height=False)
#as labels
label_titulo = ttk.Label(janela_numeros, text="NUMERO MISTERIO", font="Talkactive, 20")
label_titulo.place(x=55, y=0)

label_numero = ttk.Label(janela_numeros, text="?", font="Talkactive, 50")
label_numero.place(x=170, y=30)
#entrada
entrada_numero = ttk.Entry(janela_numeros)
entrada_numero.place(x=130, y=100)
#os botoes
btn_1 = criar_botao_numero(1)
btn_1.place(x=10, y=150)
btn_2 = criar_botao_numero(2)
btn_2.place(x=80, y=150)
btn_3 = criar_botao_numero(3)
btn_3.place(x=150, y=150)
btn_4 = criar_botao_numero(4)
btn_4.place(x=220, y=150)
btn_5 = criar_botao_numero(5)
btn_5.place(x=10, y=190)
btn_6 = criar_botao_numero(6)
btn_6.place(x=80, y=190)
btn_7 = criar_botao_numero(7)
btn_7.place(x=150, y=190)
btn_8 = criar_botao_numero(8)
btn_8.place(x=220, y=190)
btn_9 = criar_botao_numero(9)
btn_9.place(x=290, y=150)
btn_10 = criar_botao_numero(10)
btn_10.place(x=290, y=190)
btn_enviar = ttk.Button(janela_numeros, text="ENVIAR", command=enviar_numero)
btn_enviar.place(x=50, y=100)

janela_numeros.mainloop()


