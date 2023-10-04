from .models import Saleservice
from rest_framework import viewsets, permissions
from .serializers import SaleserviceSerializer

class SaleserviceViewSet(viewsets.ModelViewSet):
    ## queryset is a list of all Todo objects
    queryset = Saleservice.objects.all()
    # The serializer_class attribute is used to control which serializer class should be used for serializing and deserializing queryset and model instances.
    serializer_class = SaleserviceSerializer
    # Set permission_classes to allow unrestricted access to the API.
    permission_classes = [permissions.AllowAny]
