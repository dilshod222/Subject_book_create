# Generated by Django 3.2.9 on 2021-11-24 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0003_auto_20211124_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='file',
            field=models.FileField(default=1, upload_to='upload/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='picture',
            field=models.FileField(upload_to='images/'),
        ),
    ]
