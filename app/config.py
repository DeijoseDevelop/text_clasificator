from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

import os
import secrets
from datetime import timedelta


## charge enviroment variables
load_dotenv()

app = Flask(__name__)

# secret key for mongo session
tokens_session = secrets.token_hex(20)
app.config["SECRET_KEY"] = tokens_session

# Cors config
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = tokens_session
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=2)
jwt = JWTManager(app)

app.config['TIMEZONE'] = 'America/Bogota'

app.config['X-API-KEY'] = os.getenv("X_API_KEY")

# Swagger config
template = {
    "swagger": "2.0",
    "info": {
        "title": "Users management microservice",
        "description": "Microservice created by me",
        "contact": {
            "responsibleOrganization": "DeijoseDevelop",
            "responsibleDeveloper": "DeijoseDevelop",
            "email": "estudiandovazmore@gmail.com",
        },
        "version": "0.1.0"
    },
}

app.config["model"] = "/Users/lsvtech2022/Documents/projects/python/text_clasificator/app/modules/category_classificator/data/train_models/model.joblib"
app.config["vectorizer"] = "/Users/lsvtech2022/Documents/projects/python/text_clasificator/app/modules/category_classificator/data/train_models/vectorizer.joblib"

swagger = Swagger(app, template=template)

app.config["UPLOAD_FOLDER"] = os.getenv("UPLOAD_FOLDER")
