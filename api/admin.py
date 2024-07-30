from django.contrib import admin
from django.urls import path

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
import csv
from .forms import CSVImportForm

from .models import GrammarCategory, GrammarSubCategory, GrammarTestSection, GrammarTest, GrammarBlog, GrammarBlogAssessment
from .views import bulk_import_view

class GrammarTestAdmin(admin.ModelAdmin):
    list_display = ('question', 'test_type', 'test_section')
    change_list_template = 'admin/myapp/grammartest/change_list.html'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('bulk_import/', self.admin_site.admin_view(self.bulk_import_view), name='bulk_import'),
        ]
        return custom_urls + urls

    def bulk_import_view(self, request):
        if request.method == 'POST':
            form = CSVImportForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = request.FILES['csv_file']
                decoded_file = csv_file.read().decode('utf-8').splitlines()
                reader = csv.DictReader(decoded_file)
                for row in reader:
                    GrammarTest.objects.create(
                        test_type=row['test_type'],
                        question=row['question'],
                        answer=row['answer'],
                        option_one=row['option_one'],
                        option_two=row['option_two'],
                        option_three=row['option_three'],
                        feedback=row['feedback'],
                        test_section_id=row['test_section']
                    )
                messages.success(request, "Bulk import successful.")
                return HttpResponseRedirect("../")  # Redirect to the change list
        else:
            form = CSVImportForm()

        context = self.admin_site.each_context(request)
        context['form'] = form
        return render(request, 'admin/bulk_import.html', context)

# Register your models here.
admin.site.register(GrammarCategory)
admin.site.register(GrammarSubCategory)
admin.site.register(GrammarTestSection)
admin.site.register(GrammarTest, GrammarTestAdmin)
admin.site.register(GrammarBlog)
admin.site.register(GrammarBlogAssessment)