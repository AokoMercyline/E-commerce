# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from pyuploadcare.dj.models import ImageField
from pyuploadcare.dj.forms import FileWidget

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from pyuploadcare.dj.models import ImageField
from pyuploadcare.dj.forms import FileWidget

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    profile_id = models.IntegerField(default=0)
    image = models.ImageField(upload_to = 'images/', default="")
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)
    AUTH_PROFILE_MODULE = 'app.UserProfile'

    def __str__(self):
            return f'{self.user.username} Profile'

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()
        
    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()

# Create your models here.
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )

class Product(models.Model):
    productName = models.CharField(max_length=200)
    productDescription = models.TextField(null=True, blank=True)
    image_url = models.CharField(max_length=1000, null=True, blank=True)
    productPrice = models.FloatField(null=True, blank=True)
    # productCategory
    def __str__(self):
        return self.name