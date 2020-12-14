from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User, Group
from .serializersAdmin import UserListAdminSerializer, UserGroupListAdminSerializer, UserDetailAdminSerializer

# Create your views here.
class UserListAdminView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListAdminSerializer

class UserGroupListAdminView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = UserGroupListAdminSerializer

class UserDetailAdminView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    serializer_class = UserDetailAdminSerializer
    # permission_classes = (IsAdminUser,)
    queryset = User.objects.all()