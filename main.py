from tkinter import *
import tkinter.font as tkFont



    
#especificaçoes da tela e cores
janela = Tk()
janela.configure(bg="gray")
janela.title("CALCULADORA SISTEMA NUMERICO")
janela.geometry("800x600")

#importar fontes
fontStyle = tkFont.Font(family="Lucida Grande", size=20)

def calcular():
    botao.configure(background="white",fg='black')


#posicionar os botoes e labels
texto = Label(janela, text = "CALCULADORA DE SISTEMA NUMERICOS DE MAQUINA", font = fontStyle)
texto.pack(side="top")

entrada = Entry(janela,width=50)
entrada.pack()

botao = Button(janela, text = 'CALCULAR', bg="black", fg="white", width=20 ,height=5, command=calcular)
botao.pack(side = "bottom")















janela.mainloop()