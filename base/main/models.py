from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    twitter = models.CharField(max_length=500)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])