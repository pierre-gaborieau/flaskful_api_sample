#from bs4 import BeautifulSoup ##used for parsing html
from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api
from conf import conf

#Configuration des paramètres de l'application
app = Flask(__name__)
cors = CORS(app)
api = Api(app)

#Exemple de ressource
class Home(Resource):
  def get(self, token, param):
    #On vérifie que le token est valide
      if(token != conf().guid):
        return {'error': 'Invalid token'}, 401
      else :
        return {'message': 'Welcome to the API : {pParam}'.format(pParam = param)}, 200

#On ajoute la classe aux chemins de l'applications
api.add_resource(Home, '/path/<string:token>/<string:param>/')

#Racine de l'application
@app.route('/')
def index():
    return "<h1>API Homepage</h1>"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)