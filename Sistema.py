import RegistroBanca as RegistroBanca

class Sistema:
    def __init__(self):
        self.Registros = []
        self.__Validadas = 0
        self.__NaoValidadas = 0

    def setValidadas(self, validadas):
        self.__Validadas = validadas
    
    def setNaoValidadas(self,nvalidadas):
        self.__NaoValidadas = nvalidadas
    
    def getValidadas(self):
        return self.__Validadas
    
    def getNaoValidadas(self):
        return self.__NaoValidadas

    def registrarAtividade(self, curso, assunto, apresentador, duracao, data):
        registro = RegistroBanca.RegistroBanca(curso, assunto, apresentador, duracao, data)
        self.Registros.append(registro)
        
    def deletarAtividade(self,indice):
        del (self.Registros[indice])
        
    #def editarAtividade(self):
        #TODO

    def validarAtividade(self,indice):
        self.deletarAtividade(indice)
        self.setValidadas(self.getValidadas()+1)
        return "Atividade validada com sucesso!"

    def naoValidarAtividade(self,indice):
        self.deletarAtividade(indice)
        self.setNaoValidadas(self.getNaoValidadas()+1)
        return "Atividade não foi validada!"