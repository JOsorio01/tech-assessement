# Generated by Django 4.2.2 on 2023-06-26 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NamesMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_name', models.CharField(max_length=255)),
                ('match_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='show',
            name='duration_type',
            field=models.CharField(choices=[('M', 'Minutes'), ('S', 'Seasons')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='show',
            name='show_type',
            field=models.CharField(choices=[('M', 'Movie'), ('T', 'TV Show')], default='M', max_length=1),
        ),
        migrations.CreateModel(
            name='FileTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_name', models.CharField(max_length=255)),
                ('ignore_fields', models.ManyToManyField(related_name='ignored', to='core.namesmatch')),
                ('match_names', models.ManyToManyField(to='core.namesmatch')),
            ],
        ),
        migrations.AddField(
            model_name='show',
            name='cast',
            field=models.ManyToManyField(to='core.actor'),
        ),
        migrations.AddField(
            model_name='show',
            name='categories',
            field=models.ManyToManyField(to='core.category'),
        ),
        migrations.AddField(
            model_name='show',
            name='country',
            field=models.ManyToManyField(to='core.country'),
        ),
        migrations.AddField(
            model_name='show',
            name='directors',
            field=models.ManyToManyField(to='core.director'),
        ),
        migrations.AddField(
            model_name='show',
            name='rating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.rating'),
        ),
    ]
