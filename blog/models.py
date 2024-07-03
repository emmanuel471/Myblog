from django.db import models
from django.contrib.auth.models import User



def get_default_image():
    return 'images/profiledefault.png'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=200, null=False)
    objective = models.TextField(max_length=600, null=False)
    userimage = models.ImageField(null=False, default=get_default_image)

    def __str__(self):
	    return self.user.username
 
class Project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
     
class Category(models.Model):
      name = models.CharField(max_length=50)
      
      def __str__(self):
          return self.name 
class Education(models.Model):
      qualification =models.CharField(max_length=100)
      status = models.CharField(max_length=50)
      category = models.ForeignKey(Category, on_delete=models.CASCADE, default =1)
      
      def __str__(self):
        return self.qualification