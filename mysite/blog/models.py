from django.db import models

# Create your models here.
class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)  # ���ͱ���
    body = models.TextField()                   # ��������
    timestamp = models.DateTimeField()          # ����ʱ��