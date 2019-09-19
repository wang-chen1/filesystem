import os

from django.views.generic import View
from django.http import JsonResponse

from common.getpath import getpath
from dbmysql.models.File import File

class FileDel(View):
    def delete(self, request):
        file_id = request.GET.get('file_id')

        file_lists = []
        # 判断删除单个文件还是多个文件,并转化为list类型
        if type(file_id) is int:
            file_lists.append(file_id)
        else:
            file_lists = list(file_id.split(','))
        # 循环删除文件
        for file_list in file_lists:
            try:
                file = File.objects.filter(id=file_list).first()
                # 文件目录
                path = getpath('media', file.url)
                # 删除文件
                os.remove(path)
                # 删除该文件的数据库信息
                file.delete()
            except Exception:
                if os.path.exists(path):
                    raise Exception(u'删除文件失败')
        data = {
            'file_id': file_id,
            'file_lists': file_lists,
            'path': path,
        }
        return JsonResponse(
            data=data
        )

