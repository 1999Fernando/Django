from django.db import models

class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=120)
    correo = models.EmailField(max_length=200)

    def _str_(self):
        return self.nombre







