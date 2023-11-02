from flask import Flask
from flask_pydantic_sped import FlaskPydanticSpec

server = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='Live de Python')
spec.register(server)

@server.get('/pessoas') # Rota, endpoint, recurso...
def buscar_pessoas():
    return 'Programaticamente Falando, Vitor Gusmao'

server.run()
