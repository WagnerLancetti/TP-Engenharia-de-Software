import Professor

class Chefe(Professor.Professor):
    def __init__(self,nome, idade, sexo, cpf, departamento, materias, email, senha, codTipo):
        super().__init__(nome,idade,sexo,cpf,departamento, materias, email, senha, 2)
    
    def validarAtividade(self,Professor,indice):
        Professor.getRegistro(indice).setStatus(2)

    def naoValidarAtividade(self,Professor,indice):
        Professor.getRegistro(indice).setStatus(0)