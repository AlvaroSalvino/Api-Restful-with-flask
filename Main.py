from flask import Flask

server = Flask(__name__)

@server.get('/pessoas')
def buscar_pessoas():
    return 'Programaticamente Falando, Vitor Gusmao'

server.run()
