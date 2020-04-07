from django.db import models

# Create your models here.


#User model
from django.contrib.auth.models import User

#get_absolute_url : to get url as string using name of url
from django.urls import reverse
'''
#for shopkeeper, person, policeman
class Owner_model(models.Model):

	user = models.OneToOneField(User,on_delete=models.CASCADE)
	ph_num=models.CharField("phone number",max_length=lenn,null=True)
	ac_year=models.CharField("academic year",max_length=lenn,null=True)
	branch=models.CharField("branch",max_length=lenn,null=True)
	address=models.CharField(max_length=lenn,null=True)
	dp=models.FileField(upload_to='media/owner/pdf',blank=True)
	
	def  get_absolute_url(self):
		return reverse('polls:detail', kwargs={'pk':self.pk})
	def get_fields(self):
		return [(field.name, field.value_to_string(self)) for field in Owner_model._meta.fields]
	

	def __str__(self):
        	return self.user.username


'''
# Vishal 1
# Dhiraj 2
# Kate2 12
# Aniket 17
# Nishant 18


class PersonAddressModel(models.Model):

	author = models.ForeignKey(User, on_delete=models.CASCADE)

	address_line1 = models.CharField(max_length = 50, blank=True)
	address_line2 = models.CharField(max_length = 50, blank=True)
	address_line3 = models.CharField(max_length = 50, blank=True)

	landmark = models.CharField(max_length = 50, blank=True)

	msg="Phone number must be entered in the format: '[6-9]\d{9}'. Up to 10 digits allowed."
	from  django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
	phone_regex = RegexValidator(regex=r'^[6-9]\d{9}$', message=msg)
    
	additional_ph_no = models.CharField("additional_phone_number", 
		validators=[phone_regex],max_length=10,blank=True)
		# verbose_name=) 
    # validators should be a list

	num_fam_mem = models.PositiveSmallIntegerField(default=3, 
		validators=[MinValueValidator(1), MaxValueValidator(20)],
		verbose_name="number_of_family_members")

	google_map_location = models.CharField(max_length = 500, blank=True)

	# def __str__(self):
	# 	return self.address_line1

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})











