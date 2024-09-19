from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, LoginForm

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        return render(request, 'webapp/index.html')

def register(request):
    user_form = CreateUserForm()
    if request.method == "POST":
        user_form = CreateUserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect("login")
    context = {}
    context['user_form'] = user_form
    return render(request, 'webapp/register.html', context=context)


def login(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        form = LoginForm()
        if request.method == "POST":
            form = LoginForm(request, data=request.POST)
            if form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    return redirect("dashboard")
        context = {'loginform': form}
        return render(request, 'webapp/login.html', context=context)

def logout(request):
    auth.logout(request)
    return redirect("index")

@login_required(login_url="login")
def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        context = {}
        context['username'] = request.user
        return render(request, 'webapp/dashboard.html', context=context)
    
@login_required(login_url="login")
def account(request):
    if request.user.is_authenticated:
        # properties = Property.objects.filter(user_id=request.user, is_delete=False).all()
        # business = Business.objects.filter()
        context = {}
        context['user'] = request.user
        # context['properties'] = properties
        return render(request, 'webapp/account.html', context=context)