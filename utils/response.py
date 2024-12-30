from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework import status

def custom_response(data=None, msg="success", code=0):
    """
    自定义响应格式
    :param data: 响应数据
    :param msg: 响应信息
    :param code: 响应代码，0表示成功，1表示错误
    """
    return Response({
        "code": code,
        "msg": msg,
        "data": data
    })

def custom_exception_handler(exc, context):
    """
    自定义异常处理
    :param exc: 异常对象
    :param context: 异常上下文
    """
    response = exception_handler(exc, context)
    
    if response is not None:
        # 获取具体的错误信息
        if isinstance(response.data, dict):
            msg = next(iter(response.data.values()))[0] if response.data else "请求错误"
        elif isinstance(response.data, list):
            msg = response.data[0] if response.data else "请求错误"
        else:
            msg = str(response.data)

        response.data = {
            "code": 1,
            "msg": msg,
            "data": None
        }

    return response 