from django.db import models
from apps.projects.models import Project

class Device(models.Model):
    """设备模型类"""
    name = models.CharField(max_length=100, verbose_name="设备名称")
    brand = models.CharField(max_length=100, null=True, blank=True, verbose_name="品牌")
    model = models.CharField(max_length=100, null=True, blank=True, verbose_name="设备型号")
    
    # 项目关联
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='devices',
        verbose_name="所属项目"
    )

    # 网络配置
    ip_address = models.GenericIPAddressField(
        protocol='both', 
        unpack_ipv4=False, 
        null=True, 
        blank=True, 
        verbose_name="IP地址"
    )
    subnet_mask = models.GenericIPAddressField(
        protocol='both', 
        unpack_ipv4=False, 
        null=True, 
        blank=True, 
        verbose_name="子网掩码"
    )
    gateway = models.GenericIPAddressField(
        protocol='both', 
        unpack_ipv4=False, 
        null=True, 
        blank=True, 
        verbose_name="网关"
    )

    # 设备照片
    photo = models.ImageField(upload_to='devices/photos/', null=True, blank=True, verbose_name="设备照片")

    # 地理位置
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, 
        null=True, blank=True, 
        verbose_name="经度"
    )
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, 
        null=True, blank=True, 
        verbose_name="纬度"
    )

    # 远程控制信息
    remote_code = models.CharField(max_length=50, null=True, blank=True, verbose_name="远程控制码")
    remote_password = models.CharField(max_length=50, null=True, blank=True, verbose_name="远程控制密码")

    # 产品说明书
    product_manual = models.FileField(
        upload_to='devices/manuals/', 
        null=True, 
        blank=True, 
        verbose_name="产品说明书"
    )

    # 时间信息
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "设备"
        verbose_name_plural = verbose_name
        ordering = ['-created_at']

    def __str__(self):
        model_info = f" - {self.model}" if self.model else ""
        return f"{self.name}{model_info} ({self.project.name})"
