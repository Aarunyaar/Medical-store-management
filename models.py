from django.db import models

class Medicine(models.Model):
    username = models.CharField(max_length=150)  
    name = models.CharField(max_length=100)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
