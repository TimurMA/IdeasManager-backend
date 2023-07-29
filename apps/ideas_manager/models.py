from django.db import models

class Idea(models.Model):
    class StatusType(models.TextChoices):
        on_approval = 'на согласовании'
        on_adoption = 'на утверждении'
        adopted = 'утверждено'
    
    name = models.CharField(max_length=127, verbose_name="Название идей")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15, choices=StatusType.choices, default='на согласовании')
    rating = models.FloatField(default=0.0,)
    risk = models.FloatField(default=0.0,)

    def __str__(self) -> str:
        return self.name

