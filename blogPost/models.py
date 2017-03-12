from django.db import models
from django.utils import timezone

class WritePost(models.Model):
    date_posted = models.DateField(blank=True, null=True)
    blog_title = models.CharField(max_length=300)
    blog_post = models.CharField(max_length=3000)
    post_author = models.CharField(max_length=50)
    
    def publish(self):
        self.date_posted =timezone.now()
        self.save()
    
    def __str__(self):
        return self.blog_title

        
