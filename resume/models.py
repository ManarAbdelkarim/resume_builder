from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth import get_user_model 
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class PersonalInfo(models.Model):

    full_name =  models.CharField(max_length=100)
    user_image = models.ImageField(upload_to="static/images")
    job_title =  models.CharField(max_length=200)
    email = models.EmailField()
    website = models.URLField()
    phone_number = PhoneNumberField()
    personal_info = models.TextField(default='a summary about yourself')
    key_skills = models.TextField()
    job_title_c = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description_c = models.TextField()
    university_name = models.CharField(max_length=200)
    major = models.CharField(max_length=200)
    description_u = models.TextField()
  
  
    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('cv', args=[str(self.id)])



