"""pginfobackend URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger文档配置
schema_view = get_schema_view(
    openapi.Info(
        title="设备信息管理系统 API",
        default_version='v1',
        description="""
设备信息管理系统的API文档

响应格式说明：
```json
{
    "code": 0,    # 响应代码：0表示成功，1表示错误
    "msg": "success",    # 响应信息
    "data": {    # 响应数据，错误时为null
        ...    # 具体的数据内容
    }
}
```

分页响应格式：
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "count": 100,    # 总记录数
        "next": "http://api.example.org/accounts/?page=2",    # 下一页链接
        "previous": null,    # 上一页链接
        "results": [    # 当前页数据
            {
                ...
            }
        ]
    }
}
```

错误响应示例：
```json
{
    "code": 1,
    "msg": "设备不存在",
    "data": null
}
```
""",
        terms_of_service="",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/projects/', include('apps.projects.urls')),
    path('api/devices/', include('apps.devices.urls')),
    
    # Swagger文档URL
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 