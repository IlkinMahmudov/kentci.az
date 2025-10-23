from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField("Bio", blank=True, null=True)
    profile_image = models.ImageField("Profil şəkli", upload_to='profil_shekilləri/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Elan(models.Model):
    ad = models.CharField("Məhsulun adı", max_length=100)
    qiymet = models.DecimalField("Qiymət (AZN)", max_digits=10, decimal_places=2)
    tarix = models.DateField("Tarix", auto_now_add=True)
    shekil = models.ImageField("Şəkil", upload_to='elanlar/')
    melumat = models.TextField("Qısa məlumat", blank=True, null=True)
    istifadeci = models.ForeignKey("UserProfile", on_delete=models.CASCADE, null=True, blank=True)  # <-- bu xətt yeni əlavə olunub

    def __str__(self):
        return self.ad
