import requests
import sys
import urllib

metodo = 'POST'
uri = "http://gae-sw-2017.appspot.com/processForm"
cabeceras = {'Host': 'gae-sw-2017.appspot.com', 'Content-Type': 'application/x-www-form-urlencoded'}

cuerpo={'dni': '12345678'}
cuerpo_encoded=urllib.parse.urlencode(cuerpo)
cabeceras['Content-Length'] = str(len(cuerpo_encoded))
respuesta=requests.request(metodo, uri, headers=cabeceras, data=cuerpo_encoded, allow_redirects=False)

codigo = respuesta.status_code
descripcion = respuesta.reason
print(str(codigo) + ' ' + descripcion)
for cabecera in respuesta.headers:
    print(cabecera + ': ' + respuesta.headers[cabecera])
cuerpo=respuesta.content
print(cuerpo)
