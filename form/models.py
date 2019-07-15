from django.utils.translation import gettext as _
from django.db import models

class ContactKeyword(models.Model):
    keyword = models.CharField(max_length=30)
    answer = models.TextField(null=True)

    def __str__(self):
        return str(self.keyword)

    class Meta:         
        verbose_name = u'Contact Keyword'
        verbose_name_plural = u'Contact Keywords'
