# Generated by Django 4.1.6 on 2023-02-06 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_account_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='birthday',
            field=models.DateField(blank=True, max_length=30, null=True, verbose_name='Дата рождения'),
        ),
    ]
