from rest_framework import serializers

from core import models


class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Director
        fields = "__all__"
        read_only_fields = ("id",)


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Actor
        fields = "__all__"
        read_only_fields = ("id",)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = "__all__"
        read_only_fields = ("id",)


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Country
        fields = "__all__"
        read_only_fields = ("id",)


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Rating
        fields = ["rating"]


class ShowSerializer(serializers.ModelSerializer):
    directors = DirectorSerializer(many=True, required=False)
    cast = ActorSerializer(many=True, required=False)
    categories = CategorySerializer(many=True, required=False)
    country = CountrySerializer(many=True, required=False)
    rating = RatingSerializer(many=False, required=False)

    class Meta:
        model = models.Show
        fields = [
            "id", "title", "date_added", "release_year", "duration",
            "duration_type", "description", "show_type", "directors",
            "cast", "categories", "country", "rating"
        ]
        read_only_fields = ("id",)
