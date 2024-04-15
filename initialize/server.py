import os

from flask import Flask
from flask_cors import CORS

from api.functions import register_blueprints
from initialize import db

app = Flask(__name__)
# 增加CORS支持
CORS(app)


def RunServer():
    db.init_db()
    initServer()


@app.teardown_appcontext
def teardown_appcontext(exception):
    db.close_db()


def initServer():
    # 自动导入所有蓝图
    register_blueprints(app, 'api.controller', 'api/controller')
    app.run(host=os.getenv("SERVER", "localhost"), port=os.getenv("PORT", 8080))
