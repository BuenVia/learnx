from django.contrib.auth.models import User
from .models import Subject, Category, Learn, PracticeSection, Questions, TestData
from rest_framework import serializers # type: ignore

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']

        def create(self, validated_data):
            user = User(
                username=validated_data['username'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name']
            )
            user.set_password(validated_data['password'])
            user.save()
            return user

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

