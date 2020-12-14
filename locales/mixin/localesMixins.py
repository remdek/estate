from locales.models import Lang, InputLang, TextLang
from locales.serializers import InputLangSerializer, TextLangSerializer


# get translateValue
def translate_value(self, obj, type):
    request = self.context.get("request")
    # if request:
    #     print(request.GET['lang'])
    #     selectedLang = request.GET.get('lang')
    # else:
    selectedLang = None
    if type == 'InputLang':
        langsArr = InputLangSerializer(obj, many=True).data
    else:
        langsArr = TextLangSerializer(obj, many=True).data

    if selectedLang:
        for lang in langsArr:
            if lang.get('lang') == selectedLang:
                return lang.get('value')
    else:
        langs = {}
        for lang in langsArr:
            langs.update({lang.get('lang'): lang.get('value')})

        return langs


def translateUpdate(self, obj, type):
    if type == 'InputLang':
        translateArr = InputLangSerializer(obj, many=True).data
    else:
        translateArr = TextLangSerializer(obj, many=True).data

    if len(translateArr):
        langs = {}
        for lang in translateArr:
            # langs.update({lang.get('lang'): lang.get('value')})
            langs.update({lang.get('lang'):
                              {"value": lang.get('value'), "id": lang.get('id')}})
    else:
        langs = None
    return langs


def createUpdateLangField(arr, type, new):
    if arr and len(arr):
        langs = Lang.objects.all()
        for key in arr:
            '''updating'''
            if arr[key]['id']:
                if type == 'InputLang':
                    InputLang.objects.filter(pk=arr[key]['id']).update(value=arr[key]['value'])
                else:
                    TextLang.objects.filter(pk=arr[key]['id']).update(value=arr[key]['value'])
                    '''creating'''
            elif len(arr[key]['value']) > 0:
                new.create(value=arr[key]['value'], lang=langs.get(short=key))
