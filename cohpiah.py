import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    i = 0
    soma_traco_linguistico = 0

    while i < 6:
        diff = abs(as_a[i] - as_b[i])
        soma_traco_linguistico = soma_traco_linguistico + diff
        i = i + 1

    similaridade = soma_traco_linguistico / 6
    return similaridade


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    count_setencas = len(separa_sentencas(texto))
    lista_setencas = separa_sentencas(texto)

    lista_frases = []
    count_caract_setenca = 0
    for setenca in lista_setencas:
        count_caract_setenca = count_caract_setenca + len(setenca)
        lista_frases = lista_frases + separa_frases(setenca)
    count_frases = len(lista_frases)

    lista_palavras = []
    count_caract_frase = 0
    for frase in lista_frases:
        count_caract_frase = count_caract_frase + len(frase)
        lista_palavras = lista_palavras + separa_palavras(frase)
    count_palavras = len(lista_palavras)
    
    count_tamanho_palavra = 0
    for palavra in lista_palavras:
        count_tamanho_palavra = count_tamanho_palavra + len(palavra)

    palavras_unicas = n_palavras_unicas(lista_palavras)
    palavras_diff = n_palavras_diferentes(lista_palavras)

    wal = count_tamanho_palavra/count_palavras
    ttr = palavras_diff/count_palavras
    hlt = palavras_unicas/count_palavras
    sal = count_caract_setenca/count_setencas
    sac = count_frases/count_setencas
    pal = count_caract_frase/count_frases

    return[wal, ttr, hlt, sal, sac, pal]
    

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    lista_similaridades = []
    
    for texto in textos:
        assinatura = calcula_assinatura(texto)
        similaridade_texto = compara_assinatura(assinatura, ass_cp)
        lista_similaridades.append(similaridade_texto)
    
    maior_similaridade = min(lista_similaridades)
    index_texto = lista_similaridades.index(maior_similaridade) + 1

    return index_texto

def main():
    assinatura_cp = le_assinatura()
    leitura_texto = le_textos()
    print (avalia_textos(leitura_texto, assinatura_cp))

main()