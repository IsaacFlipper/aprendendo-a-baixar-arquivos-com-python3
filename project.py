import urllib.request, urllib.parse, urllib.error

pasta = ['promo_hgss','hgss1','hgss2','hgss3','hgss4','col',
		 'promo_bw','bw1','bw2','bw3','bw4','bw5','bw6','bw7',
		 'bw8','bw9','bw10','bw11','promo_xy','xy1', 'xy2',
		 'xy3','xy4','xy5','xy6','xy7','xy8','xy9','xy10',
		 'xy11','xy12','promo_sm']
cont = 0
card = 1
pastas = 0
while True:
    lista = []
    for i in range(100):
        if i < 9:
            sair = 'https://www.pkparaiso.com/tcg/'+pasta[pastas]+'/es_256/00'+str(card)+'.jpg'
        
        else:
            sair = 'https://www.pkparaiso.com/tcg/'+pasta[pastas]+'/es_256/0'+str(card)+'.jpg'
        
        lista.append(sair)
        card += 1

    for i in lista:
        try:
             link = i
             nome = str(cont)+'.png'
             urllib.request.urlretrieve(link, nome)
             print(f'BAIXADO: ({link})')
             cont += 1
    	    
        except:
               print(f'ERROR:   ({i})')

    if pastas < 31:
        pastas += 1
        card = 1

    else:
        print('programa encerrado!')
        break
