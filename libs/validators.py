import json
from flask import request
from flask_wtf import FlaskForm
from libs.error import APIException
from wtforms import Field, ValidationError


class BaseForm(FlaskForm):
    """基础方法"""
    def validate_(self):
        """表单验证"""
        if request.method == 'GET':
            if self.validate() is False:
                message = ''
                for key in self.errors:
                    message = message + '%s:%s' % (key,
                                                   self.errors[key][0]) + ','
                raise APIException(code=415, message=message)
            else:
                return self
        else:
            if self.validate_on_submit() is False:
                message = ''
                for key in self.errors:
                    message = message + '%s:%s' % (key,
                                                   self.errors[key][0]) + ','
                raise APIException(code=415, message=message)
            else:
                return self


class JsonField(Field):
    """验证json类型数据字段"""
    def process_formdata(self, value):
        """验证数据类型"""
        data = value

        if not isinstance(
                data, (dict, list)) and '[' not in data and '{' not in data:
            raise ValidationError('value to json error')
        if isinstance(data, (dict, list)):
            self.data = data
        else:
            try:
                self.data = json.loads(data)
            except BaseException:
                raise ValidationError('value to json error')
