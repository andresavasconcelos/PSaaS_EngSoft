import time

class Codificacao:

    def codificacaoFuncionalidades(self, projeto):

        funcionalidades = []

        for i in range(1,len(projeto)+1):
            funcionalidades.append("Funcionalidade "+ str(i) + ": " + projeto[i-1][1])
            print("Projetando funcionalidade "+ str(i) + ": " + projeto[i-1][1] + " a partir da: " + projeto[i-1][0])
            time.sleep(1.5)

        print('verificando a execucao das funcionalidades ...')
        print('apresentando funcionalidades ao usuario...')
        time.sleep(3)
        print('Validações da codificacao efetuadas com sucesso')

        return funcionalidades
