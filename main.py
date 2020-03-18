from estagio.Requisitos import Requisitos
from estagio.Projetos import Projetos
from estagio.Codificacao import Codificacao

class Main:
    print("Ola")
    req = Requisitos()
    pro = Projetos()
    cod = Codificacao()
    cod.codificacaoFuncionalidades(pro.criacaoProjeto(req.printaFase()))


#fase requisitos

#fase de projeto

#fase de construção

#fase de testes

#fase de implementacao
