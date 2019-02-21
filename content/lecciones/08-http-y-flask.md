Title: HTTP y Flask
Author: Mauricio Collazos
Date: 2019-02-20
![]()
---
class: center, middle, light, first-slide
# HTTP y Flask
## Mauricio Collazos
.footnote[]
---
class: light
# HTTP
  - Recursos
  - Métodos
    - GET
    - PUT
    - POST
    - DELETE
  - Respuestas
    - 200: OK
    - 201: Created
    - 301: Moved Permanently
    - 302: Moved
    - 400: Bad Request
    - 401: Unauthorized
    - 403: Forbidden
    - 404: Not Found
    - 405: Method Not Allowed
    - 500: Internal Server Error
    - 502: Bad Gateway
    - 503: Service Unavailable
    - 504: Gateway Timeout
  - Encabezados

---
# Instalando Flask

```bash
conda install flask
```

---

# Prototipo de aplicación
```python
import json
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)

```

---
# Utilizando un Rest Client
- [Advanced Rest Client Chrome](https://chrome.google.com/webstore/detail/advanced-rest-client/hgmloofddffdnphfgcellkdfbfbjeloo?hl=es)
- [Reslet Client Chrome](https://chrome.google.com/webstore/detail/restlet-client-rest-api-t/aejoelaoggembcahagimdiliamlcdmfm)
- [RestClient, Mozilla](https://addons.mozilla.org/es/firefox/addon/restclient/)
- [Advanced REST Client Stand Alone](https://install.advancedrestclient.com/install)
- [Insomnia](https://insomnia.rest/)
- [Postman](https://www.getpostman.com/)
- [Curl](https://curl.haxx.se/)
- [Requests Python](http://docs.python-requests.org/en/master/)

---
# Identificando el método
```python
@app.route("/method", methods=["GET", "POST", "PUT", "DELETE"])
def methods():
    return request.method
```

---
# Status code
```python
@app.route("/status-code/<int:status_code>/")
def status_code(status_code):
    return "status{}".format(status_code)
```
---
# Form Data
```python
@app.route("/", methods=["POST"])
def post_data():
    return json.dumps(request.form)


@app.route("/data", methods=["POST"])
def data():
    return request.data
```

---
# Respondiendo Responses explícitos
```python
@app.route("/plain-response")
def plain_response():
    return Response(
        "{'response': 'Hello World'}",
        status=200,
        headers=dict(),
        content_type="text/plain"
    )


@app.route("/json-response")
def json_response():
    response = dict()
    response["value"] = "hello world"
    return jsonify(response), 200


@app.route("/json-response-2")
def json_response_2():
    response = dict()
    response["value"] = "hello world"
    return Response(json.dumps(response), status=200, content_type="application/json")

```
---
# Archivos
```python
@app.route("csv", methods=["POST"])
def csv():
    archivo = request.files.get("archivo")
    binary_lines = archivo.readlines()
    decoded_lines = [line.decode() for line in binary_lines]
    posts  = list()
    reader = csv.reader(decoded_lines)
    for r in reader:
        pass
    return "OK", 200
```

---
# Ejercicios
- Lista de tareas

---
# Para crear un proyecto