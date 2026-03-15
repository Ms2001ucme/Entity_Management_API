from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ProductCourseMapping
from .serializers import ProductCourseMappingSerializer
from drf_yasg.utils import swagger_auto_schema


class ProductCourseMappingListCreateAPIView(APIView):

    def get(self, request):

        product_course_mappings = ProductCourseMapping.objects.filter(is_active=True)
        serializer = ProductCourseMappingSerializer(product_course_mappings, many=True)

        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=ProductCourseMappingSerializer)
    def post(self, request):

        serializer = ProductCourseMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductCourseMappingDetailAPIView(APIView):

    def get_object(self, pk):

        try:
            return ProductCourseMapping.objects.get(pk=pk)
        except ProductCourseMapping.DoesNotExist:
            return None

    def get(self, request, pk):

        product_course_mappings = self.get_object(pk)

        if not product_course_mappings:
            return Response({"error": "ProductCourseMapping not found"}, status=404)

        serializer = ProductCourseMappingSerializer(product_course_mappings)
        return Response(serializer.data)

    def put(self, request, pk):

        product_course_mappings = self.get_object(pk)

        serializer = ProductCourseMappingSerializer(product_course_mappings, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def patch(self, request, pk):

        product_course_mappings = self.get_object(pk)

        serializer = ProductCourseMappingSerializer(product_course_mappings, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, pk):

        product_course_mappings = self.get_object(pk)

        product_course_mappings.delete()

        return Response(status=204)