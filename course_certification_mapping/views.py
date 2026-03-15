from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CourseCertificationMapping
from .serializers import CourseCertificationMappingSerializer
from drf_yasg.utils import swagger_auto_schema


class CourseCertificationMappingListCreateAPIView(APIView):

    def get(self, request):

        course_certification_mappings = CourseCertificationMapping.objects.filter(is_active=True)
        serializer = CourseCertificationMappingSerializer(course_certification_mappings, many=True)

        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=CourseCertificationMappingSerializer)
    def post(self, request):

        serializer = CourseCertificationMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseCertificationMappingDetailAPIView(APIView):

    def get_object(self, pk):

        try:
            return CourseCertificationMapping.objects.get(pk=pk)
        except CourseCertificationMapping.DoesNotExist:
            return None

    def get(self, request, pk):

        course_certification_mappings = self.get_object(pk)

        if not course_certification_mappings:
            return Response({"error": "CourseCertificationMapping not found"}, status=404)

        serializer = CourseCertificationMappingSerializer(course_certification_mappings)
        return Response(serializer.data)

    def put(self, request, pk):

        course_certification_mappings = self.get_object(pk)

        serializer = CourseCertificationMappingSerializer(course_certification_mappings, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def patch(self, request, pk):

        course_certification_mappings = self.get_object(pk)

        serializer = CourseCertificationMappingSerializer(course_certification_mappings, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, pk):

        course_certification_mappings = self.get_object(pk)

        course_certification_mappings.delete()

        return Response(status=204)