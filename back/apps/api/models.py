from djongo import models


class Plates(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    allergens = models.TextField(blank=True, null=True)

    objects = models.DjongoManager()

    def __str__(self):
        return self.name


class Sections(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    plates = models.ArrayReferenceField(to=Plates, on_delete=models.SET_NULL, blank=True, null=True)

    objects = models.DjongoManager()

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, default=0.00)
    sections = models.ArrayReferenceField(to=Sections, on_delete=models.SET_NULL, blank=True, null=True)

    objects = models.DjongoManager()

    def __str__(self):
        return self.name
