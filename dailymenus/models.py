from django.db import models


class DailyMenu(models.Model):

    availability_day = models.DateField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('availability_day', )
        verbose_name = 'dailymenu'

class MenuAlternative(models.Model):

    description = models.CharField(max_length=256)
    daily_menu = models.ForeignKey(DailyMenu, on_delete=models.CASCADE)
