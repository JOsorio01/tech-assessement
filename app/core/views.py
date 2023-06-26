from typing import Any, List
import numpy as np
import pandas as pd
from dateutil.parser import parse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from core.models import (
    Show,
    FileTemplate,
    Director,
    Actor,
    Country,
    Category,
    Rating,
)


DEFAULT_FIELD_MAPPER = {
    "show_type": "type",
    "title": "title",
    "directors": "director",
    "cast": "cast",
    "country": "country",
    "date_added": "date_added",
    "release_year": "release_year",
    "rating": "rating",
    "duration": "duration",
    "categories": "listed_in",
    "description": "description",
}


def load_file_and_return_dataframe(data) -> pd.DataFrame | None:
    if data is not None:
        filename: str = data.name
        # Get the extension from the last index
        extension = filename.split(".")[-1]
        if extension == "csv":
            return pd.read_csv(data).replace([np.nan], [None])
        elif extension == "xlsx" or extension == "xls":
            return pd.read_excel(data).replace([np.nan], [None])
    return None


def get_mapped_data(field: str, data: dict) -> Any | None:
    active_template = FileTemplate.objects.filter(active=True)
    if active_template.exists():
        # TODO Logic to use a saved template
        pass
    else:
        value = data[DEFAULT_FIELD_MAPPER.get(field, None)]
        if field == "duration":
            return value.split(" ")
        return value


def process_and_save_data(data: List) -> None:
    for show_data in data:
        show = Show.objects.create(
            title=get_mapped_data("title", show_data),
            date_added=parse(get_mapped_data("date_added", show_data)).date(),
            release_year=get_mapped_data("release_year", show_data),
            duration=int(get_mapped_data("duration", show_data)[0]),
            duration_type=get_mapped_data("duration", show_data)[1],
            description=get_mapped_data("description", show_data),
            show_type=get_mapped_data("show_type", show_data),
        )

        directors_data = get_mapped_data("directors", show_data)
        directors_data = directors_data.split(",") if directors_data else []
        for director in directors_data:
            director_obj, _ = Director.objects.get_or_create(
                director_name=director.title()
            )
            show.directors.add(director_obj)

        cast_data = get_mapped_data("cast", show_data)
        cast_data = cast_data.split(",") if cast_data else []
        for cast in cast_data:
            cast_obj, _ = Actor.objects.get_or_create(
                actor_name=cast.title()
            )
            show.cast.add(cast_obj)

        country_data = get_mapped_data("country", show_data)
        country_data = country_data.split(",") if country_data else []
        for country in country_data:
            country_obj, _ = Country.objects.get_or_create(
                country_name=country.title()
            )
            show.country.add(country_obj)

        categories_data = get_mapped_data("categories", show_data)
        categories_data = categories_data.split(",") if categories_data else []
        for categories in categories_data:
            categories_obj, _ = Category.objects.get_or_create(
                category_name=categories.title()
            )
            show.categories.add(categories_obj)

        rating_data = get_mapped_data("rating", show_data)
        rating_obj, _ = Rating.objects.get_or_create(
            rating=rating_data
        )
        show.rating = rating_obj
        show.save()


@api_view(['POST'])
def upload_file(request):
    request_file = request.data.get("file", None)
    file_data = load_file_and_return_dataframe(request_file)
    if file_data is not None:
        data: List = file_data.to_dict(orient='records')

        process_and_save_data(data)

        return Response({"message": "Successful"}, status=status.HTTP_201_CREATED)
    else:
        return Response(
            {"message": "Unsuported file format"},
            status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
        )
