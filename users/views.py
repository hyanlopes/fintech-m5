from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import User
from .permissions import IsAdminPermission, IsOwnerPermission
from .serializers import UserSerializer


class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminPermission]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerPermission]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "user_id"


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                "token": token.key,
                "user_id": user.id,
            }
        )
