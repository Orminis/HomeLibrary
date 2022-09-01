from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api

from db import db
from resources.routes import routes

app = Flask(__name__)

db.init_app(app)
app.config.from_object("config.DevelopmentConfig")

api = Api(app)
migrate = Migrate(app, db)
CORS(app)


# commit all responses before sending it
@app.after_request
def return_response(resp):
    db.session.commit()
    return resp


[api.add_resource(*route) for route in routes]

if __name__ == "__main__":
    app.run(debug=True)
