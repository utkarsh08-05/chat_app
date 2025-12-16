from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

@login_required
def welcome(request):
    if request.user.is_authenticated:
        return redirect("chat_home")
    return render(request, "welcome.html")
