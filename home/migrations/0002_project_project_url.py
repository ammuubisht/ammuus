# Generated by Django 3.2.5 on 2022-02-26 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_url',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
