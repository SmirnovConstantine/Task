# Generated by Django 2.2.6 on 2019-10-20 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('mng', 'Менеджер'), ('use', 'Пользователь')], max_length=3, verbose_name='Тип пользователя'),
        ),
    ]
