from django.db import models
from django.contrib.auth.models import User
from dbmysql.models.Folder import Folder
from dbmysql.models.File import File


class Permission(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=u'使用者',
        on_delete=models.CASCADE,
        related_name='permission'
    )
    file = models.ForeignKey(
        File,
        verbose_name=u'文件权限',
        on_delete=models.CASCADE,
        related_name=u'permissionFile',
        null=True,
        blank=True
    )
    folder = models.ForeignKey(
        Folder,
        verbose_name=u'文件夹权限',
        on_delete=models.CASCADE,
        related_name=u'permissionFolder',
        null=True,
        blank=True
    )
    right = models.BooleanField(
        choices=(
            (0, '可读'),
            (1, '读写')
        ),
        default=1
    )

    class Meta:
        verbose_name = u'权限表'
        verbose_name_plural = u'权限表'

    def __str__(self):
        return u'%s 权限表' % self.user.username
