from flask import Blueprint
from utils.R import R

indexController = Blueprint("indexController", __name__)


@indexController.route('/')
def index():
    return "Hello Flask"


@indexController.route('/json')
def json():
    return R().success("请求成功", {
        "list": [
            1, 2, 3
        ]
    })


@indexController.route('/err')
def err():
    err = 1 / 0
    return "error"
