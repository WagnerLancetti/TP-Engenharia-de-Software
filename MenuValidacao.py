from tkinter import *
import ControleValidacao as ControleValidacao


class MenuValidacao:
    def __init__(self):
        self.controleVal = ControleValidacao.ControleValidacao()
        
    def menu(self, Professores, Chefe):
        self.corBack = "#e9e9e9"
        self.fontepadrao = ("Arial", "12")
        self.menuVal = True
        self.Chefe = Chefe # Lista de Chefes
        self.Professores = Professores # Lista de todos os professores
        self.Emails = []
        while (self.menuVal): # Visao
            self.Janela = Tk()
            self.Janela.title("Menu Validação")
            #self.Janela.geometry("700x450")
            self.Janela.state('zoomed')
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
            self.Container2["pady"] = 10
            self.Container2['bg'] = self.corBack
            self.Container2.pack()
            self.tituloContainer2 = Label(self.Container2, text = "Qual atividade deseja validar?", bg = self.corBack, font = ("Arial","15"))
            self.tituloContainer2.pack()
            # Opções
            self.Container3 = Frame(self.Janela)
            self.Container3["padx"] = 20
            self.Container3["pady"] = 10
            self.Container3['bg'] = self.corBack
            self.Container3.pack()
            self.opcao = IntVar()
            i = 0
            j = 0
            cont = 0
            while (j < self.controleVal.quantidadeProfessores(self.Professores)): # Percorro a lista de professores
                i = 0
                while (i < self.controleVal.tamLista(self.Professores[j])): # Percorro a lista de registro de cada professor
                    Radiobutton(self.Container3, text = self.controleVal.printRegistro(self.Professores[j], i), variable = self.opcao, value = cont+1, bg = self.corBack, font = self.fontepadrao).grid(row = cont, column = 0)
                    self.Emails.append(self.Professores[j].getEmail())
                    Button(self.Container3, width = 8, font = self.fontepadrao, text = "Validar", fg = "green", command = self.menuDecisao).grid(row = cont, column = 1)
                    Button(self.Container3, width = 8, font = self.fontepadrao, text = "Não Validar", fg = "red", command = self.menuDecisao2).grid(row = cont, column = 2)
                    cont = cont + 1
                    i = i + 1
                j = j + 1
            #Botao de Confirmar
            '''
            self.Container4 = Frame(self.Janela)
            self.Container4["padx"] = 20
            self.Container4['bg'] = self.corBack
            self.Container4.pack()
            self.decisao = Button(self.Container4)
            self.decisao["width"] = 8
            self.decisao["text"] = "Validar"
            self.decisao["fg"] = "green"
            self.decisao["font"] = self.fontepadrao
            self.decisao.bind("<Button-1>",self.menuDecisao)
            #self.decisao["command"] = self.menuDecisao # Controle
            self.decisao.grid(row = 0, column = 0)

            self.decisao2 = Button (self.Container4)
            self.decisao2["width"] = 8
            self.decisao2["padx"] = 20
            self.decisao2["text"] = "Não Validar"
            self.decisao2["fg"] = "red"
            self.decisao2["font"] = self.fontepadrao
            self.decisao2.bind("<Button-1>",self.menuDecisao2)
            #self.decisao2["command"] = self.menuDecisao2 # Controle
            self.decisao2.grid(row = 0, column = 3)
            '''
            # Botão de sair
            self.Container5 = Frame(self.Janela)
            self.Container5["padx"] = 20
            self.Container5["pady"] = 20
            self.Container5["bg"] = self.corBack
            self.Container5.pack()
            self.decisao3 = Button(self.Container5)
            self.decisao3["width"] = 8
            self.decisao3["text"] = "Sair"
            self.decisao3["font"] = self.fontepadrao
            self.decisao3.bind("<Button-1>",self.Sair)
            #self.decisao3["command"] = self.Sair # Controle
            self.decisao3.pack()
            # Deixar a janela rodando
            self.Janela.mainloop()
    
    def menuDecisao(self):
        self.Janela.destroy()
        idprof = self.controleVal.match(self.Professores,self.Emails[self.opcao.get()-1])
        idatv = self.controleVal.idAtividade(idprof,self.opcao.get()-1,self.Professores)
        self.controleVal.ValidarAtividades(self.Professores[idprof], self.Chefe[0], idatv)
            
    def menuDecisao2(self):
        self.Janela.destroy()
        idprof = self.controleVal.match(self.Professores,self.Emails[self.opcao.get()-1])
        idatv = self.controleVal.idAtividade(idprof,self.opcao.get()-1,self.Professores)

        self.controleVal.naoValidarAtividade(self.Professores[idprof], self.Chefe[0], idatv)

    def Sair(self,event):
        self.Janela.destroy()
        self.menuVal = False