import time

class Requisitos:
    # def _requisitos(self, requisitos):
    #     requisitos = [1, 2, 3, 4, 5, 6]

    #     for requisito in requisitos:
    #         print(requisito)

    #     return requisitos

    def printaFase(self):


        ##Processe de engenharia de requisitos
        #print("Iniciando os requisitos, aguarde")
        #time.sleep(1)

        ##Estudo de viabilidade da requisição
        print("Incio do estudo de viabilidade...")
        time.sleep(1)

        print("Confirmação da viabilidade do software requerido...")
        time.sleep(1)
        #Elicitação e análise de requisitos
        print("Discussão com cliente...")
        time.sleep(1)

        print("Compreendendo o sistema solicitado...")
        time.sleep(1)

        escolha = input("Deseja realizar prototipo? 'Sim' ou 'Nao'\n")
        if(escolha == "Sim" or escolha == "sim"):
            print("Desenvolvimento de prototipo...")
            time.sleep(1.5)
            print("Prototipo desenvolvido com sucesso!\n")
            time.sleep(1)
            print("Recebendo resposta do cliente!\n")
            time.sleep(1)

        print("Definicao dos requisitos funcionais...\n")
        requisitos = []

        operacao = "Inicial"
        i = 0
        while(operacao != "Requisitos Determinados" and operacao != "requisitos determinados"):
            operacao = input("Digite um requisito ou 'Requisitos Determinados' para proseguir com esses requisitos funcionais\n")
            if(operacao != "Requisitos Determinados" and operacao != "requisitos determinados"):
                requisitos.append(operacao)
            i = i + 1

        print("Recebendo todos os requisitos...")
        time.sleep(1.5)

        #Os requisitos
        #print('Entendendo os requisitos ...\n')
        #time.sleep(1.5)

        print('Requisitos funcionais: ')
        for i in requisitos:
            print(i)
            time.sleep(1)
        time.sleep(1)
        print("\n")

        print("Recebendo e processando requisitos nao funcional...")
        time.sleep(1)
        print("Recebendo e processando requisitos de dominio...")
        time.sleep(1)
        print("Recebendo e processando requisitos de dados...")
        time.sleep(1)
        print("Recebendo e processando requisitos de regra de negocio...\n")
        time.sleep(1)

        #print('Requisitos funcionais: '+ str(requisitos[0]))
        #print('Requisitos não funcionais: '+ str(requisitos[1]))
        #print('Requisitos de domínio: '+ str(requisitos[2]))
        #print('Requisitos de dados: '+ str(requisitos[3]))
        #print('Requisitos regra de negócio: '+ str(requisitos[4]))

        #Fase de prioridades
        print('Prioridades definidas\n')
        time.sleep(1.5)

        #Fase de Especificação
        print('Definindo a especificação do Software ...')
        time.sleep(1)
        print('Definindo as restrições do Software ...\n')
        time.sleep(2.5)
        print('Especificação definida!\n')

        #fase de validacao de requisitos
        #print('Verificando a validade do software ...')
        #time.sleep(1)
        #print('verificando a consistencia ...')
        #time.sleep(1)
        #print("verificando o realismo ...")
        #print('Validações em processamento, aguarde ...\n')
        #time.sleep(2.5)
        print('Validacao com o cliente, aguarde ...\n')
        time.sleep(2.5)
        print('Validacoes efetuadas com sucesso\n')
        time.sleep(1)

        return requisitos
        pass
