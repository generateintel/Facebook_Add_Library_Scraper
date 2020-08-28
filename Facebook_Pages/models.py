from django.db import models
from django.utils.datetime_safe import datetime
# Create your models here.
class Facebook_Category(models.Model):
    name = models.CharField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

    class Meta:
        unique_together = (('name'),)
class FacebookDatapages(models.Model):
    category = models.ForeignKey(Facebook_Category, on_delete=models.CASCADE, related_name='facebook_category')
    title = models.CharField(max_length=1000)
    likes = models.BigIntegerField(default=0,null=True)
    fb_page_link = models.CharField(max_length=1000, blank=True)
    Description=models.CharField(max_length=10000,blank=True,null=True)
    all_Description = models.CharField(max_length=100000, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    scrape_status = models.BooleanField(default=True)
    page_id=models.BigIntegerField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)




