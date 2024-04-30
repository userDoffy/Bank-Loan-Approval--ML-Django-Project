from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    gender=models.CharField(max_length=10)
    married=models.CharField(max_length=10)
    dependents=models.IntegerField()
    education=models.CharField(max_length=20)
    self_employed=models.CharField(max_length=10)
    applicant_income=models.FloatField()
    coapplicant_income=models.FloatField()
    loan_amount=models.FloatField()
    loan_amount_term=models.IntegerField()
    credit_history=models.CharField(max_length=10)
    property_area=models.CharField(max_length=10)
    loan_approval=models.IntegerField()
    def __str__(self) -> str:
        return str(self.user)+'_information'