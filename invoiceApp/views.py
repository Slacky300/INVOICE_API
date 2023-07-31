from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializers import *
from django.http import HttpResponse
from rest_framework import status



class InvoiceViewSet(APIView):

    def get(self,request):

        queryset = Invoice.objects.all()
        serializer = InvoiceSerializer(queryset, many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request):

        try:
            serializer = InvoiceSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(status= status.HTTP_500_INTERNAL_SERVER_ERROR)
