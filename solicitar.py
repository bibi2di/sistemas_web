import requests

# La petición tiene 4 partes: metodo, uri, cabecera y cuerpo
metodo = 'GET'
uri = "http://www.httpwatch.com/httpgallery/chunked/chunkedimage.aspx"
cabeceras = {'Host': 'www.httpwatch.com'}
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

fichero= open('imagen.jpg', 'wb')
fichero.write(cuerpo)
fichero.close()