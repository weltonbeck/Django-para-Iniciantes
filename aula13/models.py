from django.db import models


class UploadFile(models.Model):
    
    name = models.CharField(
        u'Nome',
        max_length=100,
    )

    file = models.FileField(
        u'Arquivo',
        upload_to='uploads'
    )

    def __unicode__(self):
        return self.name
