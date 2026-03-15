from rest_framework import serializers
from .models import ProductCourseMapping


class ProductCourseMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCourseMapping
        fields = "__all__"

    def validate(self, data):

        if ProductCourseMapping.objects.filter(
            vendor=data['vendor'],
            product=data['product']
        ).exists():
            raise serializers.ValidationError("Mapping already exists")

        return data