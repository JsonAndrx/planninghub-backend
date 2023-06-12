from django.db import models

from apps.utils.models import PlanningModel

class Profile(PlanningModel):

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    picture = models.ImageField('profile picture', upload_to='users/pictures/', blank=True, null=True)
    biography = models.CharField('biography', max_length=250, blank=True)
    
    def __str__(self):
        return str(self.user)