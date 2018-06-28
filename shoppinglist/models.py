from django.db import models


class ItemsList(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=255, blank=True, null=True)
    is_bought = models.BooleanField(default=False)
    items_list = models.ForeignKey(ItemsList, on_delete=models.CASCADE, verbose_name="List of items")

    def __str__(self):
        return self.name
