from django.db import models
from django.contrib.auth.models import User,auth
import datetime
# from django.utils import timezone
# Create your models here.
gender=[
('M','male'),
('F','female'),
('O','other')
]
# class user(models.Model):
# 	firstname = models.CharField('firstname',max_length=10,unique=True)
# 	lastname= models.CharField('lastname',max_length=10)
# 	email = models.EmailField('email')
# 	password = models.CharField('password',max_length=20)
# 	phone = models.CharField('phone',max_length=10)
# 	address= models.CharField('address',max_length=100)
# 	usertype = models.CharField('user',max_length = 10,default='other')
# 	gender= models.CharField(choices=gender,max_length=10)

# 	def __str__(self):
# 		return self.firstname
# 	class Meta:
# 		verbose_name_plural="client"

class contactus(models.Model):
	fname = models.CharField('fname',max_length=10)
	lname= models.CharField('lname',max_length=10)
	email = models.EmailField('email')
	phone = models.CharField('phone',max_length=10)
	message= models.CharField('message',max_length=100)

	
	class Meta:
		verbose_name_plural="contactus"

class feedbacks(models.Model):
	username = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
	msg=models.CharField('msg',max_length=1000)



	class Meta:
		verbose_name_plural="feedback"

class box(models.Model):
	sb_price = models.IntegerField()
	mb_price = models.IntegerField()
	lb_price = models.IntegerField()

class orders(models.Model):
	orders_id =models.AutoField(primary_key=True)
	# items_json = models.CharField(max_length=5000,default="")
	# username = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
	sbox = models.IntegerField()
	mbox = models.IntegerField()
	lbox = models.IntegerField()
	month = models.IntegerField()
	amount = models.IntegerField(default=0)
	# username = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
	name = models.CharField(max_length=10)
	email = models.EmailField()
	phone = models.IntegerField()
	pickup_location = models.CharField(max_length=100)
	zipcode = models.IntegerField()
	date = models.DateField(default=datetime.date.today)
	hour = models.IntegerField()
	minutes = models.IntegerField()	

	class Meta:
		verbose_name_plural="orders"


		
				



			
						


