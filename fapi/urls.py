from django.urls import path

from fapi.views.Fileadd import FileAdd
from fapi.views.FileDel import FileDel
from fapi.views.FileRename import FileRename
from fapi.views.FileCopyPaste import FileCopyPaste
from fapi.views.FolderAdd import FolderAdd
from fapi.views.FolderRename import FolderRename
from fapi.views.FolderDel import FolderDel
from fapi.views.Test import Test

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('folderadd/', csrf_exempt(FolderAdd.as_view())),
    path('folderdel/', csrf_exempt(FolderDel.as_view())),
    path('folderrename/', csrf_exempt(FolderRename.as_view())),
    path('fileadd/', csrf_exempt(FileAdd.as_view())),
    path('filedel/', csrf_exempt(FileDel.as_view())),
    path('filerename/', csrf_exempt(FileRename.as_view())),
    path('filecopypaste/', csrf_exempt(FileCopyPaste.as_view())),
    path('test/', Test.as_view()),
]

