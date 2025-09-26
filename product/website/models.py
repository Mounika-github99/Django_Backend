from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()

    def __str__(self):
        return self.name


class AuthUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    REQUIRED_FIELDS = ["email"]
    def __str__(self):
        return self.email


# Signal to create auth token when a user is created
@receiver(post_save, sender=AuthUser)
def create_auth_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
