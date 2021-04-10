import Pessoa
import RegistroBanca as RegistroBanca

class Professor (Pessoa.Pessoa):
    def __init__(self, nome, idade, sexo, cpf, departamento, materias, email, senha, codTipo):
        super().__init__(nome,idade,sexo,cpf)
        self.__Departamento = departamento
        self.__Materias = materias
        self.__Registros = []
        self.__Email = email
        self.__Senha = senha
        self.__codTipo = codTipo
    
    def setMaterias(self,Materias):
        self.__Materias = Materias
    
    def setDepartamento(self,Departamento):
        self.__Departamento = Departamento

    def setRegistros(self,registro):
        self.__Registros.append(registro)
    
    def setCodTipo (self, codTipo):
        self.__codTipo = codTipo
    
    def getMaterias(self):
        return self.__Materias

    def setEmail(self):
        return self.__Email
    
    def getDepartamento(self):
        return self.__Departamento

    def getRegistro(self,indice):
        return self.__Registros[indice]

    def getCodTipo(self):
        return self.__codTipo

    def getEmail(self):
        return self.__Email

    def getSenha(self):
        return self.__Senha

    def getTamLista(self):
        return len(self.__Registros)

    def registrarAtividade(self, curso, assunto, apresentador, avaliadores, data, status):
        registro = RegistroBanca.RegistroBanca(curso, assunto, apresentador, avaliadores, data, status)
        self.setRegistros(registro)