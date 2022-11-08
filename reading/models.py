from email.policy import default
from django.db import models

class House(models.Model):
    name = models.CharField(max_length=255)
    is_occupied = models.BooleanField(default=False)
    color = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return f'{str(self.id)} - {self.name}'
    
class Tenant(models.Model):
    name = models.CharField(max_length=255)
    house_id = models.ForeignKey(House, on_delete=models.DO_NOTHING)
    fb_messenger = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    date_started = models.DateField(auto_now_add=True,blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class YearlyBill(models.Model):
    year = models.IntegerField()
    month = models.CharField(max_length=255)
    bill_type = models.CharField(max_length=255)
    bill = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return f'{str(self.year)}-{str(self.month)}-{self.bill_type}'

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
    

