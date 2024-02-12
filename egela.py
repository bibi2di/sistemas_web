import requests

metodo='GET'
uri = 'http://egela.ehu.eus'
cabeceras = {'Host': 'egela.ehu.eus'}
cuerpo = ''
respuesta=requests.request(metodo, uri, headers=cabeceras, data=cuerpo, allow_redirects=False)

codigo = respuesta.status_code
descripcion = respuesta.reason
print(str(codigo) + " " + descripcion)
for cabecera in respuesta.headers:
    print(cabecera + ": " + respuesta.headers[cabecera])
cuerpo = respuesta.content
print(cuerpo)

metodo = 'GET'
uri = respuesta.headers['Location']
cabeceras = {'Host': uri.split('/')[2]}
cuerpo = ''
respuesta=requests.request(metodo, uri, headers=cabeceras, data=cuerpo, allow_redirects=False)

codigo = respuesta.status_code
descripcion = respuesta.reason
print(str(codigo) + " " + descripcion)
for cabecera in respuesta.headers:
    print(cabecera + ": " + respuesta.headers[cabecera])
cuerpo = respuesta.content
print(cuerpo)

metodo = 'GET'
uri = respuesta.headers['Location']
cabeceras = {'Host': uri.split('/')[2]}
cuerpo = ''
respuesta=requests.request(metodo, uri, headers=cabeceras, data=cuerpo, allow_redirects=False)

codigo = respuesta.status_code
descripcion = respuesta.reason
print(str(codigo) + " " + descripcion)
for cabecera in respuesta.headers:
    print(cabecera + ": " + respuesta.headers[cabecera])
cuerpo = respuesta.content.decode("utf-8")
print(cuerpo)
fichero=open('egela.html', 'w')
fichero.write(cuerpo)
fichero.close()