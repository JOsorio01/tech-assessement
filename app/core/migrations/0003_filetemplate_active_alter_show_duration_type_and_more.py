# Generated by Django 4.2.2 on 2023-06-26 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_actor_category_country_director_namesmatch_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='filetemplate',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='show',
            name='duration_type',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='show',
            name='show_type',
            field=models.CharField(max_length=255),
        ),
    ]
