from email.policy import default
from django.db import models

class House(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Tenant(models.Model):
    name = models.CharField(max_length=255)
    fb_messenger = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    

class Reading(models.Model):
    house_id = models.ForeignKey(House,on_delete=models.CASCADE)
    tenant_id = models.ForeignKey(Tenant, on_delete=models.DO_NOTHING)
    bill_type = models.CharField(max_length=255, blank=True, null=True)
    due_date = models.DateField(auto_now_add=True,blank=True, null=True)
    start_date = models.DateField(auto_now_add=True,blank=True, null=True)
    end_date = models.DateField(auto_now_add=True,blank=True, null=True)
    previous_reading = models.IntegerField(blank=True, null=True)
    present_reading = models.IntegerField(blank=True, null=True)
    consumption = models.IntegerField(blank=True, null=True)
    peso_per_consumption = models.IntegerField(blank=True, null=True)
    bill = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True,blank=True, null=True)
    paid_at = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.house_id)
    

