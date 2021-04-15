from flask import jsonify
import json
import decimal


class DecimalEncoder(json.JSONEncoder):
    def default(self, res):
        if isinstance(res, decimal.Decimal):
            return float(res)
        super(DecimalEncoder, self).default(res)


def result_format(code: object = 200, data: object = None, **kwargs):
    if data is None:
        data = ''
    r = {
        'code': code,
        'data': data,
        **kwargs
    }
    return jsonify(r)
