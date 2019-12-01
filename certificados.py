import requests
import zipfile
import os

dist_folder = '/ACcompactado'

# Realiza o download
r = requests.get('http://acraiz.icpbrasil.gov.br/credenciadas/CertificadosAC-ICP-Brasil/ACcompactado.zip', 
    allow_redirects=True)

# Escreve o zip
with open('ACcompactado.zip', 'wb') as zip:
    zip.write(r.content)

# Extrai o zip
with zipfile.ZipFile('ACcompactado.zip', 'r') as zip_ref:
    zip_ref.extractall('.' + dist_folder)

# Lista arquivos da pasta
for r, d, f in os.walk('.' + dist_folder):
    # Itera sobre o arquivos
    for c in f:
        f = os.getcwd() + dist_folder + '/' + c
        if 'ICP' in c:
            print('CERTUTIL -addstore Root '  + f)
            os.system('CERTUTIL -addstore Root '  + f)
        else:
            print('CERTUTIL -addstore CA ' + f)
            os.system('CERTUTIL -addstore CA ' + f)
