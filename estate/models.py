from django.db import models
from locales.models import Location, InputLang, TextLang
from users.models import User

ESTATE_PROPERTY_SELECT_TYPE = [
    ('input', 'Without Childrens'),
    ('select', 'Children Select'),
    ('multi', 'Multiple Childrens')
]

PRICE_PAYMENT_VALUE = [
    ('%', 'Percent'),
    ('€', 'Euro')
]

class EstateStatus(models.Model):
    name = models.ManyToManyField(InputLang, related_name="estateStatus_name")

    def __str__(self):
        return self.pk

#### -----Estate Properties---------------
class EstateProperty(models.Model):
    """Estate Objects Properties"""
    name = models.ManyToManyField(InputLang, related_name="estateProperty_name")
    parent = models.ForeignKey('self', null=True, blank=True, default=None, related_name='estateProperty_children',
                               on_delete=models.CASCADE)
    type = models.CharField('Estate Property Select Type', choices=ESTATE_PROPERTY_SELECT_TYPE,
                                max_length=8, db_index=True)
    slug = models.SlugField("Slug", db_index=True)

    def __str__(self):
        return self.name


class EstatePropertyOption(models.Model):
    """Estate Properties options for select & multiselect"""
    name = models.ManyToManyField(InputLang, related_name="estatePropertyOption_name")
    parent = models.ForeignKey(EstateProperty, related_name='estatePropertyOption_children', on_delete=models.CASCADE)

    def __str__(self):
        return self.pk


class EstatePropertyValue(models.Model):
    """Estate Properties Values for input, select & multiselect"""
    input = models.CharField('Input value', max_length=20)
    select = models.ManyToManyField(EstatePropertyOption, related_name="estatePropertyValue_select", blank=True)
    parent = models.ForeignKey(EstateProperty, related_name='EstatePropertyValue_children',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.pk



#  -----Estate Categories---------------

class EstateCategory(models.Model):
    """Estate Categories"""
    name = models.ManyToManyField(InputLang, related_name="estateCategory_name")
    slug = models.SlugField("Slug", db_index=True)
    title = models.ManyToManyField(InputLang, related_name="estateCategory_title")
    description = models.ManyToManyField(TextLang, related_name="estateCategory_description")
    robots = models.BooleanField("Robots", default=True, db_index=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='estateCategory_children',
                               on_delete=models.CASCADE)
    props = models.ManyToManyField(EstateProperty, related_name="estateCategory_props")

    def __str__(self):
        return self.slug
    #
    class Meta:
        verbose_name = "Categories"
        verbose_name_plural = "Categories"
        ordering = ['pk']

class EstateImageCard(models.Model):
    name = models.CharField('Header', max_length=100)
    field1 = models.CharField('Field 1', max_length=100, blank=True)
    field2 = models.CharField('Field 2', max_length=100, blank=True)
    field3 = models.CharField('Field 3', max_length=100, blank=True)
    field4 = models.CharField('Field 4', max_length=100, blank=True)
    field5 = models.CharField('Field 5', max_length=100, blank=True)
    total = models.CharField('Field 5', max_length=100, blank=True)

    def __str__(self):
        return self.name

class Estate(models.Model):
    """Estate Objects"""
    categories = models.ManyToManyField(EstateCategory, related_name="estate_categories")
    type = models.ForeignKey(EstateCategory, related_name='estate_type',
                                      on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(EstateStatus, related_name='estate_status', on_delete=models.SET_NULL, null=True)

    country = models.ForeignKey(Location, related_name='estate_country',
                                on_delete=models.CASCADE)
    county = models.ForeignKey(Location, related_name='estate_county',
                               on_delete=models.CASCADE)
    town = models.ForeignKey(Location, related_name='estate_town',
                             on_delete=models.CASCADE)
    district = models.ForeignKey(Location, related_name='estate_district',
                                 on_delete=models.SET_NULL, null=True, blank=True)

    street = models.CharField('Street', max_length=250)
    address = models.CharField('Address', max_length=200)
    address_num = models.CharField('Address Num', max_length=10)
    hide_address_num = models.BooleanField('Hide address Number', default=False)
    flat = models.CharField('Flat', max_length=10, blank=True)
    hide_flat_num = models.BooleanField('Hide address Number', default=False)
    place = models.CharField('Place', max_length=200)

    lat = models.CharField('Latitude', max_length=15, blank=True)
    lon = models.CharField('Longitude', max_length=15, blank=True)

    cadastral = models.CharField('Cadastral Number', max_length=20, blank=True)
    km_from_city = models.PositiveIntegerField("Km from City", null=True, blank=True)

    area = models.DecimalField("Area", max_digits=10, decimal_places=2)
    price = models.PositiveIntegerField("Price")
    price_m2 = models.DecimalField("Price for m2", max_digits=10, decimal_places=2, null=True)

    comission = models.PositiveIntegerField("Comission", blank=True, null=True)
    comission_pay_value = models.CharField('Comission payment value', max_length=8,
                                           choices=PRICE_PAYMENT_VALUE, default='%')
    deposit = models.PositiveIntegerField("Deposit", blank=True, null=True)
    deposit_pay_value = models.CharField('Deposit payment value', max_length=8,
                                           choices=PRICE_PAYMENT_VALUE, default='%')
    prepayment = models.PositiveIntegerField("Prepayment", blank=True, null=True)
    prepayment_pay_value = models.CharField('Comission payment value', max_length=8,
                                           choices=PRICE_PAYMENT_VALUE, default='%')

    summer_payments = models.DecimalField("Summer payments", max_digits=5, decimal_places=2, null=True, blank=True)
    winter_payments = models.DecimalField("Winter payments", max_digits=5, decimal_places=2, null=True, blank=True)

    towater_distance = models.CharField('Distance to water', max_length=8, blank=True)
    # promo_text = models.ForeignKey(Location, related_name='estate_promoText',
    #                              on_delete=models.SET_NULL, null=True, blank=True)

    # owner
    # broker

    images = models.ManyToManyField('attach.Image', related_name="estate_images", blank=True)
    # files = models.ManyToManyField('attach.File', related_name="estate_files", blank=True)
    robots = models.BooleanField("Robots", default=True, db_index=True)

    broker = models.ForeignKey(User, related_name='estate_broker', on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(User, related_name='estate_owner', on_delete=models.SET_NULL, null=True)

    created_by = models.ForeignKey(User, related_name='estate_CreatedBy', on_delete=models.SET_NULL, null=True)
    updated_by = models.ForeignKey(User, related_name='estate_UpdatedBy', on_delete=models.SET_NULL, null=True)

    created = models.DateTimeField("Created", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField("Updated", auto_now_add=False, auto_now=True)


    def __str__(self):
        return self.address

    class Meta:
        verbose_name = "Estate Objects"
        verbose_name_plural = "Estate Objects"
        ordering = ['id']
