# Generated by Django 4.0 on 2021-12-23 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
