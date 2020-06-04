from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


# schemas -> relations -> base de donnée -> modéliser php -> requête -> afficher


# schema -> modéliser -> views

class MenuCategory(models.Model):
    titre = models.CharField(max_length=255)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Catégorie de menu"
        verbose_name_plural = "Catégories de menu"

    def __str__(self):
        return str(self.titre)


class Ingredient(models.Model):
    titre = models.CharField(max_length=255)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"

    def __str__(self):
        return str(self.titre)


class Plat(models.Model):
    titre = models.CharField(max_length=255)
    prix = models.IntegerField()
    categorie = models.ForeignKey('MenuCategory', on_delete=models.CASCADE, related_name='menus')
    ingredients = models.ManyToManyField('Ingredient', related_name='menus')
    isRecommended = models.BooleanField(default=False)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Plat"
        verbose_name_plural = "Plats"

    def __str__(self):
        return str(self.titre)

    @property
    def getCategorieTitre(self):
        return self.categorie.titre

    @property
    def getIngredients(self):
        return self.ingredients.filter(status=True)

    @property
    def isNew(self):
        return (timezone.now() - self.date_add) < datetime.timedelta(weeks=1)

    @property
    def pricingTag(self):
        if self.isNew:
            return 'New'
        elif self.isRecommended:
            return 'Recommended'
        else:
            return False

# 1 à 1 : 1 Category < = > 1 plat
# 1 à plusieurs : 1 Category < = > plusieurs plats
# plusieurs à plusieurs: plusieurs Category < = > plusieurs plats
