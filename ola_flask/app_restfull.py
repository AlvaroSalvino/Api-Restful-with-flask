from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id':'0',
        'nome':'Alvaro',
         'habilidades':['Python','Flask']
    },

    {
        'id':'1',
        'nome':'Meyre',
         'habilidades':['Python','Django']
    }
]
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido, Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status':'sucess', 'mensagem':'registro excluido'}

class listaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        

api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(listaDesenvolvedores, '/dev/')


if __name__ == '__main__':
    app.run(debug=True)
