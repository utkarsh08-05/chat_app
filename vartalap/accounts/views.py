from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request,'accounts/register.html',{'form':form})
class CustomLoginView(LoginView):
    template_name='accounts/login.html'
def logout_view(request):
    logout(request)
    return redirect('login')
