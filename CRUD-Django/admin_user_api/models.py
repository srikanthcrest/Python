from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ADMIN = '1'
    USER = '2'
    
    EMAIL_TO_USER_TYPE_MAP = {
        'admin': ADMIN,
        'user': USER,
    }

    user_type_data = ((ADMIN, "admin"), (USER, "user"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)
