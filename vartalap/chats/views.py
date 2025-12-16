from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Message

@login_required
def user_list (request):
    users=User.objects.exclude(id=request.user.id)
    return render(request,'chat/all_chat.html',{'users':users})
@login_required
def chat_detail(request,user_id):
    other_user=get_object_or_404(User,id=user_id)
    messages=Message.objects.filter(
        Q(sender=request.user ,receiver=other_user)|
        Q(sender=other_user ,receiver=request.user)
    ).order_by('timestamp')
    if request.method=='POST':
        content=request.POST.get('content')
        if content:
            Message.objects.create(
                sender=request.user,
                receiver=other_user,
                content=content
            )
        return redirect('chat_detail',user_id=other_user.id)
    return render(
        request,'chat/chat_detail.html',{
            'other_user':other_user,
            'messages':messages
        }
    )

  
# Create your views here.
