from django.db import models


# Create your models here.
class Travel(models.Model):
    id = models.AutoField(primary_key=True)
    Yourname=models.CharField(max_length=50)
    Destination=models.CharField(max_length=50)
    Person=models.CharField(max_length=100)
    HowmanyDays=models.IntegerField()
    profile_image= models.ImageField(upload_to='profile_images/',null=True,blank=True)
    resume= models.FileField(upload_to='resume/',null= True, blank=True)
   
    
    def __str__(self):
        return f"{self.Yourname} {self.Destination} {self.Person} {self.HowmanyDays}"