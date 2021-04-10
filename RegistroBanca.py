# Classe de Registro de Banca de Defesa
class RegistroBanca:
    def __init__(self, curso, assunto, apresentador, avaliadores, data, status):
        self.__Curso = curso # Graduação, Mestrado, Doutorado
        self.__Assunto = assunto
        self.__Apresentador = apresentador
        self.__Avaliadores = avaliadores
        self.__Data = data
        self.__status = status # 0 = Nao validada // 1 = Em espera // 2 = Validada
    
    def setCurso(self, curso):
        self.__Curso = curso

    def setAssunto(self, assunto):
        self.__Assunto = assunto
    
    def setApresentador(self, apresentador):
        self.__Apresentador = apresentador
    
    def setAvaliadores (self, avaliadores):
        self.__Avaliadores = avaliadores
    
    def setData (self, data):
        self.__Data = data
    
    def setStatus (self, status):
        self.__status = status
    
    def getCurso (self):
        return self.__Curso

    def getAssunto(self):
        return self.__Assunto
    
    def getApresentador(self):
        return self.__Apresentador
    
    def getAvaliadores (self):
        return self.__Avaliadores
    
    def getData (self):
        return self.__Data
    
    def getStatus (self):
        return self.__status
    
    def toString(self):
        if (self.getStatus() == 0):
            return "Registro Banca de "+self.getCurso()+ ".\n Apresentador: "+self.getApresentador()+".\n Tema: "+self.getAssunto()+".\n Avaliadores: "+self.getAvaliadores()+".\n Data: "+self.getData()+".\n NÃO VALIDADA."
        elif (self.getStatus() == 1):
            return "Registro Banca de "+self.getCurso()+ ".\n Apresentador: "+self.getApresentador()+".\n Tema: "+self.getAssunto()+".\n Avaliadores: "+self.getAvaliadores()+".\n Data: "+self.getData()+".\n Atividade precisa de validação."
        elif (self.getStatus() == 2):
            return "Registro Banca de "+self.getCurso()+ ".\n Apresentador: "+self.getApresentador()+".\n Tema: "+self.getAssunto()+".\n Avaliadores: "+self.getAvaliadores()+".\n Data: "+self.getData()+".\n VALIDADA."