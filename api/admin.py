from django.contrib import admin


from .models import Subject, Category, Learn, PracticeSection, Questions, TestData

# Register your models here.
admin.site.register(Subject)
admin.site.register(Category)
admin.site.register(Learn)
admin.site.register(PracticeSection)
admin.site.register(Questions)
admin.site.register(TestData)