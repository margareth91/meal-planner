from rest_framework import serializers

from planner.models import Meal


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ["id", "author", "weekday", "name", "description"]
