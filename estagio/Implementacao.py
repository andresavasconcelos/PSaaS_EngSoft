from estagio.Testes import Testes
import time

class Implementacao:

    def validaTeste(self, testes):
        req = Testes()
        if(req):
            return True
            return False

        return True


    def faseImplementacao(self, requisitos):

        print('Esperando a validação dos testes ...')
        time.sleep(2)

        if(self.validaTeste(requisitos)):
            print('Agendando o processo de implementação ...')
            time.sleep(2)
            print("Processo agendado!")
            time.sleep(1)

            print('Configurando o software de desenvolvimento para produção ...')
            time.sleep(2)
            print('Software configurado!')
            time.sleep(1)
            print('Realizando ultima validacao com o cliente...')
            time.sleep(2)
            print('Cliente aprovou o software!')
            time.sleep(1)

            escolha = input("Deseja colocar o software em producao? 'Sim' ou 'Nao'\n")
            if(escolha == "Sim" or escolha == "sim"):
                print('Iniciando processo de deploy')
                time.sleep(3.5)
            else:
                print("Abandonando o software! :(")
                raise SystemExit

            print('Deploy realizado com sucesso')
            time.sleep(1)

            print('Verificando possíveis problemas de deploy ...')
            time.sleep(3.5)
            #print('Software em execução!')
            print('Deploy foi bem sucedido!')
            time.sleep(1)
            print('Fim da fase de implementação')
            input("Digite algo para encerrar!")
