# Generated by Django 4.2.11 on 2024-04-11 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Укажите, название задачи', max_length=100, verbose_name='Название')),
                ('description', models.TextField(help_text='Введите описание задачи', max_length=500, verbose_name='Описание')),
                ('completed', models.BooleanField(default=False, help_text='Отметьте, если задача выполнена', verbose_name='Выполнено')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Дата и время создания этой задачи.', verbose_name='Создан')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'ordering': ['-created_at'],
            },
        ),
    ]
