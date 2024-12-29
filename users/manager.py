from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,role,password=None,**extra_fieds):
        user=self.model(role=role,**extra_fieds)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self,role,password=None,**extra_fieds):
        extra_fieds.setdefault("is_staff",True)
        extra_fieds.setdefault("is_active",True)
        extra_fieds.setdefault("is_superuser",True)
        
        return self.create_user(role,password=None,**extra_fieds)