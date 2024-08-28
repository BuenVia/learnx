from django.contrib.auth.models import User
from django.http import HttpResponse #type: ignore
from rest_framework import status, generics #type: ignore
from rest_framework.views import APIView #type: ignore
from rest_framework.response import Response #type: ignore
from rest_framework.permissions import AllowAny #type: ignore

from .models import Subject, Category, Learn, PracticeSection, Questions, TestData
from .serializer import SubjectSerializer, CategorySerializer, LearnSerializer, PracticeSectionSerializer, QuestionsSerializer, TestDataSerializer, UserSerializer

# Create your views here.
def index(request):
    return HttpResponse("Welcome to the LangX API...")

## Users
class UserViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

### Categories
class SubjectViewSet(APIView):
    def get(self, request, *args, **kwargs):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CategoriesViewSet(APIView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CategoryViewSet(APIView):
    def get(self, request, id, *args, **kwargs):
        categories = Category.objects.filter(subject=id)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

### Learn
class LearnViewSet(APIView):
    def get(self, request, id, *args, **kwargs):
        learn = Learn.objects.filter(category=id)
        serializer = LearnSerializer(learn, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class LearnPageViewSet(APIView):
    def get(self, request, id, *args, **kwargs):
        learn = Learn.objects.filter(id=id)
        serializer = LearnSerializer(learn, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
### Practice
class PracticeSectionsViewSet(APIView):
    def get(self, request, id, *args, **kwargs):
        psecs = PracticeSection.objects.filter(category=id)
        serializer = PracticeSectionSerializer(psecs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PracticeSectionViewSet(APIView):
    def get(self, request, id, *args, **kwargs):
        psec = PracticeSection.objects.filter(id=id)
        serializer = PracticeSectionSerializer(psec, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class QuestionsViewSet(APIView):
    def get(self, request, id, *args, **kwargs):
        questions = Questions.objects.filter(practice_section=id)
        serializer = QuestionsSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

### Test
class TestDataViewSet(APIView):
    def get(self, request, id, *args, **kwargs):
        test_data = TestData.objects.filter(category=id)
        serializer = TestDataSerializer(test_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)





