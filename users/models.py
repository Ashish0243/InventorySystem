from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUserModel(AbstractUser):
    roles=[("CC","Club_Coordinator"),("Core","Core_Team")]
    role=models.CharField(max_length=25,choices=roles,null=False,blank=False)
    
    def is_CC(self):
        return self.role=="Club_Coordinator"
    
    def is_Core(self):
        return self.role=="Core_Team"
        