from django.http import JsonResponse
from django.db import transaction
from common.ParamMissingException import ParamMissingException


# http请求返回装饰器

def httpresult(func):
    def wrapper(request,*args,**kwargs):
        try:
            with transaction.atomic():
                res = func(request,*args,**kwargs)
                return JsonResponse(
                    data=res
                )
        # 参数缺失
        except ParamMissingException as err:
            data = {
                'code': 1,
                'msg': "ERROR",
                'details': str(err)
            }
            return JsonResponse(
                status=402,
                data=data
            )
        except Exception as err:
            print('error:',err)
            data = {
                'code': 1,
                'msg': "ERROR",
                'details':str(err)
            }
            return JsonResponse(
                status=500,
                data=data
            )

    return wrapper
