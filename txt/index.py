arquivo = open('Alunos.txt', 'r')
linhas =  arquivo.readlines()
del linhas[:4]

qtde_anuncio = 0
qtde_org = 0
qtde_yt_org = 0
qtde_igfb_org = 0
qtde_site_org = 0

for linha in linhas:
    email, origem = linha.split(',')
    if '_org' in origem:
        qtde_org += 1
        if 'hashtag_yt_org' in origem:
            qtde_yt_org += 1
        if 'hashtag_site_org' in origem:
            qtde_site_org += 1
        if 'hashtag_ig_org' in origem or 'hashtag_igfb_org':
            qtde_igfb_org += 1

    else:
        qtde_anuncio += 1

arquivo.close()

with open('indicadores.txt' , 'w') as arquivo_indicadores:
    arquivo_indicadores.write('Quantidade youtube: {}\n'.format(qtde_yt_org))
    arquivo_indicadores.write('Quantidade instagram: {}\n'.format(qtde_igfb_org))
    arquivo_indicadores.write('Quantidade site: {}\n'.format(qtde_site_org))
    arquivo_indicadores.write('Quantidade anuncio: {}\n'.format(qtde_anuncio))
    arquivo_indicadores.write('Quantidade orgânico: {}\n'.format(qtde_org))