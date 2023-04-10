from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("partners", views.PartnerView.as_view()),
    path("login", jwt_views.TokenObtainPairView.as_view()),
    path("partners/<uuid:id>", views.PartnerDetailView.as_view()),
    path(
        'last-partners',
        views.LastPartnersView.as_view()
    ),
]