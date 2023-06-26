# Generated by Django 4.2.2 on 2023-06-26 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date_added', models.DateField()),
                ('release_year', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]
