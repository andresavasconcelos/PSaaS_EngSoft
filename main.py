from estagio.Requisitos import Requisitos
from estagio.Projetos import Projetos
from estagio.Codificacao import Codificacao
from estagio.Testes import Testes
from estagio.Implementacao import Implementacao
import time

class Main:
    print("Iniciando processo de Engenharia de Software ...\n")
    time.sleep(2)
    req = Requisitos()
    pro = Projetos()
    cod = Codificacao()
    imp = Implementacao()

    def chamaTeste(projeto, funcionalidades):
        tes = Testes()
        if(tes.teste(funcionalidades) == True):
            print("\n")
            #Chama implementacao
            time.sleep(1)
        else:
            print("Retornando para codificacao\n")
            funcionalidades = cod.codificacaoFuncionalidades(projeto)
            self.chamaTeste(projeto, funcionalidades)
            time.sleep(1)

    #fase requisitos

    requisitos = req.printaFase()

    #fase de projeto
    escolha = input("Etapa de requisitos concluida, deseja fazer o projeto? 'Sim' ou 'Nao'\n")
    if(escolha == "Sim" or escolha == "sim"):
        print("Iniciando etapa de projeto!")
        time.sleep(1)
    else:
        print("Abandonando processo de criacao de software!")
        raise SystemExit
    projeto = pro.criacaoProjeto(requisitos)

    #fase de codificacao
    escolha = input("Etapa de projeto concluida, deseja fazer a codificacao? 'Sim' ou 'Nao'\n")
    if(escolha == "Sim" or escolha == "sim"):
        print("Iniciando codificacao!")
        time.sleep(1)
    else:
        print("Abandonando processo de criacao de software!")
        raise SystemExit
    funcionalidades = cod.codificacaoFuncionalidades(projeto)

    #fase de testes
    escolha = input("Codificacao concluida, prosseguir para teste? 'Sim' ou 'Nao'\n")
    if(escolha == "Sim" or escolha == "sim"):
        print("Iniciando etapa de teste!")
        time.sleep(1)
    else:
        escolha = input("Deseja realizar a implementacao sem teste? 'Sim' ou 'Nao'\n")
        if(escolha == "Sim" or escolha == "sim"):
            #fase de implementacao
            print("Implementacao sem teste!")
            time.sleep(1)
            implementacao = imp.faseImplementacao(1)
        raise SystemExit

    chamaTeste(projeto,funcionalidades)
    #fase de implementacao
    implementacao = imp.faseImplementacao(1)
