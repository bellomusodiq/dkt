from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import AccountSerializer, ProfileSerializer
from accounts.permissions import OwnerPermissionOrSuperuser
from .models import UserType, Profile

# Create your views here.
User = get_user_model()


class UserViewSet(ModelViewSet):
    permission_classes = [OwnerPermissionOrSuperuser]
    queryset = User.objects.all()
    serializer_class = AccountSerializer


class CreateUser(APIView):

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            username = serializer.data.get('username')
            user = User.objects.get(username=username)
            user_type = UserType.objects.get(pk=request.data.get('user_type'))
            user_profile = Profile.objects.create(
                dokita=request.data.get("dokita"),
                user_type=user_type,
                user=user
            )
            response = {
                **serializer.data,
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'userid': user.id,
        'user_type': UserType.objects.get(profile__user=user).type
    }
