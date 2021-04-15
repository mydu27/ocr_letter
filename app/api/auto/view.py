from . import api
from libs.functions import result_format


@api.route('/test')
def auto_test():
    """自动化测试"""
    return result_format(code=200, data='successful!')
