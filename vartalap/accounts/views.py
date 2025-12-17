from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
def welcome(request):
    if request.user.is_authenticated:
        return redirect("chat_home")
    return render(request, "welcome.html")
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
    else:
        form = UserCreationForm()

    for field in form.fields.values():
        field.widget.attrs['class'] = 'form-control'

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('login')

    return render(request, 'accounts/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name='accounts/login.html'
def logout_view(request):
    logout(request)
    return render(request,'chat/welcome.html')

@login_required
def update_profile(request):
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()
            return redirect("chat_home")

    else:
        form = ProfileForm(instance=profile)

    return render(request, "chat/profile.html", {
        "form": form,
        "profile": profile,
    })
