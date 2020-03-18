from estagio.Requisitos import Requisitos
from estagio.Projetos import Projetos
from estagio.Codificacao import Codificacao
from estagio.Testes import Testes
from estagio.Implementacao import Implementacao
import time

class Main:
    print("Iniciando processo de Engenharia de Software ...")
    time.sleep(3)
    req = Requisitos()
    pro = Projetos()
    cod = Codificacao()
    imp = Implementacao()

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
    impletacao = imp.faseImplementacao(1)


#fase requisitos

#fase de projeto

#fase de construção

#fase de testes

#fase de implementacao
