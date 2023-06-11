from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from apps.users.serializers.users import UserSerializer, UserSignupSerializer


class LoginUser(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        data = {'message': 'I need job'}
        return Response(data, status=status.HTTP_200_OK)
    

class SingupUser(APIView):

    def post(self, request, format=None):
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)
