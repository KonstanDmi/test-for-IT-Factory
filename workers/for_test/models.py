from django.db import models

# Create your models here.
class Worker(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

class Store(models.Model):
    title = models.CharField(max_length=255)
    workers = models.ManyToManyField(Worker) #спец поле само создает третью таблицу со связанными полями, магия ORM (обожаю)
    latitude = models.IntegerField(blank=False) #думаю широта и долгота должна быть не только у посещения + так просто проще потом разобраться и не делать лишних запросов в базу
    longtitude = models.IntegerField(blank=False)

class Visit(models.Model):
    date_of_visit = models.DateField(auto_now=True)
    store = models.ForeignKey(Store, on_delete=models.PROTECT, editable=False)
    worker = models.ForeignKey(Worker, on_delete=models.PROTECT, editable=False) # в последствии понял что визит не рандомный а от конкретного работника, ну и поиск же нужен был по работникам
    latitude = models.IntegerField(blank=False, editable=False)
    longtitude = models.IntegerField(blank=False, editable=False)