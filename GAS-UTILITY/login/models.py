from django.db import models

class AdminUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Django uses a hashed password
    confirm_password = models.CharField(max_length=128)  # Usually not stored, used in forms
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.username