from django.db import models
from datetime import datetime 


class Categories(models.Model):
    category_name = models.CharField(max_length = 50, null=False)
    category_summury = models.CharField(max_length = 200)
    url_slug = models.CharField(max_length = 30, null=False)
    def __str__(self):
        return "Category: %s" %(self.category_name)


class Blog_news(models.Model):
    tittle = models.CharField(max_length = 200, null=False)
    text = models.TextField(null=False)
    date = models.DateTimeField(default=datetime.now())
    published_date = models.DateTimeField("date published", 
                                          null=True, blank=True)
    image =models.ImageField(upload_to='img/',
                             blank= True, null=True)
    news_category = models.ForeignKey(Categories, 
                                      on_delete=models.SET_DEFAULT,
                                      default=1)
    url_slug_news = models.CharField(max_length = 30, 
                                null=False, 
                                default="default")                                   
    def publish(self):
        self.published_date = datetime.now()
        self.save()

    def __str__(self):
        return "Post tittle: %s" %(self.tittle)
 
