from rest_framework.generics import ListAPIView
from .models import User
from .serializers import UserListSerializer

# Create your views here.
class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
