from django.db import models

class GrammarCategory(models.Model):
    name = models.CharField(max_length=90)
    description = models.CharField(max_length=255)
    
    class Meta:
        db_table = "grammarcategory"

    def __str__(self) -> str:
        return f"Category: {self.name}"

class GrammarSubCategory(models.Model):
    name = models.CharField(max_length=90)
    category = models.ForeignKey(GrammarCategory, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "grammarsubcategory"

    def __str__(self) -> str:
        return f"Sub-category: {self.name}"

# Tests
class GrammarTestSection(models.Model):
    name = models.CharField(max_length=10)
    instruction = models.TextField(blank=True)
    sub_category = models.ForeignKey(GrammarSubCategory, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "grammartestsection"

    def __str__(self) -> str:
        return f"Test Section: {self.name}"

class GrammarTest(models.Model):
    test_type = models.IntegerField()
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    option_one = models.CharField(max_length=255, blank=True)
    option_two = models.CharField(max_length=255, blank=True)
    option_three = models.CharField(max_length=255, blank=True)
    feedback = models.CharField(max_length=255, blank=True)
    test_section = models.ForeignKey(GrammarTestSection, on_delete=models.CASCADE)

    class Meta:
        db_table = "grammartests"

    def __str__(self) -> str:
        return f"Test: {self.question}" 

# Blog
class GrammarBlog(models.Model):
    name = models.CharField(max_length=90)
    author = models.CharField(max_length=90)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    sub_category = models.ForeignKey(GrammarSubCategory, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "grammarblog"

    def __str__(self) -> str:
        return f"Blog: {self.name}"

class GrammarBlogAssessment(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=45)
    blog = models.ForeignKey(GrammarBlog, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "grammarblogassessment"

    def __str__(self) -> str:
        return f"Blog Assessment: {self.question}"

class Vocab(models.Model):
    pass

    class Meta:
        pass

    def __str__(self) -> str:
        pass