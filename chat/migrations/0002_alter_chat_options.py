# Generated by Django 4.1.4 on 2023-02-25 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chat',
            options={'ordering': ('created_at',)},
        ),
    ]
