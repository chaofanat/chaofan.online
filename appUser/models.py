from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='appUser/profile_pics/default.jpg', upload_to='appUser/profile_pics')
    bio = models.TextField(max_length=500, blank=True, default='一句话介绍不了我。')
    website = models.URLField(max_length=200, blank=True)
    followers = models.ManyToManyField(User, related_name='followers', blank=True)
    following = models.ManyToManyField(User, related_name='following', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    class Meta:
        ordering = ['-created_at']
        get_latest_by = 'created_at'
        default_related_name = 'profile'
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
        

