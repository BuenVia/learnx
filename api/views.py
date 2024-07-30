from django.shortcuts import render, redirect #type: ignore
from django.contrib import messages #type: ignore
from django.http import HttpResponse #type: ignore
from rest_framework import status #type: ignore
from rest_framework.views import APIView #type: ignore
from rest_framework.response import Response #type: ignore
import csv

from .models import GrammarCategory, GrammarSubCategory, GrammarTestSection, GrammarTest, GrammarBlog, GrammarBlogAssessment
from .serializer import GrammarCategorySerializer, GrammarSubCategorySerializer, GrammarTestSectionSerializer, GrammarTestSerializer, GrammarBlogSerializer, GrammarBlogAssessmentSerializer
from .forms import CSVImportForm

# Create your views here.
def index(request):
    return HttpResponse("Welcome to the LangX API...")

def bulk_import_view(request):
    if request.method == 'POST':
        form = CSVImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            for row in reader:
                GrammarTest.objects.create(
                    test_type=row['test_type'],
                    instruction=row['instruction'],
                    question=row['question'],
                    answer=row['answer'],
                    option_one=row['option_one'],
                    option_two=row['option_two'],
                    option_three=row['option_three'],
                    feedback=row['feedback'],
                    test_section_id=row['test_section']
                )
            messages.success(request, "Bulk import successful.")
            return redirect('admin:myapp_grammartest_changelist')
    else:
        form = CSVImportForm()
    
    context = {
        'form': form
    }
    return render(request, 'admin/bulk_import.html', context)

### Categories
class GrammarCategoryViewSet(APIView):
    def get(self, request, *args, **kwargs):
        gcs = GrammarCategory.objects.all()
        serializer = GrammarCategorySerializer(gcs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GrammarSubCategoriesViewSet(APIView):
    def get(self, request, *args, **kwargs):
        gscs = GrammarSubCategory.objects.all()
        serializer = GrammarSubCategorySerializer(gscs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GrammarSubCategoryViewSet(APIView):
    def get(self, request, id, *args, **kwargs):
        gscs = GrammarSubCategory.objects.filter(category=id)
        serializer = GrammarSubCategorySerializer(gscs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
### TESTS
class GrammarTestSectionsViewSet(APIView):
    def get(self, request, id, *args, **kwargs):
        gts = GrammarTestSection.objects.filter(sub_category=id)
        serializer = GrammarTestSectionSerializer(gts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GrammarTestSectionViewSet(APIView):
    def get(self, request, id, *args, **kwargs):
        gt = GrammarTestSection.objects.filter(id=id)
        serializer = GrammarTestSectionSerializer(gt, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GrammarTestsViewSet(APIView):
    def get(self, request, id, *args, **kwargs):
        gt = GrammarTest.objects.all()
        serializer = GrammarTestSerializer(gt, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GrammarTestViewSet(APIView):
    def get(self, request, id, *args, **kwargs):
        gt = GrammarTest.objects.filter(test_section=id)
        serializer = GrammarTestSerializer(gt, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

### BLOGS
class GrammarBlogsViewSet(APIView):
    def get(self, request, id, *args, **kwargs):
        gbs = GrammarBlog.objects.all()
        serializer = GrammarBlogSerializer(gbs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GrammarBlogViewSet(APIView):
    def get(self, request, id, *args, **kwargs):
        gb = GrammarBlog.objects.filter(sub_category=id)
        serializer = GrammarBlogSerializer(gb, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GrammarAssessmentViewSet(APIView):
    def get(self, request, id, *args, **kwargs):
        gas = GrammarBlogAssessment.objects.filter(blog=id)
        serializer = GrammarBlogAssessmentSerializer(gas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)