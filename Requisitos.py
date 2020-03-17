import time

class Requisitos:
    requisitos = []

    def _init_(self, requisitos):
        self.requisitos = [1, 2, 3, 4, 5, 6]

    def Faserequisitos(self, tipo_requisitos):
        for requisito in self.requisitos:
            print('requisito:' + requisito)

        return

    def printaFase(self, faseRequistos):
    ##Processe de engenharia de requisitos
        print("Iniciando os requisitos, aguarde")
        time.sleep(1.5)

    def teste(self):
        print("Teste suscedido")

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

        print("Recebendo os requisitos" + self.requisitos)
        time.sleep(2)

        #Os requisitos
        print('Entendendo os requisitos, aguarde')
        time.sleep(2)

        print('Requisitos funcionais: '+ {self.requisitos[1]})











        ##criar uma array com todas as posições dos Requisitos
        ##printar cada fase dos requisitos
