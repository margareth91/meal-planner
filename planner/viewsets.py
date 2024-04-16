from rest_framework import viewsets

from planner.models import Meal
from planner.serializers import MealSerializer


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
