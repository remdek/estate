from django.utils.decorators import method_decorator
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from .models import Estate, EstateCategory
from rest_framework.viewsets import ModelViewSet
from .serializers import EstateCategoryTreeSerializer
from rest_framework.response import Response


# Create your views here.
class EstateCategoryTreeView(ModelViewSet):
    queryset = EstateCategory.objects.all()
    serializer_class = EstateCategoryTreeSerializer

    @action(detail=False)
    def roots(self, request):
        queryset = self.queryset.filter(parent=None)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)