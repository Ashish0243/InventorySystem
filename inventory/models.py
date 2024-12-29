from django.db import models

class Inventory(models.Model):
    item=models.CharField(null=False,blank=False,max_length=100)
    description=models.TextField(max_length=500,null=True,blank=True)
    image=models.FileField(upload_to="static/images/")
    quantity_available=models.IntegerField(default=0)
    quantity_claimable=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
