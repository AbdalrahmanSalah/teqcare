from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer ,RefreshToken
from django.contrib.auth.hashers import make_password
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from core.models import User


class Userserializers(serializers.ModelSerializer):
    """serializers for the user object"""

    class Meta:
        model = User
        fields = ['email','password','name']
        extra_kwargs = {'password': {'min_length':6}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it """
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(password)
        user.save()
        return user

    # def validate_password(self, value: str) -> str:
    #     """Hash value passed by user , :param value: password of a user , :return: a hashed version of the password"""
    #     return make_password(value)

class CustomTokenObtainSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)


        token['email'] = user.email
        token['name'] = user.name
        token['is_staff'] = user.is_staff
        token['user'] = user.is_active

        return token

    def validate(self, attrs):
        credentials = {
            'email': attrs.get("email"),
            'password': make_password(attrs.get("password")),

        }
        if not User:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authorization')

        return super().validate(credentials)
