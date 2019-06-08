from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
'''
this is goona be baese of our usermodel AbstractBaseUser

PermissionsMixin allows us to add permission
so we can set what a user can or can't do in our system
'''
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    '''help django to works with our costem user model'''
    def create_user(self, email, name, password=None):
        '''create a new user profile object'''
        if not email:
            raise ValueError('User must have email address')
        '''now we normalizing the email address,it converts to the lowwer case so that all emails are standardize in the system'''
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        '''set_password function wll encript the password for us
        because it convert into user hash and it is best pratice'''
        user.set_password(password)
        '''using = self._db this means use the same db that we creat with userprofie manager'''
        user.save(using = self._db)
        return user

    '''how to crate a superuser'''
    def create_superuser(self, email, name, password):
        '''creates and saves a new superuser with given detailss
        '''
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    '''
    represent user profile inside our system
    '''
    email = models.EmailField(max_length=255, unique=True)
    '''unique is means only one email is in system at a time'''
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    '''is_active use to determin if currunt user is active in system
    it a req when you add custom user to the systme'''
    is_staff = models.BooleanField(default=False)

    '''object manger
    it require when substitue cosmeuser
    '''
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    '''
    USERNAME_FIELD is like handler which is used to login 
    we are going to replace it with email
    so our user login using email
    '''
    REQUIRED_FIELDS = ['name']
    '''REQUIRED_FIELDS will the list of req fields here we are using name only because email is already default set to required'''
    '''couple of helper function'''

    def get_full_name(self):
        '''
        used to get a user full name
        '''
        return self.name

    def get_short_name(self):
        '''used to get users short name'''
        return self.name
    '''it will tell which fields to print of our user objects'''
    def __str__(self):
        '''dhango uses this  when it needs to converst the object to a string'''
        return self.email