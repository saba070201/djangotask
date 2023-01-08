from django.db import models
class FullItem(models.Model):
    title=models.CharField(max_length=100)
    def __str__(self):
        return self.title
class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='info/images/')
    parentid=models.ForeignKey(FullItem,on_delete=models.CASCADE)
    def __str__(self):
        return self.title


# Create your models here.
