import os

from flask import Flask
from flask_cors import CORS

from api.functions import register_blueprints
from initialize import db
from utils.R import R

app = Flask(__name__)
# 增加CORS支持
CORS(app)
# 配置Debug模式
app.debug = os.getenv('DEBUG', 'false').lower() == 'true'


def RunServer():
    db.init_db()
    initServer()


@app.teardown_appcontext
def teardown_appcontext(exception):
    db.close_db()


@app.errorhandler(Exception)
def handle_exception(e):
    return R().error('系统异常', str(e))


def initServer():
    # 自动导入所有蓝图
    register_blueprints(app, 'api.controller', 'api/controller')
    app.run(host=os.getenv("SERVER", "localhost"), port=os.getenv("PORT", 8080))
