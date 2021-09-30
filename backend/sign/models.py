from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
  def create_user(self, name, email, nick_name, phone_number, password=None):
    if not name:
      raise ValueError('user name')
    if not email:
      raise ValueError('user email')
    user = self.model(
      name=name,
      email=self.normalize_email(email),
      nick_name=nick_name,
      phone_number=phone_number,
    )
    user.set_password(password)
    user.save(using=self._db)
    return user
  
  def create_superuser(self, name, email, nick_name, phone_number, password):
    user = self.create_user(
      name=name,
      email=self.normalize_email(email),
      nick_name=nick_name,
      phone_number=phone_number,
      password=password
    )
    user.is_admin = True
    user.save(using=self._db)
    return user

class User(AbstractBaseUser):
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length=255, unique=True)
  nick_name = models.CharField(max_length=100)
  phone_number = models.CharField(max_length=20)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)

  objects = UserManager()

  USERNAME_FIELD  = 'name'
  REQUIRED_FIELDS = ['email', 'nick_name', 'phone_number']

  def __str__(self):
    return self.name

def has_perm(self, perm, obj=None):
  return True

def has_module_perms(self, app_label):
  return True

@property
def is_staff(self):
  return self.is_admin



# class CustomUser(AbstractUser):
#   phone_number = models.CharField(max_length=30)
#   nickname = models.CharField(max_length=100)
