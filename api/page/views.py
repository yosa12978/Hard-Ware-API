from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Processor
from .serializers import ProcessorSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated

class Index(APIView):
    renderer_classes = (JSONRenderer, )
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        if "id" in request.GET:
            processors = Processor.objects.filter(id = request.GET["id"])
        elif "title" in request.GET:
            processors = Processor.objects.filter(title__icontains = request.GET["title"])
        else:
            processors = Processor.objects.order_by("-id")
        serializer = ProcessorSerializer(processors, many=True)
        return Response(serializer.data)

class Create(APIView):
    renderer_classes = (JSONRenderer, )
    permission_classes = (IsAuthenticated, )
    def post(self, request):
        serializer = ProcessorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": 201})
        else:
            return Response(serializer.errors)

class SignUp(APIView):
    renderer_classes = (JSONRenderer, )
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        try:
            if username is None and password is None:
                return Response({"status": 400})
            else:
                User.objects.create_user(username = username, password = password).save()
                return Response({"status": 201})
        except IntegrityError:
            return Response({"status": 400})