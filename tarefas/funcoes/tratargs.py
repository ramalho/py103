#!/usr/bin/env python
# coding: utf-8

def tag(nome, *linhas, **atributos):
    saida = ['<' + nome]
    for par in atributos.items():
        saida.append(' %s="%s"' % par)
    if linhas:
        saida.append('>')
        if len(linhas) == 1: 
            saida.append(linhas[0])
        else:
            saida.append('\n')
            for linha in linhas:
                spc = ' ' * 4
                saida.append(spc+'%s\n' % linha)
        saida.append('</%s>' % nome)
    else:
        saida.append(' />')
    return ''.join(saida)
    
if __name__=='__main__':
    import doctest
    from os.path import splitext
    nome_arq = '%s_test.txt' % splitext(__file__)[0]
    doctest.testfile(nome_arq)
    
