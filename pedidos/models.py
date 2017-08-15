from django.db import models

# Create your models here.
class adicional(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.nome

class acai(models.Model):
    SIZES = (
        ('P', 'Pequeno'),
        ('G', 'Grande'),
    )
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    obs = models.CharField(max_length=200, null=True, blank=True)
    tamanho = models.CharField(max_length=1, choices=SIZES)
    adicionais = models.ManyToManyField(adicional)
    def __str__(self):
        return self.nome

class itemacai(models.Model):
    id = models.AutoField(primary_key=True)
    acai_item = models.ForeignKey(acai)
    adicionais = models.ManyToManyField(adicional)
    qnt = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return str(self.id)

class comanda(models.Model):
    id = models.AutoField(primary_key=True)
    acais = models.ManyToManyField(itemacai)
    mixs = models.ManyToManyField(itemmix)
    casadinhos = models.ManyToManyField(itemcasadinho)
    cremes = models.ManyToManyField(itemcreme)
    sorvetes = models.ManyToManyField(itemsorvete)
    mshakes = models.ManyToManyField(itemmshake)
    petits = models.ManyToManyField(itempetits)
    fondues = models.ManyToManyField(itemfondue)
    produtos = models.ManyToManyField(itemprodutos)
    sucos = models.ManyToManyField(itemsucos)
    total = models.DecimalField(max_digits=5, decimal_places=2, defaul='0')
    def __str__(self):
        return str(self.id)