import time

class Codificacao:

    def codificacaoFuncionalidades(self, projeto):

        funcionalidades = []

        for i in range(1,len(projeto)+1):
            funcionalidades.append("Funcionalidade "+ str(i) + ": " + projeto[i-1][1])
            print("Projetando funcionalidade "+ str(i) + ": " + projeto[i-1][1] + " a partir da: " + projeto[i-1][0])
            time.sleep(1)

        print('\nVerificando a execucao das funcionalidades ...')
        time.sleep(1)
        print('Apresentando funcionalidades ao usuario...')
        time.sleep(2.5)
        print('Validações da codificacao efetuadas com sucesso!\n')
        time.sleep(1)

        return funcionalidades
