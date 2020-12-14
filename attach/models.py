import os, datetime
from django.db import models
from users.models import User
from django_resized import ResizedImageField

from gloreal_dj.mixins.mixins import generateRandomString

def image_folder(instance, filename, allow_unicode=True):
    # print('instance', instance)
    # if (instance.type.id == 9):
    #     dir = 'img/orders'
    # elif (instance.type.id == 5):
    #     dir = 'img/completed'
    # else:
    dir = 'img'
    filename = filename.lower()
    if filename.endswith('.jpg'):
        ext = 'jpg'
    elif filename.endswith('.jpeg'):
        ext = 'jpeg'
    elif filename.endswith('.png'):
        ext = 'png'
    elif filename.endswith('.webp'):
        ext = 'webp'
    elif filename.endswith('.gif'):
        ext = 'gif'
    string = generateRandomString(32)
    filename = string + '.'+ ext
    now = datetime.datetime.now()
    filepath = f"{dir}/{now.year}/{now.month}/{filename}"
    return filepath


# Create your models here.
class Image(models.Model):
    url = ResizedImageField(size=[800, 600], upload_to=image_folder)
    name = models.CharField("Alt", max_length=150, blank=True)
    owner = models.ForeignKey(User, verbose_name="", related_name="image_owner",
                              on_delete=models.PROTECT, default=1)
    direction = models.CharField('Direction', max_length=1, default='h')
    created = models.DateTimeField("Created", auto_now_add=True, auto_now=False)

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.url.path):
            os.remove(self.url.path)
        super(Image, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
