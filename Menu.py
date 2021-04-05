from tkinter import *
import Sistema as Sistema
import MenuRegistro as MenuRegistro



class Menu():
    def __init__(self):
        self.sistema = Sistema.Sistema()
    def MenuVisao(self):
        self.fontepadrao = ("Arial", "10")
        self.saida = True
        self.corBack = "#e9e9e9"
        while (self.saida):
            # Criação da Janela
            self.PMenu = Tk()
            self.PMenu.title("Menu Principal")
            self.PMenu.geometry("700x450")
            self.PMenu['bg'] = self.corBack
            self.PMenu.resizable(0,0)
            # Titulo
            self.Container1 = Frame(self.PMenu)
            self.Container1["pady"] = 5
            self.Container1['bg'] = self.corBack
            self.Container1.pack()
            self.tituloContainer1 = Label(self.Container1, text = "Menu Principal", bg = self.corBack)
            self.tituloContainer1["font"] = ("Arial", "30", "bold", "underline")
            self.tituloContainer1.pack()
            # Mensagem de Opções
            self.Container2 = Frame(self.PMenu)
            self.Container2["padx"] = 20
            self.Container2['bg'] = self.corBack
            self.Container2.pack()
            self.mensagem =Label(self.Container2,text ="\nMarque o que deseja fazer: \n",bg =self.corBack)
            self.mensagem["font"] = ("Arial", "15")
            self.mensagem.pack(side=LEFT)
            # Opções
            self.Container3 = Frame(self.PMenu)
            self.Container3["padx"] = 20
            self.Container3['bg'] = self.corBack
            self.Container3.pack()
            self.valor = IntVar()
            Radiobutton(self.Container3, text = "Sair do Programa", variable = self.valor, value = 1, bg = self.corBack,font = ("Arial","12")).pack()
            Radiobutton(self.Container3, text = "Registrar Atividade", variable = self.valor, value = 2, bg = self.corBack,font = ("Arial","12")).pack()
            Radiobutton(self.Container3, text = "Validar Atividade", variable = self.valor, value = 3, bg = self.corBack,font = ("Arial","12")).pack()
            # Botao de Confirmar
            self.Container4 = Frame(self.PMenu)
            self.Container4["padx"] = 20
            self.Container4['bg'] = self.corBack
            self.Container4.pack()
            self.botao = Button(self.Container4,text="Confirmar")
            self.botao["width"] = 8
            self.botao["font"] = self.fontepadrao
            self.botao["command"] = self.decisao # Controle
            self.botao.pack(side=LEFT)
            # Deixar a janela rodando sem parar
            self.PMenu.mainloop()

    def decisao(self): #Controle
        if (self.valor.get() == 1):
            self.saida = False
            self.PMenu.destroy() # Visao
        elif (self.valor.get() == 2):
            self.PMenu.destroy()
            MenuRegistro.MenuRegistro().menu(self.sistema)
 #       elif (self.valor.get() == 3):
            # Entrar em Validação

TP = Menu()
TP.MenuVisao()