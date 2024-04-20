from flask import Blueprint
from utils.R import R

app = Blueprint("indexController", __name__)


@app.route('/')
def index():
    return "Hello Flask"


@app.route('/json')
def json():
    return R().success("请求成功", {
        "list": [
            1, 2, 3
        ]
    })


@app.route('/err')
def err():
    err = 1 / 0
    return "error"
