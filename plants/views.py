from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication

from drf_spectacular.utils import extend_schema

from .models import Plant
from .serializers import PlantSerializer , PlantDetailSerializer
from .permissions import IsPlantOwner

class PlantView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

    def perform_create(self, serializer):
        serializer.save(partner=self.request.user)

@extend_schema(
    methods=["PUT"],
    exclude=True,
)
class PlantDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsPlantOwner]

    queryset = Plant.objects.all()
    serializer_class = PlantDetailSerializer
    lookup_url_kwarg = "id"


class TopCapacityPlantsView(generics.ListAPIView):
    queryset = Plant.objects.order_by('-maximum_capacity_GW')[:5]
    serializer_class = PlantSerializer