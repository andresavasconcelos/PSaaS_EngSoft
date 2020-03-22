import time

class Codificacao:

    def codificacaoFuncionalidades(self, projeto, veioDoTeste):

        funcionalidades = []

        if(veioDoTeste == False):
            ambienteDesenvolvimento = input("Digite a(as) linguagem(ens) de programacao/plataformas escolhida(as) para o desenvolvimento do sistema:\n")
            print("Iniciando codificacao do sistema nas linguagens/plataformas: " + ambienteDesenvolvimento + "...")
            time.sleep(2)

        for i in range(1,len(projeto)+1):
            funcionalidades.append("Funcionalidade "+ str(i) + ": " + projeto[i-1][1])
            print("Codificando funcionalidade "+ str(i) + ": " + projeto[i-1][1] + " a partir da: " + projeto[i-1][0])
            time.sleep(1)

        print('\nVerificando a execucao das funcionalidades ...')
        time.sleep(1)
        print('Apresentando funcionalidades ao cliente...')
        time.sleep(2.5)
        print('Validações da codificacao efetuadas com sucesso!\n')
        time.sleep(1)

        return funcionalidades
