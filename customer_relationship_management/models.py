from django.db import models

from text_query.models import Query

class Ticket(models.Model):
        id = models.AutoField(primary_key=True)
        query = models.ForeignKey('text_query.Query')
        #mymodel1 = models.ForeignKey('app1.MyModel1')

# Create your models here.
