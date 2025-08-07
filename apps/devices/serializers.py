from rest_framework import serializers
from .models import Device

class DeviceSerializer(serializers.ModelSerializer):
    """设备序列化器"""
    project_name = serializers.CharField(source='project.name', read_only=True)  # 项目名称
    project_description = serializers.CharField(source='project.description', read_only=True)  # 项目描述

    def to_internal_value(self, data):
        """处理空字符串"""
        # 将空字符串转换为None
        for field in ['ip_address', 'subnet_mask', 'gateway', 'longitude', 'latitude']:
            if field in data and data[field] == "":
                data[field] = None
        return super().to_internal_value(data)

    class Meta:
        model = Device
        fields = [
            'id', 'name', 'brand', 'model',
            'project', 'project_name', 'project_description',  # 项目相关字段
            'ip_address', 'subnet_mask', 'gateway', 'location', 'status',
            'photo', 'longitude', 'latitude',
            'remote_code', 'remote_password',
            'product_manual',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {
            'photo': {'use_url': True},  # 使用完整URL
            'product_manual': {'use_url': True},  # 使用完整URL
            'ip_address': {'required': False, 'allow_null': True},  # IP地址为可选
            'subnet_mask': {'required': False, 'allow_null': True},  # 子网掩码为可选
            'gateway': {'required': False, 'allow_null': True},  # 网关为可选
            'longitude': {'required': False, 'allow_null': True},  # 经度为可选
            'latitude': {'required': False, 'allow_null': True},  # 纬度为可选
            'brand': {'required': False, 'allow_blank': True},  # 品牌可以为空
            'model': {'required': False, 'allow_blank': True},  # 型号可以为空
            'remote_code': {'required': False, 'allow_blank': True},  # 远程控制码可以为空
            'remote_password': {'required': False, 'allow_blank': True},  # 远程密码可以为空
            'location': {'required': False, 'allow_blank': True},  # 位置可以为空
            'status': {'required': False, 'allow_blank': True},  # 状态可以为空
        } 
