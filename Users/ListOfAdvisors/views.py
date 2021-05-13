from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Advisors
from .serializers import AdvisorSerializer

class advisorList(APIView):

    def get(self, request):
        advisor1 = Advisors.objects.all()
        serializer = AdvisorSerializer(advisor1, many=true)
        return Response(serializer.data)

    def post(self):
        pass
