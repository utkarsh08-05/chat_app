from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

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
    return redirect('login')
