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

    def __str__(self):
        return str(self.house_id)
    

