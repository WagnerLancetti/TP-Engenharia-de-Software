from tkinter import *
import ControleRegistro as ControleRegistro

class MenuRegistro:
    def __init__(self):
        self.controleReg = ControleRegistro.ControleRegistro()
        
    def menu(self,Professor):
        self.corBack = "#e9e9e9"
        self.fontePadrao = ("Arial", "12")
        self.menuReg = True
        self.Professor = Professor
        self.mensagem2 = ""
        while (self.menuReg):
            # Janela Principal
            self.Janela = Tk()
            self.Janela.title("Menu de Registro")
            #self.Janela.geometry("700x450")
            self.Janela.state('zoomed')
            self.Janela['bg'] = self.corBack
            # Título
            self.Container1 = Frame(self.Janela)
            self.Container1["pady"] = 10 # Distancia do container no eixo y
            self.Container1['bg'] = self.corBack
            self.Container1.pack()
            self.tituloContainer1 = Label(self.Container1, text = "Menu de Registro",bg = self.corBack)
            self.tituloContainer1["font"] = ("Arial", "30", "bold", "underline")
            self.tituloContainer1.pack()
            # Mensagem para o usuário
            self.Container2 = Frame(self.Janela) # Mensagem para o usuário
            self.Container2["padx"] = 20 # Distancia do container no eixo x
            self.Container2['bg'] = self.corBack
            self.Container2.pack()
            self.tituloContainer2 = Label(self.Container2,bg = self.corBack, text = "O que voce deseja fazer?",font = self.fontePadrao)
            self.tituloContainer2["font"] = ("Arial", "12")
            self.tituloContainer2.pack(side=LEFT)
            # Opções para o usuário
            self.Container3 = Frame(self.Janela) # Opcoes que o usuario pode fazer
            self.Container3["padx"] = 20 # Distancia do container no eixo x
            self.Container3["pady"] = 10
            self.Container3['bg'] = self.corBack
            self.Container3.pack()
            self.opcao = StringVar()
            self.opcao1 = ["Voltar para o Menu Principal","Registrar participação em bancas de defesa", "Registrar orientação de projetos de iniciação científica", "Registrar emissão de parecer","Registrar publicação de artigos científicos", "Registrar participação em eventos científicos", "Registrar organização de eventos científicos"]
            self.opcao.set(self.opcao1[0])
            OptionMenu(self.Container3, self.opcao,*self.opcao1).pack()
            # Botão de Confirmar
            self.Container4 = Frame(self.Janela) # Botao de escolha
            self.Container4["padx"] = 40 # Distancia do container no eixo x
            self.Container4["pady"] = 10
            self.Container4['bg'] = self.corBack
            self.Container4.pack()
            self.decisao = Button(self.Container4)
            self.decisao["text"] = "Confirmar"
            self.decisao["font"] = self.fontePadrao
            self.decisao["width"] = 8
            self.decisao.bind("<Button-1>",self.menuControle)
            self.decisao.pack(side=LEFT)
            # Container para mostrara  resposta
            self.Container5 = Frame(self.Janela)
            self.Container5["padx"] = 20
            self.Container5["bg"] = self.corBack
            self.Container5.pack()
            self.tituloContainer5 = Label(self.Container5, text = self.mensagem2,bg = self.corBack, font = self.fontePadrao)
            self.tituloContainer5.pack()
            # Manter a janela rodando
            self.Janela.mainloop()
    
    def menuRegistrarAtividade(self):
        # Limpa os titulos e o menu de opção
        self.tituloContainer5.destroy()
        self.Container2.destroy()
        self.Container3.destroy()
        self.Container4.destroy()
        # Titulo
        self.Container2 = Frame(self.Janela)
        self.Container2["padx"] = 20
        self.Container2['bg'] = self.corBack
        self.Container2.pack()
        self.tituloContainer2 = Label(self.Container2, text = "Registrar participação em bancas de defesa \n",bg = self.corBack)
        self.tituloContainer2["font"] = ("Arial", "12")
        self.tituloContainer2.pack()
        # Opções
        self.Container3 = Frame(self.Janela) # Placa
        self.Container3["padx"] = 20
        self.Container3['bg'] = self.corBack
        self.Container3.pack()
        self.valor = IntVar()
        Radiobutton(self.Container3, text = "Graduação", variable = self.valor, value = 1, bg = self.corBack,font = ("Arial","12")).pack()
        Radiobutton(self.Container3, text = "Mestrado", variable = self.valor, value = 2, bg = self.corBack,font = ("Arial","12")).pack()
        Radiobutton(self.Container3, text = "Doutorado", variable = self.valor, value = 3, bg = self.corBack,font = ("Arial","12")).pack()
        # Campo Assunto apresentado
        self.Container4 = Frame(self.Janela) # Marca
        self.Container4["padx"] = 20
        self.Container4['bg'] = self.corBack
        self.Container4.pack()
        self.tituloContainer4 = Label(self.Container4, text ="Assunto apresentado           ", font = self.fontePadrao,bg = self.corBack)
        self.tituloContainer4.grid(row = 0, column = 0)
        self.assunto = Entry(self.Container4)
        self.assunto["width"] = 30
        self.assunto["font"] = self.fontePadrao
        self.assunto.grid(row = 0, column = 1)
        # Campo Nome do apresentador
        self.Container5 = Frame(self.Janela) # Cor
        self.Container5["padx"] = 20
        self.Container5['bg'] = self.corBack
        self.Container5.pack()
        self.tituloContainer5 = Label(self.Container5, text ="Nome do(a) Apresentador(a)", font = self.fontePadrao,bg = self.corBack)
        self.tituloContainer5.grid(row = 1, column = 0)
        self.apresentador = Entry(self.Container5)
        self.apresentador["width"] = 30
        self.apresentador["font"] = self.fontePadrao
        self.apresentador.grid(row = 1, column = 1)
        # Campo Duração da apresentação
        self.Container6 = Frame(self.Janela) # Modelo
        self.Container6["padx"] = 20
        self.Container6['bg'] = self.corBack
        self.Container6.pack()
        self.tituloContainer6 = Label(self.Container6, text ="Avaliadores                 ", font = self.fontePadrao,bg = self.corBack)
        self.tituloContainer6.grid(row = 2, column = 0)
        self.avaliadores = Entry(self.Container6)
        self.avaliadores["width"] = 30
        self.avaliadores["font"] = self.fontePadrao
        self.avaliadores.grid(row = 2, column = 1)
        # Campo Data da defesa
        self.Container7 = Frame(self.Janela) # Ano
        self.Container7["padx"] = 20
        self.Container7['bg'] = self.corBack
        self.Container7.pack()
        self.tituloContainer7 = Label(self.Container7, text ="Data que ocorreu a defesa    ", font = self.fontePadrao,bg = self.corBack)
        self.tituloContainer7.grid(row = 3, column = 0)
        self.data = Entry(self.Container7)
        self.data["width"] = 30
        self.data["font"] = self.fontePadrao
        self.data.grid(row = 3, column = 1)
        # Botao de confirmação
        self.Container8= Frame(self.Janela)
        self.Container8["padx"] = 20
        self.Container8["pady"] = 10
        self.Container8['bg'] = self.corBack
        self.Container8.pack()
        self.decisao = Button(self.Container8)
        self.decisao["text"] = ("Confirmar")
        self.decisao["width"] = 8
        self.decisao["font"] = self.fontePadrao
        self.decisao.bind("<Button-1>",self.menuVerificaRegistro)
        self.decisao.pack(side=LEFT)
    
    def menuVerificaRegistro(self, event):
        self.decisao.destroy()
        self.mensagem2 = ""
        self.mensagem2 = self.controleReg.RegistrarAtividades(self.valor.get(), self.assunto.get(), self.apresentador.get(), self.avaliadores.get(),self.data.get(), self.Professor)
        self.Janela.destroy()

    def menuControle (self, event):
        verifica = self.controleReg.decisao(self.opcao.get())
        if (verifica == 0):
            self.Janela.destroy()
            self.menuReg = False
        elif (verifica == 1):
            self.menuRegistrarAtividade()