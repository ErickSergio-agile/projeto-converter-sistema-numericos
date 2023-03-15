from tkinter import *
import tkinter.font as tkFont



    
#especificaçoes da tela e cores
class Calculadora():
    def __init__(self):
        
        self.janela = Tk()
        #importar fontes
        self.fontStyle = tkFont.Font(family="Lucida Grande", size=15)
        self.janela.configure(bg="gray")
        self.janela.title("CALCULADORA SISTEMA NUMERICO")
        self.janela.geometry("400x700")

        v= 0
        
        #posicionar os botoes e labels
        self.texto = Label(self.janela, text = "CALCULADORA DE S.NUMERICOS", font = self.fontStyle, bg="gray", fg="white")
        self.entrada = Entry(self.janela,width=50)
        self.binario = Radiobutton(self.janela, text="binario", bg="gray", padx=20, value=v)
        self.hexa = Radiobutton(self.janela, text="hexadecimal", bg="gray", padx=20, value=v)
        self.result = Label(self.janela, text="o resultado é", bg="gray")
        self.botao = Button(self.janela, text = 'CALCULAR', bg="black", fg="white", width=20 ,height=5, command=self.calcular )
        
        # todos os enpacotamento
        self.texto.pack(side="top")
        self.entrada.pack()
        self.binario.pack()
        self.hexa.pack()
        self.result.pack(pady=200)
        self.botao.pack(side = "bottom", pady=50)
        
        #executa o codigo
        self.janela.mainloop()
        

    def calcular(self):
        self.botao.configure(background="white",fg='black')
        self.result.config(text="000000")



app=Calculadora()









