import Sistema as Sistema


class ControleRegistro:
    def __init__(self):
        self.sistema = None
    # Recebe os dados para registrar uma atividade
    def decisao(self, opcao):
        if (opcao == "Voltar para o Menu Principal"):
            return 0
        elif (opcao == "Registrar participação em bancas de defesa"):
            return 1

    def RegistrarAtividades(self, valor, nomeProjeto,nomeApresentador,duracao, data, sistema):
        verifica = 0
        mensagem = ""
        if (nomeProjeto == ''):
            mensagem = "*Digite o nome do Projeto"
            verifica = verifica + 1
        if (nomeApresentador == ''):
            mensagem = mensagem +  "\n*Digite quem apresentou a defesa"
            verifica = verifica + 1
        if (duracao == ''):
            mensagem = mensagem + "\n*Digite quanto tempo durou a defesa"
            verifica = verifica + 1
        if (data == ''):
            mensagem = mensagem + "\n*Digite quando aconteceu a defesa"
            verifica = verifica + 1
        if (verifica == 0):
            curso = ""
            if (valor == 1):
                curso = "Graduação"
            elif (valor == 2):
                curso = "Mestrado"
            else:
                curso = "Doutorado"
            self.sistema = sistema
            self.sistema.registrarAtividade(curso, nomeProjeto, nomeApresentador, duracao, data)
            return "Atividade registrada com sucesso!"
        else:
            return mensagem        