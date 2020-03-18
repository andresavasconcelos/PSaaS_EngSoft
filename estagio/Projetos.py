import time

class Projetos:

    def criacaoProjeto(self, requisitos):

        projeto = []

        for i in range(1,len(requisitos)+1):
            tuplaProjeto = ("Mondelagem requisito "+ str(i) + ": " + requisitos[i-1], requisitos[i-1])
            projeto.append(tuplaProjeto)
            print("Modelando o requisito "+ str(i) + ": " + requisitos[i-1])
            time.sleep(1.5)

        #fase de validacao de requisitos
        print('Verificando a validade computacional...')
        print('verificando a consistencia ...')
        time.sleep(3)
        print('Validações do projeto efetuadas com sucesso')

        return projeto
