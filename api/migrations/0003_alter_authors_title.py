# Generated by Django 4.0.1 on 2022-06-07 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_authors_remove_articles_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
