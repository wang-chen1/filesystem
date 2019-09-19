import os
import json

from django.views.generic import View
from django.http import JsonResponse

from common.getpath import getpath
from dbmysql.models.File import File
from dbmysql.models.Folder import Folder

class FileRename(View):
    def put(self, request):
        data = json.loads(request.body)
        file_id = data.get('file_id')
        new_name = data.get('new_name')

        file = File.objects.filter(id=file_id).first()
        foid = file.pfolder_id
        folder = Folder.objects.filter(id=foid).first()
        # 源文件路径
        path = getpath('media', file.url)
        # 修改名字之后的路径
        new_path = getpath('media', folder.url, new_name+file.filetype)
        try:
            file.name = new_name+file.filetype
            file.url = folder.url+'/'+file.name
            os.rename(path, new_path)
            file.save()
        except Exception:
            if os.path.exists(new_path):
                os.rename(new_path, path)
            raise Exception(u'重命名失败')


        data = {
            'path': path,
            'new_path': new_path,
        }

        return JsonResponse(data=data)
