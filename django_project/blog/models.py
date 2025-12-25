from django.db import models

# Create your models here.
from django.conf import settings
#from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



### title and text become columns.
class Post(models.Model):   # Each Post becomes a row in the database.
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)   # title and text become columns.
    title = models.CharField(max_length=200)
    content = models.TextField()
    #date_posted = models.DateTimeField(auto_now_add=True) # Correy ....to set the date posted to the current date time
    date_posted = models.DateTimeField(default=timezone.now) # use default so that you can change the time, you are passing the actual function as the default value so you remove () in front of timezone.now() function
    author = models.ForeignKey(User, on_delete=models.CASCADE)   # title and text become columns. if User is deleted, delete their post as well
    #text = models.TextField()
    #created_date = models.DateTimeField(default=timezone.now) 
    #published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title