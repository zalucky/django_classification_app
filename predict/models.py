from django.db import models

# Create your models here.

class Dataset(models.Model):
    class Meta:
        verbose_name_plural = "Dataset"
    id_dataset = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return str(self.id_dataset)+'. '+str(self.name)

class Attribute(models.Model):
    class Meta:
        verbose_name_plural = "Attribute"
    id_attribute = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    id_dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Content(models.Model):
    class Meta:
        verbose_name_plural = "Content"
    id_content = models.AutoField(primary_key=True)
    c = models.CharField(max_length=1000)
    a1 = models.FloatField(null=True, blank=True)
    a2 = models.FloatField(null=True, blank=True)
    a3 = models.FloatField(null=True, blank=True)
    a4 = models.FloatField(null=True, blank=True)
    a5 = models.FloatField(null=True, blank=True)
    a6 = models.FloatField(null=True, blank=True)
    a7 = models.FloatField(null=True, blank=True)
    a8 = models.FloatField(null=True, blank=True)
    a9 = models.FloatField(null=True, blank=True)
    id_dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    def __str__(self):
        return str([self.c,self.a1,self.a2,self.a3,self.a4,self.a5,self.a6,self.a7,self.a8,self.a9])
