from django.db import models
from django.contrib.auth.models import User


class Destination(models.Model):

      name = models.CharField(max_length=200)
      img = models.ImageField(upload_to='pics')
      desc = models.CharField(max_length=20)
      price =models.IntegerField()
      offer = models.BooleanField(default = False)
      def __str__(self):
            return self.name

class Product(models.Model):

      name = models.CharField(max_length=200)
      img = models.ImageField()
      desc = models.CharField(max_length=20)
      price =models.IntegerField()

      def __str__(self):
            return self.name

    

class Subscribe(models.Model):
      name = models.CharField(max_length=20)
      youremail = models.EmailField()

      def __str__(self):
            return self.name

class Contact(models.Model):
      name = models.CharField(max_length=10)
      mobile = models.CharField(max_length=12)
      email = models.EmailField()
      
      def __str__(self):
            return self.name



# class customer(models.Model):
#       product = models.ForeignKey(max_length=20, null=True)




      


