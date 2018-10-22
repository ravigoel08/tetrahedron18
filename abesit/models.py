from django.db import models
from django.core.validators import MaxValueValidator


class Register(models.Model):
    Name = models.CharField(max_length=20)
    Roll_No = models.CharField(default=0,max_length=12)
    Year =models.CharField(default=0,max_length=2)
    Email = models.EmailField(max_length=70)
    Contact_No = models.TextField(max_length=12)
    CSI = models.TextField(default=0,max_length=10)
    College_Code = models.PositiveIntegerField(validators=[MaxValueValidator(999)])
    Quiz = models.CharField(max_length=20)
    Gaming = models.CharField(max_length=20)
    Coding = models.CharField(max_length=20)
    Webdesigning = models.CharField(max_length=20)
    Androiddevelopment = models.CharField(max_length=20)
    Groupdiscussion = models.CharField(max_length=20)

    def __str__(self):
        return 'Name:{},Code:{}'.format(self.Name,self.Roll_No)
