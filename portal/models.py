from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('Category', null=True, blank=True, related_name='sub_category', on_delete=models.CASCADE)
    order = models.IntegerField(null=True, blank=True)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.name



