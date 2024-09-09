from ninja import Router

from .models import Flashcard, FlashcardSet, Progress
from .schemas import FlashcardIn, FlashcardOut, FlashcardSetIn, FlashcardSetOut, ProgressIn, ProgressOut
from django.shortcuts import get_object_or_404

router = Router()

from ninja.schema import Schema
class ErrorResponse(Schema):
    error: str


#################### FlashcardSet API ###################################################


# 创建 FlashcardSet
from django.views.decorators.csrf import csrf_exempt

@router.post("FlashcardSet/",response={200: FlashcardSetOut,400:ErrorResponse},tags=["FlashcardSet"])
@csrf_exempt
def create_flashcard_set(request, payload: FlashcardSetIn):
    """
    创建闪卡集

    根据传入的请求和负载数据，创建一个新的闪卡集，并将其与请求的用户关联起来。
    该函数首先会基于传入的闪卡集信息（标题和描述）以及请求的用户创建一个闪卡集实例，
    然后返回这个闪卡集的外部表示形式。

    :param request: 请求对象，包含创建闪卡集的用户信息\n
    :param payload: 闪卡集的输入数据，预期包含标题和描述\n
    :type payload: FlashcardSetIn\n
    :return: 创建的闪卡集的外部表示\n
    :rtype: FlashcardSetOut\n
    """
    
    
    try:
        flashcard_set = FlashcardSet.objects.create(title=payload.title, description=payload.description, user=request.user)
        return FlashcardSetOut.from_orm(flashcard_set)
    except Exception as e:
        #返回错误信息以及状态码

      return   400,{"error": str(e)}
    
    

# 获取所有 FlashcardSet
@router.get("FlashcardSet/list",tags=["FlashcardSet"])
def list_flashcard_sets(request):
    """
    获取所有闪卡集
    获取所有用户的闪卡集，并返回它们的外部表示形式。
    :param request: 请求对象，包含创建闪卡集的用户信息\n
    :return: 所有用户的闪卡集的外部表示\n
    :rtype: List[FlashcardSetOut]\n
    """

    flashcard_sets = FlashcardSet.objects.filter(user=request.user)
    return [FlashcardSetOut.from_orm(flashcard_set) for flashcard_set in flashcard_sets]

# 获取单个 FlashcardSet
@router.get("FlashcardSet/{int:id}",tags=["FlashcardSet"])
def get_flashcard_set(request, id: int):
    """
    获取单个闪卡集
    获取指定 ID 的闪卡集，并返回它的外部表示形式。
    :param request: 请求对象，包含创建闪卡集的用户信息\n
    :param id: 闪卡集的 ID\n
    :type id: int\n
    :return: 指定 ID 的闪卡集的外部表示\n
    :rtype: FlashcardSetOut\n
    """

    flashcard_set = get_object_or_404(FlashcardSet, id=id)
    return FlashcardSetOut.from_orm(flashcard_set)

# 更新 FlashcardSet
@router.put("FlashcardSet/{int:id}",tags=["FlashcardSet"])
def update_flashcard_set(request, id: int, payload: FlashcardSetIn):
    """
    更新闪卡集
    更新指定 ID 的闪卡集，并返回更新后的闪卡集的外部表示形式。
    :param request: 请求对象，包含创建闪卡集的用户信息\n
    :param id: 闪卡集的 ID\n
    :type id: int\n
    :param payload: 闪卡集的输入数据，预期包含标题和描述\n
    :type payload: FlashcardSetIn\n
    """
    flashcard_set = get_object_or_404(FlashcardSet, id=id)
    for attr, value in payload.dict().items():
        setattr(flashcard_set, attr, value)
    flashcard_set.save()
    return FlashcardSetOut.from_orm(flashcard_set)

# 删除 FlashcardSet
@router.delete("FlashcardSet/{int:id}",tags=["FlashcardSet"])
def delete_flashcard_set(request, id: int):
    """
    删除闪卡集
    删除指定 ID 的闪卡集。
    :param request: 请求对象，包含创建闪卡集的用户信息\n
    :param id: 闪卡集的 ID\n
    :type id: int\n
    """

    flashcard_set = get_object_or_404(FlashcardSet, id=id)
    flashcard_set.delete()
    return {"success": True}



##################### Flashcard API #########################################################



# 创建 Flashcard
@router.post("Flashcard/",response={200: FlashcardOut,400:ErrorResponse},tags=["Flashcard"])
#                                                                                       需要添加身份验证，cardset的user应和请求的user一致
def create_flashcard(request, payload: FlashcardIn):
    """
    创建闪卡
    根据传入的请求和负载数据，创建一个新的闪卡，并将其与请求的用户关联起来。
    该函数首先会基于传入的闪卡信息（前半部分内容、后半部分内容、闪卡集 ID）以及请求的用户创建一个闪卡实例，
    然后返回这个闪卡的外部表示形式。
    :param request: 请求对象，包含创建闪卡的用户信息\n
    :param payload: 闪卡的输入数据，预期包含前半部分内容、后半部分内容、闪卡集 ID\n
    :type payload: FlashcardIn\n
    :return: 创建的闪卡的外部表示\n
    :rtype: FlashcardOut\n
    """

    try:
        cardset = get_object_or_404(FlashcardSet, id=payload.cardset_id)
        flashcard = Flashcard.objects.create(front_content=payload.front_content, back_content=payload.back_content, cardset=cardset)
        return FlashcardOut.from_orm(flashcard)
    except Exception as e:
        #返回错误信息以及状态码
        return   400,{"error": str(e)}
    

# 获取指定闪卡集下所有 Flashcard
@router.get("Flashcard/list",tags=["Flashcard"])
def list_flashcards(request,cardset_id: int):
    """
    获取用户指定闪卡集所有的闪卡，并返回它们的外部表示形式。
    :param request: 请求对象，包含创建闪卡的用户信息\n
    :param cardset_id: 闪卡集的 ID\n
    :return: 所有用户的闪卡的外部表示\n
    :rtype: List[FlashcardOut]\n
    """
    flashcards = Flashcard.objects.filter(cardset_id=cardset_id)
    return [FlashcardOut.from_orm(flashcard) for flashcard in flashcards]

# 获取单个 Flashcard
@router.get("Flashcard/{int:id}",tags=["Flashcard"])
def get_flashcard(request, id: int):
    """
    获取单个闪卡
    获取指定 ID 的闪卡，并返回它的外部表示形式。
    :param request: 请求对象，包含创建闪卡的用户信息\n
    :param id: 闪卡的 ID\n
    :type id: int\n
    :return: 指定 ID 的闪卡的外部表示\n
    :rtype: FlashcardOut\n
    """
    flashcard = get_object_or_404(Flashcard, id=id)
    return FlashcardOut.from_orm(flashcard)

# 更新 Flashcard
@router.put("Flashcard/{int:id}",tags=["Flashcard"])
def update_flashcard(request, id: int, payload: FlashcardIn):
    """
    更新闪卡
    更新指定 ID 的闪卡，并返回更新后的闪卡的外部表示形式。
    :param request: 请求对象，包含创建闪卡的用户信息\n
    :param id: 闪卡的 ID\n
    :type id:int\n
    :param payload: 闪卡的输入数据，预期包含前半部分内容、后半部分内容、闪卡集 ID\n
    :type payload: FlashcardIn\n
    """
    flashcard = get_object_or_404(Flashcard, id=id)
    for attr, value in payload.dict().items():       
        setattr(flashcard, attr, value)
    flashcard.save()
    return FlashcardOut.from_orm(flashcard)

# 删除 Flashcard
@router.delete("Flashcard/{int:id}",tags=["Flashcard"])
def delete_flashcard(request, id: int):
    """
    删除闪卡
    删除指定 ID 的闪卡。
    :param request: 请求对象，包含创建闪卡的用户信息\n
    :param id: 闪卡的 ID\n
    :type id: int\n
    """
    flashcard = get_object_or_404(Flashcard, id=id)
    flashcard.delete()
    return {"success": True}

# study业务逻辑
# knowledge_level 增加1
@router.put("Flashcard/study/{int:id}",tags=["Flashcard"])
def studyed(request, id: int):
    """
    学习闪卡
    学习指定 ID 的闪卡，并返回更新后的闪卡的外部表示形式。
    :param id: 闪卡的 ID\n
    :type id: int\n
    :return: 指定 ID 的闪卡的外部表示\n
    :rtype: FlashcardOut\n
    """
    flashcard = get_object_or_404(Flashcard, id=id)
    flashcard.knowledge_level += 1
    flashcard.save()
    return FlashcardOut.from_orm(flashcard)

    


