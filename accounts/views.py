from django.shortcuts import render

from accounts.models import User
from accounts.serializers import UserSerializer

from rest_framework.generics import CreateAPIView
from rest_framework import authentication,permissions
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class SignupView(CreateAPIView):

    serializer_class=UserSerializer

class AuthUserDetailView(APIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):

        user_object=User.objects.get(id=request.user.id)

        serializer_instance=UserSerializer(user_object)

        return Response(serializer_instance.data)
    