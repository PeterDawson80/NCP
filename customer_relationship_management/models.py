from django.db import models

from text_query.models import *
# Create your models here.

class Ticket(models.Model):
        id = models.AutoField(primary_key=True)
        query = models.ForeignKey('text_query.Query', on_delete = models.CASCADE)
        #mymodel1 = models.ForeignKey('app1.MyModel1')
