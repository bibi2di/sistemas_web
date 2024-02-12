import requests
import sys
import zlib

metodo = 'GET'
uri = 'http://www.google.es'
cabeceras = {'Host':'www.google.es'}

compressed = False
if len(sys.argv) == 1:
    cabeceras['Accept-Encoding'] = 'identity'
elif sys.argv[1] == 'compress':
    compressed = True
    cabeceras['Accept-Encoding'] = 'gzip'
else:
    print("Error!")
    exit(0)

respuesta = requests.request(metodo, uri, headers=cabeceras, allow_redirects=False, stream=True)

codigo = respuesta.status_code
descripcion = respuesta.reason
print(str(codigo) + ": " + descripcion)
for cabecera in respuesta.headers:
    print(cabecera + ": " +respuesta.headers[cabecera])

print("RESPONSE CONTENT LENGTH: " + str(len(respuesta.raw.data)) + ' byte')
if compressed:
    contenido_compressed = respuesta.raw.data
    contenido_uncompressed = zlib.decompress(contenido_compressed, 16+zlib.MAX_WBITS)
    print("UNCOMPRESSED RESPONSE CONTENT LENGTH: " + str(len(contenido_uncompressed)) + " byte")

