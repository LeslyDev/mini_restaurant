from django.db import models


class MenuElement(models.Model):
    name = models.CharField(max_length=15)
    price = models.FloatField()
    description = models.TextField()
    element_type = models.CharField(max_length=5)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Table(models.Model):
    size = models.IntegerField()
    time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=4, default='free', blank=False, null=False)
    owner_name = models.CharField(max_length=10, blank=True)
    owner_number = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return 'Столик на {}'.format(self.size)
