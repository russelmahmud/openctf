from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from common.models import Gender, PlayerType

class User(AbstractUser):
    organization = models.CharField(_('organization name'), max_length=150, blank=True)
    gender = models.ForeignKey(Gender, blank=True, null=True, on_delete=models.SET_NULL)
    player_type = models.ForeignKey(PlayerType, blank=True, null=True, on_delete=models.SET_NULL)
    phone = models.CharField(_('phone number'), max_length=32, blank=True)
    picture = models.ImageField(_('profile picture'), upload_to='profiles', blank=True)
    tagline = models.CharField(_('tagline'), max_length=255, blank=True)
    public = models.BooleanField(default=False)
