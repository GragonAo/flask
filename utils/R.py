from flask import jsonify


class R:
    SUCCESS = 1
    ERROR = 0

    @staticmethod
    def success(msg="success", data=None):
        response = {
            'code': R.SUCCESS,
            'msg': msg,
            'data': data
        }
        return jsonify(response)

    @staticmethod
    def error(self, msg="error", data=None):
        response = {
            'code': R.ERROR,
            'msg': msg,
            'data': data
        }
        return jsonify(response)
