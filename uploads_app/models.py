from django.db import models

# Create your models here.



class Uploads(models.Model):
    from uploads_app.utils import uploads_url_with_instance
    media_url = models.FileField(upload_to=uploads_url_with_instance)
    original_name = models.CharField(max_length=255)
    generated_name = models.CharField(max_length=255)
    content_type = models.CharField(max_length=400)
    size = models.IntegerField(null=True)
    code = models.CharField(max_length=100)

    class Meta:
        db_table = 'uploads'