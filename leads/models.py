from django.db import models
from accounts.models import User
# Create your models here.
class Lead(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    company = models.CharField(max_length=100, blank=True, null=True)
    
    SOURCE_CHOICES = [
        ('Website', 'Website'),
        ('Social Media', 'Social Media'),
        ('Referral', 'Referral'),
        ('Advertisement', 'Advertisement'),
        ('Other', 'Other'),
    ]

    source = models.CharField(max_length=20,choices=SOURCE_CHOICES)

    STATUS_CHOICES = [
        ('New', 'New'),
        ('Contacted', 'Contacted'),
        ('Interested', 'Interested'),
        ('Converted', 'Converted'),
        ('Lost', 'Lost'),
    ]

    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='New')

    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='leads')


    def __str__(self):
        return self.name