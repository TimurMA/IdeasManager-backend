# Generated by Django 4.2.2 on 2023-07-26 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthApi', '0002_alter_user_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.UUIDField(db_index=True, editable=False, null=True, unique=True, verbose_name='Токен'),
        ),
    ]
