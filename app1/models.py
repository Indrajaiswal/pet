from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models import post_save
from django.dispatch import receiver
import uuid
from .manager import UserManager




class User(AbstractUser)
    username = None
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(defult=False)
    otp_vderification_token = models.CharField(mqax_length=6 , null=True, blank=True)


    USERNAME_Field = 'email'
    REQUIRED_FIELDS = []

    object = UserManager()

    def name(self):
        return self.first_name + '' + self.last_name
    def __str__(self):
        return self.email


