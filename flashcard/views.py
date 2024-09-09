from django.shortcuts import render,get_object_or_404

# Create your views here.

from .models import FlashcardSet
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'flashcard/index.html')

@login_required
def card(request,cardset_id):
    #获取get请求中的参数cardset_id

    cardset = get_object_or_404(FlashcardSet, pk=cardset_id)
    cardset_title = cardset.title
    
    return render(request, 'flashcard/card.html', {'cardset_id': cardset_id,"cardset_title":cardset_title})


@login_required
def study(request,cardset_id):
    cardset = get_object_or_404(FlashcardSet, pk=cardset_id)
    cardset_title = cardset.title
    return render(request, 'flashcard/study.html',{'cardset_id': cardset_id,"cardset_title":cardset_title})