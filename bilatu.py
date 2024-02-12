"""Bidane Leon Balentzia
Sistemas Web, grupo 02
Petición para consultar en bilatu"""
import sys
import requests
import urllib
from bs4 import BeautifulSoup

# La petición tiene 4 partes: metodo, uri, cabecera y cuerpo
metodo = 'POST'
uri = "https://www.ehu.eus/bilatu/buscar/sbilatu.php?lang=es1"
cabeceras = {'Host': 'www.ehu.eus',
             'Content-Type': 'application/x-www-form-urlencoded'}
cuerpo = {}
#Podemos introducir nuestros parámetros o hará una búsqueda por defecto:
if len(sys.argv) > 1:
    parametros = ' '.join(sys.argv[1:])
    cuerpo = {'abi_ize': parametros}
else:
    cuerpo = {'abi_ize': 'Alvarez Gutierrez'}

cuerpo_encoded = urllib.parse.urlencode(cuerpo)
cabeceras['Content-Length'] = str(len(cuerpo_encoded))
respuesta = requests.request(metodo, uri, headers=cabeceras, data=cuerpo_encoded)

#respuesta
codigo=respuesta.status_code
descripcion = respuesta.reason
print(str(codigo) + " " + descripcion)
for cabecera in respuesta.headers:
    print(cabecera + ": " + respuesta.headers[cabecera])
cuerpo= respuesta.content.decode("utf-8")
print(" ")
#Buscar únicamente los resultados obtenidos:
soup = BeautifulSoup(respuesta.content, 'html.parser')
cuadro_prueba = soup.find(class_='cuadro_prueba')
if cuadro_prueba:
    resultado = cuadro_prueba.text.strip()
    print(resultado)
else:
    print("No se encontró el contenedor de resultados")

#print(cuerpo)

fichero=open('bilatu.html', 'w')
fichero.write(cuerpo)
fichero.close()