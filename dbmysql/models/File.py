from django.db import models
from dbmysql.models.Folder import Folder
from django.contrib.auth.models import User


class File(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name=u'文件名',
        default=u'新建文件'
    )
    pfolder = models.ForeignKey(
        Folder,
        verbose_name=u'所属文件夹',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    filetype = models.CharField(
        max_length=200,
        verbose_name='文件类型',
        null=True,
        blank=True
    )
    depth = models.IntegerField(
        default=1,
        verbose_name=u'目录深度'
    )
    url = models.CharField(
        max_length=200,
        verbose_name=u'相对路径',
        default=''
    )
    size = models.IntegerField(
        default=0,
        verbose_name=u'文件大小'
    )

    creater = models.ForeignKey(
        User,
        verbose_name=u'创建者',
        on_delete=models.CASCADE,
        related_name='file',
        null=True
    )

    modifytime = models.DateField(
        verbose_name=u'最后修改时间',
        auto_now=True
    )
    createtime = models.DateField(
        verbose_name=u'创建时间',
        auto_now_add=True
    )

    class Meta:
        unique_together = ['name', 'pfolder']
        verbose_name = u'文件'
        verbose_name_plural = u'文件'

    def __str__(self):
        return u'%s' % self.name
