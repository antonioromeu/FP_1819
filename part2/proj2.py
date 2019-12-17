# 92427 Antonio Romeu Pinheiro

# construtor
def cria_celula(v):
    '''assinatura: {1, 0, -1} - celula
    caso o valor introduzido pertenca ao intervalo determinado {1, 0, -1},
    transforma este valor numa celula (lista com apenas um elemento)'''
    if v in (0, 1, -1):
        return [v]
    raise ValueError ('cria_celula: argumento invalido.')

# seletor
def obter_valor(c):
    '''assinatura: celula - {1, 0, -1}
    retorna o valor correspondente a celula, que pode ser 1, 0 ou -1'''
    return c[0]

# modificador
def inverte_estado(c):
    '''assinatura: celula - celula
    caso o argumento seja um celula, inverte o seu valor, passando a 1
    se esta for 0 e a 0 se a mesma for 1 (o valor -1 e considerado 
    inativo e como tal a celula nao se altera)'''
    if c[0] in (0, 1):
        c[0] = abs(c[0] - 1) #caso o primeiro elemento da celula seja 0 ou 1, e feito o absoluto da subtracao do valor por 1 e atribuido ao primeiro elemento esse valor
    return c

# reconhecedor
def eh_celula(c):
    '''assinatura: universal - logico
    recebe qualquer valor e retorna True se o argumento
    for uma celula e False caso contrario'''
    return isinstance(c, list) and (len(c) == 1) and (c[0] in (0, 1, -1))

# teste
def celulas_iguais(c1, c2):
    '''assinatura: celulas - logico
    recebe dois argumentos e devolve True se ambos forem celulas
    iguais ou False caso uma destas verificacoes nao ocorra'''
    return eh_celula(c1) and eh_celula(c2) and c1 == c2

# transformador
def celula_para_str(c):
    '''assinatura: celulas - cad. caracteres
    transforma o valor da celula introduzida numa string'''
    if eh_celula(c):
        if c == [-1]:
            return 'x' #altera o valor da celula para x caso este seja -1
        return str(c[0])

# construtor
def cria_coordenada(l, c):
    '''assinatura: naturais - coordenada
    cria uma coordenada (lista com dis elementos, onde o primeiro
    corresponde a linha e o segundo a coluna) caso os dois aegumentos
    introduzidos pertencam ao conjunto {0, 1, 2}'''
    if isinstance(l, int) and isinstance(c, int) and (l in range(tabuleiro_dimensao(tabuleiro_inicial()))) and (c in range(tabuleiro_dimensao(tabuleiro_inicial()))): #verifica se a coordenada linha e a coordenada coluna pertencem ao conjuunto (0, 1, 2) e se sao inteiros
        return [l, c]
    raise ValueError ('cria_coordenada: argumentos invalidos.')

# seletores
def coordenada_linha(c):
    '''assinatura: coordenada - naturais
    devolve o numero natural que corresponde
    a linha da coordenada c'''
    return c[0]

def coordenada_coluna(c):
    '''assinatura: coordenada - naturais
    devolve o numero natural que corresponde
    a coluna da coordenada c'''
    return c[1]

# reconhecedor
def eh_coordenada(arg):
    '''assinatura: universal - logico
    verifica se o argumento introduzido e uma coordenada
    e devolve True caso tal se verifique a False em caso
    contario'''
    if isinstance(arg, list) and (len(arg) == 2): #verifica se o argumento e uma lista e se a sua dimensao e 2
        if (coordenada_linha(arg) in range(tabuleiro_dimensao(tabuleiro_inicial()))) and (coordenada_coluna(arg) in range(tabuleiro_dimensao(tabuleiro_inicial()))): #averigua se a coordenada linha e a coordenada coluna pertecem ao conjunto {0, 1, 2}
            if (coordenada_linha(arg) == 2) and (coordenada_coluna(arg) == 0): #caso a coordenada seja [2, 0] devolve False uma vez que a posicao [2, 0] nao existe na representacao do tabuleiro
                return False
            return True
    return False

# teste
def coordenadas_iguais(c1, c2):
    '''assinatura: coordenada x coordenada - logico
    devolve verdadeiro caso os argumentos introduzidos
    sejam celula iguais'''
    return eh_coordenada(c1) and eh_coordenada(c2) and c1 == c2 #verifica se os argumentos sao coordenadas e iguais

# transformador
def coordenada_para_str(c):
    '''assinatura: coordenada - cad. caracteres
    devolve uma string composta pelas coordenadas
    (que sao representadas por um tuplo)'''
    return str(tuple([coordenada_linha(c), coordenada_coluna(c)]))

# contrutores
def tabuleiro_inicial():
    '''assinatura: {} - tabuleiro
    devolve o um determinado tabuleiro que
    aparece definido como o tabuleiro inicial'''
    return [[[-1], [-1], [-1]], [[0], [0], [-1]], [[0], [-1]]]

def str_para_tabuleiro(s):
    '''assinatura: cad. caracteres - tabuleiro
    transforma uma string composta por tuplos num tabuleiro'''
    if isinstance(s, str):
        s = eval(s)
        if isinstance(s, tuple):
            if len(s) == tabuleiro_dimensao(tabuleiro_inicial()): #verifica se a dimensao do argumento dado e igual a do tabuleiro inicial, que neste caso e 3
                for i in range(tabuleiro_dimensao(tabuleiro_inicial())): #faz um ciclo com os diversos elementos presentes no range da dimenso do tabuleiro inicial (3)
                    if not isinstance(s[i], tuple):
                        raise ValueError ('str_para_tabuleiro: argumento invalido.')
            tab = tuplo_para_lista(s) #atraves de uma funcao axiliar transforma a string numa lista
            if eh_tabuleiro(tab):
                return tab
    raise ValueError ('str_para_tabuleiro: argumento invalido.')

# seletores
def tabuleiro_dimensao(t):
    '''assinatura: tabuleiro - naturais
    retorna o comprimento do tabuleiro que corresponde
    ao numero de linhas e, consequentemente, ao numero
    de colunas'''
    return len(t)

def tabuleiro_celula(t, coor):
    '''assinatura: tabuleiro x coordenada - celula
    devolve a celula correspondente a coordenada do
    tabuleiro introduzido'''
    if coordenada_linha(coor) == 2:
        coor = aux_coor(coor) #altera o valor da coor atraves da funcao auxiliar aux_coor caso a coordenada linha seja 2
    return t[coordenada_linha(coor)][coordenada_coluna(coor)]

# modificadores
def tabuleiro_substitui_celula(t, cel, coor):
    '''assinatura: tabuleiro x celula x coordenada - tabuleiro
    retorna o tabuleiro com a celula correspondente a coordenada
    introduzida alterada para a celula introduzida'''
    if eh_celula(cel) and eh_tabuleiro(t) and eh_coordenada(coor):
        if coordenada_linha(coor) == 2:
            coor = aux_coor(coor) #altera o valor da coor atraves da funcao auxiliar aux_coor caso a coordenada linha seja 2
        t[coordenada_linha(coor)][coordenada_coluna(coor)] = cel #atribui o valor da celula introduzida a entrada do tabuleiro na respetiva posicao (definida pela coordenada)
        return t
    raise ValueError ('tabuleiro_substitui_celula: argumentos invalidos.')

def tabuleiro_inverte_estado(t, coor):
    '''assinatura: tabuleiro x coordenada - tabuleiro
    devolve o tabuleiro com a celula da coordenada introduzida
    invertida, ou seja, se for 1 passa a 0 e se for 0 passa a 1
    (caso a celula seja -1 nao ocorre inversao visto que -1 corresponde
    ao estado inativo)'''
    if eh_coordenada(coor) and eh_tabuleiro(t):
        if coordenada_linha(coor) == 2:
            coor = aux_coor(coor) #altera o valor da coor atraves da funcao auxiliar aux_coor caso a coordenada linha seja 2
        t = aux_tabuleiro_inverte_estado(t, coor)
        return t
    raise ValueError ('tabuleiro_inverte_estado: argumentos invalidos.')

# reconhecedor
def eh_tabuleiro(arg):
    '''assinatura: universal - logico
    retorna True se o argumento introduzido for um tabuleiro,
    definido como uma lista, composta por listas, cujas entrada
    sao listas e os comprimentos sao 3, 3 e 2 respetivamente,
    e False em caso contrario'''
    if isinstance(arg, list) and isinstance(arg[0], list) and isinstance(arg[1], list) and isinstance(arg[2], list):
        if (len(arg) == len(arg[0]) == len(arg[1]) == tabuleiro_dimensao(tabuleiro_inicial())) and (len(arg[2]) == 2):
            for i in range(tabuleiro_dimensao(tabuleiro_inicial())):
                for el in arg[i]:
                    if el != [-1] and el != [0] and el != [1]: #verifica se as entradas das listas sao listas cujos valores sao -1 ou 0 ou 1 e devolve False caso tal nao aconteca
                        return False
            return True
    return False
                        
# teste
def tabuleiros_iguais(t1, t2):
    '''assinatura: tabuleiro x tabuleiro - loogico
    verifica se os argumentos introduzidos sao tabuleiros iguais'''
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and t1 == t2  #verifica se os argumentos sao tabuleiros e se sao iguais

# transformador
def tabuleiro_para_str(t):
    '''assinatura: tabuleiro - cad. caracteres
    retorna a cadeia de carecteres que corresponde ao tabuleiro introduzido'''
    l1 = '+-------+'
    l2 = '|...' + celula_para_str(tabuleiro_celula(t, [0, 2])) + '...|'
    l3 = '|..' + celula_para_str(tabuleiro_celula(t, [0, 1])) + '.' + celula_para_str(tabuleiro_celula(t, [1, 2])) + '..|'
    l4 = '|.' + celula_para_str(tabuleiro_celula(t, [0, 0])) + '.' + celula_para_str(tabuleiro_celula(t, [1, 1])) + '.' + celula_para_str(tabuleiro_celula(t, [2, 2])) + '.|'
    l5 = '|..' + celula_para_str(tabuleiro_celula(t, [1, 0])) + '.' + celula_para_str(tabuleiro_celula(t, [2, 1])) + '..|'
    return (l1 + '\n' + l2 + '\n' + l3 + '\n' + l4 + '\n' + l5 + '\n' + l1)

def porta_x(t, p):
    '''assinatura: tabuleiro x {'E', 'D'} - tabuleiro
    devolve o tabuleiro correspondente a aplicacao da porta x
    (que inverte as celulas) ao lado escolhido, D ou E'''
    if p in ('D', 'E') and eh_tabuleiro(t):
        for i in range(tabuleiro_dimensao(t)):
            if p == 'E':
                t = tabuleiro_inverte_estado(t, cria_coordenada(1, i)) #altera o tabuleiro invertendo as celulas presentes nas posicoes cuja coordenada linha e 1
            else:
                t = tabuleiro_inverte_estado(t, cria_coordenada(i, 1)) #altera o tabuleiro invertendo as celulas presentes nas posicoes cuja coordenada coluna e 1
        return t
    raise ValueError ('porta_x: argumentos invalidos.')

def porta_z(t, p):
    '''assinatura: tabuleiro x {'E', 'D'} - tabuleiro
    devolve o tabuleiro correspondente a aplicacao da porta z
    (que inverte as celulas) ao lado escolhido, D ou E'''
    if p in ('D', 'E') and eh_tabuleiro(t):
        for i in range(tabuleiro_dimensao(t)):
            if p == 'E':
                t = tabuleiro_inverte_estado(t, cria_coordenada(0, i)) #altera o tabuleiro invertendo as celulas presentes nas posicoes cuja coordenada linha e 0
            else:
                t = tabuleiro_inverte_estado(t, cria_coordenada(i, 2)) #altera o tabuleiro invertendo as celulas presentes nas posicoes cuja coordenada coluna e 2
        return t
    raise ValueError ('porta_z: argumentos invalidos.')

def porta_h(t, p):
    '''assinatura: tabuleiro x {'E', 'D'} - tabuleiro
    devolve o tabuleiro correspondente a aplicacao da porta h,
    que troca cada celula de um tabuleiro com a celula
    correspondente do outro tabuleiro, dependendo do lado'''
    if p in ('D', 'E') and eh_tabuleiro(t):
        for i in range(tabuleiro_dimensao(t)):
            if p == 'E':
                cel1 = tabuleiro_celula(t, cria_coordenada(0, i)) #relaciona a variavel cel1 com os diversos valores das celulas com a coordenada linha igual a 0
                cel2 = tabuleiro_celula(t, cria_coordenada(1, i)) #relaciona a variavel cel2 com os diversos valores das celulas com a coordenada linha igual a 1
                t = tabuleiro_substitui_celula(t, cel1, cria_coordenada(1, i)) #substitui todas as celulas com a coordenada linha 1 pelo valor da cel1
                t = tabuleiro_substitui_celula(t, cel2, cria_coordenada(0, i)) #substitui todas as celulas com a coordenada linha 0 pelo valor da cel2
            else:
                cel1 = tabuleiro_celula(t, cria_coordenada(i, 2)) #relaciona a variavel cel1 com os diversos valores das celulas com a coordenada coluna igual a 2
                cel2 = tabuleiro_celula(t, cria_coordenada(i, 1)) #relaciona a variavel cel2 com os diversos valores das celulas com a coordenada coluna igual a 1
                t = tabuleiro_substitui_celula(t, cel1, cria_coordenada(i, 1)) #substitui todas as celulas com a coordenada coluna 1 pelo valor da cel1
                t = tabuleiro_substitui_celula(t, cel2, cria_coordenada(i, 2)) #substitui todas as celulas com a coordenada coluna 2 pelo valor da cel2
        return t
    raise ValueError ('porta_h: argumentos invalidos.')

# funcao adicional
def hello_quantum(s):
    '''assinatura: cad. caracteres - logico
    recebe uma cadeia de caracteres que contem o 'tabuleiro objetivo'
    e o numero maximo de jogadas e devolve True caso o jogador atinja o objetivo
    antes de ultrapassar o numero de jogadas possiveis e False caso este
    exceda o numero maximo de jogadas'''
    for i in range(len(s)):
        if s[i] == ':':
            ind = i
    tab_objetivo = str_para_tabuleiro(s[:ind]) #guarda na variavel objetivo o tabuleiro introduzido atraves da funcao hello_quantum
    tab_inicial = tabuleiro_inicial() #associa a variavel tab_inicial o que a funcao tabuleiro_inicial() retorna
    num_jogadas = eval(s[ind+1:]) #o digito a seguir a : equivale ao numero de jogadas possiveis
    jogadas_restantes = num_jogadas
    inicio = 'Bem-vindo ao Hello Quantum!' + '\n' + 'O seu objetivo e chegar ao tabuleiro:' + '\n' + tabuleiro_para_str(tab_objetivo) + '\n' + 'Comecando com o tabuleiro que se segue:' + '\n' + tabuleiro_para_str(tab_inicial)
    print(inicio)
    while jogadas_restantes > 0:
        if tab_inicial == tab_objetivo: #caso o tabuleiro inicial seja igual ao objetivo antes das jogadas acabarem devolve True
            print('Parabens, conseguiu converter o tabuleiro em ' + str(num_jogadas-jogadas_restantes) + ' jogadas!')
            return True
        porta_escolhida = input('Escolha uma porta para aplicar (X, Z ou H): ')
        qubit_escolhido = input('Escolha um qubit para analisar (E ou D): ')
        dic = {'X' : porta_x, 'Z' : porta_z, 'H' : porta_h} #atraves de um dicionario, relacionada a str da letra com a respetiva porta
        jogadas_restantes -= 1 #decrementa as jogadas restantes
        tab_inicial = dic[porta_escolhida](tab_inicial, qubit_escolhido)
        print(tabuleiro_para_str(tab_inicial))
    if tabuleiros_iguais(tab_inicial, tab_objetivo): #verifica se o tabuleiro alterado e igual ao tabuleiro objetivo e devolve True caso seja
        print('Parabens, conseguiu converter o tabuleiro em ' + str(num_jogadas) + ' jogadas!')
        return True
    return False
# funcoes auxiliares
def aux_coor(coor):
    '''assinatura: coor - coor
    recebe uma coordenada e substrai 1 a coordenada coluna
    da mesma e retorna o resultado'''
    return [coor[0], coor[1]-1] #subtrai 1 valor a coordenada coluna de modo a que a coordenada possa ser usada para obter os valores da lista de indice 2

def tuplo_para_lista(t):
    '''assinatura: tabuleiro - tabuleiro
    transforma o tabuleiro introduzido (tuplo)
    numa lista de listas e retorna a alteracao feita'''
    lista = [list(t[0]), list(t[1]), list(t[2])]
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            lista[i][j] = cria_celula(lista[i][j]) #altera as entradas do tuplo para listas com um determinado valor
    return lista

def aux_tabuleiro_inverte_estado(t, coor):
    '''assinatura: tabuleiro x coordenada - tabuleiro
    funcao auxiliar da tabuleiro_inverte_estado '''
    if t[coordenada_linha(coor)][coordenada_coluna(coor)] == [0]:
        t[coordenada_linha(coor)][coordenada_coluna(coor)] = [1] #altera o valor do tabuleiro para 1 caso este seja 0, na respetiva coordenada
    elif t[coordenada_linha(coor)][coordenada_coluna(coor)] == [1]:
        t[coordenada_linha(coor)][coordenada_coluna(coor)] = [0] #altera o valor do tabuleiro para 0 caso este seja 1, na respetiva coordenada
    return t