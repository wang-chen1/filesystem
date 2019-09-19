import os

from django.views.generic import View
from django.utils.decorators import method_decorator

from common.res import res
from common.getpath import getpath
from common.traversal import traversal
from common.folderdel import folderdel
from common.httpresult import httpresult

from dbmysql.models.Folder import Folder
from dbmysql.models.File import File

class FolderDel(View):
    @method_decorator(httpresult)
    def delete(self, request):
        folder_id = request.GET.get('folder_id')
        # 文件夹数据库查询
        folder = Folder.objects.filter(id=folder_id).first()
        if folder is None:
            raise Exception(u'文件夹不存在')
        # 目录地址
        path = getpath('media', folder.url)
        # 查询该目录下的所有子文件
        files = File.objects.filter(pfolder_id=folder_id)
        # 查询该目录下的所有子文件夹
        folders = Folder.objects.filter(parent=folder_id)
        # 删除数据库中的子文件
        for item in files:
            print('item1', item.id)
            item.delete()
        # 删除数据库中的所有子文件夹
        for item in folders:
            print('item2', item.id)
            item.delete()
        # 数据库主目录删除
        folder.delete()
        if folder.id:
            raise Exception(u'数据库文件夹删除失败')
        # 数据库信息删除完成,删除项目中的
        print(path)
        folderdel(path)

        data = {
            'path': path,
            # '文件夹id': folder.id,
            # '文件夹名': folder.name,
        }
        return res(data=data)
