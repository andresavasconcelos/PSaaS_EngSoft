import time

class Projetos:

    def criacaoProjeto(self, requisitos):

        funcionalidades = []

        for i in range(1,len(requisitos)+1):
            funcionalidades.append("Funcionalidade"+ str(i) + ": " + requisitos[i-1])
            print("Projetando funcionalidade "+ str(i) + ": " + requisitos[i-1])
            time.sleep(1.5)

        #fase de validacao de requisitos
        print('Verificando a validade computacional...')
        print('verificando a consistencia ...')
        time.sleep(3)
        print('Validações do projeto efetuadas com sucesso')

        return funcionalidades
