import Sistema as Sistema

class ControleValidacao():
    # Recebe os dados para registrar uma atividade
    def ValidarAtividades(self,sistema,indice):
        self.mensagem = ""
        self.sistema = sistema
        self.mensagem = self.sistema.validarAtividade(indice)
        return mensagem

    def naoValidarAtividade(self,sistema,indice):
        self.mensagem = ""
        self.sistema = sistema
        self.mensagem = self.sistema.naoValidarAtividade(indice)
        return mensagem