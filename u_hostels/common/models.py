from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):	#in case we need some additional data for our user (profile picture, or something, i dunno)
	authData = models.OneToOneField(User, on_delete=models.CASCADE) #should change ato a one-to-one relation
	''' User data in User model
		username			(required, string)
		first_name			(optional, string)
		last_name			(optional, string)
		email				(optional, string)
		password			(required, string(kinda))
		groups				(optional, Many-to-many relationship to Group)
		user_permissions	(optional, Many-to-many relationship to Permission)
		is_staff			(optional, bool)
		is_active			(optional, bool)
		is_superuser		(optional, bool)
		last_login			(optional, date)
		date_joined			(optional, date)
	'''
	
	room = models.ForeignKey("common.Room", on_delete=models.CASCADE)

	def __str__(self) -> str:
		return self.authData.first_name+"_"+self.authData.last_name+"_profile"

#todo 
#	create a hostel model and add that model to profile with a many-to-one relation

class Hostel(models.Model):
	address = models.CharField(max_length=150)
	hostelNumber = models.CharField(max_length=4, unique=True)

class Room(models.Model):
	hostel = models.ForeignKey("common.Hostel", on_delete=models.CASCADE)
	roomNumber = models.CharField(max_length=6, unique=True)
	
