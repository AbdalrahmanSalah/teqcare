from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from safedelete.models import SafeDeleteModel #,HARD_DELETE_NOCASCADE, SOFT_DELETE_CASCADE
from safedelete.managers import SafeDeleteManager
import safedelete

class UserManager(BaseUserManager,SafeDeleteManager):
    """creating a custom User Manager class which will allow
    creating both kind of users (superuser and other users)
    with specific requirements and autherities for each kind"""
    _safedelete_visibility = safedelete.DELETED_VISIBLE_BY_PK
    def create_user(self, email, password, **extra_fields):
        """creates and saves a new user"""
        if not email :
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """creating and saving a new suberuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_suberuser = True
        user.save(using=self._db)

        return user
class User(AbstractBaseUser, PermissionsMixin, SafeDeleteModel):
    """creating user with email instead of using username"""
    _safedelete_policy = safedelete.SOFT_DELETE
    email = models.EmailField(max_length=255 , unique = True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
