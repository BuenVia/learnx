from django.urls import path
from . import views

from .views import register_view, CustomLoginView, home_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path('', views.index, name="index"),
    path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
