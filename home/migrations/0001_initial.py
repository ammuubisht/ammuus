# Generated by Django 3.2.5 on 2022-02-26 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('project_tagline', models.CharField(max_length=255)),
                ('thumbnail', models.ImageField(upload_to='')),
            ],
        ),
    ]
