from django.db import models
from api import file_upload_path_for_db
# Create your models here.


class Video(models.Model):
    videourl = models.CharField(max_length=1000, blank=True)
    title = models.CharField(max_length=200)
    threshold = models.CharField(max_length=20)
    tags = models.CharField(max_length=500)


class VideoFile(models.Model):
    file_save_name = models.FileField(upload_to=file_upload_path_for_db, blank=False, null=False)
    # 파일의 원래 이름
    file_origin_name = models.CharField(max_length=100)    
    # 파일 저장 경로
    file_path = models.CharField(max_length=100)
    
    def __str__(self):
        return self.file.name
