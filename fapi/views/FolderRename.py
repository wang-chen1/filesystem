import os
import json

from django.views.generic import View
from django.utils.decorators import method_decorator

from common.res import res
from common.httpresult import httpresult
from common.getpath import getpath

from dbmysql.models.Folder import Folder
from dbmysql.models.File import File

class FolderRename(View):

    # 递归的修改子文件和子文件夹url
    def getprante(self, folder_id, folder_url):
        # 查询该目录下的所有子文件
        files = File.objects.filter(pfolder_id=folder_id)
        # 查询该项目下的所有子文件夹
        folders = Folder.objects.filter(parent_id=folder_id)
        # 没有子文件和子文件夹退出
        if files.count() == 0 and folders.count() == 0:
            return

        # 修改该目录下的所有子文件的路径
        if files.count() != 0:
            for item in files:
                item.url = os.path.join(folder_url, item.name)
                item.save()
        # 修改该目录下的所有子文夹路径
        if folders.count() != 0:
            for item in folders:
                item.url = os.path.join(folder_url, item.name)
                item.save()
                self.getprante(folder_id=item.id, folder_url=item.url)


    @method_decorator(httpresult)
    def put(self, request):
        # 用json的格式获取数据
        data = json.loads(request.body)
        folder_id = data.get('folder_id')
        folder_name = data.get('folder_name')

        folder = Folder.objects.filter(id=folder_id).first()
        if folder is None:
            raise Exception(u"该文件不存在")

        # 实际文件
        # 该文件夹地址
        path = getpath('media', folder.url)
        # 文件的父目录,绝对路径
        path_parent = os.path.split(path)[0]
        path_new = os.path.join(path_parent, folder_name)
        os.rename(path, path_new)

        # 在数据库中修改URL
        folder.url = os.path.split(folder.url)[0]+'/'+folder_name
        folder.name = folder_name
        print(folder.url, folder.name)
        folder.save()
        # 调用递归函数
        self.getprante(folder_id=folder_id, folder_url=folder.url)

        data = {
            'folder_id': folder_id,
            'folder_name': folder_name,
            'path': path,
            'path_parent': path_parent,
            'path_new': path_new,
        }
        return res(action='rename', data=data)
