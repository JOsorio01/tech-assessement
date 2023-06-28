from django.db import models


class Director(models.Model):
    director_name = models.CharField(max_length=255)


class Actor(models.Model):
    actor_name = models.CharField(max_length=255)


class Country(models.Model):
    country_name = models.CharField(max_length=255)


class Category(models.Model):
    category_name = models.CharField(max_length=255)


class Rating(models.Model):
    rating = models.CharField(max_length=10)


class Show(models.Model):
    title = models.CharField(max_length=255)
    date_added = models.DateField()
    release_year = models.IntegerField()
    duration = models.IntegerField()
    duration_type = models.CharField(max_length=255)
    description = models.TextField()
    show_type = models.CharField(max_length=255)
    directors = models.ManyToManyField('Director')
    cast = models.ManyToManyField('Actor')
    categories = models.ManyToManyField('Category')
    country = models.ManyToManyField('Country')
    rating = models.ForeignKey(
        Rating,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.title


class NamesMatch(models.Model):
    db_name = models.CharField(max_length=255)
    match_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.db_name


class FileTemplate(models.Model):
    template_name = models.CharField(max_length=255)
    match_names = models.ManyToManyField('NamesMatch')
    ignore_fields = models.ManyToManyField(
        'NamesMatch',
        related_name='ignored',
        null=True,
        blank=True,
    )
    active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.template_name
