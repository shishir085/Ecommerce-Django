from django.db import models
from base.models import BaseModel
# Create your models here.
class Category(BaseModel):
    category_name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True,null=True,blank=True)
    category_image=models.ImageField(upload_to="catgories/")


class Products(BaseModel):
    product_name=models.CharField(max_length=40)
    slug=models.SlugField(unique=True,null=True,blank=True)

    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
    product_description=models.TextField(max_length=255)
    price=models.IntegerField()


class productImage(BaseModel):
    product=models.ForeignKey(Products,on_delete=models.CASCADE,related_name="products_images")
    image=models.ImageField(upload_to="products/")
