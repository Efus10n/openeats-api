# Generated by Django 2.0.1 on 2018-02-19 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_remove_menuitem_occurrence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='update_date',
        ),
    ]