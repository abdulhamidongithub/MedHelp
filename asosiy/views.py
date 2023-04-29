from django.shortcuts import render, redirect
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *

class MijozAPIView(APIView):
    def post(self, request):
        serializer = MijozSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HomeView(View):
    def get(self, request):
        content = {
            'sorovlar': Mijoz.objects.filter(faol=True)
        }
        return render(request, 'home.html', content)

class MijozOchir(View):
    def get(self, request, pk):
        Mijoz.objects.filter(id=pk).delete()
        return redirect("hammasi")


