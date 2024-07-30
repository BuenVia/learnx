from .models import Subject, Category, Learn, PracticeSection, Questions, TestData
from rest_framework import serializers # type: ignore


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["id", "name", "description", "user_id"]
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "subject", "user_id"]

# Learn
class LearnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Learn
        fields = ['id', 'name', 'author', 'body', 'date_created', 'category', "user_id"]

# Practice
class PracticeSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticeSection
        fields = ['id', 'name', 'instruction', 'category', "user_id"]

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = [
            'id',
            'test_type',
            'question',
            'answer',
            'option_one',
            'option_two',
            'option_three',
            'feedback',
            'category',
            'practice_section',
            'user_id'
        ]

# Test
class TestDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestData
        fields = ['id', 'date_taken', 'category', 'user_id']

