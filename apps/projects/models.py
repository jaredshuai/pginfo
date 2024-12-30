from django.db import models

class Project(models.Model):
    """项目模型类"""
    name = models.CharField(max_length=100, verbose_name='项目名称')
    description = models.TextField(blank=True, verbose_name='项目描述')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = verbose_name
        ordering = ['-created_at']

    def __str__(self):
        return self.name 