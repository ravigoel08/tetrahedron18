from django.db import models
from django.core.validators import MaxValueValidator


class Register(models.Model):
    Name = models.CharField(max_length=20)
    Code = models.CharField(max_length=20)
    Email = models.EmailField(max_length=70)
    Contact_No = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])
    CSI = models.PositiveIntegerField(default= 0,validators=[MaxValueValidator(99999999)])
    College_Code = models.PositiveIntegerField(validators=[MaxValueValidator(999)])
    Quiz = models.CharField(max_length=20)
    Gaming = models.CharField(max_length=20)
    Coding = models.CharField(max_length=20)
    Webdesigning = models.CharField(max_length=20)
    Androiddevelopment = models.CharField(max_length=20)
    Groupdiscussion = models.CharField(max_length=20)

    def __str__(self):
        return 'Name:{},Code:{}'.format(self.Name,self.Code)
