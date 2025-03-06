from django.core.exceptions import ValidationError
from django.utils import timezone
from django.urls import reverse
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.



class Togaraklar(models.Model):

    nomi = models.CharField('nomi',max_length=100)
    image = models.ImageField(upload_to='togarak_images/')

    publish_time = models.DateTimeField(auto_now_add=True)
    body_small = models.CharField("To'garak haqida qisqacha",max_length=250,)
    active = models.BooleanField(default=True)



    def str(self):
        return self.nomi
    class Meta:
        ordering = ['-publish_time']
        verbose_name_plural = "To'garaklar"
        verbose_name = "To'garak"

class Tanlov(models.Model):
    nomi = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tanlov_images/')
    slug = models.SlugField(max_length=150,unique=True)
    boshlanish_sanasi = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    body_small = models.CharField(max_length=250,)
    active = models.BooleanField(default=True)
    publish_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomi
    def get_absolute_url(self):
        pass
        return reverse("tanlov", kwargs={"slug": self.slug})


    class Meta:
        ordering = ['-boshlanish_sanasi']

        verbose_name_plural = "Tanlovlar"
        verbose_name = "Tanlov"

class Tadbir(models.Model):
    nomi = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tadbir_images/')
    slug = models.SlugField(max_length=150,unique=True)
    boshlanish_sanasi = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    body_small = models.CharField(max_length=250,)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.nomi
    def get_absolute_url(self):
        return reverse("tadbir", kwargs={"slug": self.slug})


    class Meta:
        ordering = ['-boshlanish_sanasi']
        # ordering = ['publish_time'] # birinchi yozilgna birinchi chiqadi
        verbose_name_plural = "Tadbirlar"
        verbose_name = "Tadbir"

class Konfirensiya(models.Model):
    nomi = models.CharField(max_length=100)
    image = models.ImageField(upload_to='konfirensiya_images/')
    slug = models.SlugField(max_length=150,unique=True)
    boshlanish_sanasi = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    body_small = models.CharField(max_length=250,)
    active = models.BooleanField(default=True)
    publish_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nomi
    def get_absolute_url(self):
        return reverse("konfirensiya", kwargs={"slug": self.slug})


    class Meta:
        ordering = ['-boshlanish_sanasi']
        # ordering = ['publish_time'] # birinchi yozilgna birinchi chiqadi
        verbose_name_plural = "Konfirensiyalar"
        verbose_name = "Konfirensiya"

class Rahbariyat(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='rahbariyat_images/')
    lavozimi = models.CharField(max_length=100)
    email = models.EmailField()
    numbers = models.IntegerField()
    bio = models.TextField(default="")

    telegram = models.URLField()
    instagram = models.URLField()
    facebook = models.URLField()
    twitter = models.URLField()

    publish_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.last_name} {self.name} {self.fathers_name}"
    class Meta:
        ordering = ['-publish_time']
        verbose_name_plural = 'Rahbariyat'

class Budjet(models.Model):
    nomi = models.CharField(max_length=100)
    body_small = models.CharField(max_length=250,)
    active = models.BooleanField(default=True)
    narxi = models.IntegerField(default=0)
    date = models.DateField(default=timezone.now)
    publish_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomi


    class Meta:
        ordering = ['-publish_time']
        # ordering = ['publish_time'] # birinchi yozilgna birinchi chiqadi
        verbose_name_plural = "Budjetlar"
        verbose_name = "Budjet"

class Oxirgi_ishlar(models.Model):
    nomi = models.CharField(max_length=100)
    body_small = models.CharField(max_length=250,)
    image = models.ImageField(upload_to='oxirgi_images/')
    publish_time = models.DateField(default=timezone.now, verbose_name="Oxirgi qilingan ish sanasi ")
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.nomi


    class Meta:
        ordering = ['publish_time']
        # ordering = ['publish_time'] # birinchi yozilgna birinchi chiqadi
        verbose_name_plural = "Oxirgi ishlar"
        verbose_name = "Oxirgi ish"

class Numbers(models.Model):
    maktablar = models.PositiveIntegerField(default=0)
    bogchalar = models.PositiveIntegerField(default=0)
    yangilanishlar = models.PositiveIntegerField(default=0, verbose_name="Qayta ta'mirlanganlar soni")
    rejada = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if Numbers.objects.exists() and not self.pk:
            raise ValidationError("Faqat bitta sonlar to'plamini yaratish mumkin! Yaxshisi eski sonlarni tahrirlang")
        super().save(*args, **kwargs)
    class Meta:
        verbose_name_plural = "Maktab,bogchalar soni"
        verbose_name = "Maktab,bogcha soni"


class Hududiy_Rahbariyat(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='rahbariyat_images/')
    lavozimi = models.CharField(max_length=100)
    email = models.EmailField()
    numbers = models.IntegerField()
    bio = models.TextField(default="")

    telegram = models.URLField()
    instagram = models.URLField()
    facebook = models.URLField()
    twitter = models.URLField()

    publish_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.last_name} {self.name} {self.fathers_name}"
    class Meta:
        ordering = ['-publish_time']
        verbose_name_plural = "Hududiy Bo'lim Rahbarlari"

class Korrupsiya_kurash(models.Model):
    nomi = models.CharField(max_length=100)
    body_small = models.CharField(max_length=250,)
    image = models.ImageField(upload_to='korrupsiya_images/')
    publish_time = models.DateField(default=timezone.now, verbose_name=" Targ'ibot sanasi ")
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.nomi


    class Meta:
        ordering = ['publish_time']
        # ordering = ['-publish_time'] # eng oxirgi qo'shilgan element birinchi chiqadi
        verbose_name_plural = "Korrupsiyaga qarshi kurash"

class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    message = models.TextField()
    number = PhoneNumberField(region="UZ")
    class Meta:
        verbose_name_plural = "Bog'lanishlar"

class Bayonotlar(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='rahbariyat_images/')
    lavozimi = models.CharField(max_length=100)

    body = models.TextField(default="")

    publish_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.last_name} {self.name} {self.fathers_name}"
    class Meta:
        ordering = ['-publish_time']
        verbose_name_plural = 'Bayonotlar'

class Harakatlar(models.Model):
    maktablar = models.PositiveIntegerField(default=0)
    bogchalar = models.PositiveIntegerField(default=0)
    yangilanishlar = models.PositiveIntegerField(default=0, verbose_name="Qayta ta'mirlanganlar soni")
    rejada = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if Harakatlar.objects.exists() and not self.pk:
            raise ValidationError("Faqat bitta sonlar to'plamini yaratish mumkin! Yaxshisi eski sonlarni tahrirlang")
        super().save(*args, **kwargs)
    class Meta:
        verbose_name_plural = "Harakatlar strategiyasi raqamlari"
        verbose_name = "Harakatlar strategiyasi"

class Yangiliklar_turi(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Yangiliklar turi'

class Yangiliklar(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    slug = models.SlugField(unique=True, max_length=150)
    body = models.TextField()
    body_small = models.CharField(max_length=150)
    turi = models.ForeignKey(Yangiliklar_turi, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='yangiliklar_images/')
    active = models.BooleanField(default=True)
    publish_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("yangilik", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Yangiliklar'







