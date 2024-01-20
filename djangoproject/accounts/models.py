from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Permission


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError("The phone number is not given.")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.is_active = True
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff = True")

        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser = True")
        return self.create_user(phone_number, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    GENDER_CHOICES = (
        (1, 'male'),
        (2, 'female'),
        (3, 'other')
    )

    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True)
    email=models.EmailField()
    password = models.CharField(max_length=128, null=True)
    age = models.CharField(max_length=10, null=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES)
    aadhar_number = models.CharField(max_length=128, null=True)
    district = models.CharField(max_length=128, null=True)
    panchayath = models.CharField(max_length=128, null=True)
    krishibhavan = models.CharField(max_length=128, null=True)
    pincode = models.CharField(max_length=15, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['gender']

    objects = UserManager()

    def __str__(self):
        return self.phone_number

    def get_all_permissions(self, obj=None):
        return self.user_permissions.all() if hasattr(self, 'user_permissions') else set()

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True

    def __str__(self):
        return self.phone_number or "No phone number"
class LandRegistrationInfo(models.Model):


    phone_number = models.ForeignKey(CustomUser,blank=True, null=True,on_delete=models.SET_NULL)





    def __str__(self):
        return str(self.phone_number)

class LandInfo(models.Model):
    AREA_CHOICES = (
        ('Own Land', 'own land'),
        ('Leased Land', 'leased land'),
        ('Both', 'both')
    )
    IRRIGATION_CHOICES = (
        ('Canal', 'canal'),
        ('Well', 'well'),

    )
    CROP_CHOICES = (
        ('Tomato', 'tomato'),
        ('Cardomom', 'cardomom'),
        ('Paddy', 'paddy')
    )

    phone_number = models.ForeignKey(CustomUser,blank=True, null=True,on_delete=models.SET_NULL)
    crop=  models.ForeignKey(LandRegistrationInfo,blank=True, null=True,on_delete=models.SET_NULL)
    irigation_facilities=models.CharField(max_length=128, choices=IRRIGATION_CHOICES, null=True, blank=True)
    Area = models.CharField(max_length=128, choices=AREA_CHOICES, null=True, blank=True)
    name_of_field = models.CharField(max_length=128, null=True)
    crop_variety=models.CharField(max_length=128, choices=CROP_CHOICES, null=True, blank=True)

    land_area= models.CharField(max_length=128, null=True)

    survey_number= models.CharField(max_length=128, null=True)
    tax_receipt_image = models.ImageField(upload_to='images/', null=True, blank=True)
    pincode = models.CharField(max_length=15, null=True)
    panchayath = models.CharField(max_length=128, null=True)

    district= models.CharField(max_length=128, null=True)
    state = models.CharField(max_length=128, null=True)

    krishibhavan= models.CharField(max_length=128, null=True)

    def __str__(self):
        return str(self.phone_number) if self.phone_number else "No phone number available"


