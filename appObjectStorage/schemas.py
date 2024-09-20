

from datetime import datetime
from typing import Optional

from pydantic import ConfigDict
from pydantic import BaseModel, ConfigDict
from ninja.files import UploadedFile
from ninja import Schema



# 定义一个模型来接受上传文件
class StoredFileIn(Schema):
    file: UploadedFile
    filename: str
    size: int
    file_type: Optional[str] = None
    bucket: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[str] = None

    model_config = ConfigDict(arbitrary_types_allowed=True)
    

    


class StoredFileOut(Schema):
    id: int  # 主键ID
    file: str  # 文件路径
    filename: str  # 文件名
    size: int  # 文件大小
    file_type: Optional[str]  # 文件类型
    bucket: Optional[str]  # 存储桶
    description: Optional[str]  # 文件描述
    tags: Optional[str]  # 标签
    upload_time: datetime  # 上传时间
    last_modified: datetime  # 最后修改时间
    user_id: int  # 用户ID
    get_absoulte_url: str
    
    @classmethod
    def from_orm(cls, obj):
        # 将 Django ORM 对象转换为 Pydantic 模型
        return cls(
            id=obj.id,
            file=str(obj.file),
            filename=obj.filename,
            size=obj.size,
            file_type=obj.file_type,
            bucket=obj.bucket,
            description=obj.description,
            tags=obj.tags,
            upload_time=obj.upload_time,
            last_modified=obj.last_modified,
            user_id=obj.user_id,
            get_absoulte_url=obj.get_absolute_url
        )