import urllib.request

try:
    site = urllib.request.urlopen('http://www.uol.com.br/')
except:
    print(f'o site UOL nao esta acessivel no momento')
else:
    print(f'Consegui acessar o site do UOL com sucesso!')


# opção 2
# import request
# try:
#     site = requests.get('https://www.uol.com.br/')
#     cod = site.status_code # 200 significa requisição OK
#
#     if cod == 200:
#         print(f'consegui acessar o site do pudim com sucesso!! ')
# except:
#     print(f'o site uol nao esta acessivel no momento')
