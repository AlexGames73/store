from django.db import models


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
    author = models.CharField(max_length=16)
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
