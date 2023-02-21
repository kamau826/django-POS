from django.db import models

# Create your models here.

class Category(models.Model):
	name= models.CharField(max_length=155)

	def __str__(self):
		return self.name

class Product(models.Model):
	class Status(models.TextChoices):
		SOLD= 'SD','Sold'
		RENT = 'RT','Rent'
		AVAILABLE = 'AV','Available'


	name= models.CharField(max_length=200)
	category=models.ManyToManyField(Category)
	buying_price=models.IntegerField()
	selling_price=models.IntegerField(null=True,blank=True)
	description=models.TextField()
	updated=models.DateTimeField(auto_now=True)
	created=models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=3,
		  choices=Status.choices,default=Status.AVAILABLE)

	class Meta:
		ordering=['-updated','-created']
	


	def __str__(self):
		return self.name


class Sale(models.Model):
	created=models.DateTimeField(auto_now_add=True)
	products=models.ManyToManyField(Product,related_name='products',null=True)

	def __str__(self):
		return self.products
    
   

	




