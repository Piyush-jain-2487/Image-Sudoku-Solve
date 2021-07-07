from django.db import models
import os
from uuid import uuid4

def path_and_rename(instance, filename):
    upload_to = "./input_image"
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, "png")
    else:
        # set filename as random string
        filename = '{}.{}'.format("input", "png")
    # return the whole path to the file
    return os.path.join(upload_to, filename)

def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Image.objects.get(pk=instance.pk).file
    except Image.DoesNotExist:
        return False

    new_file = instance.file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to = path_and_rename,)
    def __str__(self):
        return self.title