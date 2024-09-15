from django.contrib.auth.models import User
from django.http import HttpResponse #type: ignore
from django.shortcuts import get_object_or_404
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
    def get(self, request, pk=None, *args, **kwargs):
        # Filter subjects by the logged-in user
        user_id = request.query_params.get('user_id')
        if pk is not None:
            # Retrieve a single subject associated with the user by its ID
            subject = get_object_or_404(Subject, pk=pk, user_id=user_id)
            serializer = SubjectSerializer(subject)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Retrieve all subjects associated with the user
            subjects = Subject.objects.filter(user_id=user_id)
            serializer = SubjectSerializer(subjects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
   
    def post(self, request, *args, **kwargs):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, *args, **kwargs):
        try:
            subject = Subject.objects.get(pk=kwargs['pk'])
        except Subject.DoesNotExist:
            return Response({"error": "Subject not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            subject = Subject.objects.get(pk=kwargs['pk'])
        except Subject.DoesNotExist:
            return Response({"error": "Subject not found."}, status=status.HTTP_404_NOT_FOUND)

        subject.delete()
        return Response({"message": "Subject deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

class CategoriesViewSet(APIView):
    def get(self, request, pk=None, *args, **kwargs):
        user_id = request.query_params.get('user_id')
        # Filter categories by the logged-in user
        if pk is not None:
            print(pk)
            # Retrieve a single category associated with the user by its ID
            category = get_object_or_404(Category, pk=pk, user_id=user_id)
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Retrieve all categories associated with the user
            categories = Category.objects.filter(user_id=user_id)
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class CategoryViewSet(APIView):
#     def get(self, request, id, *args, **kwargs):
#         categories = Category.objects.filter(subject=id)
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

### Learn
class LearnViewSet(APIView):
    def get(self, request, category_id=None, pk=None, *args, **kwargs):
        # If pk is provided, return a specific Learn object by its primary key
        if pk is not None:
            learn = get_object_or_404(Learn, pk=pk)
            serializer = LearnSerializer(learn)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # If category_id is provided, filter Learn objects by category_id
        if category_id is not None:
            learn = Learn.objects.filter(category=category_id)
            serializer = LearnSerializer(learn, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # If neither is provided, return all Learn objects (optional)
        learn = Learn.objects.all()
        serializer = LearnSerializer(learn, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # Create a new Learn object
        serializer = LearnSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        # Update an existing Learn object by primary key
        learn = get_object_or_404(Learn, pk=pk)
        serializer = LearnSerializer(learn, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        # Delete a specific Learn object by primary key
        learn = get_object_or_404(Learn, pk=pk)
        learn.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# class LearnPageViewSet(APIView):
#     def get(self, request, id, *args, **kwargs):
#         learn = Learn.objects.filter(id=id)
#         serializer = LearnSerializer(learn, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
### Practice
class PracticeSectionsViewSet(APIView):
    def get(self, request, category_id=None, pk=None, *args, **kwargs):
        # Get a specific PracticeSection object by its primary key
        if pk is not None:
            practice_section = get_object_or_404(PracticeSection, pk=pk)
            serializer = PracticeSectionSerializer(practice_section)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # Get all PracticeSection objects filtered by category_id
        if category_id is not None:
            psecs = PracticeSection.objects.filter(category=category_id)
            serializer = PracticeSectionSerializer(psecs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Get all PracticeSection objects if no category_id or pk is provided
        psecs = PracticeSection.objects.all()
        serializer = PracticeSectionSerializer(psecs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # Create a new PracticeSection object
        serializer = PracticeSectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        # Update a specific PracticeSection object by its primary key
        practice_section = get_object_or_404(PracticeSection, pk=pk)
        serializer = PracticeSectionSerializer(practice_section, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        # Delete a specific PracticeSection object by its primary key
        practice_section = get_object_or_404(PracticeSection, pk=pk)
        practice_section.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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





