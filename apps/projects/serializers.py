from rest_framework import serializers
from .models import Project
from apps.devices.models import Device

class DeviceInProjectSerializer(serializers.ModelSerializer):
    """项目中显示的设备信息序列化器"""

    class Meta:
        model = Device
        fields = ['id', 'name', 'brand', 'model', 'ip_address', 'location', 'status']

class ProjectSerializer(serializers.ModelSerializer):
    """项目序列化器"""
    device_count = serializers.SerializerMethodField()  # 设备数量
    devices = DeviceInProjectSerializer(many=True, read_only=True)  # 嵌套设备信息

    class Meta:
        model = Project
        fields = [ 'id', 'name', 'description', 'device_count', 'devices', 'created_at', 'updated_at' ]
        read_only_fields = ['created_at', 'updated_at']

    def get_device_count(self, obj):
        """获取项目下的设备数量"""
        return obj.devices.count() 
