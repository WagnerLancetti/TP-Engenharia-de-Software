
class Controle:
    def Login(self, email, senha, Professores):
        i = 0
        verifica = 0
        while (i < len(Professores)):
            verifica = 0
            if (email == Professores[i].getEmail()):
                verifica = verifica + 1
            if (senha == Professores[i].getSenha()):
                verifica = verifica + 1
            if (verifica == 2):
                indice = i
                i = i + len(Professores)
            i = i + 1
        if (verifica == 2):
            return Professores[indice].getCodTipo() # 1 se for professor // 2 se for chefe
            print ("Entro aqui!")
        else:
            return 3 # Se nao aceitar o login

    def match (self, email, professores):
        i = 0
        idprof = 0
        while (i < len(professores)):
            if (professores[i].getEmail() == email):
                idprof = i
                i = i + len(professores) 
            i = i + 1 
        return idprof