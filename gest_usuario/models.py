from django.db import models

# Create your models here.
class Jugadores(models.Model):
	nickname=models.CharField(max_length=20, primary_key=True)
	nombre=models.CharField(max_length=30)
	apellidos=models.CharField(max_length=60)
	street=models.CharField(max_length=40)
	number=models.IntegerField()
	level=models.IntegerField()
	door=models.CharField(max_length=2)
	cp_code=models.CharField(max_length=5)
	city=models.CharField(max_length=40)
	country=models.CharField(max_length=30)
	telefono=models.CharField(max_length=9, default="0000000")
	mail=models.EmailField(default="mail@address.com")

class Chats(models.Model):
	sender = models.CharField(max_length=30)
	receiver = models.CharField(max_length=30)
	message = models.CharField(max_length=200)

class Statistics(models.Model):
	nickname=models.CharField(max_length=20)
	won=models.IntegerField()
	lost=models.IntegerField()

	