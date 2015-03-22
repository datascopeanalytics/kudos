from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Kudo(models.Model):
    giver = models.ForeignKey(User, related_name='giver', editable=False)
    receivers = models.ManyToManyField(User, related_name='receivers')
    date = models.DateField(auto_now_add=True)
    count = models.IntegerField(default=1)
    message = models.CharField(max_length=140, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('kudo_update', kwargs={'id': self.id})
