from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .models import Estate, EstateCategory, EstateProperty, EstatePropertyOption
from .serializersAdmin import EstateListAdminSerializer, \
    EstateCategoryListAdminSerializer, EstateCategoryDetailAdminSerializer, \
    EstatePropsListAdminSerializer, EstatePropOptionsListAdminSerializer, EstateDetailAdminSerializer

from locales.mixin.localesMixins import createUpdateLangField


# ========Estate Object===========
class EstateListAdminView(ListAPIView):
    queryset = Estate.objects.all()
    serializer_class = EstateListAdminSerializer


class EstateDetailAdminView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    serializer_class = EstateDetailAdminSerializer
    # permission_classes = (IsAdminUser,)
    queryset = Estate.objects.all()


# ===========Estate Category============
class CategoryListAdminView(ListCreateAPIView):
    queryset = EstateCategory.objects.all()
    serializer_class = EstateCategoryListAdminSerializer

    def post(self, request, *args, **kwargs):
        category = request.data
        names = category['name']
        titles = category['title']
        descriptions = category['description']
        catCreate = EstateCategory.objects.create(slug=category['slug'],
                                                  parent_id=category['parent'])

        createUpdateLangField(names, 'InputLang', catCreate.name)

        createUpdateLangField(titles, 'InputLang', catCreate.title)

        createUpdateLangField(descriptions, 'TextLang', catCreate.description)

        return Response({'msg': 'Ok', 'status': 'success'})


class CategoryDetailAdminView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    serializer_class = EstateCategoryDetailAdminSerializer
    # permission_classes = (IsAdminUser,)
    queryset = EstateCategory.objects.all()

    ### -----Update category
    def patch(self, request, *args, **kwargs):
        category = request.data
        print(category)
        names = category['name']
        titles = category['title']
        descriptions = category['description']

        catUpdate = EstateCategory.objects.get(pk=category['id'])
        catUpdate.slug = category['slug']
        catUpdate.parent_id = category['parent']
        catUpdate.robots = category['robots']
        catUpdate.save()

        # catUpdate.update(slug=category['slug'], parent_id=category['parent'])

        catUpdate.props.clear()
        catUpdate.props.add(*category['props'])

        createUpdateLangField(names, 'InputLang', catUpdate.name)

        createUpdateLangField(titles, 'InputLang', catUpdate.title)

        createUpdateLangField(descriptions, 'TextLang', catUpdate.description)

        return Response({'msg': 'Ok', 'status': 'success'})


######   Category properties

class EstatePropsListAdminView(ListCreateAPIView):
    queryset = EstateProperty.objects.all()
    serializer_class = EstatePropsListAdminSerializer

    def post(self, request, *args, **kwargs):
        getProp = request.data
        names = getProp['name']
        print(getProp)
        newProp = EstateProperty.objects.create(parent_id=getProp['parent'], type=getProp['type'])
        createUpdateLangField(names, 'InputLang', newProp.name)
        return Response({'msg': 'Ok', 'status': 'success'})


class EstatePropOptionsListAdminView(ListCreateAPIView):
    queryset = EstatePropertyOption.objects.all()
    serializer_class = EstatePropOptionsListAdminSerializer

    def post(self, request, *args, **kwargs):
        getProp = request.data
        names = getProp['name']
        print(getProp)
        newPropOption = EstatePropertyOption.objects.create(parent_id=getProp['parent'])
        createUpdateLangField(names, 'InputLang', newPropOption.name)
        return Response({'msg': 'Ok', 'status': 'success'})
