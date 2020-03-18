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

            print('Configurando o software de desenvolvimento para produção ...')
            time.sleep(2)
            print('Software configurado!')

            print('Iniciando processo de deploy')
            time.sleep(3.5)
            print('Deploy realizado com sucesso')
        
            print('Verificando possíveis problemas de deploy ...')
            time.sleep(3.5)
            print('Software em execução!')
            print('Fim da fase de implementação')



        







