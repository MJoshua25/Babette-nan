from django.db import models


# Create your models here.


# schemas -> relations -> base de donnée -> modéliser php -> requête -> afficher


# schema -> modéliser -> views

class MenuCategory(models.Model):
    titre = models.CharField(max_length=255)

    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Catégorie de menu"
        verbose_name_plural = "Catégories de menu"

    def __str__(self):
        return str(self.titre)
