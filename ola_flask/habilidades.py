from flask_restful import Resource, Api

habilidade = ['Python', 'Java', 'C#', 'Ruby', 'PHP']
class Habilidades(Resource):
    def get(self):
        return habilidade
