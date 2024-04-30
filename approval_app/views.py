from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import logout
import joblib
from approval_app.models import Customer
mod=joblib.load('model/LoanApprovalmodel1.pkl')
# Create your views here.
data_columns = ["gender", "married", "dependents", "education", "self_employed", "applicantincome", "coapplicantincome", "loanamount", "loan_amount_term", "credit_history", "property_area"]


def home(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        cus=None
        try:
            cus=Customer.objects.get(user=request.user)
        finally:
            return render(request,'home.html',{'user':request.user,'customer':cus})

def checkapproval(request):
    if not request.user.is_authenticated:
        return HttpResponse("Page Not Available")

    if request.method=='POST':
        gender = request.POST.get('genderRadioDefault')
        married = request.POST.get('marriedRadioDefault')
        dependents = request.POST.get('dependentsRadioDefault')
        education = request.POST.get('educationRadioDefault')
        self_employed= request.POST.get('self_employedRadioDefault')
        applicantincome=request.POST.get('applicantincome')
        coapplicantincome=request.POST.get('coapplicantincome')
        loanamount=request.POST.get('loanamount')
        loanamountterm=request.POST.get('loanamountterm')
        credit_history = request.POST.get('credit_historyRadioDefault')
        property_area= request.POST.get('property_areaRadioDefault')
        

        gender_f=1 if gender=="Male" else 0
        married_f=1 if married=="Yes" else 0
        dependents_f=int(dependents)
        education_f=1 if education=="notgraduate" else 0
        self_employed_f=1 if self_employed=="Yes" else 0
        applicantincome_f=float(applicantincome)
        coapplicantincome_f=float(coapplicantincome)
        loanamount_f=float(loanamount)
        loanamountterm_f=float(loanamountterm)
        credit_history_f=1 if credit_history=="Yes" else 0
        if property_area=='Rural':
            property_area_f=0
        elif property_area=='Semiurban':
            property_area_f=1
        else:
            property_area_f=2

        inp=[gender_f,married_f,dependents_f,education_f,self_employed_f,applicantincome_f,coapplicantincome_f,loanamount_f,loanamountterm_f,credit_history_f,property_area_f]
        approval=mod.predict([inp])[0]

        cus=Customer.objects.filter(user=request.user)
        if cus:
            cus.update(user=request.user,gender=gender,married=married,dependents=dependents,education=education,self_employed=self_employed,applicant_income=applicantincome,coapplicant_income=coapplicantincome,loan_amount=loanamount,loan_amount_term=loanamountterm,credit_history=credit_history,property_area=property_area,loan_approval=approval)
        else:
            cus=Customer(user=request.user,gender=gender,married=married,dependents=dependents,education=education,self_employed=self_employed,applicant_income=applicantincome,coapplicant_income=coapplicantincome,loan_amount=loanamount,loan_amount_term=loanamountterm,credit_history=credit_history,property_area=property_area,loan_approval=approval)
            cus.save()
    return redirect('/approve')


def loggout(request):
    logout(request)
    return redirect('/')