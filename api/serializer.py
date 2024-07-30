from .models import GrammarCategory, GrammarSubCategory, GrammarTestSection, GrammarTest, GrammarBlog, GrammarBlogAssessment
from rest_framework import serializers # type: ignore



class GrammarCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GrammarCategory
        fields = ["id", "name", "description"]
        
class GrammarSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GrammarSubCategory
        fields = ["id", "name", "category"]

class GrammarTestSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrammarTestSection
        fields = ['id', 'name', 'instruction', 'sub_category']

class GrammarTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrammarTest
        fields = [
            'id',
            'test_type',
            'question',
            'answer',
            'option_one',
            'option_two',
            'option_three',
            'feedback',
            'test_section'
        ]
  
class GrammarBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrammarBlog
        fields = ['id', 'name', 'author', 'body', 'date_created', 'sub_category']
      
class GrammarBlogAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrammarBlogAssessment
        fields = ['id', 'question', 'answer', 'blog']

