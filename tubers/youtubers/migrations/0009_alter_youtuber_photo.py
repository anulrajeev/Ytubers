# Generated by Django 3.2.5 on 2021-07-15 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0008_alter_youtuber_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='photo',
            field=models.ImageField(blank=True, default='media/dummy.png', null=True, upload_to='media/ytubers/%Y/%m'),
        ),
    ]
