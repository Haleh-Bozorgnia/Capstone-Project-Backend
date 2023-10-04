from .models import Saleservice
from rest_framework import serializers

## Class TodoSerializer is a subclass of serializers.HyperlinkedModelSerializer.
## For serializing and deserializing data into representations such as json.
class SaleserviceSerializer(serializers.HyperlinkedModelSerializer):
    ## Meta class is for configuring the TodoSerializer class.
    class Meta:
        # model to serialize
        model = Saleservice
        # fields to show in json
        fields = ('id', 'title', 'group', 'location', 'price', 'unit', 'image', 'provider', 'phone')