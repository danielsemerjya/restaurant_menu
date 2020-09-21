from django.db import models

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500, default="")

    class Meta:
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.name


# Classa tworząca posiłek
class Dish(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pub_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(default="")

    #Meta classa dająca liczbę mnogą nazwy
    class Meta:
        verbose_name_plural = "Dishes"

    def __str__(self):
        return self.name

