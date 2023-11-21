
class NoArvoreBB():
    def __init__(self, dado, esq=None, dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

# insere é um função
def insere(raiz, no):
    if not raiz:
        return no
    
    if no.dado < raiz.dado:
        raiz.esq = insere(raiz.esq, no)
    else:
        raiz.dir = insere(raiz.dir, no)

    return raiz

    


def preorder(raiz):
    pass

def inorder(raiz):
    pass

def posorder(raiz):
    pass

def busca_largura(raiz, dado):
    pass

raiz = NoArvoreBB(50)
raiz = insere(raiz, NoArvoreBB(17))
raiz = insere(raiz, NoArvoreBB(72))
raiz = insere(raiz, NoArvoreBB(12))
raiz = insere(raiz, NoArvoreBB(23))
raiz = insere(raiz, NoArvoreBB(54))
raiz = insere(raiz, NoArvoreBB(76))
raiz = insere(raiz, NoArvoreBB(9))
raiz = insere(raiz, NoArvoreBB(14))
raiz = insere(raiz, NoArvoreBB(19))
raiz = insere(raiz, NoArvoreBB(67))

print('iu')