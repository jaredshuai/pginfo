from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Project
from .serializers import ProjectSerializer, DeviceInProjectSerializer
from utils.response import custom_response

class DevicesPagination(PageNumberPagination):
    """设备列表分页器"""
    page_size = 10  # 每页显示的记录数
    page_size_query_param = 'page_size'  # 允许客户端通过此参数指定每页记录数
    max_page_size = 100  # 每页最大记录数

class ProjectViewSet(viewsets.ModelViewSet):
    """项目视图集"""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def list(self, request, *args, **kwargs):
        """获取项目列表"""
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return custom_response(self.get_paginated_response(serializer.data).data)
        serializer = self.get_serializer(queryset, many=True)
        return custom_response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """获取项目详情"""
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return custom_response(serializer.data)

    def create(self, request, *args, **kwargs):
        """创建项目"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return custom_response(serializer.data, msg="创建成功")

    def update(self, request, *args, **kwargs):
        """更新项目"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return custom_response(serializer.data, msg="更新成功")

    def destroy(self, request, *args, **kwargs):
        """删除项目"""
        instance = self.get_object()
        self.perform_destroy(instance)
        return custom_response(None, msg="删除成功")

    @action(detail=True, methods=['get'])
    def devices(self, request, pk=None):
        """获取项目下的设备列表（分页）"""
        project = self.get_object()
        paginator = DevicesPagination()
        devices = project.devices.all()
        result = paginator.paginate_queryset(devices, request)
        serializer = DeviceInProjectSerializer(result, many=True)
        return custom_response(paginator.get_paginated_response(serializer.data).data)

    def get_queryset(self):
        """支持按名称搜索"""
        queryset = Project.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset 