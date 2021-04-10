import Chefe as Chefe

class ControleValidacao():
    def ValidarAtividades(self, Professor, Chefe, indice):
        self.Chefe = Chefe
        self.Professor = Professor
        self.Chefe.validarAtividade(Professor,indice)

    def naoValidarAtividade(self, Professor, Chefe,indice):
        self.Chefe = Chefe
        self.Professor = Professor
        self.Chefe.naoValidarAtividade(Professor,indice)

    def quantidadeProfessores(self, Professores):
        self.Professores = Professores
        return len(self.Professores)

    def tamLista(self, Professor):
        self.Professor = Professor
        return self.Professor.getTamLista()
    
    def printRegistro(self, Professor, indice):
        self.Professor = Professor
        return "Cadastro Professor(a) "+self.Professor.getNome()+".\n"+ self.Professor.getRegistro(indice).toString() +"\n\n"
    
    def match (self, Professor, email):
        i = 0
        idprof = 0
        while (i < len(Professor)):
            if (Professor[i].getEmail() == email):
                idprof = i
                i = i + len(Professor) 
            i = i + 1 
        return idprof
    
    def idAtividade (self, idprof,total,Professores):
        i = 0
        j = 0
        idatv = total
        while (i != idprof):
            idatv = total - Professores[i].getTamLista()
            i = i + 1
        return idatv

        