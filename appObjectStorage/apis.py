from ninja import  Router
from typing import List
# 假设已定义的模型和 schema
from .models import StoredFile
from .schemas import StoredFileIn, StoredFileOut

# 创建 API 路由器
router = Router()

from ninja.schema import Schema
class ErrorResponse(Schema):
    error: str

# 文件上传处理逻辑
@router.post("/files/", response={201: StoredFileOut},tags=["文件对象存储"])
def upload_file(request, payload: StoredFileIn):
    # 处理上传文件逻辑
    file = payload.file
    filename = payload.filename
    size = payload.size
    file_type = payload.file_type
    bucket = payload.bucket
    description = payload.description
    tags = payload.tags
    
    user = request.user  # 假设当前用户已登录
    
    stored_file = StoredFile(
        file=file,
        filename=filename,
        size=size,
        file_type=file_type,
        bucket=bucket,
        description=description,
        tags=tags,
        user=user
    )
    stored_file.save()
    
    return 201, StoredFileOut.from_orm(stored_file)

# 获取文件详情
@router.get("/files/{int:id}", response={201:StoredFileOut, 404:ErrorResponse},tags=["文件对象存储"])
def get_file(request, id: int):
    try:
        stored_file = StoredFile.objects.get(id=id)
        return 201, StoredFileOut.from_orm(stored_file)
    except StoredFile.DoesNotExist:
        return 404, {"error": "File not found"}

# 获取所有文件列表
@router.get("/files/", response=List[StoredFileOut],tags=["文件对象存储"])
def list_files(request):
    files = StoredFile.objects.all()
    return [StoredFileOut.from_orm(file) for file in files]

# 删除文件
@router.delete("/files/{int:id}",tags=["文件对象存储"], response={204: None, 404: ErrorResponse})
def delete_file(request, id: int):
    try:
        stored_file = StoredFile.objects.get(id=id)
        stored_file.delete()
        return 204, {"detail": "File deleted successfully"}
    except StoredFile.DoesNotExist:
        return 404, {"error": "File not found"}

# 更新文件
@router.put("/files/{int:id}", response={200: StoredFileOut , 404 : ErrorResponse} ,tags=["文件对象存储"])
def update_file(request, id: int, payload: StoredFileIn):
    try:
        stored_file = StoredFile.objects.get(id=id)
        
        # 更新文件信息
        stored_file.filename = payload.filename or stored_file.filename
        stored_file.size = payload.size or stored_file.size
        stored_file.file_type = payload.file_type or stored_file.file_type
        stored_file.bucket = payload.bucket or stored_file.bucket
        stored_file.description = payload.description or stored_file.description
        stored_file.tags = payload.tags or stored_file.tags
        
        stored_file.save()
        
        return 200, StoredFileOut.from_orm(stored_file)
    except StoredFile.DoesNotExist:
        return 404, {"error": "File not found"}

