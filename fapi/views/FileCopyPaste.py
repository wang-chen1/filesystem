import os
import shutil

from django.views.generic import View
from django.utils.decorators import method_decorator

from common.getpath import getpath
from common.res import res
from common.httpresult import httpresult

from dbmysql.models.Folder import Folder
from dbmysql.models.File import File

class FileCopyPaste(View):
    @method_decorator(httpresult)
    def post(self, request):
        file_id = request.POST.get('file_id')
        folder_id = request.POST.get('folder_id')

        folder_copy = Folder.objects.filter(id=folder_id).first()
        file = File.objects.filter(id=file_id).first()
        # 原路径
        path = getpath('media', file.url)
        # copy的路径
        path_c = getpath('media', folder_copy.url, file.name)
        # 把copy之后的文件信息存入数据库
        url = folder_copy.url+'/'+file.name
        File.objects.create(name=file.name, url=url, size=file.size,
                            depth=folder_copy.depth + 1, creater_id=1,
                            pfolder_id=folder_id, filetype=file.filetype)
        # 实际目录的拷贝
        shutil.copyfile(path, path_c)
        data = {
            'path': path,
            'path_c': path_c,
        }
        return res(data=data)
