from rest_framework import generics

from .models import User
from .serializers import UserSerializer


class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


# Create your views here.
