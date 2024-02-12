import requests

# La petición tiene 4 partes: metodo, uri, cabecera y cuerpo
metodo = 'GET'
uri = "https://egela.ehu.eus/theme/ehu/pix/logo.png"
cabeceras = {'Host': 'www.egela.ehu.eus'}
cuerpo = ''
respuesta = requests.request(metodo, uri, headers=cabeceras, data=cuerpo)

#respuesta
codigo=respuesta.status_code
descripcion = respuesta.reason
print(str(codigo) + " " + descripcion)
for cabecera in respuesta.headers:
    print(cabecera + ": " + respuesta.headers[cabecera])
cuerpo= respuesta.content
#print(cuerpo)
print(" ")

fichero= open('imagen.jpg', 'wb')
fichero.write(cuerpo)
fichero.close()

metodo = 'GET'
uri = "https://egela.ehu.eus/theme/ehu/pix/logo.png"
cabeceras = {'Host': 'www.egela.ehu.eus',
             'If-Modified-Since': 'Fri, 15 Dec 2023 10:19:57 GMT',
             'If-None-Match': '"657c284d-231e"' }
cuerpo = ''
respuesta = requests.request(metodo, uri, headers=cabeceras, data=cuerpo)

#respuesta
codigo=respuesta.status_code
descripcion = respuesta.reason
print(str(codigo) + " " + descripcion)
for cabecera in respuesta.headers:
    print(cabecera + ": " + respuesta.headers[cabecera])
cuerpo= respuesta.content
print(cuerpo)
