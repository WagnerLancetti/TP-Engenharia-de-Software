import Pessoa

class Professor (Pessoa.Pessoa):
    def __init__(self, nome, idade, sexo, cpf, materias, atividades)
        super().__init__(nome,idade,sexo,cpf)
        self.__Materias = materias
        self.__Atividades = atividades
    
    def setMaterias(self,Materias):
        self.__Materias = Materias
    
    def setAtividades(self,Atividades):
        self.__Atividades = Atividades
    
    def getMaterias(self):
        return self.__Materias
    
    def getAtividades(self):
        return self.__Atividades
    
    def toString(self):
        if (self.getSexo == "Masculino"):
            return "Professor "+self.getNome()+", " +self.getIdade()+" anos. Leciona "+self.getMaterias()+ ". Realiza "+self.getAtividades()+" atividades."
        else:
            return "Professora "+self.getNome()+", " +self.getIdade()+" anos. Leciona "+self.getMaterias()+ ". Realiza "+self.getAtividades()+" atividades."