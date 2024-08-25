from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, permissions


from .models import ChecklistItem
from .serializers import ChecklistItemSerializer


class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        user = User.objects.create_user(
            username=request.data['username'],
            password=request.data['password']
        )
        return Response({"username": user.username}, status=status.HTTP_201_CREATED)
    



class ChecklistItemViewSet(viewsets.ModelViewSet):
    queryset = ChecklistItem.objects.all()
    serializer_class = ChecklistItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)