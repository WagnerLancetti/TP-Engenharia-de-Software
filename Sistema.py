import RegistroBanca as RegistroBanca

class Sistema:
    def __init__(self):
        self.Registros = []

    def registrarAtividade(self, curso, assunto, apresentador, duracao, data):
        registro = RegistroBanca.RegistroBanca(curso, assunto, apresentador, duracao, data)
        self.Registros.append(registro)
        
    #def deletarAtividade(self):
        #TODO
    #def editarAtividade(self):
        #TODO
    #def validarAtividade(self):
        #TODO
    #def naoValidarAtividade(self):
        #TODO