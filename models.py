from django.bd import models
class book(models.Model):
    name = models.CharField(max_length=100)
    pub_date = models.DateField()