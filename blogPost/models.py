from django.db import models
from django.utils import timezone
from django.db.models import permalink
from django.template.defaultfilters import slugify

class WritePost(models.Model):
    date_posted = models.DateField(blank=True, null=True)
    blog_title = models.CharField(max_length=300)
    blog_post = models.CharField(max_length=3000)
    post_author = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, default='pblog')
    absolink = models.CharField(max_length=150)
    
    def __str__(self):
        return self.blog_title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.blog_title)
        self.absolink = self.get_absolute_url
        super(WritePost, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse("post_detail",args=(self.slug,))
