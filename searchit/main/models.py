from django.conf import settings
from django.db import models


class VacanciesCategory(models.Model):
    title = models.CharField('Название', max_length=16)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    def vacancies(self):
        return Vacancy.objects.filter(category_id=self.id)

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'


class Card(models.Model):
    title = models.CharField('Название', max_length=32)
    price = models.IntegerField()
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'карточку'
        verbose_name_plural = 'карточки'


class Vacancy(models.Model):
    category = models.ForeignKey(VacanciesCategory, models.CASCADE)
    title = models.CharField('Название', max_length=64)
    salary = models.IntegerField('Запрлата')
    text = models.TextField('Описание')

    def __str__(self):
        return self.title

    def description(self):
        return (self.text[:75] + '..') if len(self.text) > 75 else self.text

    class Meta:
        verbose_name = 'вакансию'
        verbose_name_plural = 'вакансии'


class Summary(models.Model):
    vacancy = models.ForeignKey(Vacancy, models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    number = models.CharField('Телефонный номер', max_length=12)
    text = models.TextField('Расскажите о себе')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'резюме'
        verbose_name_plural = 'резюме'