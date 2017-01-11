from django.db import models
from django.core.urlresolvers import reverse

class Vuln(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    afetado = models.CharField(max_length=50)
    severidade = models.CharField(max_length=10)
    status = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('vuln:vuln_edit', kwargs={'pk': self.pk})
