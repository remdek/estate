from django.db import models

# Vars
LOCATION_TYPE_CHOICE = [
    ('country', 'Country'),
    ('county', 'County'),
    ('town', 'Town'),
    ('district', 'District')
]


# Create your models here.
class Lang(models.Model):
    name = models.CharField('Name', max_length=100)
    short = models.CharField('Short Name', max_length=3)

    def __str__(self):
        return self.short

    class Meta:
        verbose_name = "Languages"
        verbose_name_plural = "Languages"
        ordering = ['short']


class InputLang(models.Model):
    value = models.CharField('Input Value', max_length=250)
    lang = models.ForeignKey(Lang, related_name='inputLang_lang', on_delete=models.CASCADE)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "InputLang Value"
        verbose_name_plural = "InputLang Value"
        ordering = ['value']


class TextLang(models.Model):
    value = models.CharField('Input Value', max_length=200)
    lang = models.ForeignKey(Lang, related_name='textLang_lang', on_delete=models.CASCADE)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "TextLang Value"
        verbose_name_plural = "TextLang Value"
        ordering = ['value']


class Location(models.Model):
    name = models.CharField('Location Name', max_length=100)
    type = models.CharField('Location Type', max_length=8, choices=LOCATION_TYPE_CHOICE, default='county')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='location_parent',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Location"
        ordering = ['id']


class Translation(models.Model):
    name = models.CharField('Group', max_length=50)
    parent = models.ForeignKey('self', null=True, default=None, related_name='translation_parent',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TranslationValue(models.Model):
    value = models.ForeignKey(InputLang, related_name='translationValue_value',
                            on_delete=models.CASCADE)
    key = models.ForeignKey(Translation, related_name='translationValue_key',
                            on_delete=models.CASCADE)

    def __str__(self):
        return self.value.value
