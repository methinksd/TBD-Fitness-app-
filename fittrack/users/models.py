from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    fitness_goal = models.TextField(blank=True, null=True)


from django.db import models

# Create your models here.
