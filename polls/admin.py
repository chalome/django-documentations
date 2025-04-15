from django.contrib import admin
from .models import *
# Register your models here.
class ChoiceInline(admin.StackedInline):
    model=Choice
    extra=3
    
class QuestionAdmin(admin.ModelAdmin):
    fields=['question_text'] # This will change the order of fields in the admin page
    exclude=["pub_date"]
    inlines=[ChoiceInline]
    list_display=('question_text','pub_date','was_published_recently')

admin.site.register(Question,QuestionAdmin)
# admin.site.register(Choice)
