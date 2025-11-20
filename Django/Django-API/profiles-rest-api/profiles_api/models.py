from django.db import models # type: ignore
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager # type: ignore
from django.contrib.auth.models import PermissionsMixin # type: ignore
from django.conf import settings # type: ignore
# Create your models here.


class UserProfileManager(BaseUserManager):
    """Manager for our user profiles"""
     
    def create_user(self,email,name,password=None):
        """Create a new user profile"""
        
        if not email:
            raise ValueError('Use rmust have an email')
        
        email=self.normalize_email(email)
        user = self.model(email=email,name=name)
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self,email,name,password):
        """Create and save new superuser with given details"""
        user = self.create_user(email,name,password)
        
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        
        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""
    email=models.EmailField(max_length=255, unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    
    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def get_full_name(self):
        """Retieve full name of user"""
        return self.name
    
    def get_short_name(self):
        """Retieve short name of user"""
        return self.name
    
    def __str__(self):
        """Return string representation of our user"""
        return self.email
    
class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text=models.CharField(max_length=255)
    created_on=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return the model as a String"""
        return self.status_text