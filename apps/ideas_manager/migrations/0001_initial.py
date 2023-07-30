# Generated by Django 4.2.2 on 2023-07-30 13:19

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
            name='Idea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='Название идеи')),
                ('problem', models.TextField(verbose_name='Проблема, которую решает ваша идея')),
                ('solution', models.TextField(verbose_name='Предлогаемое решение')),
                ('proposed_result', models.TextField(verbose_name='Предпологаемый результат')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('on approval', 'On Approval'), ('on adoption', 'On Adoption'), ('adopted', 'Adopted')], default='на согласовании', max_length=15)),
                ('rating', models.FloatField(default=0.0)),
                ('risk', models.FloatField(default=0.0)),
                ('initiator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='token', verbose_name='Инициатор')),
            ],
        ),
    ]
