from rest_framework import serializers
from .models import CourseCertificationMapping


class CourseCertificationMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseCertificationMapping
        fields = "__all__"

    def validate(self, data):

        if CourseCertificationMapping.objects.filter(
            course=data['course'],
            certification=data['certification']
        ).exists():
            raise serializers.ValidationError("Mapping already exists")

        return data