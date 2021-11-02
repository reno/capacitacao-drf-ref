from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    '''Custom user manager. Extends the default UserManager.'''

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return super()._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return super()._create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    '''Custom user model.

    CustomUser inherits the following fields from AbstractUser:
    username, first_name, last_name, date_joined, last_login, is_staff, is_superuser
    '''
    email = models.EmailField(
        unique=True,
        error_messages = {'unique': 'This email is already registered.'}
    )
    is_active = models.BooleanField(default=True)
    bio = models.CharField(max_length=280, blank=True, null=True)
    website_url = models.URLField(max_length=555, blank=True, null=True)
    objects = CustomUserManager()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.username
