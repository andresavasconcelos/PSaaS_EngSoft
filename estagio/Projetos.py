import time

class Projetos:

    def criacaoProjeto(self, requisitos):

        projeto = []

        for i in range(1,len(requisitos)+1):
            tuplaProjeto = ("Mondelagem requisito "+ str(i) + ": " + requisitos[i-1], requisitos[i-1])
            projeto.append(tuplaProjeto)
            print("Modelando o requisito "+ str(i) + ": " + requisitos[i-1])
            time.sleep(1)

        #fase de validacao de requisitos
        #Fase de modelagem
        print('Definindo modelagem do Software ...')
        time.sleep(1)
        print('Definindo modelo UML ...')
        time.sleep(1)
        print('Encadeando cenário ...\n')
        time.sleep(2.5)
        print('Modelagem do sistema definida!\n')
        time.sleep(1)
        print('\nVerificando a validade computacional...')
        time.sleep(1)
        print('Verificando a consistencia...')
        time.sleep(2.5)
        print('Validacao do projeto efetuada com sucesso!\n')
        time.sleep(1)

        return projeto
