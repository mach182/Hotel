from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class My_User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_lenght=100)
    apellido = models.CharField(max_length=100)
    edad = models.DateTimeField()
    correo = models.EmailField()
    telefono = PhoneNumberField()


    def __str__(self):
        return "%s" % self.user
