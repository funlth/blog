from django.db import models

# Create your models here.


from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/GIF/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Photo ({self.category}): {self.image.path}"
