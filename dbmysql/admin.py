from django.contrib import admin
from dbmysql.models.Folder import Folder
from dbmysql.models.File import File
from dbmysql.models.Permission import Permission

# Register your models here.
admin.site.register(File)
admin.site.register(Folder)
admin.site.register(Permission)
