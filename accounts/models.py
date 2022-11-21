from distutils.command.upload import upload
import email
from tabnanny import verbose
from django.db import models
from django.conf import settings
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager

class MyAccountManager(BaseUserManager):
    def _create_user(self, email, name, address, phone_number, LC1_letter, nin, National_Id, password):
        if not email:
            raise ValueError("User must have an email")
        if not name:
            raise ValueError("User must have a username")

        user = self.model(
               email = self.normalize_email(email),
               name = name, address=address,
               phone_number = phone_number, LC1_letter = LC1_letter, nin = nin, National_Id=National_Id, password=password
            )   

        user.set_password(password)
        user.save(using=self._db)
        return user 

    def create_user(self, email, name, address=None, phone_number=None, LC1_letter=None, nin=None, National_Id=None, password=None):
        return self._create_user(email, name, address, phone_number, LC1_letter, nin, National_Id, password)

    def create_superuser(self, email, name, password):
        """
        Creates and saves a superuser with the given email, name and password.
        """
        user = self.create_user(email=email,
            name=name,
            password=password,
            
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user




class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    name = models.CharField(verbose_name='name', unique=True, max_length=60, null=True)
    address = models.CharField(verbose_name='address', max_length=200, null=True)
    phone_number = models.IntegerField(verbose_name='phone_number', null=True)
    LC1_letter = models.FileField(verbose_name='Lc1_letter', null=True )
    nin = models.CharField(verbose_name='NIN' , max_length=60, blank=False, null=True)
    National_Id = models.CharField(verbose_name='National_ID',  unique=True, max_length=60, blank=False, null=True)
    last_login = models.DateTimeField(verbose_name='last_login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = MyAccountManager()


    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True