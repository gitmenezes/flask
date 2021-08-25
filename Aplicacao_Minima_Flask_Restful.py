#Aplicação Mínima Flask-Restful
from flask import Flask, request, render_template, Response
import json
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class conecta(Resource):
    def get(self):
        return Response(response=render_template('index.html'))#conecta a página index.html


api.add_resource(conecta, '/')

if __name__ == '__main__':
    app.run(debug=1)# Ativa o servidor
