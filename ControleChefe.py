import Chefe as Chefe

class ControleProfessor():
    def __init__(self):
        self.Chefe = Chefe.Chefe()
    
    # Recebe os dados para registrar uma atividade
    def ValidarAtividades(self):
        criacaoDoTrabalho = True