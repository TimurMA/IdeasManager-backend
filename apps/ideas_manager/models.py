from django.db import models

class Idea(models.Model):
    class StatusType(models.TextChoices):
        on_approval = 'on approval'
        on_adoption = 'on adoption'
        adopted = 'adopted'

    name = models.CharField(max_length=127, verbose_name="Название идеи")
    problem = models.TextField(verbose_name="Проблема, которую решает ваша идея")
    solution = models.TextField(verbose_name="Предлогаемое решение")
    proposed_result = models.TextField(verbose_name='Предпологаемый результат')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15, choices=StatusType.choices, default='на согласовании')
    rating = models.FloatField(default=0.0,)
    risk = models.FloatField(default=0.0,)
    initator = models.ForeignKey('AuthApi.User', on_delete=models.CASCADE, verbose_name='Инициатор', to_field='token')

    def __str__(self) -> str:
        return self.name

