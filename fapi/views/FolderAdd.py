import os

from django.http import JsonResponse
from django.views.generic import View

from dbmysql.models.Folder import Folder
from common.getpath import getpath
from common.traversal import traversal

class FolderAdd(View):
    def post(self, request):
        folder_name = request.POST.get('folder_name')
        folder_pid = request.POST.get('folder_pid')

        folder = Folder.objects.filter(id=folder_pid).first()

        # 文件根目录
        path_root = getpath('media', folder.url)

        if '/' in folder_name:
            folder_name = folder_name.split('/')[-1]
        # 该文件是否在同级目录中重名
        if folder_name in traversal(bool=False, path=path_root)[0]:
            raise Exception(u'该文件夹已存在！！！')
        if folder_name is None:
            folder_name = u'新建文件夹'
        # 文件夹路径
        path = os.path.join(path_root, folder_name)
        try:
            # 添加数据
            depth = folder.depth+1
            Folder.objects.create(name=folder_name, parent_id=folder_pid,
                                  depth=depth, url=folder.url+'/'+folder_name, creater_id=1)
            # 创建文件夹
            os.mkdir(path)
        except Exception:
            # 是否创建文件成功
            if os.path.exists(path):
                os.remove(path)
            raise Exception(u'创建文件夹失败')





        # 测试数据
        data = {
            'code': 0,
            'name': folder.name,
            'url': folder.url,
            'path_root': path_root,
            'path': path,
        }
        return JsonResponse(
            data=data
        )





