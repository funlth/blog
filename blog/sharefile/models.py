from django.db import models

# Create your models here.
from django.db import models

class SharedFile(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='shared_files/')
    created_at = models.DateTimeField(auto_now_add=True)