# Generated by Django 3.2.4 on 2021-08-15 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20210815_1840'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='doi',
            new_name='DOI',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='doi',
            new_name='DOI',
        ),
        migrations.RenameField(
            model_name='conferencearticle',
            old_name='doi',
            new_name='DOI',
        ),
    ]
