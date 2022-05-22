# Generated by Django 4.0.4 on 2022-05-15 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_alter_vacanciescategory_options_alter_card_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary',
            field=models.IntegerField(verbose_name='Запрлата'),
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=12, verbose_name='Телефонный номер')),
                ('text', models.TextField(verbose_name='Расскажите о себе')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.vacancy')),
            ],
            options={
                'verbose_name': 'Резюме',
                'verbose_name_plural': 'Резюме',
            },
        ),
    ]
