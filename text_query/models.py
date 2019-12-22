from django.db import models

# Create your models here.
class Query(models.Model):
        id = models.AutoField(primary_key=True)
        email = models.EmailField(max_length=70,blank=True)
        CATEGORY1 = 'cat1'
        CATEGORY2 = 'cat2'
        CATEGORY3 = 'cat3'
        CATEGORY4 = 'cat4'
        CATEGORY5 = 'cat5'
        CATEGORY_CHOICES = [
            (CATEGORY1, 'Category1'),
            (CATEGORY2, 'Category2'),
            (CATEGORY3, 'Category3'),
            (CATEGORY4, 'Category4'),
            (CATEGORY5, 'Category5'),
        ]
        category = models.CharField(
            max_length=20,
            choices = CATEGORY_CHOICES
        )
        body = models.TextField(max_length=2000)
        datetime = models.DateTimeField(auto_now_add=True, blank=True)

        def summary(self):
            return self.body[:50]

        def date_only(self):
            return self.datetime.strftime('%b %e %Y')    
