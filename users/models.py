from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from locales.models import Location


# Create your models here.
class Contacts(models.Model):
    name = models.CharField("Contact Name", max_length=100)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class Group(models.Model):
    name = models.CharField("Groups", max_length=20)
    parent = models.ForeignKey('self', null=True, default=None, related_name='group_parent',
                               on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, block = False):
        if not email:
            raise ValueError("Email or phone required")
        if not password:
            raise ValueError("Password required")
        # if not first_name:
        #     raise ValueError("Укажите ваше имя")

        user_obj = self.model(
            email = self.normalize_email(email),

        )
        user_obj.set_password(password)
        # user_obj.group.set(group)
        user_obj.block = block
        # user_obj.staff = is_staff
        # user_obj.admin = is_admin
        # user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            # group = [2],
            # is_staff=True
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            # is_staff=True,
            # is_admin=True
        )
        return user

class User(AbstractBaseUser):
    email = models.EmailField("Email", unique=True, blank=True, null=True, default=None)
    phone = models.DecimalField("Телефон", blank=True, null=True, max_digits=11, decimal_places=0)
    block = models.BooleanField("Active", default=False)
    block_description = models.TextField("Blocking reason", blank=True)

    group = models.ManyToManyField(Group, related_name='user_group', verbose_name='Group')
    password = models.CharField('Password', max_length=128, blank=True)

    first_name = models.CharField("First name", max_length=50)
    last_name = models.CharField("Last Name", max_length=50, blank=True)
    position = models.CharField("Должность", max_length=100, blank=True)

    avatar = models.ForeignKey('attach.Image', verbose_name="Avatar", blank=True, null=True, on_delete=models.SET_NULL,
                               related_name='user_avatar')
    description = models.TextField("Description", blank=True)
    birth = models.DateField("Date birth", blank=True, null=True)
    uid = models.CharField("User ID", max_length=20, blank=True)

    address = models.CharField("Address", blank=True, max_length=250)

    contacts = models.ManyToManyField(Contacts, through='UserContacts', related_name="user_contacts",
                                    blank=True)
    card = models.DecimalField("Номер карты", blank=True, null=True, max_digits=16, decimal_places=0)

    last_ip = models.CharField("Last IP", max_length=20, blank=True)

    confirm = models.CharField("Код подтверждения", max_length=32, blank=True, null=True)

    created = models.DateTimeField("Создана", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField("Обновлена", auto_now_add=False, auto_now=True, db_index=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    #
    # def __str__(self):
    #     return self.email
    #
    # def has_perm(self, perm, obj=None):
    #     return True
    #
    # def has_module_perms(self, app_label):
    #     return True
    #
    # @property
    # def is_staff(self):
    #     return self.staff
    #
    # @property
    # def is_admin(self):
    #     return self.admin
    #
    # @property
    # def is_active(self):
    #     return self.active

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class UserContacts(models.Model):
    user = models.ForeignKey(User, verbose_name="User", related_name="userContacts_user", on_delete=models.CASCADE)
    contact = models.ForeignKey(Contacts, verbose_name="Contact", related_name="userContacts_contact", on_delete=models.CASCADE)
    value = models.CharField("Value", max_length=200)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'UserContact'
        verbose_name_plural = 'UsersContacts'