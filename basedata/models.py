from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length=100)


class Human(models.Model):
    name = models.CharField(max_length=100)
    friends = models.ManyToManyField(Dog, through="DogFriendHuman")


class DogFriendHuman(models.Model):
    human = models.ForeignKey(Human, on_delete=models.CASCADE)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
