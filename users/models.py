from django.db import models
from django.contrib.auth.models import User
#resize image
from PIL import Image
from  django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

class Profile(models.Model):#person address
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    first_name = models.CharField(max_length=30)#x1
    last_name = models.CharField(max_length=30)#x2
    phone_regex = RegexValidator(regex=r'^[6-9]\d{9}$', 
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], 
        max_length=10, blank=True) # validators should be a list
    adhaar_regex = RegexValidator(regex=r'^\d{4}\s\d{4}\s\d{4}$', 
        message="eg. 1234 1234 1234")
    adhaar_no = models.CharField(validators=[adhaar_regex], 
    max_length=30)#x3

    def __str__(self):
        return f'{self.user.username} Profile'

    #resize image 
    def save(self, *args, **kwargs):
    	super(Profile, self).save(*args, **kwargs)

    	img = Image.open(self.image.path)

    	if img.height>300 or img.width>300:
    		output_size = (300, 300)
    		img.thumbnail(output_size)
    		img.save(self.image.path)


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    address_line1 = models.CharField(max_length = 50)
    address_line2 = models.CharField(max_length = 50, blank=True)
    address_line3 = models.CharField(max_length = 50, blank=True)

    landmark = models.CharField(max_length = 50)

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

    gmap_location = models.PositiveSmallIntegerField(default=3, 
        validators=[MinValueValidator(1), MaxValueValidator(50)],
        verbose_name="Distance from center in km")

    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk': self.pk})

class Shop(models.Model):
    #shop form
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_shopkeeper = models.BooleanField(verbose_name="Are you a shopkeeper")
    shop_name = models.CharField(max_length=30, blank=True)
    shop_category_CHOICES=[('dairy','dairy'),('grocery','grocery'),
    ('electronics','electronics'), ('mechanic','mechanic')]
    category = models.CharField(max_length=30, choices=shop_category_CHOICES,null=True)

    shop_address_line1 = models.CharField(max_length = 50, blank=True)
    shop_address_line2 = models.CharField(max_length = 50, blank=True)
    shop_address_line3 = models.CharField(max_length = 50, blank=True)

    shop_gmap_location = models.PositiveSmallIntegerField(default=3, 
        validators=[MinValueValidator(1), MaxValueValidator(50)],
        verbose_name="Distance from center in km")
    # def __str__(self):
    #   return self.address_line1

    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk': self.pk})

