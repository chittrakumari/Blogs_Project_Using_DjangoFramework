from django.db import models

# Create your models here.
class Article(models.Model):
    #for small sized text we use char feild.
    title = models.CharField(max_length=100)
    
    # feild used by django used to store and generate valid urls
    slug =models.SlugField()
    
    body = models.TextField()
    
    #auto_now_add=automatically populates the time feild when the article is created
    date=models.DateTimeField(auto_now_add=True)
    
    thumb = models.ImageField(default='default.png',blank=True)
    
    #how the objects would look if we retrive them i.e through titles
    def __str__(self):
        return self.title;
        
        
    def snippet(self):
        return self.body[:50] + "..."