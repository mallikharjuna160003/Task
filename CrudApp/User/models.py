from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import uuid
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True)
    name = models.CharField(max_length=200, blank=True,null=True)
    gender = models.CharField(max_length=200, blank=True,null=True)
    dateofbirth = models.DateField(blank=True,null=True)
    phone = models.CharField(max_length=200, blank=True,null=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return str(self.user.username)
class Address(models.Model):
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    address1 = models.TextField(max_length=200, blank=True,null=True)
    address2 = models.TextField(max_length=200, blank=True,null=True)
    pincode = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return str(self.pincode)
