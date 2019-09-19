from django.contrib.auth.models import User
from django.db import models



class Folder(models.Model):
    name = models.CharField(
        max_length=200,
        default=u'新建文件夹'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        verbose_name=u'父文件夹',
        related_name=u'folder_son',
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
    creater = models.ForeignKey(
        User,
        verbose_name=u'创建者',
        on_delete=models.CASCADE
    )
    createtime = models.DateField(
        verbose_name=u'创建时间',
        auto_now_add=True
    )

    class Meta:
        unique_together = ['name', 'parent']
        ordering = ['id']
        verbose_name = u'文件夹'
        verbose_name_plural = u'文件夹'

    def __str__(self):
        return u'%s' % self.name
