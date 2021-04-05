class Pessoa():
    def __init__ (self, nome = None, idade = -1, sexo = None, cpf = None):
        self.__Nome = nome
        self.__Idade = idade
        self.__Sexo = sexo
        self.__CPF = cpf

    def setNome(self,Nome):
        self.__Nome = Nome

    def setIdade(self,Idade):
        self.__Idade = Idade

    def setSexo(self,Sexo):
        self.__Sexo = Sexo

    def setCPF(self,CPF):
        self.__CPF = CPF

    def getNome(self):
        return self.__Nome

    def getIdade(self):
        return self.__Idade

    def getSexo(self):
        return self.__Sexo

    def getCPF(self):
        return self.__CPF