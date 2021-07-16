# Generated by Django 3.2.5 on 2021-07-15 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0005_alter_youtuber_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='category',
            field=models.CharField(choices=[('code', 'code'), ('mobile_review', 'mobile_review'), ('vlogs', 'vlogs'), ('comedy', 'comedy'), ('gaming', 'gaming'), ('film_making', 'film_making'), ('entertainment', 'entertainment')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media/ytubers/%Y/%m'),
        ),
    ]