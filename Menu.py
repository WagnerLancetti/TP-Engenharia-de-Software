from tkinter import *
import Controle as Controle
import MenuRegistro as MenuRegistro
import MenuValidacao as MenuValidacao
import Professor as Professor
import Chefe as Chefe


class Menu():
    def __init__(self):
        self.controle = Controle.Controle()
        
    def MenuVisao(self):
        self.mensagem3 = ""
        self.Professores = []
        self.Chefes = []
        Prof = Professor.Professor("Sofia da Costa Paiva",30,"Feminino","xxx.xxx.xxx-xx", "Ciência da Computação","Engenharia de Software","sofia@gmail.com", "1234", 1)
        Prof1 = Professor.Professor("Dárlinton Barbosa Feres Carvalho", 30, "Masculino", "zzz.zzz.zzz-zz", "Ciência da Computação", "Interação Humano Computador", "darlinton@gmail.com", "1234", 1)
        Chef = Chefe.Chefe("Daniel Luiz Alves Madeira", 30, "Masculino", "yyy.yyy.yyy-yy", "Ciência da Computação", "Computação gráfica", "daniel@gmail.com", "1234", 2)
        self.Professores.append(Prof)
        self.Professores.append(Prof1)
        self.Professores.append(Chef)
        self.Chefes.append(Chef)
        self.fontePadrao = ("Arial", "12")
        self.saida = True
        self.corBack = "#e9e9e9"
        while (self.saida):
            # Criação da Janela
            self.PMenu = Tk()
            self.PMenu.title("Menu Principal")
            #self.PMenu.geometry("700x450")
            self.PMenu.state('zoomed')
            self.PMenu['bg'] = self.corBack
            # Titulo
            self.Container1 = Frame(self.PMenu)
            self.Container1["pady"] = 5
            self.Container1['bg'] = self.corBack
            self.Container1.pack()
            self.tituloContainer1 = Label(self.Container1, text = "Login", bg = self.corBack)
            self.tituloContainer1["font"] = ("Arial", "30", "bold", "underline")
            self.tituloContainer1.pack()
            # Mensagem de Opções
            self.Container2 = Frame(self.PMenu)
            self.Container2["padx"] = 20
            self.Container2["pady"] = 20
            self.Container2['bg'] = self.corBack
            self.Container2.pack()
            self.mensagem =Label(self.Container2,text ="Email",bg =self.corBack)
            self.mensagem["font"] = ("Arial", "14")
            self.mensagem.pack()
            self.Email = Entry(self.Container2)
            self.Email["width"] = 30
            self.Email["font"] = self.fontePadrao
            self.Email.pack()
            # Opções
            self.Container3 = Frame(self.PMenu)
            self.Container3["padx"] = 20
            self.Container3["pady"] = 15
            self.Container3['bg'] = self.corBack
            self.Container3.pack()
            self.mensagem2 =Label(self.Container3,text ="Senha",bg =self.corBack)
            self.mensagem2["font"] = ("Arial", "14")
            self.mensagem2.pack()
            self.Senha = Entry(self.Container3)
            self.Senha["width"] = 30
            self.Senha["font"] = self.fontePadrao
            self.Senha.pack()

            # Botao de Confirmar
            self.Container4 = Frame(self.PMenu)
            self.Container4["padx"] = 20
            self.Container4['bg'] = self.corBack
            self.Container4.pack()
            self.botao = Button(self.Container4,text="Entrar")
            self.botao["width"] = 8
            self.botao["font"] = self.fontePadrao
            self.botao["command"] = self.Login # Controle
            self.botao.pack(side=LEFT)
            # Deixar a janela rodando sem parar

            self.Container5 = Frame(self.PMenu)
            self.Container5["padx"] = 20
            self.Container5["pady"] = 20
            self.Container5['bg'] = self.corBack
            self.Container5.pack()
            self.texto = Label(self.Container3,text = self.mensagem3,bg =self.corBack)
            self.texto["font"] = ("Arial", "14")
            self.texto["fg"] = "red"
            self.texto.pack()

            self.Container6 = Frame(self.PMenu)
            self.Container6["padx"] = 20
            self.Container6["pady"] = 50
            self.Container6["bg"] = self.corBack
            self.Container6.pack()
            self.decisao = Button(self.Container6)
            self.decisao["width"] = 8
            self.decisao["text"] = "Sair"
            self.decisao["font"] = self.fontePadrao
            self.decisao.bind("<Button-1>",self.Sair)
            self.decisao.pack()

            self.PMenu.mainloop()

    def Login(self):
        email = self.Email.get()
        valor = self.controle.Login(email, self.Senha.get(), self.Professores)
        if (valor == 1):
            self.PMenu.destroy()
            self.mensagem3 = ""
            idprof = self.controle.match(email, self.Professores)
            MenuRegistro.MenuRegistro().menu(self.Professores[idprof])
        elif (valor == 2):
            self.PMenu.destroy()
            self.mensagem3 = ""
            MenuValidacao.MenuValidacao().menu(self.Professores,self.Chefes)
        elif (valor == 3):
            self.Container5.destroy()
            self.PMenu.destroy()
            self.mensagem3 = "Nao foi possível fazer login. Campos Incorretos!"

    def Sair(self, event):
        self.PMenu.destroy()
        self.saida = False



TP = Menu()
TP.MenuVisao()