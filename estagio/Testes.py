import time
import random

class Testes:

    casosTeste = ["Primeiro Teste","Segundo Teste","Terceiro Teste","Quarto Teste","Teste Final"]

    def executaFuncionalidade(self, funcionalidade, entrada):
        if(random.random() <= 0.015):
            print("Execucao falhou para : " + entrada)
            return False
        else:
            print("Execucao realizada com sucesso para : " + entrada)
            time.sleep(0.3)
            return True

    def testaFuncionalidade(self, funcionalidade, casosTesteFuncionalidade):
        for i in casosTesteFuncionalidade:
            print("Teste unitario da componente: " + funcionalidade)
            if(self.executaFuncionalidade(funcionalidade, i) == False):
                print("Teste da funcionalidade falhou para o: " + i)
                return False
        print("Realizado com sucesso!")
        time.sleep(0.5)
        return True

    def testeDoSistema(self, funcionalidades, casosTesteSistema):
        print("Iniciando teste do Sistema...")
        time.sleep(1)
        for i in casosTesteSistema:
            #print("Teste Debug")
            #print(i)
            #print(funcionalidades[0])
            #print("Teste Debug")
            if(self.executaFuncionalidade("Sistema", i) == False):
                print("Teste do Sistema falhou, retornar para codificacao")
                time.sleep(1)
                return False
        print("Teste do Sistema realizado com sucesso, prosseguir para implementacao")
        time.sleep(1)
        return True

    def teste(self, funcionalidades):
        escolha = input("Prosseguir para teste unitario das funcionalidades? 'Sim' ou 'Nao'\n")
        if(escolha == "Sim" or escolha == "sim"):
            for i in funcionalidades:
                #print("Teste Debug")
                #print(i)
                #print(funcionalidades[0])
                #print("Teste Debug")
                if(self.testaFuncionalidade(i,self.casosTeste) == False):
                    print("Teste unitario falhou, retornar para codificacao")
                    time.sleep(1)
                    return False
        else:
            print("Nao sera realizado nenhum teste unitario!\n")
            time.sleep(1)

        escolha = input("Prosseguir para teste do sistema? 'Sim' ou 'Nao'\n")
        if(escolha == "Sim" or escolha == "sim"):
            return self.testeDoSistema(funcionalidades, self.casosTeste)
        else:
            print("Nao sera realizado teste de sistema, seguir para implementacao!\n")
            time.sleep(1)

        return True
