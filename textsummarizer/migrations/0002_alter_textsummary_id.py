# Generated by Django 5.0.3 on 2024-06-11 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textsummarizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textsummary',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
