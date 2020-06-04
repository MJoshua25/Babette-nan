from django.db import models


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

# 1 à 1 : 1 Category < = > 1 plat
# 1 à plusieurs : 1 Category < = > plusieurs plats
# plusieurs à plusieurs: plusieurs Category < = > plusieurs plats
