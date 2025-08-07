from fastapi.responses import JSONResponse

def custom_response(data, msg="success", code=0):
    return JSONResponse(content={"code": code, "msg": msg, "data": data})

