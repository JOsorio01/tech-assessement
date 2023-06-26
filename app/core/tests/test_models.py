"""
Test for application models.
"""
from datetime import datetime

from django.test import TestCase

from core import models


class ApplicationModelsTests(TestCase):

    def test_create_show(self):
        show = models.Show.objects.create(
            title="Show title",
            date_added=datetime.now(),
            release_year=2020,
            duration=90,
            description="Some description",
        )

        self.assertEqual(str(show), show.title)
