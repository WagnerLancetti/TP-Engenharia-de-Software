from tkinter import *
import ControleValidacao as ControleValidacao


class MenuValidacao:
    def __init__(self):
        self.corBack = "#e9e9e9"
        self.fontepadrao = ("Arial", "20")
        self.menuVal = True
        self.controleVal = ControleValidacao.ControleValidacao()
    def menu(self, sistema):
        self.menuLoca = True
        self.sistema = sistema
        self.mensagem2 = ""
        while (self.menuLoca): # Visao
            self.Janela = Tk()
            self.Janela.title("Menu Locacao")
            self.Janela.geometry("700x450")
            self.Janela['bg'] = self.corBack
            # Título
            self.Container1 = Frame(self.Janela)
            self.Container1["pady"] = 10
            self.Container1['bg'] = self.corBack
            self.Container1.pack()
            self.tituloContainer1 = Label(self.Container1,text = "Validação de Atividades", bg = self.corBack)
            self.tituloContainer1["font"] = ("Arial","30","bold","underline")
            self.tituloContainer1.pack()
            # Mensagem
            self.Container2 = Frame(self.Janela)
            self.Container2["padx"] = 20
            self.Container2['bg'] = self.corBack
            self.Container2.pack()
            self.tituloContainer2 = Label(self.Container2, text = "Qual atividade deseja validar?", bg = self.corBack, font = ("Arial","15"))
            self.tituloContainer2.pack()
            # Opções
            self.Container3 = Frame(self.Janela)
            self.Container3["padx"] = 20
            self.Container3['bg'] = self.corBack
            self.Container3.pack()
            self.opcao = IntVar()
            i = 0
            while (i < len(self.sistema.Registros)):
                Radiobutton(self.Container3, text = self.sistema.Registros[i].toString(), variable = self.opcao, value = i+1, bg = self.corBack, font = self.fontepadrao).pack()
                i = i + 1
            #Botao de Confirmar
            self.Container4 = Frame(self.Janela)
            self.Container4["padx"] = 20
            self.Container4['bg'] = self.corBack
            self.Container4.pack()
            self.decisao = Button(self.Container4)
            self.decisao["width"] = 8
            self.decisao["text"] = "Confirmar"
            self.decisao["font"] = self.fontepadrao
            self.decisao["command"] = self.Validacao # Controle
            self.decisao.pack()
            # Botão de sair
            self.Container5 = Frame(self.Janela)
            self.Container5["padx"] = 20
            self.Container5["bg"] = self.corBack
            self.Container5.pack()
            self.decisao2 = Button(self.Container5)
            self.decisao2["width"] = 8
            self.decisao2["text"] = "Sair"
            self.decisao2["font"] = self.fontepadrao
            self.decisao2["command"] = self.Sair # Controle
            self.decisao2.pack()
            # Deixar a janela rodando
            self.Janela.mainloop()
    
    def Validacao(self):
        self.controleVal.ValidarAtividades(self.sistema, self.opcao.get()-1)
        self.Janela.destroy()

    def Sair(self):
        self.Janela.destroy()
        self.menuLoca = False