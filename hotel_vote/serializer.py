from .models import Hotel,CustomUser,history_winner
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    max_votes = serializers.IntegerField(required=False, min_value=1, max_value=3, default=3)
    class Meta:
        model = CustomUser
        fields = ("id", "username", 'password',
                  'password2', 'max_votes')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            max_votes=validated_data['max_votes']
          
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", 'password',
                  'password2', 'max_votes']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=128, write_only=True,  required=True)
    password = serializers.CharField(
        max_length=128, write_only=True,  required=True)
    token = serializers.CharField(max_length=255, read_only=True)


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id','name', 'address', 'votes']

class HistoryWinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = history_winner
        fields = ['winner']
        depth = 1


