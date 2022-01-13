from django.db import models


class AdditionData(models.Model):
    number1 = models.IntegerField(default=0)
    number2 = models.IntegerField(default=0)
    answer = models.IntegerField(null=True)
