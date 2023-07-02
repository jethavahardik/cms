from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group, BaseUserManager
from django.utils.translation import gettext_lazy as _


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
class TimeStampModel(models.Model):
    # timestamp model for time of creation and updation
    created_at = models.DateTimeField(_("time of creation"), auto_now_add=True)
    updated_at = models.DateTimeField(_("time of updation"), auto_now=True)
    
    class Meta:
        abstract = True
        
class User(AbstractUser, TimeStampModel):
    # user model 
    # fields like is_superuser, is_staff, is_active and date_joined is created from AbstractUser
    
    email = models.EmailField(_("email_address"), unique=True)
    first_name = models.CharField(_("first_name"),max_length=100, blank=True, null=True)
    last_name = models.CharField(_("last_name"),max_length=150, blank=True, null=True)
    phone_number = models.CharField(_("phone_number"),max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("user permissions"),
        blank=True,
        related_name="user_permissions_set",
    )
    groups = models.ManyToManyField(Group, verbose_name=_("groups"), blank=True, related_name="user_groups")

    def __str__(self):
        return self.email