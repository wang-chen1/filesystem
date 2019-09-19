from django.http import JsonResponse
from django.views.generic import View

from dbmysql.models.Folder import Folder

class Test(View):
    def get(self, request):
        folder = Folder.objects.first()

        data = {
            'code': 0,
            'message': 'SUCCESS',
            'id': folder.id,
            'name': folder.name,
            'time': folder.createtime
        }
        return JsonResponse(data=data)
