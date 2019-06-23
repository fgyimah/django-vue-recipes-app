# a serializer class to convert the model into json format
from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ("id", "name", "ingredients", "picture",
                  "difficulty", "prep_time", "prep_guide")
