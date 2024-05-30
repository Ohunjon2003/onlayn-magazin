from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255,verbose_name='Kategoriya',unique=True)


    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoryalar'
        ordering = ['title']
class Post(models.Model):
    name = models.CharField(max_length=255,verbose_name='Mahsulot nomi')
    price = models.CharField(max_length=100,verbose_name='Narhi')
    content = models.TextField(blank=True,null=True,verbose_name='Mahsulot haqida')
    photo = models.ImageField(verbose_name="Rasmi",upload_to='photos/',null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Kiritilgan vaqti')
    update = models.DateTimeField(auto_now=True,verbose_name='Tahrirlangan vaqti')
    views = models.IntegerField(default=0,verbose_name='korishlar soni')
    published = models.BooleanField(default=True,verbose_name='Saytga chiqarish')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='kategoriya')
    author = models.ForeignKey(User,on_delete=models.CASCADE)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'
        ordering = ('-pk',)

class UserProfile(models.Model):
    userphoto = models.ImageField(upload_to='users/',null=True,blank=True)
    status = models.CharField(max_length=150,null=True,blank=True)
    adress = models.CharField(max_length=255,null=True,blank=True)
    phone = models.CharField(max_length=13,null=True,blank=True)
    mobile = models.CharField(max_length=13,null=True,blank=True)
    sayt = models.URLField(null=True,blank=True)
    github = models.CharField(max_length=255,null=True,blank=True)
    telegram = models.CharField(max_length=255,null=True,blank=True)
    instagram = models.CharField(max_length=255,null=True,blank=True)
    fasebook = models.CharField(max_length=255,null=True,blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.user.username}"

class Comment(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.text
