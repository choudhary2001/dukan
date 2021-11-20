from django.db import models
from django.utils.html import mark_safe
# Create your models here.
from io import BytesIO
from PIL import Image

class Banner(models.Model):
    alt_text=models.CharField(max_length=100)
    img=models.ImageField(upload_to="banner_imgs")
    class Meta:
        verbose_name_plural='1. Banners'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.img.url))


    def __str__(self):
       return self.alt_text

class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cat_imgs/")
    slug = models.SlugField(max_length=250)
    ordering = models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural='2. Categories'
        ordering = ['ordering']
 
    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title


class Product(models.Model):
    title=models.CharField(max_length=200)
    slug=models.CharField(max_length=500)
    details=models.TextField()
    specs=models.TextField()
    category=models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    size = models.IntegerField(default=1)
    weight = models.IntegerField(default=1)
    image1=models.ImageField(upload_to="product_imgs/")
    image2=models.ImageField(upload_to="product_imgs/", default="",null=True,blank=True)
    image3=models.ImageField(upload_to="product_imgs/", default="",null=True,blank=True)
    image4=models.ImageField(upload_to="product_imgs/", default="",null=True,blank=True)
    image5=models.ImageField(upload_to="product_imgs/", default="",null=True,blank=True)
    quantity = models.PositiveIntegerField(default=1)
    price=models.PositiveIntegerField(default=0)
    discount=models.CharField(max_length=150, blank=True, null=True)
    date_addeed = models.DateTimeField(auto_now_add=True)
    
    is_featured=models.BooleanField(default=False)



    def save(self, *args, **kwargs):
	    super().save(*args, **kwargs)

	    img1 = Image.open(self.image1.path)
	    if img1.height > 1500 or img1.width > 1500:
		    output_size = (1500, 1500)
		    img1.thumbnail(output_size)
		    img1.save(self.image1.path)
	    if self.image2:
		    img2 = Image.open(self.image2.path)
		    if img2.height > 1500 or img2.width > 1500:
			    output_size = (1500, 1500)
			    img2.thumbnail(output_size)
			    img2.save(self.image2.path)

	    if self.image3:
		    img3 = Image.open(self.image3.path)
		    if img3.height > 1500 or img3.width > 1500:
			    output_size = (1500, 1500)
			    img3.thumbnail(output_size)
			    img3.save(self.image3.path)

	    if self.image4:
		    img4 = Image.open(self.image4.path)
		    if img4.height > 1500 or img4.width > 1500:
			    output_size = (1500, 1500)
			    img4.thumbnail(output_size)
			    img4.save(self.image4.path)

	    if self.image5:
		    img5 = Image.open(self.image5.path)
		    if img5.height > 1500 or img5.width > 1500:
			    output_size = (1500, 1500)
			    img5.thumbnail(output_size)
			    img5.save(self.image5.path)

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image1.url))


    class Meta:
        verbose_name_plural='3. Product'

    def __str__(self):
        return self.title