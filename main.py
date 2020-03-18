from estagio.Requisitos import Requisitos
from estagio.Projetos import Projetos
from estagio.Codificacao import Codificacao
from estagio.Testes import Testes
import time

class Main:
    print("Ola")
    req = Requisitos()
    pro = Projetos()
    cod = Codificacao()

    def chamaTeste(projeto, funcionalidades):
        tes = Testes()
        if(tes.testeDoSistema(funcionalidades) == True):
            print("Colocando em producao")
            #Chama implementacao
            time.sleep(1)
        else:
            print("Retornando para codificacao")
            funcionalidades = cod.codificacaoFuncionalidades(projeto)
            self.chamaTeste(projeto, funcionalidades)
            time.sleep(1)

    requisitos = req.printaFase()
    projeto = pro.criacaoProjeto(requisitos)
    funcionalidades = cod.codificacaoFuncionalidades(projeto)
    chamaTeste(projeto,funcionalidades)


#fase requisitos

#fase de projeto

#fase de construção

#fase de testes

#fase de implementacao
