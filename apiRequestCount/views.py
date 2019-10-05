from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from .decorators import requestCount

# Create your views here.

class CountView(APIView):
    @requestCount
    def get(self, request, **kwargs):
        """test view1"""

        return JsonResponse(["All ok"],safe=False,status=status.HTTP_200_OK)

class CountView2(APIView):
    @requestCount
    def get(self, request, **kwargs):
        """test view2"""

        return JsonResponse(["All ok"],safe=False,status=status.HTTP_200_OK)
