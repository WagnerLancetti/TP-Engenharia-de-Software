import Pessoa

class Chefe(Pessoa.Pessoa):
    def __init__(self, nome, idade, sexo, cpf, departamento)
        super().__init__(nome,idade,sexo,cpf)
        self.__Departamento = departamento
    
    def setDepartamento (self, departamento):
        self.__Departamento = departamento
    
    def getDepartamento (self):
        return self.__Departamento

    def toString(self):
        return "Chefe "+self.getNome()+", " +self.getIdade()+" anos. Trabalha no departamento de "+self.getDepartamento()+ "."