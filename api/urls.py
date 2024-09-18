from django.urls import path

from . import views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView #type: ignore

urlpatterns = [
    path('', views.index, name="index"),
    # User
    path('user/', views.UserViewSet.as_view(), name='user-create'),
    # JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Subjects
    path('subject/', views.SubjectViewSet.as_view()),
    path('subject/<int:pk>', views.SubjectViewSet.as_view()),
    # Categories
    path('categories/', views.CategoriesViewSet.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoriesViewSet.as_view(), name='category-detail'),
    # path('api/category/<id>', views.CategoryViewSet.as_view()),
    # Learn
    path('learn/', views.LearnViewSet.as_view(), name='learn-list'),  # To get all Learn objects (optional)
    path('learn/category/<int:category_id>/', views.LearnViewSet.as_view(), name='learn-by-category'),  # To get Learn objects by category
    path('learn/<int:pk>/', views.LearnViewSet.as_view(), name='learn-detail'),  # To get/update/delete a specific Learn object
    # Practice

    path('practice-sections/', views.PracticeSectionsViewSet.as_view(), name='practice-sections-list'),  # To get all PracticeSections or create a new one
    path('practice-sections/category/<int:category_id>/', views.PracticeSectionsViewSet.as_view(), name='practice-sections-by-category'),  # To get PracticeSections by category
    path('practice-sections/<int:pk>/', views.PracticeSectionsViewSet.as_view(), name='practice-section-detail'),  # To get/update/delete a specific PracticeSection

    # path('api/practice/all/<id>', views.PracticeSectionsViewSet.as_view()),
    # path('api/practice/<id>', views.LearnViewSet.as_view()),
    path('questions/<id>', views.QuestionsViewSet.as_view()),
    # Test
    path('test-data/<id>', views.LearnViewSet.as_view()),
]
