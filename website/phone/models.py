from django.db import models

# Create your models here.
Category=(('WA','WashingMachine'),
           ('FR','Refridgerator'),
           ('CR','Camera'),
           ('MB','mobile'),
           ('TB','Tabs'),
           ('HE','HomeElectoronics'),
           ('SQ','Security'),
           )

class devices(models.Model):
    Name=models.CharField(max_length=100)
    Description=models.TextField()
    Category=models.CharField(Category,max_length=2)
    Date_of_Manufacture=models.DateField(default="Now()")
    Serial_Number=models.CharField(max_length=10)
    product_image=models.ImageField(upload_to="devices")

    def __str__(self):
        return self.Name


