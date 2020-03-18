import time

class Requisitos:
    # def _requisitos(self, requisitos):
    #     requisitos = [1, 2, 3, 4, 5, 6]

    #     for requisito in requisitos:
    #         print(requisito)

    #     return requisitos

    def printaFase(self):
        requisitos = ["fazer1", "fazer2", "fazer3", "fazer4", "fazer5", "fazer6"]

        ##Processe de engenharia de requisitos
        print("Iniciando os requisitos, aguarde")
        time.sleep(1.5)

        ##Estudo de viabilidade da requisição
        print("Incio do estudo de viabilidade, aguarde")
        time.sleep(1.5)

        print("Confirmação da viabilidade do softer requerido, aguarde")
        time.sleep(1.5)
        #Elicitação e análise de requisitos
        print("Discussão com usuário, aguarde")
        time.sleep(1.5)

        print("Compreendendo o sistema solicitado, aguarde")
        time.sleep(1.5)

        print("Desenvolvimento de prototipo, aguarde")
        time.sleep(2)

        print("Recebendo todos os requisitos")
        time.sleep(2)

        #Os requisitos
        print('Entendendo os requisitos ...')
        time.sleep(2)

        print('Requisitos funcionais: '+ str(requisitos[0]))
        print('Requisitos não funcionais: '+ str(requisitos[1]))
        print('Requisitos de domínio: '+ str(requisitos[2]))
        print('Requisitos de dados: '+ str(requisitos[3]))
        print('Requisitos regra de negócio: '+ str(requisitos[4]))

        #Fase de prioridades
        print('Prioridades definidas')
        time.sleep(2)

        #Fase de Especificação
        print('Definindo a especificação do Software ...')
        print('Definindo as restrições do Softwsre ...')
        time.sleep(3)
        print('Especificação definida!')

        #Fase de modelagem
        print('Definindo modelagem do Software ...')
        print('Definindo modelo UML ...')
        print('Encadeando cenário ...')
        time.sleep(3)
        print('Modelagem definida!')

        #fase de validacao de requisitos
        print('Verificando a validade do software ...')
        print('verificando a consistencia ...')
        print('verificando o realismo ...')
        print('Validações em processamento, aguarde ...')
        time.sleep(3)
        print('Validações efetuada com sucesso')

        return requisitos
        pass
