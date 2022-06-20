from django.contrib import admin
from .models import VacanciesCategory, Card, Vacancy, Summary, Feedback

admin.site.register(VacanciesCategory)
admin.site.register(Card)
admin.site.register(Vacancy)
admin.site.register(Summary)
admin.site.register(Feedback)