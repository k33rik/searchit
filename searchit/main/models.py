from django.conf import settings
from django.db import models


class VacanciesCategory(models.Model):
    title = models.CharField('Название', max_length=32)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    def vacancies(self):
        return Vacancy.objects.filter(category_id=self.id, status=1)

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'


class Card(models.Model):
    title = models.CharField('Название', max_length=32)
    price = models.IntegerField()
    task = models.TextField('Описание')
    link = models.CharField('Подробнее ссылка', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'карточку'
        verbose_name_plural = 'карточки'


class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mail = models.CharField('Электронная почта', max_length=50)
    subject = models.CharField('Тема', max_length=255)
    text = models.TextField('Опишите проблему')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'обратная связь'
        verbose_name_plural = 'обратные связи'


class Vacancy(models.Model):
    STATUS_CHOICES = (
        (0, 'В рассмотрении'),
        (1, 'Принят'),
        (2, 'Не принят')
    )
    company_name = models.CharField('Название компании', max_length=255)
    mail = models.CharField('Почта', max_length=255)
    number = models.CharField('Телефон', max_length=12)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    category = models.ForeignKey(VacanciesCategory, models.CASCADE, verbose_name='Категория')
    title = models.CharField('Название вакансии', max_length=255)
    salary = models.IntegerField('Запрлата')
    text = models.TextField('Описание')

    def __str__(self):
        return self.title

    def description(self):
        return (self.text[:200] + '..') if len(self.text) > 200 else self.text

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