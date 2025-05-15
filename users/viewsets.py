from django.contrib.auth import get_user_model

from rest_framework import viewsets
from .serializers import UserSerializer
from .permissions import IsUserOwnerOrGetAndPostOnly

User = get_user_model()
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUserOwnerOrGetAndPostOnly]
    lookup_field = 'user_id' 