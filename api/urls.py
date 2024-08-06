from django.urls import path

from . import views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView #type: ignore

urlpatterns = [
    path('', views.index, name="index"),
    # User
    path('api/user/', views.UserViewSet.as_view(), name='user-create'),
    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Categories
    path('api/subject', views.SubjectViewSet.as_view()),
    path('api/category/', views.CategoriesViewSet.as_view()),
    path('api/category/<id>', views.CategoryViewSet.as_view()),
    # Learn
    path('api/learn/<id>', views.LearnViewSet.as_view()),
    path('api/learn/page/<id>', views.LearnPageViewSet.as_view()),
    # Practice
    path('api/practice/all/<id>', views.PracticeSectionsViewSet.as_view()),
    path('api/practice/<id>', views.LearnViewSet.as_view()),
    path('api/questions/<id>', views.QuestionsViewSet.as_view()),
    # Test
    path('api/test-data/<id>', views.LearnViewSet.as_view()),
]
