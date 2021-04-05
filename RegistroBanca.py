# Classe de Registro de Banca de Defesa
class RegistroBanca:
    def __init__(self, curso, assunto, apresentador, duracao, data):
        self.__Curso = curso # Graduação, Mestrado, Doutorado
        self.__Assunto = assunto
        self.__Apresentador = apresentador
        self.__Duracao = duracao
        self.__Data = data
    
    def setCurso(self, curso):
        self.__Curso = curso

    def setAssunto(self, assunto):
        self.__Assunto = assunto
    
    def setApresentador(self, apresentador):
        self.__Apresentador = apresentador
    
    def setDuracao (self, duracao):
        self.__Duracao = duracao
    
    def setData (self, data):
        self.__Data = data
    
    def getCurso (self):
        return self.__Curso

    def getAssunto(self):
        return self.__Assunto
    
    def getApresentador(self):
        return self.__Apresentador
    
    def getDuracao (self):
        return self.__Duracao
    
    def getData (self):
        return self.__Data
    
    def toString(self):
        return "Registro: Banca de "+self.getCurso()+ " defendida por "+self.getApresentador()+" sobre o assunto "+self.getAssunto()+". Apresentação durou "+self.getDuracao()+" no dia "+self.getData()+"."