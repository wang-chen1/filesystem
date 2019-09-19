import os

from django.views.generic import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator

from dbmysql.models.File import File
from dbmysql.models.Folder import Folder

from common.getpath import getpath
from common.httpresult import httpresult
from common.ParamMissingException import ParamMissingException
from common.res import res


class FileAdd(View):

    @method_decorator(httpresult)
    def post(self, request):
        file_pid = request.POST.get('file_pid')
        # file_name = request.POST.get('file_name')
        file_ = request.FILES.get('file_')
        folder = Folder.objects.filter(id=file_pid).first()
        file = File.objects.filter(pfolder_id=file_pid,
                                   name=file_.name)
        if file.count() != 0:
            raise Exception(u'该文件已存在')
        if folder.id is None:
            raise ParamMissingException(u'父文件夹不存在')

        if file_.name is None:
            file_.name = u'新建文件'

        # 根目录
        path_root = getpath('media', str(folder.url))
        # 文件路径
        path = os.path.join(path_root, file_.name)
        # 写入文件
        f = open(path, 'w')
        f.close()
        # 文件大小
        size = os.path.getsize(path)
        # 文件类型
        file_type = os.path.splitext(path)
        file_type = file_type[-1]

        file_new = File.objects.create(name=file_.name, url=folder.url + '/' + file_.name,
                            size=size, depth=folder.depth + 1, creater_id=1,
                            pfolder_id=folder.id, filetype=file_type)

        if file_new.id is None:
            os.remove(path)

        data = {
            'path_root': path_root,
            # 'file_': file_,
            'file_id': file_new.id,
            'file_name': file_new.name,
        }

        return res(action='add file', data=data)
