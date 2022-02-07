def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de v´qrios alunos.
    :param n:  uma ou mais notas dos alunos (aceita várias)
    :return: dicionário com várias informaçoes sobre a situação da turma
    """

    d = dict()
    d['Total'] = len(n)
    d['Maior'] = max(n)
    d['Menor'] = min(n)
    d['Média'] = sum(n)/len(n)

    if sit:
        if d['Média'] >= 7 :
            d['Situação'] = 'BOA'
        elif d['Média'] >= 5:
            d['Situação'] ='Razoavel'
        else:
            d['Situação'] ='RUIM'

    # print(dicionario)
    # print(dicionario['quantidade'])
    return d


resp = notas(4.5,8.6,9,5,sit=True)
print(resp)

