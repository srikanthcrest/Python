from django.db import models
from django.contrib.auth.models import User
from admin_user_api.models import CustomUser

class ToDo(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Link to the User model
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'todo'  # Custom table name
