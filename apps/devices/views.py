from rest_framework import viewsets, filters
from .models import Device
from .serializers import DeviceSerializer
from utils.response import custom_response

class DeviceViewSet(viewsets.ModelViewSet):
    """设备视图集"""
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filterset_fields = ['project', 'type']
    search_fields = ['name', 'ip_address']
    ordering_fields = ['created_at', 'name']

    def list(self, request, *args, **kwargs):
        """获取设备列表"""
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return custom_response(self.get_paginated_response(serializer.data).data)
        serializer = self.get_serializer(queryset, many=True)
        return custom_response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """获取设备详情"""
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return custom_response(serializer.data)

    def create(self, request, *args, **kwargs):
        """创建设备"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return custom_response(serializer.data, msg="创建成功")

    def update(self, request, *args, **kwargs):
        """更新设备"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return custom_response(serializer.data, msg="更新成功")

    def destroy(self, request, *args, **kwargs):
        """删除设备"""
        instance = self.get_object()
        self.perform_destroy(instance)
        return custom_response(None, msg="删除成功")

    def get_queryset(self):
        """支持按项目ID和设备类型过滤"""
        queryset = Device.objects.all()
        project_id = self.request.query_params.get('project', None)
        device_type = self.request.query_params.get('type', None)

        if project_id is not None:
            queryset = queryset.filter(project_id=project_id)
        if device_type is not None:
            queryset = queryset.filter(type=device_type)
            
        return queryset 