from rest_framework import viewsets

from .serializer import UserModelSerializer
from main.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
