# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests 

# Faz requisição da url e retorna o seu conteúdo html
def request_html(url):
    # Requisição
    req = requests.get(url)
    # Resultado do conteudo
    result = req.text[0:]
    # Recebe o conteudo HTML
    html = BeautifulSoup(result, "lxml")

    return html
            
# Retorna o conteudo em texto das divs
def remove_tags(html):
    # Receberá o conteudo final sem as tags
    final = ''
    # BeautifulSoup - biblioteca que extrai texto do conteudo html
    # Modelo - BeautifulSoup (counteudo_html, parser)
    # Parsers
        # html.parser (Rápido mas não muito tolerante)
        # lxml (Muito rápido, tolerante mas faz uso externo de bibliotecas em C) 
            # Instalação pip3 install lxml
        # html5lib (Extremamente tolerante, faz o parse igual a navegadores, porém muito lento)
            # Instalação pip3 install html5lib
    # Extração do conteudo em html apenas com as divs
    content = BeautifulSoup(html,"lxml")
    # Para cada termo 'div' no conteudo html
    for div in content.findAll('div',):
        # Recebe o texto da div e quebra a linha
        final = (final + div.text) + "\n"
    return final

# Rede Cinemak        
def cinemark(html):
    content = []
    price = ''
    pricess = []
    para = []
    session_type = ''
    # Recebe todas as divs com preços e informação da sala
    for div in html.find_all('div', {"class":"hidden"}):
        if "Preço" in div.text:
            content.append(div)
    for i in range(0, len(content)):
        title = content[i].find('div', {"class":"modal-title"}).text
        for p in content[i].find('p'):
            if "price-cinemark" in p:
                session_type = p.text
                print (session_type)
            elif "price-infos" in p:
                price = p.text
            para.append({"type":session_type, "price": price})    

    return 0

# Rede UCI
def uci(html):
    # Recebe todas as divs com preços e informação da sala
    divs = html.find_all('div', {"class":"cinema-texto-informativo"})    
    return divs

# Rede PlayArte       
def playarte(html):
    # Cria um contador da quantidade de divs
    count_div = 0
    # Variavel para armazenar as divs
    content = ''
    # Para cada linha entre 0 e o tamanho do array com o documento html
    for i in range(0, len(html)):
        # Se existir div com o id theater-prices que guarda as informações de preço
        if 'class=salaArea"' in html[i]:
            # + 1 no contador de divs
            count_div += 1
            # Enquanto existir <div
            while count_div:
                # Se existir div conta + 1
                if '<div' in html[i]:
                    count_div += 1
                # Se existir tag de fechamento de div e existir divs não fechadas
                elif '</div' in html[i] and count_div > 0:
                    # Remove um do contador
                    count_div -= 1
                # Adiciona a linha na váriavel texto enquanto existir conteudo dentro das divs
                content += html[i] + '\n'
                # Passa pra próxima linha        
                i+=1
    return remove_tags(content)

# Rede Cine Araujo       
def cine_araujo(html, url, city):
    # Cria um contador da quantidade de divs
    count_div = 0
    # Variavel para armazenar as divs
    content = ''
    # Array com dict de locais e id
    final = []
    # Extração do conteudo em html apenas com as options
    content = BeautifulSoup(str(html),"html.parser")
    # Para cada termo 'option' no conteudo html
    for option in content.findAll('option',):
        try:
            # Recebe o valor do atributo value
            value = option['value']
            # Faz unicode da cidade que está no formato latin
            city =  ((option.text).encode('latin1')).decode('utf-8')
            # Recebe o texto da option e quebra a linha
            final.append({'city': city, 'id': value})
        except:
            pass
    # Passa pelo array de cidades
    for i in range(len(final)):
        # Se a cidade existir na lista, busca o id
        if final[i]['city'] == "Taboão da Serra":
            # Gera a nova url
            url = url + "?cid_id=" + final[i]['id']
    # Retorna a nova url
    html = request_html(url,0)
    # Variavel para armazenar o html extraído
    content = ''
    # Para cada linha entre 0 e o tamanho do array com o documento html
    for i in range(0, len(html)):
        # Se existir div com o id theater-prices que guarda as informações de preço
        if 'id="precosWrapper"' in html[i]:
            # + 1 no contador de divs
            count_div += 1
            # Enquanto existir <div
            while count_div:
                # Se existir div conta + 1
                if '<div' in html[i]:
                    count_div += 1
                # Se existir tag de fechamento de div e existir divs não fechadas
                elif '</div' in html[i] and count_div > 0:
                    # Remove um do contador
                    count_div -= 1
                # Adiciona a linha na váriavel texto enquanto existir conteudo dentro das divs
                content += html[i] + '\n'
                # Passa pra próxima linha        
                i+=1
    return remove_tags(content)

# Seleciona as divs com o conteúdo dos preços
def select_cine(cine, url, city):
    # Recebe o conteudo html
    lines = request_html(url)
    # Se a rede de cinemas for a Cinemark    
    if cine.lower() == 'cinemark':
        return cinemark(lines)
    # Se a rede de cinemas for a UCI    
    if cine.lower() == 'uci':
        return uci(lines)
    # Se a rede de cinemas for a Playarte   
    if cine.lower() == 'playarte':
        # Recebe o conteudo html
        lines = request_html(url, 1)
        return playarte(lines)
    # Se a rede de cinemas for a UCI    
    if cine.lower() == 'cine araujo':
        return cine_araujo(lines, url, city)

print(select_cine('cinemark', 'https://www.cinemark.com.br/sao-paulo/cinemas', 0))
#print(select_cine('uci', 'https://www.ucicinemas.com.br/cinemas/UCI-Santana-Parque-Shopping', 0))
#print(select_cine('playarte', 'http://www.playartecinemas.com.br/cinemas/bri'))
#print(select_cine('cine araujo', 'http://www.cinearaujo.com.br/precos.asp', "Taboão da Serra"))
