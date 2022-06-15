import re
from django.shortcuts import render
from rest_framework.views import APIView
from hotel_vote.serializer import *
from .models import *
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404

from rest_framework import generics
from .serializer import RegisterSerializer, LoginSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings
JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER
from django.contrib.auth.models import update_last_login
from .models import CustomUser
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import F
from rest_framework import permissions
from  rest_framework.permissions import IsAuthenticated

class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class LoginView(generics.CreateAPIView):
    permission_classes= (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        user= request.data
        serializer= self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            username = request.data.get('username', None)
            password = request.data.get("password", None)
            try:
                user= CustomUser.objects.get(username=username)
            except:
                return Response({"error": "Your username/email is not correct. Please try again or register your details"})
            user = authenticate(username= username, password=password)
            token = RefreshToken.for_user(user)

            if user is not None:
                jwt_access_token_lifetime =  settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']
                jwt_refresh_token_lifetime =  settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']

                update_last_login(None, user)
                response = {
                    'success': 'True',
                    'status code': status.HTTP_200_OK,
                    'message': 'User logged in successfully',
                    'access': str(token.access_token),
                    'referesh_token':str(token),
                    "access_token_life_time_in_seconds" : jwt_access_token_lifetime.total_seconds(),
                    "refresh_token_life_time_in_seconds" : jwt_refresh_token_lifetime.total_seconds(),
                }

                status_code = status.HTTP_200_OK
                return Response(response, status=status_code)
            else:
                return Response({"error": 'Your password is not correct please try again or reset your password'}, status=401)


class Hotel_list(APIView):
    permission_classes= (IsAuthenticated, ) 
    def get_object(self, pk):
        try:
            return Hotel.objects.get(pk=pk)
        except Hotel.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        hotel_data = Hotel.objects.all().order_by('votes')
        serializer = HotelSerializer(hotel_data,many=True)
        return Response(serializer.data)


    def post(self, request):
        """
        create a Hotel.
        """
        hotel_data = request.data

        serializer = HotelSerializer(data=hotel_data)
        if serializer.is_valid(raise_exception=True):
            assignment_saved = serializer.save()
        return Response({"success": "Hotel created successfully".format(assignment_saved.votes)})


    def put(self, request, pk, format=None):
        """
        update a Hotel.
        """
        assignment = Hotel.objects.get(id=pk)
        serializer = HotelSerializer(assignment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"success": "Hotel deleted successfully"},status=status.HTTP_204_NO_CONTENT)
    

class Daily_Winners_history(APIView):
    permission_classes= (IsAuthenticated, ) 
    def get(self, request):
        hotel_data = history_winner.objects.all()
        serializer = HistoryWinnerSerializer(hotel_data,many=True)
        return Response(serializer.data)

class vote(APIView):
    permission_classes= (IsAuthenticated, ) 
    def post(self, request, pk=None, format=None):
        if pk:
            if request.user.max_votes >= str(0.5):
                CustomUser.objects.filter(pk=request.user.id).update(max_votes=F('max_votes')*.5)    
                total = float(request.user.max_votes)*.5 
                Hotel.objects.filter(pk=pk).update(votes=F('votes')+total)
                return Response({"success": "Vote added"},status=status.HTTP_204_NO_CONTENT)
            return Response({"success": "You dont have enaugh vote"})
        return Response({"success": "Vote added"},status=status.HTTP_204_NO_CONTENT)
