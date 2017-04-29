from django.db import models


class IdentityModel(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Identity'
        verbose_name_plural = 'Identities'

    def __unicode__(self):
        return '%s %s' % (self.username, self.password)
