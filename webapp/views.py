from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegisterForm

from api.models import Subject

def home_view(request):
    subjects = Subject.objects.filter(user_id=request.user.id)
    context = {"subjects": subjects}
    return render(request, 'webapp/home.html', context=context)

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately after registration
            return redirect('home')  # Redirect to the homepage or dashboard after registration
    else:
        form = RegisterForm()
    
    return render(request, 'webapp/register.html', {'form': form})


@login_required
def dashboard(request):
    return HttpResponse("Dashboard")

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'webapp/login.html'

    def get_success_url(self):
        return redirect('home').url  # Redirect to the homepage or dashboard after login
