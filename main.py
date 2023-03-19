from tkinter import *
import tkinter.font as tkFont

#programa criado por Erick Sergio  dev


    
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
        self.checkvar1=IntVar()
        self.checkvar2=IntVar()
        self.checkvar3=IntVar()
        self.checkvar1.set(0)
        self.checkvar2.set(0)
        self.checkvar3.set(0)
        
        if self.checkvar1.get()==1:
            self.checkvar2.set(0)
        if self.checkvar2.get()==1:
            self.checkvar1.set(0)
        
        #posicionar os botoes e labels
        self.texto = Label(self.janela, text = "CALCULADORA DE S.NUMERICOS", font = self.fontStyle, bg="gray", fg="white")
        self.entrada = Entry(self.janela,width=50)
        self.binario = Checkbutton(self.janela, text="binario", bg="gray", padx=20, variable=self.checkvar1)
        self.hexa = Checkbutton(self.janela, text="hexadecimal", bg="gray", padx=20, variable=self.checkvar2)
        self.result = Label(self.janela, text="o resultado é", bg="gray")
        self.botao = Button(self.janela, text = 'CALCULAR', bg="black", fg="white", width=20 ,height=5, command=self.calcular )
        self.sair = Button(self.janela, text="SAIR ", bg="red", fg="white", width=20, height=5, command=self.quit)
        
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
        #self.botao.configure(background="white",fg='black')
        #vai mostrar o numero binario na tela
        if self.checkvar1.get()==1:
            self.checkvar2.set(0)
            print("binario marcado")
            self.decimal = int(self.entrada.get())
            self.decimal = int((self.decimal))
            self.binario2 = bin(self.decimal)
            self.fbin = self.binario2.replace("0b","")
            self.result.config(text=self.fbin, fg="blue") 
            
            
        if  self.checkvar2.get()==1:
            self.checkvar2.set(0)
            print("hexadecimal marcado")
            self.decimal = int(self.entrada.get())
            self.decimal = int((self.decimal))
            self.hexa = hex(self.decimal)
            self.fhex = self.hexa.replace("0x","")
            self.result.config(text=self.fhex, fg="blue") 
            
        if self.checkvar3.get()==1:
            print("octal acionado")
            self.decimal = int(self.entrada.get())
            self.decimal = int((self.decimal))
            self.octal = oct(self.decimal)
            self.foctal = self.octal.replace("0o","")
            self.result.config(text=self.foctal, fg="blue") 
            
            
        if self.checkvar1.get()==0 and self.checkvar2.get()==0 and self.checkvar3.get()==0:
            self.result.config(text="marque alguma opçao", fg="red")
            print("binario desmarcado")
            
    def quit(self):
        self.janela.destroy()
        
        



app=Calculadora()
