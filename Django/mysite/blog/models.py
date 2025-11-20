from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
    caption=models.CharField(max_length=20)
    def __str__(self):
        return self.caption
    

class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.fullname()

class Post(models.Model):
    title=models.CharField(max_length=150)
    excerpt=models.CharField(max_length=200)
    # image_name=models.CharField(max_length=100)
    image_name=models.ImageField(upload_to='images',null=True, height_field=None, width_field=None, max_length=None)
    date=models.DateField(auto_now=True, auto_now_add=False)
    slug=models.SlugField(unique=True,db_index=True)
    content=models.TextField(validators=[MinLengthValidator(10)])
    author=models.ForeignKey(Author, on_delete=models.SET_NULL,null=True,related_name='posts')
    tag=models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.title    
    
class Comment(models.Model):
    user_name=models.CharField(max_length=120)
    user_email=models.EmailField()
    text=models.TextField(max_length=400)
    post=models.ForeignKey(Post,on_delete=models.CASCADE, null=True,related_name='comments')
    def __str__(self):
        return self.text


