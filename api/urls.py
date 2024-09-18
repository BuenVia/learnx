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
    # Subjects
    path('api/subject/', views.SubjectViewSet.as_view()),
    path('api/subject/<int:pk>', views.SubjectViewSet.as_view()),
    # Categories
    path('api/categories/', views.CategoriesViewSet.as_view(), name='category-list'),
    path('api/categories/<int:pk>/', views.CategoriesViewSet.as_view(), name='category-detail'),
    # path('api/category/<id>', views.CategoryViewSet.as_view()),
    # Learn
    path('api/learn/', views.LearnViewSet.as_view(), name='learn-list'),  # To get all Learn objects (optional)
    path('api/learn/category/<int:category_id>/', views.LearnViewSet.as_view(), name='learn-by-category'),  # To get Learn objects by category
    path('api/learn/<int:pk>/', views.LearnViewSet.as_view(), name='learn-detail'),  # To get/update/delete a specific Learn object
    # Practice

    path('api/practice-sections/', views.PracticeSectionsViewSet.as_view(), name='practice-sections-list'),  # To get all PracticeSections or create a new one
    path('api/practice-sections/category/<int:category_id>/', views.PracticeSectionsViewSet.as_view(), name='practice-sections-by-category'),  # To get PracticeSections by category
    path('api/practice-sections/<int:pk>/', views.PracticeSectionsViewSet.as_view(), name='practice-section-detail'),  # To get/update/delete a specific PracticeSection

    # path('api/practice/all/<id>', views.PracticeSectionsViewSet.as_view()),
    # path('api/practice/<id>', views.LearnViewSet.as_view()),
    path('api/questions/<id>', views.QuestionsViewSet.as_view()),
    # Test
    path('api/test-data/<id>', views.LearnViewSet.as_view()),
]
