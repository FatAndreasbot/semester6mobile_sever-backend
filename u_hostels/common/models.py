from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):	#in case we need some additional data for our user (profile picture, or something, i dunno)
	authData = models.OneToOneField(User, on_delete=models.CASCADE)
		# username			(required, string)
		# first_name			(optional, string)
		# last_name			(optional, string)
		# email				(optional, string)
		# password			(required, string(kinda))
		# groups				(optional, Many-to-many relationship to Group)
		# user_permissions	(optional, Many-to-many relationship to Permission)
		# is_staff			(optional, bool)
		# is_active			(optional, bool)
		# is_superuser		(optional, bool)
		# last_login			(optional, date)
		# date_joined			(optional, date)
	
	def __str__(self) -> str:
		return self.authData.first_name+"_"+self.authData.last_name+"_profile"

	