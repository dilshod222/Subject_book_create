# Generated by Django 3.2.9 on 2021-11-25 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0006_book_generated_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='picture',
        ),
    ]