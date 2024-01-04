from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
#This line defines a djngo model named post .It inherits from models.Model
    post_title = models.CharField(max_length=255)
    post_description = models.TextField()
    post_shortname = models.SlugField(max_length=300,unique=True)
    post_published_datetime = models.DateTimeField(auto_now_add=True)
    post_author = models.ForeignKey(User,on_delete=models.CASCADE)
    post_image = models.ImageField(upload_to='post/images/')
    #post_author is a field in the model
    #models.Foreignkey defines a foreign key relationship.Each Post instance will
    #have a

    def __str__(self):
        return self.post_title
