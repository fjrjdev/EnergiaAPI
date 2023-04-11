from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication

from drf_spectacular.utils import extend_schema

from .models import Partner
from .serializers import PartnerSerializer
from .permissions import IsPartnerOwner

class PartnerView(generics.ListCreateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

@extend_schema(
    methods=["PUT"],
    exclude=True,
    )
class PartnerDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsPartnerOwner]
    
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    lookup_url_kwarg = "id"

class LastPartnersView(generics.ListAPIView):
    queryset = Partner.objects.order_by('-created_at')[:10]
    serializer_class = PartnerSerializer