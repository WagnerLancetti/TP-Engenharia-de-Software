import Professor as Professor

class ControleProfessor():
    def __init__(self):
        self.Professor = Professor.Professor()
    
    # Recebe os dados para registrar uma atividade
    def RegistrarAtividades(self):
        criacaoDoTrabalho = True