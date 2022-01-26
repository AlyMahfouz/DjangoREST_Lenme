from django.shortcuts import render

# Create your views here.

from django.http.request import HttpRequest 
from django.http.response import JsonResponse

from django.views.decorators.csrf import csrf_exempt

import app.models as models


@csrf_exempt
def create_borrower(request:HttpRequest):
    if request.method == 'POST':
        data = request.POST
        if "name" in data:
            b = models.Borrower(name=data["name"])
            b.save()
            return JsonResponse({"Message":f"{b.name}, you have been successfully registered as a Borrower."})
        else:
            return JsonResponse({"Message":"Missing the name field."})
    else:
        return JsonResponse({"Message":"Sorry not the expected HTTP Method."})


@csrf_exempt
def create_investor(request:HttpRequest):
    if request.method == 'POST':
        data = request.POST
        if "name" and "balance" in data:
            i = models.Investor(name=data["name"], balance=float(data["balance"]))
            i.save()
            return JsonResponse({"Message":f"{i.name}, you have been successfully registered as an Investor with a sufficient balance of ${i.balance}."})
        else:
            return JsonResponse({"Message":"Missing the name or balance field."})
    else:
        return JsonResponse({"Message":"Sorry not the expected HTTP Method."})


def view_borrowers(request:HttpRequest):
    if request.method == 'GET':
        b = models.Borrower.objects
        b = b.all()

        def prod_to_dict(px: models.Borrower):
            dt = {
            'id': px.id,
            'name': px.name,
            }
            return dt
        
        return JsonResponse({'data': [prod_to_dict(pt) for pt in b]})


def view_investors(request:HttpRequest):
    if request.method == 'GET':
        i = models.Investor.objects
        i = i.all()

        def prod_to_dict(px: models.Investor):
            dt = {
            'id': px.id,
            'name': px.name,
            'balance': px.balance,
            }
            return dt
        
        return JsonResponse({'data': [prod_to_dict(pt) for pt in i]})


@csrf_exempt
def loan_request(request:HttpRequest):
    if request.method == 'POST':
        data = request.POST
        if "amount" and "period" in data:
            bor = models.Borrower.objects.get(id=1) # hard coding borrower id...
            req = models.Loan(borrower=bor, amount=float(data['amount']), period=data['period'])
            req.save()
            return JsonResponse({"Message":"Your loan request has been successfully made."})
        else:
            return JsonResponse({"Message":"Missing one of the amount or period field."})
    else:
        return JsonResponse({"Message":"Sorry not the expected HTTP Method."})


@csrf_exempt
def offer_request(request:HttpRequest):
    if request.method == 'POST':
        data = request.POST
        if "interest_rate" in data:
             bor = models.Borrower.objects.get(id=1) # hard coding borrower id... 
             inv = models.Investor.objects.get(id=1) # hard coding investor id...
             loan = models.Loan.objects.get(id=1) # hard coding loan id...
             req = models.Offer(borrower=bor, investor=inv, loan=loan, interest_rate=float(data['interest_rate']))
             req.save()
             return JsonResponse({"Message":"Your offer to the borrower has been successfully submitted."})
        else:
            return JsonResponse({"Message":"Missing the interest_rate field."})
    else:
        return JsonResponse({"Message":"Sorry not the expected HTTP Method."})


@csrf_exempt
def accept_offer(request:HttpRequest):
    if request.method == 'POST':
        req = models.Offer.objects.get(borrower_id=1) # hard coding borrower id... 
        req.status="Accepted"
        req.save()
        total_loan_amount = req.loan.amount + 3.00
        if (req.investor.balance >= total_loan_amount):
            loan = models.Loan.objects.get(borrower_id=1)
            loan.investor=req.investor
            loan.interest_rate=req.interest_rate
            loan.status="Funded"
            loan.save()
            principal_amount = loan.amount
            interest_amount = (principal_amount*loan.interest_rate)/(12/loan.period)
            final_amount_per_month = (principal_amount + interest_amount) / loan.period
            return JsonResponse({"Message":f"The proposed offer has been accepted and the loan will be funded successfully. You will be paying ${final_amount_per_month} every month for {loan.period} Month(s)." })
        else:
            return JsonResponse({"Message":"The proposed offer has been accepted, but unfortunately the loan will not be funded due to the investor insufficient balance."})
    else:
        return JsonResponse({"Message":"Sorry not the expected HTTP Method."})
        

@csrf_exempt
def monthly_payment(request:HttpRequest):
    if request.method == 'POST':
        data = request.POST
        if "amount_settled" in data:
            loan = models.Loan.objects.get(borrower_id=1)
            loan.amount_settled = loan.amount_settled + float(data['amount_settled'])

            principal_amount = loan.amount
            interest_amount = (principal_amount*loan.interest_rate)/(12/loan.period)
            final_amount = (principal_amount + interest_amount)

            if (loan.amount_settled >= final_amount):
                loan.status="Completed"
                loan.save()
                return JsonResponse({"Message":"Congratulations! All the payments are successfully paid back to the investor."})
            else:
                loan.save()
                return JsonResponse({"Message":"See you next month."})

        else:
            return JsonResponse({"Message":"Missing the amount_settled field."})
    else:
        return JsonResponse({"Message":"Sorry not the expected HTTP Method."})