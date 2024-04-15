from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    title = models.CharField(
        max_length = 100,
        verbose_name = "Название",
        help_text = "Укажите, название задачи"
    )

    description = models.TextField(
        max_length = 500,
        verbose_name="Описание",
        help_text="Введите описание задачи"
    )

    completed = models.BooleanField(
        default=False,
        verbose_name="Выполнено",
        help_text="Отметьте, если задача выполнена"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Создан",
        help_text="Дата и время создания этой задачи."
    )

    def __str__(self):
        return f"{self.title} - {self.user.username}"
    
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        ordering = ["-created_at"]
    
  
