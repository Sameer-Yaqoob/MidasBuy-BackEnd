from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, full_name, profile_picture=None, gender=None,  username=None, password=None, is_admin=False, is_staff=False, is_active=True):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not full_name:
            raise ValueError("User must have a full name")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.full_name = full_name
        user.username = username
        user.set_password(password)  # change password to hash
        # user.profile_picture = profile_picture
        user.gender = gender
        user.admin = is_admin
        user.profile_picture = profile_picture
        user.staff = is_staff
        user.active = is_active
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, profile_picture, gender, full_name, password=None):
        user = self.create_user(
            email,
            full_name,
            profile_picture,
            gender,
            password=password,
            is_staff=True,
        )
        return user

    def create_superuser(self,  email, profile_picture, gender, full_name, username, password=None):
        user = self.create_user(
            email,
            full_name,
            profile_picture,
            gender,
            username,
            password=password,
            is_staff=True,
            is_admin=True,
        )
        return user

class User(AbstractUser):
   name = models.CharField(max_length=100)
   email = models.CharField(max_length=100, unique=True)
   password = models.CharField(max_length=100)
   # username = models.CharField(max_length=100, default="", blank=True, null=True)
   
   USERNAME_FIELD = 'username'
   REQUIRED_FIELDS = []
   # objects = UserManager()

