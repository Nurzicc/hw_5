# Generated by Django 5.1.4 on 2025-01-04 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_steps'),
    ]

    operations = [
        migrations.AddField(
            model_name='steps',
            name='title',
            field=models.CharField(default=1, max_length=255, verbose_name='Заголовок'),
            preserve_default=False,
        ),
    ]
