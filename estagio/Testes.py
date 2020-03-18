import time

class Testes:

    def executaFuncionalidade(self, funcionalidade, entrada):
        print("Execucao realizada com sucesso para : " + entrada)
        time.sleep(0.2)
        return True

    def testaFuncionalidade(self, funcionalidade, casosTesteFuncionalidade):
        for i in casosTesteFuncionalidade:
            if(self.executaFuncionalidade(funcionalidade, i) == False):
                print("Teste da funcionalidade falhou para o: " + i)
                return False
        print("Teste unitario da componente: " + funcionalidade + " realizado com sucesso")
        time.sleep(0.5)
        return True

    def testeDoSistema(self,funcionalidades):
        casosTeste = ["Primeiro Teste","Segundo Teste","Terceiro Teste","Quarto Teste","Teste Final"]
        print("Iniciando teste do Sistema...")
        time.sleep(1)
        for i in funcionalidades:
            #print("Teste Debug")
            #print(i)
            #print(funcionalidades[0])
            #print("Teste Debug")
            if(self.testaFuncionalidade(i,casosTeste) == False):
                print("Teste do Sistema falhou, retornar para codificacao")
                time.sleep(1)
                return False
        print("Teste do Sistema realizado com sucesso, prosseguir para implementacao")
        time.sleep(1)
        return True
