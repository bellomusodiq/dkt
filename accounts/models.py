from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='accounts/profile_image', blank=True, null=True)
    dokita = models.CharField(max_length=100)
    user_type = models.ForeignKey(UserType, on_delete=models.DO_NOTHING)
    age = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(default=0)
    height = models.PositiveIntegerField(default=0)
    blood_type = models.CharField(max_length=3)

    def __str__(self):
        return self.user.username


class AllergiesReaction(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    detail = models.CharField(max_length=120)

    def __str__(self):
        return self.details


class Meditation(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    detail = models.CharField(max_length=120)

    def __str__(self):
        return self.profile.user.username


class PersonalDoctor(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile')
    personal_doctor = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='personal_doctor')

    def __str__(self):
        return self.profile.user.username


class EmergencyContact(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=400)
    phone_number = models.CharField(max_length=20)
    relationship = models.CharField(max_length=100)


class Checkup(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_profile')
    doctor = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='doctor_profile')
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.profile.user.username




