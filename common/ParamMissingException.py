# -*- coding:utf-8 -*-
class ParamMissingException(Exception):
    def __init__(self, code=402, error=u'参数缺失', data=u'参数缺失'):
        self.code = code
        self.error = error
        self.data = data

    def __str__(self):
        return "%d %s : %s " %(self.code, self.error, self.data)
