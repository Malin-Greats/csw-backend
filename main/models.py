from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.core.validators import MaxValueValidator,\
    MinValueValidator, MinLengthValidator
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from random import randint
from main.choices import MEMBER, MANAGER,\
    REGISTRATION_STATUS, ROLES

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)



class UserManager(BaseUserManager):

    def create_user(self, username,first_name, last_name, email, password=None, **kwargs):
        """Create and return a `User` with an email, phone number, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email.')

        user = self.model(username=username,first_name=first_name, last_name=last_name, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')
        if email is None:
            raise TypeError('Superusers must have an email.')
        if username is None:
            raise TypeError('Superusers must have an username.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255)
    first_name = models.CharField(db_index=True, max_length=255, blank=True)
    last_name = models.CharField(db_index=True, max_length=255, blank=True)
    email = models.EmailField(db_index=True, unique=True,  null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False,)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"


class Member(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="members")
    member_number = models.CharField(max_length=10, blank=True)
    next_of_kin = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    date_of_birth = models.DateField(
                                     validators=[MaxValueValidator(
                                         timezone.now().date())])
    age = models.IntegerField(blank=True)
    town = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    national_id = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)


    def __str__(self) -> str:
        return self.member_name

    def calculate_age(self):
        today = timezone.now()
        born = self.date_of_birth
        self.age = today.year - born.year\
            - ((today.month, today.day) < (born.month, born.day))

    def generate_member_number(self):
        self.member_number = f'CSW-{self.random_with_N_digits(8)}'

    def random_with_N_digits(n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)
        
    def save(self, *args, **kwargs):
        self.calculate_age()
        super().save(*args, **kwargs)


def member_post_save(sender, instance, created, *args, **kwargs):
    if created:
        instance.generate_member_number()
        instance.save()


post_save.connect(member_post_save, sender=Member)