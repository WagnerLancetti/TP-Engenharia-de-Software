import Professor as Professor


class ControleRegistro:
    def decisao(self, opcao):
        if (opcao == "Voltar para o Menu Principal"):
            return 0
        elif (opcao == "Registrar participação em bancas de defesa"):
            return 1

    def RegistrarAtividades(self, valor, assunto, apresentador, avaliadores, data, professor):
        verifica = 0
        mensagem = ""
        if (assunto == ''):
            mensagem = "*Digite o assunto do projeto"
            verifica = verifica + 1
        if (apresentador == ''):
            mensagem = mensagem +  "\n*Digite quem apresentou a defesa"
            verifica = verifica + 1
        if (avaliadores == ''):
            mensagem = mensagem + "\n*Digite quem estava na banca como avaliador"
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
            professor.registrarAtividade(curso,assunto,apresentador,avaliadores,data,1)
            return "Atividade registrada com sucesso!"
        else:
            return mensagem