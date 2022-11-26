import datetime
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100,
                                  verbose_name='Имя')
    last_name = models.CharField(max_length=100,
                                 verbose_name='Фамилия')
    email = models.EmailField(verbose_name="почта",
                              unique=True,
                              default='')
    phone = models.CharField(max_length=12,
                             verbose_name="телефон")
    friend_list = models.ManyToManyField('CustomUser', blank=True)
    scores_point = models.IntegerField(verbose_name="Количество набранных очков",
                                       blank=True, default=0)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class TodoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title

class TodoItem(models.Model):
    ONCE = 'один раз'
    INTERVAL = 'с интервалом'
    EVERY_DAY = 'каждый день'
    TRIGGER = 'по триггеру'
    REMINDER_TYPE_CHOICE = [
        (ONCE, 'один раз'),
        (INTERVAL, 'интервал'),
        (EVERY_DAY, 'каждый день'),
        (TRIGGER, 'по триггеру')
    ]
    OPEN = 'открыта'
    CLOSE = 'закрыта'
    COMPLETED = 'завершена'
    STATUS_CHOICE = [
        (OPEN, 'открыта'),
        (CLOSE, 'закрыта'),
        (COMPLETED, 'завершена')
    ]
    reminder_type = models.CharField(max_length=20,
                                     choices=REMINDER_TYPE_CHOICE,
                                     verbose_name="Тип напоминания",
                                     default=ONCE)
    task_name = models.CharField(max_length=255, verbose_name="Название задачи")
    description = models.TextField(verbose_name="Описание")
    time_interval = models.ExpressionWrapper(models.F('data') + models.F('end') + datetime.timedelta(days=1),
    output_field=models.DateTimeField(verbose_name="Временно интервал"))
    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICE,
                              verbose_name="Статус",
                              default=OPEN)
    notification_method = models.CharField(max_length=20,
                                           choices=[("почта", 'Почта'),
                                                    ('телефон', "телефон")],
                                           verbose_name="Метод оповещения")
    scores = models.IntegerField(validators=[
        MinValueValidator(0)])
    subscribers = models.ManyToManyField(CustomUser)

    def __str__(self):
        return self.task_name