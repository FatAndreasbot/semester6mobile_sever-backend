from django.db import models
from common import models as common

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150, blank=True, default="")
    author = models.ForeignKey(common.Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to="images/")
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title