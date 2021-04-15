from flask import request, json
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    code = 200
    message = 'sorry, we made a mistake!'
    error_code = 415

    def __init__(self, message=None, code=None, error_code=None,
                 headers=None, **kwargs):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if message:
            self.message = message
        self.kwargs = kwargs
        super(APIException, self).__init__(message, None)

    def get_body(self, environ=None):
        body = dict(
            message=self.message,
            error_code=self.error_code,
            request=request.method + ' ' + self.get_url_no_param()
        )
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]


class ViewException(Exception):
    """view错误基类"""

    def __init__(self, error_code: int, code: int = 200, message='', **kwargs):
        self.error_code = error_code
        self.code = code
        self.message = message
        self.kwargs = kwargs

    @property
    def info(self):
        """请求相关信息"""
        return {'code': self.code, 'error_code': self.error_code, 'message': self.message, **self.kwargs}


class FormException(ViewException):
    """表单验证错误"""

    @property
    def info(self):
        """表单错误信息"""
        return {'code': self.code, 'error_code': self.error_code, 'message': self.message, **self.kwargs}


class NotFound(APIException):
    message = 'Not Found'
    error_code = 404

    @property
    def info(self):
        """表单错误信息"""
        return {'code': self.code, 'error_code': self.error_code, 'message': self.message, **self.kwargs}
