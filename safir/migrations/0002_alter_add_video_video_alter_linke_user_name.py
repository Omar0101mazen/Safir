# Generated by Django 4.2.2 on 2023-10-25 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safir', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_video',
            name='video',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='linke',
            name='user_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
