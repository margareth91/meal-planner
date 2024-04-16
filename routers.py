from rest_framework import routers

from planner.viewsets import MealViewSet

router = routers.DefaultRouter()

router.register(r"meal-planner", MealViewSet, basename="planner")

urlpatterns = router.urls
