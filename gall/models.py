from django.db import models

# Create your models here.


class Location(models.Model):
    location = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.location
   

class Category(models.Model):
    name = models.CharField(max_length=10,,unique=True)

    
    def __str__(self):
        return self.name


class Posts(models.Model):
    name = models.CharField(max_length=50)
    caption = models.CharField(max_length = 50)
    description = models.CharField(max_length=50)
    article_image = models.ImageField(upload_to = 'articles/')
    location = models.ForeignKey(Location)
    category = models.ManyToManyField(Category)

    @classmethod
    def save_post(self):
        self.save()
    @classmethod
    def get_posts(cls):
         posts = cls.objects.all()
         return posts
    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__icontains=search_term)
        return images

    
    def __str__(self):
        return self.name