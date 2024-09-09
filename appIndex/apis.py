from ninja import Router
from .schemas import *
from django.shortcuts import get_object_or_404

router = Router()

from ninja.schema import Schema
class ErrorResponse(Schema):
    error: str


#################### FlashcardSet API ###################################################


# # 创建 FlashcardSet

# @router.post("FlashcardSet/",response={200: FlashcardSetOut,400:ErrorResponse},tags=["FlashcardSet"])
# def create_flashcard_set(request, payload: FlashcardSetIn):
#     """
#     创建闪卡集

#     根据传入的请求和负载数据，创建一个新的闪卡集，并将其与请求的用户关联起来。
#     该函数首先会基于传入的闪卡集信息（标题和描述）以及请求的用户创建一个闪卡集实例，
#     然后返回这个闪卡集的外部表示形式。

#     :param request: 请求对象，包含创建闪卡集的用户信息\n
#     :param payload: 闪卡集的输入数据，预期包含标题和描述\n
#     :type payload: FlashcardSetIn\n
#     :return: 创建的闪卡集的外部表示\n
#     :rtype: FlashcardSetOut\n
#     """
    
    
#     try:
#         flashcard_set = FlashcardSet.objects.create(title=payload.title, description=payload.description, user=request.user)
#         return FlashcardSetOut.from_orm(flashcard_set)
#     except Exception as e:
#         #返回错误信息以及状态码

#       return   400,{"error": str(e)}
    
    

# # 获取所有 FlashcardSet
# @router.get("FlashcardSet/list",tags=["FlashcardSet"])
# def list_flashcard_sets(request):
#     """
#     获取所有闪卡集
#     获取所有用户的闪卡集，并返回它们的外部表示形式。
#     :param request: 请求对象，包含创建闪卡集的用户信息\n
#     :return: 所有用户的闪卡集的外部表示\n
#     :rtype: List[FlashcardSetOut]\n
#     """

#     flashcard_sets = FlashcardSet.objects.filter(user=request.user)
#     return [FlashcardSetOut.from_orm(flashcard_set) for flashcard_set in flashcard_sets]

# # 获取单个 FlashcardSet
# @router.get("FlashcardSet/{int:id}",tags=["FlashcardSet"])
# def get_flashcard_set(request, id: int):
#     """
#     获取单个闪卡集
#     获取指定 ID 的闪卡集，并返回它的外部表示形式。
#     :param request: 请求对象，包含创建闪卡集的用户信息\n
#     :param id: 闪卡集的 ID\n
#     :type id: int\n
#     :return: 指定 ID 的闪卡集的外部表示\n
#     :rtype: FlashcardSetOut\n
#     """

#     flashcard_set = get_object_or_404(FlashcardSet, id=id)
#     return FlashcardSetOut.from_orm(flashcard_set)

# # 更新 FlashcardSet
# @router.put("FlashcardSet/{int:id}",tags=["FlashcardSet"])
# def update_flashcard_set(request, id: int, payload: FlashcardSetIn):
#     """
#     更新闪卡集
#     更新指定 ID 的闪卡集，并返回更新后的闪卡集的外部表示形式。
#     :param request: 请求对象，包含创建闪卡集的用户信息\n
#     :param id: 闪卡集的 ID\n
#     :type id: int\n
#     :param payload: 闪卡集的输入数据，预期包含标题和描述\n
#     :type payload: FlashcardSetIn\n
#     """
#     flashcard_set = get_object_or_404(FlashcardSet, id=id)
#     for attr, value in payload.dict().items():
#         setattr(flashcard_set, attr, value)
#     flashcard_set.save()
#     return FlashcardSetOut.from_orm(flashcard_set)

# # 删除 FlashcardSet
# @router.delete("FlashcardSet/{int:id}",tags=["FlashcardSet"])
# def delete_flashcard_set(request, id: int):
#     """
#     删除闪卡集
#     删除指定 ID 的闪卡集。
#     :param request: 请求对象，包含创建闪卡集的用户信息\n
#     :param id: 闪卡集的 ID\n
#     :type id: int\n
#     """

#     flashcard_set = get_object_or_404(FlashcardSet, id=id)
#     flashcard_set.delete()
#     return {"success": True}



