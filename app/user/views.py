from rest_framework import generics, status, serializers
from rest_framework_simplejwt.views import TokenViewBase
from user.serializers import CustomTokenObtainSerializer, Userserializers
from rest_framework.permissions import AllowAny
from django.db.models import Q
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework.settings import api_settings
from core.models import User
from rest_framework.response import Response

class CreatUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = Userserializers


class CustomTokenView(TokenViewBase):

    serializer_class = CustomTokenObtainSerializer
    permission_classes = ([AllowAny])
    def post(self, request, *args, **kwargs):
        try:
            user_obj = User.objects.filter(Q(email=request.data["email"]) ).first()
            if user_obj:
                request.data["email"] = user_obj.email
            else:
                request.data["email"] = 0


            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                data = serializer.validated_data
                user = Userserializers(user_obj)
                data['user'] = user.data
                return Response(data, status=status.HTTP_200_OK)


        except TokenError as e:
            raise InvalidToken(e.args[0])

        except User.DoesNotExist:
            return Response("Can't find user", status=status.HTTP_404_NOT_FOUND)
