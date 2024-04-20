from flask import Blueprint, request

from api.model.FlaskUser import FlaskUser
from api.validate.IndexValidate import IndexValidate
from utils.R import R

app = Blueprint("DbDemoController", __name__, url_prefix="/demo")


@app.route('/userList')
def userList():
    users = FlaskUser.select()
    user_list = [{"id": user.id, "name": user.name} for user in users]
    return R().success("列表获取成功", {"user_list": user_list})


@app.route('/addUser', methods=['POST'])
def addUser():
    data = request.json
    form = IndexValidate(data=data)

    if form.validate():
        user = FlaskUser(**form.data)
        user.save()
        return R().success("创建成功", {
            "id": user.id
        })
    else:
        errors = form.errors
        return R().error("字段验证失败", errors)
