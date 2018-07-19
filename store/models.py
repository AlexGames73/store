import datetime
from random import randint
from django.db import models
from hashlib import sha1


class Product(models.Model):
    title = models.CharField(max_length=128)
    code = models.AutoField(primary_key=True)
    price = models.IntegerField()
    sale = models.BooleanField()
    sale_price = models.IntegerField(blank=True, null=True)
    description = models.TextField()
    characteristics = models.TextField()
    country = models.CharField(max_length=16)


class Comment(models.Model):
    author_id = models.CharField(max_length=16)
    date_created = models.DateTimeField()
    text = models.TextField(max_length=1024)
    product_code = models.ForeignKey(Product, models.CASCADE)
    id = models.AutoField(primary_key=True)
    likes = models.IntegerField(blank=True, null=True)
    dislikes = models.IntegerField(blank=True, null=True)
    reply_rating = models.IntegerField(blank=True, null=True)
    reply = models.IntegerField(blank=True, null=True)


class Rating(Comment):
    advantages = models.TextField(max_length=256, blank=True, null=True)
    disadvantages = models.TextField(max_length=256, blank=True, null=True)


class User(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    email = models.EmailField(max_length=32)
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    date_of_birth = models.DateField()
    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=256, blank=True, null=True)
    is_verify = models.BooleanField(default=False)
    access_level = models.IntegerField(default=1)
    last_tokenize = models.DateField(blank=True, null=True)
    rand_key_for_verify = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.username

    def tokenize(self, check=False):
        if not check:
            self.last_tokenize = datetime.datetime.now()
            self.rand_key_for_verify = randint(100000, 1000000)
            self.token = sha1((self.username +
                               self.password +
                               self.email +
                               self.rand_key_for_verify.__str__() +
                               self.last_tokenize.__str__()).encode()).hexdigest()
            return self.token
        else:
            return sha1((self.username +
                         self.password +
                         self.email +
                         self.rand_key_for_verify.__str__() +
                         self.last_tokenize.__str__()).encode()).hexdigest()
