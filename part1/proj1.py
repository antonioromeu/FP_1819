# 92427 Antonio Romeu

def eh_tabuleiro (t): 
    """assinatura: universal - booleano
    verifica se o argumento dado e um tabuleiro"""
    n = (1, -1, 0)
    
    if isinstance (t, tuple):
        if len (t) == 3:
            for i in (0, 1, 2):
                if not isinstance (t [i], tuple):
                    return False
            if len (t[0]) == 3 and len (t[1]) == 3 and len (t[2]) == 2:
                if t[0][0] in n and t[0][1] in n and t[0][2] in n:
                    if t[1][0] in n and t[1][1] in n and t[1][2] in n:
                        if t[2][0] in n and t[2][1] in n:
                            return True
    return False

def tabuleiro_str (t):
    """assinatura: tabuleiro - cad. caracteres
    transforma o tabuleiro fornecido numa string"""
    if eh_tabuleiro(t):
        t = [list(t[0]), list(t[1]), list(t[2])]
        for i in (0, 1, 2):
            if t[0][i] == -1:
                t[0][i] = 'x'
            if t[1][i] == -1:
                t[1][i] = 'x'
        
        for i in (0, 1):
            if t[2][i] == -1:
                t[2][i] = 'x'
    else:
        raise ValueError ('tabuleiro_str: argumento invalido')

    l1 = '+-------+'
    l2 = '|...' + str(t[0][2]) + '...|'
    l3 = '|..' + str(t[0][1]) + '.' + str(t[1][2]) + '..|'
    l4 = '|.' + str(t[0][0]) + '.' + str(t[1][1]) + '.' + str(t[2][1]) + '.|'
    l5 = '|..' + str(t[1][0]) + '.' + str(t[2][0]) + '..|'
    
    return (l1 + '\n' + l2 + '\n' + l3 + '\n' + l4 + '\n' + l5 + '\n' + l1)

def tabuleiros_iguais (x, y):
    """assinatura: tabuleiro x tabuleiro - booleano
    verifica se os tabuleiros fornecidos sao iguais e devolve o valor logico"""
    if eh_tabuleiro (x) and eh_tabuleiro (y):
        return x == y
    
    elif not eh_tabuleiro (x) or not eh_tabuleiro (y):
        raise ValueError ('tabuleiros_iguais: um dos argumentos nao e tabuleiro')

def porta_x (t, l):
    """assinatura: tabuleiro x {"E", "D"} - tabuleiro
    inverte no tabuleiro dado, dependendo do lado escolhido, esquerdo ou
    direito, o valor da celula inferior e consequentemente de todas as restantes
    celulas na mesma linha ou coluna"""
    if l != "D" and l != "E" or not eh_tabuleiro (t):
        raise ValueError ('porta_x: um dos argumentos e invalido')
    
    t = [list(t[0]), list(t[1]), list(t[2])]
    
    if l == "E":
        for i in (0, 1, 2):
            if t[1][i] == -1:
                t[1][i] = -1
            elif t[1][i] == 0:
                t[1][i] = 1
            elif t[1][i] == 1:
                t[1][i] = 0
    
    elif l == "D":
        for i in (0, 1):
            if t[i][1] == -1:
                t[i][1] = -1
            elif t[i][1] == 0:
                t[i][1] = 1
            elif t[i][1] == 1:
                t[i][1] = 0
        if t[2][0] == -1:
            t[2][0] = -1
        elif t[2][0] == 0:
            t[2][0] = 1
        elif t[2][0] == 1:
            t[2][0] = 0
    
    return (tuple(t[0]), tuple(t[1]), tuple(t[2]))

def porta_z(t, l):
    """assinatura: tabuleiro x {"E", "D"} - tabuleiro
    apresenta resultados parecidos aos da porta_x, com excecao que opera 
    sobre a celula superior"""
    if l != "D" and l != "E" or not eh_tabuleiro (t):
        raise ValueError ('porta_z: um dos argumentos e invalido')
    
    t = [list(t[0]), list(t[1]), list(t[2])]
   
    if l == "E":
        for i in (0, 1, 2):
            if t[0][i] == -1:
                t[0][i] = -1
            elif t[0][i] == 0:
                t[0][i] = 1
            elif t[0][i] == 1:
                t[0][i] = 0
    
    elif l == "D":
        for i in (0, 1):
            if t[i][2] == -1:
                t[i][2] = -1
            elif t[i][2] == 0:
                t[i][2] = 1
            elif t[i][2] == 1:
                t [i][2] = 0
        if t[2][1] == -1:
            t[2][1] = -1
        elif t[2][1] == 0:
            t[2][1] = 1
        elif t[2][1] == 1:
            t[2][1] = 0

    return (tuple(t[0]), tuple(t[1]), tuple(t[2]))

def porta_h(t, l):
    """assinatura: tabuleiro x {"E", "D"} - tabuleiro
    tem como resultado a troca de estado de ambas as celulas entre si"""
    if l != "D" and l != "E" or not eh_tabuleiro (t):
        raise ValueError ('porta_h: um dos argumentos e invalido')
    
    t = [list(t[0]), list(t[1]), list(t[2])]
   
    if l == "E":
        aux = t [0][0]
        t [0][0] = t [1][0]
        t [1][0] = aux
        aux = t [0][1]
        t [0][1] = t [1][1]
        t [1][1] = aux
        aux = t [0][2]
        t [0][2] = t [1][2]
        t [1][2] = aux
    
    elif l == "D":
        aux = t [2][0]
        t [2][0] = t [2][1]
        t [2][1] = aux
        aux = t [1][1]
        t [1][1] = t [1][2]
        t [1][2] = aux
        aux = t [0][1]
        t [0][1] = t [0][2]
        t [0][2] = aux

    return (tuple(t[0]), tuple(t[1]), tuple(t[2]))