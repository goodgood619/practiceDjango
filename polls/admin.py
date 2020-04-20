from django.contrib import admin

from .models import Question, Choice


# extra : choice(Model)를 몇개더 추가적으로(extra) 띄울것인가
# StackedInline(그냥다른스타일) or TabularInline(Table스타일)
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
