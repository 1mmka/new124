from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=64,verbose_name='Название')
    date = models.DateTimeField(auto_now_add=False,db_index=True,verbose_name='Дата')
    
    def __str__(self):
        return self.name