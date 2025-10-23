from django.db import models
from django.db import models

class UserProfile(models.Model):
    user_name = models.CharField("İstifadəçi adı", max_length=150)
    email = models.EmailField("Email ünvanı", unique=True)
    bio = models.TextField("Bio", blank=True, null=True)
    profile_image = models.ImageField("Profil şəkli", upload_to='profil_shekilləri/', blank=True, null=True)

    def __str__(self):
        return self.user_name

class Elan(models.Model):
    ad = models.CharField("Məhsulun adı", max_length=100)
    qiymet = models.DecimalField("Qiymət (AZN)", max_digits=10, decimal_places=2)
    tarix = models.DateField("Tarix", auto_now_add=True)
    shekil = models.ImageField("Şəkil", upload_to='elanlar/')
    melumat = models.TextField("Qısa məlumat", blank=True, null=True)

    def __str__(self):
        return self.ad
