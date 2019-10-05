from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class ApiRequest(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='api_request_user')
    view_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return str(self.user)+self.view_name
    
