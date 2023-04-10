from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("plants", views.PlantView.as_view()),
    path("plants/<uuid:id>", views.PlantDetailView.as_view()),
    path(
        'top-capacity-plants',
        views.TopCapacityPlantsView.as_view()
    ),
]