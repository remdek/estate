from rest_framework.generics import ListAPIView
from .models import Location
from .serializers import LocationListSerializer

# Create your views here.
class LocationView(ListAPIView):
    serializer_class = LocationListSerializer
    def get_queryset(self, *args, **kwargs):
        queryset = Location.objects.all()
        select = self.request.GET.get('select')
        if select:
            if select == 'country':
                queryset = queryset.filter(parent=None)
            if select == 'county':
                queryset = queryset.filter(type='county')
            if select == 'town':
                queryset = queryset.filter(type='town')
            if select == 'district':
                queryset = queryset.filter(type='district')
            return queryset



