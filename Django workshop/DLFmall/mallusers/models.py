from django.db import models

# Create your models here.
class userDetails(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(primary_key=True)
    number=models.IntegerField(unique=True)
    password=models.CharField(max_length=20)
    address=models.CharField(max_length=100) # null and blank is used to non mendatory action


membershipName=(("Gold","Gold"),
                    ("Silver","Silver"),
                    ("Bronze","Bronze"))

class memmbershipDetails(models.Model):
        membershipCategory=models.CharField(max_length=20, choices=membershipName)
        membershipId=models.AutoField(primary_key=True)
        email=models.ForeignKey(userDetails,on_delete=models.CASCADE)
        validaty=models.DateField()


class eventDetails(models.Model):
    eventId=models.AutoField(primary_key=True)
    eventname=models.CharField(max_length=50,unique=True)
    eventDescription=models.CharField(max_length=100)
    eventDate=models.DateTimeField()
    eventVenue=models.CharField(max_length=100)

class eventRegistrationDetails(models.Model):
    registrationId=models.AutoField(primary_key=True)
    eventId=models.ForeignKey(eventDetails,on_delete=models.CASCADE)
    email=models.ForeignKey(userDetails,on_delete=models.CASCADE)
