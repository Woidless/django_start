from django.db import models

# Create your models here.


# class Cars(models.Model):
#     title = models.CharField(max_length=150, reqiured=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField(null=True)
#     phone = models.CharField(max_length=30)
#     owner = models.CharField(max_length=50)

#     class Meta:
#         verbose_name = 'Car'
#         verbose_name_plural = 'Cars'

#     def str(self):
#         return self.title


class Musician(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=50)

    class Meta:
        pass

    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'
    

class Song(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Musician, 
                                on_delete = models.CASCADE,
                                related_name='songs')
    feat = models.ForeignKey(Musician, 
                            on_delete=models.CASCADE,
                            null=True,
                            related_name='feats')
    poster = models.ImageField(upload_to='images/')
    year = models.DateField()
    
    def __str__(self) -> str:
        if self.feat: return f'{self.author} -> {self.title} f.{self.feat}'
        return f'{self.author} -> {self.title}'


