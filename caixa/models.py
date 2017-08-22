from django.db import models
import datetime

# Create your models here.
class caixa(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length= 20, default="Entrada")
    item = models.CharField(max_length= 200, null=True, blank=True)
    obs = models.CharField(max_length= 200, null=True, blank=True)
    data = models.DateTimeField(default=datetime.datetime.now())
    total = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return str(self.id)
