from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # Categories
    path('api/category', views.GrammarCategoryViewSet.as_view()),
    path('api/sub-category/', views.GrammarSubCategoriesViewSet.as_view()),
    path('api/sub-category/<id>', views.GrammarSubCategoryViewSet.as_view()),
    # Tests
    path('api/tests/<id>', views.GrammarTestSectionsViewSet.as_view()),
    path('api/section/questions/<id>', views.GrammarTestSectionViewSet.as_view()),
    path('api/questions/<id>', views.GrammarTestViewSet.as_view()),
    # Blogs
    path('api/blogs/', views.GrammarBlogsViewSet.as_view()),
    path('api/blogs/<id>', views.GrammarBlogViewSet.as_view()),
    path('api/blogs/assess/<id>', views.GrammarAssessmentViewSet.as_view()),
    
    
]
