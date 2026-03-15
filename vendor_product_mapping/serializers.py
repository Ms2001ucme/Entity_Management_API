from rest_framework import serializers
from .models import VendorProductMapping


class VendorProductMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = VendorProductMapping
        fields = "__all__"

    def validate(self, data):

        if VendorProductMapping.objects.filter(
            vendor=data['vendor'],
            product=data['product']
        ).exists():
            raise serializers.ValidationError("Mapping already exists")

        return data